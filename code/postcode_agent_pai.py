# postcode_agent_pai.py — Patch 7: the postcode agent with Pydantic AI running the loop.
# Compare with postcode_agent.py: same tool, same fake model's two jobs, same answers.
# What changes is who writes the loop. What does not change is who holds authority.
#
# Framework syntax checked against the official Pydantic AI docs (v2). The syntax is
# not the lesson; the mapping to run_agent is.

from pydantic_ai import Agent, ModelResponse, TextPart, ToolCallPart, UsageLimitExceeded, UsageLimits
from pydantic_ai.models.function import FunctionModel

from postcode_agent import is_valid_postcode, lookup_postcode   # safe: its demo is behind __main__


# ---- The model: same two jobs, now reading the framework's message history ----

def fake_model(messages, info):
    """Stand-in for an LLM. messages is the framework's history (it replaces state["trace"])."""
    request = messages[0].parts[-1].content              # the user's words
    code = request.split()[-1].strip("?")
    if len(messages) == 1:                               # first turn: nothing observed yet
        return ModelResponse(parts=[ToolCallPart("lookup", {"code": code})])   # PROPOSE, don't act
    observation = messages[-1].parts[0].content          # what your tool returned
    if observation.get("rejected"):
        answer = f"'{code}' isn't a valid 5-digit US postcode."
    elif observation.get("found"):
        answer = f"{code} is {observation['place']}, {observation['state']}, {observation['country']}."
    elif observation.get("error") == "http" and observation.get("status") == 404:
        answer = f"I couldn't find a US place for {code}."
    else:
        answer = f"I couldn't look up {code} right now ({observation.get('error')})."
    return ModelResponse(parts=[TextPart(answer)])      # plain text = final answer; the loop stops


# ---- The framework's loop: replaces your while True ---------------------------

agent = Agent(FunctionModel(fake_model))


# ---- The tool: YOURS ---------------------------------------------------------
# Register a function named `lookup` on the agent with the decorator @agent.tool_plain
# It takes code: str and returns a dict.
# The framework has only checked that code is a string. Your guard goes here:
#   - if the code fails is_valid_postcode → return a dict with "rejected": True
#   - otherwise → return whatever lookup_postcode(code) returns

@agent.tool_plain                 # ← the only Pydantic AI line: "the model may propose this"
def lookup(code: str) -> dict:    # ← an ordinary Python function
    if is_valid_postcode(code):
        observation = lookup_postcode(code, timeout = 5)
    else:
        observation = {"rejected": True, "code": code, "reason": "isn't a valid 5-digit US postcode."}
    return observation

# ---- Running it: replaces your run_agent -------------------------------------

def run_agent(request, max_steps):
    try:
        result = agent.run_sync(request, usage_limits=UsageLimits(request_limit=max_steps))
    except UsageLimitExceeded:                           # the framework raises; we turn it back into a stop reason
        return {"stop_reason": "max_steps", "answer": None, "messages": []}
    return {"stop_reason": "final_answer", "answer": result.output, "messages": result.all_messages()}


if __name__ == "__main__":
    for request in ["where is 15213?", "where is 1521?", "where is 99999?"]:
        result = run_agent(request, 5)
        print(request)
        print("  stop_reason:", result["stop_reason"], "| messages:", len(result["messages"]))
        print("  answer:", result["answer"])
