# postcode_agent.py — Patch 6: the tiny_agent loop with the external API tool.
# Self-contained on purpose: new_state is copied from tiny_agent.py and the tool
# from api_tool.py, so neither of those files changes.
# The lesson: the loop does not change when its tool reaches a network.

import json
import urllib.error
import urllib.request


def new_state(request, max_steps):
    """Build the starting state for one run of the agent."""
    return {
        "request": request,        # what the user asked
        "step": 0,                 # which pass of the loop we are on
        "max_steps": max_steps,    # the limit; code stops here, not the model
        "trace": [],               # history: every proposal and observation, in order
        "stop_reason": None,       # None while running; one label when it stops
    }


# ---- The tool: copied from api_tool.py, unchanged ----------------------------

POSTCODE_URL = "https://api.zippopotam.us/us/{code}"


def is_valid_postcode(code):
    """The check at the door: exactly 5 digits. No request is built if this fails."""
    return isinstance(code, str) and code.isdigit() and len(code) == 5


def lookup_postcode(code, timeout=5):
    """GET one US postal code. Read-only. Returns one result per failure kind."""
    if not is_valid_postcode(code):
        return {"error": "invalid_input", "status": None, "reason": "exactly 5 digits required"}

    try:
        with urllib.request.urlopen(POSTCODE_URL.format(code=code), timeout=timeout) as response:
            status = response.status
            raw = response.read()
    except urllib.error.HTTPError as exc:        # they answered, with a non-success status
        return {"error": "http", "status": exc.code, "reason": "service refused the request"}
    except Exception as exc:                     # timeout, DNS, refused connection: nothing usable came back
        return {"error": "network", "status": None, "reason": type(exc).__name__}

    if status != 200:                            # success is 200 and nothing else
        return {"error": "http", "status": status, "reason": "not a success status"}

    try:
        body = json.loads(raw)
    except ValueError:
        return {"error": "shape", "status": status, "reason": "body was not JSON"}

    places = body.get("places")                  # a 200 does not promise the fields we need
    if not isinstance(places, list) or not places:
        return {"error": "shape", "status": status, "reason": "no places in body"}
    if "country" not in body:
        return {"error": "shape", "status": status, "reason": "body is missing country"}

    place = places[0]
    if "place name" not in place or "state" not in place:
        return {"error": "shape", "status": status, "reason": "place is missing required fields"}

    # Bounded result: three fields, not the whole body.
    return {"found": True, "code": code, "place": place["place name"], "state": place["state"], "country": body["country"]}


# ---- The model: new --------------------------------------------------------

def fake_model(state):
    """Stand-in for an LLM. Job 1: pull the code out of the request and propose.
    Job 2: turn the observation into an honest answer. Changes nothing."""
    code = state["request"].split()[-1].strip("?")
    if not state["trace"]:
        return {"kind": "tool", "tool": "lookup_postcode", "code": code}
    observation = state["trace"][-1]["observation"]
    if observation.get("rejected"):
        return {"kind": "final", "answer": f"'{code}' isn't a valid 5-digit US postcode."}
    if observation.get("found"):
        return {"kind": "final", "answer": f"{code} is {observation['place']}, {observation['state']}, {observation['country']}."}
    if observation.get("error") == "http" and observation.get("status") == 404:
        return {"kind": "final", "answer": f"I couldn't find a US place for {code}."}
    return {"kind": "final", "answer": f"I couldn't look up {code} right now ({observation.get('error')})."}


# ---- The loop: YOURS -------------------------------------------------------
# Write run_agent(request, max_steps) here, from memory.
# It proposes with fake_model, guards with is_valid_postcode, runs lookup_postcode,
# and returns the state. A rejected proposal's observation should be a dict with
# "rejected": True (fake_model checks for that key).

def run_agent(request, max_steps):
    """The loop. Code owns every decision about running tools and stopping."""
    state= new_state(request, max_steps)
    while True:
        if state["step"] >= state["max_steps"]:
            state["stop_reason"] = "max_steps"
            return state
        try:
            proposal = fake_model(state)
        except Exception as error:
            state["stop_reason"] = "model_error"
            state["trace"].append({"error": f"{type(error).__name__}: {error}", "step": state["step"]})
            return state
        if proposal["kind"] == "final":
            state["trace"].append({"step": state["step"], "proposal": proposal, "observation": None})
            state["stop_reason"] = "final_answer"
            return state
            
        if proposal["tool"] == "lookup_postcode" and is_valid_postcode(proposal["code"]):
            observation = lookup_postcode(proposal["code"], timeout = 5)
        else:
            observation = {"rejected": True, "code": proposal["code"], "reason": "isn't a valid 5-digit US postcode."}
        state["trace"].append({"step": state["step"], "proposal": proposal, "observation": observation})
        state["step"] = state["step"] + 1
        
# ---- Demo: your Gate 3 prediction table --------------------------------------

if __name__ == "__main__":
    for request in ["where is 15213?", "where is 1521?", "where is 99999?"]:
        result = run_agent(request, 5)
        print(request)
        print("  stop_reason:", result["stop_reason"], "| trace length:", len(result["trace"]))
        print("  answer:", result["trace"][-1]["proposal"]["answer"])
