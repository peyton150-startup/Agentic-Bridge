# tiny_agent.py — Day 1.
# Patch 1: the agent's state.
# Patch 2: one read-only tool and its input check.
# Patch 3: a fake model and the bounded loop.


def new_state(request, max_steps):
    """Build the starting state for one run of the agent."""
    return {
        "request": request,        # what the user asked
        "step": 0,                 # which pass of the loop we are on
        "max_steps": max_steps,    # the limit; code stops here, not the model
        "trace": [],               # history: every proposal and observation, in order
        "stop_reason": None,       # None while running; one label when it stops
    }


# The tool's data. Read-only: nothing in this file ever changes it.
DICTIONARY = {
    "agent": "something that acts in an environment to reach a goal",
    "persistence": "keeping information after the program stops",
    "provenance": "where a piece of information came from",
    "picasso" : "a famous painter",
}


def is_valid_word(word):
    """The check at the door: letters only, 1-30 characters."""
    return isinstance(word, str) and word.isalpha() and 1 <= len(word) <= 30


def lookup_word(word):
    """The tool. Assumes the word already passed is_valid_word."""
    if word in DICTIONARY:
        return {"found": True, "word": word, "definition": DICTIONARY[word]}
    return {"found": False, "word": word}


def fake_model(state):
    """Stand-in for an LLM. Reads the state, returns a proposal, changes nothing."""
    word = state["request"].split("'")[1]
    if not state["trace"]:
        return {"kind": "tool", "tool": "lookup_word", "word": word}
    observation = state["trace"][-1]["observation"]
    if observation.get("rejected"):
        return {"kind": "final", "answer": f"'{word}' is not a word I can look up."}
    if observation.get("found"):
        return {"kind": "final", "answer": f"'{word}' means {observation['definition']}"}
    return {"kind": "final", "answer": f"I couldn't find '{word}' in the dictionary."}


def run_agent(request, max_steps):
    """The loop. Code owns every decision about running tools and stopping."""
    state = new_state(request, max_steps)
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
        if proposal["tool"] == "lookup_word" and is_valid_word(proposal["word"]):
            observation = lookup_word(proposal["word"])
        else:
            observation = {"rejected": True, "word": proposal["word"], "reason": "failed input check: letters only, 1-30 characters"}
        state["trace"].append({"step": state["step"], "proposal": proposal, "observation": observation})
        state["step"] = state["step"] + 1


for request in ["what does 'agent' mean?", "what does '12345' mean?"]:
    result = run_agent(request, 5)
    print(request)
    print("  step:", result["step"], "| stop_reason:", result["stop_reason"])
    print("  answer:", result["trace"][-1]["proposal"]["answer"])
    print("  trace length:", len(result["trace"]))
print(run_agent("what does 'agent' mean?", 1)["stop_reason"])
print(run_agent("define agent", 5))
