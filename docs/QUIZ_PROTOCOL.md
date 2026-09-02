# Quiz Protocol

## Passing Standard

A quiz is passed when the learner can answer **at least 4 of 5** questions correctly and can handle one changed transfer example.

Do not reuse the exact same question after explaining the answer.

## Day 1 Quiz — Agent / Tool Loop

Ask five selected from:

1. For a given assistant, identify goal, environment, state/observation, and actions.
2. What part of a tool-calling system should own permission to mutate authoritative state?
3. A model emits valid JSON naming a real tool. Does that prove the tool call should execute? Why?
4. What state must persist from one loop step to the next?
5. Name two different termination mechanisms.
6. What should happen if the model repeatedly proposes an invalid action?
7. Why is a tool result an observation/input rather than automatically “the answer”?
8. On an unseen trace, predict the next loop state.

### Transfer requirement

Give a different domain, such as calendar, files, or factory operations, and ask the learner to define one safe read-only action/tool.

---

## Day 2 Quiz — Memory / RAG

Ask five selected from:

1. Classify an item as current context, working state, authoritative durable state, non-authoritative memory, retrieved evidence, or model inference.
2. Why should a model-written “memory” not automatically overwrite authoritative application data?
3. What changes when document chunk boundaries change?
4. What does an embedding/vector represent in the retrieval pipeline?
5. Explain top-k without naming a library.
6. Give an example where retrieval succeeds but generation fails.
7. Give an example where generation never had a fair chance because retrieval failed.
8. Why can retrieved text be a trust/safety concern?

### Transfer requirement

Given a new document corpus and three user questions, describe what evidence would need to be retrievable for each.

---

## Day 3 Quiz — Reasoning / Multi-Agent / Evaluation

Ask five selected from:

1. What is the difference between adding a planning step and merely making a prompt longer?
2. Name a cost introduced by additional reasoning branches/steps.
3. What information must cross an agent-to-agent handoff?
4. What new failure mode appears when two agents share mutable state?
5. Why should a multi-agent design be compared to a single-agent baseline?
6. Define a success criterion for an agent before running it.
7. What evidence should an execution trace contain?
8. What does sandboxing/credentialing protect at a high level?
9. A run ends with a good answer but performed a forbidden tool mutation. Did it pass? Why?
10. An agent failed. What is the difference between guessing the cause and diagnosing from execution evidence?

### Transfer requirement

Give one unfamiliar agent architecture and require the learner to identify role, state, actions, termination, and one evaluation case.

---

## Final Delayed Quiz

Without notes, ask the learner to define and connect:

```text
agent
state
action/tool
agent loop
termination
authority
memory
RAG
embedding
retrieval failure
generation failure
planning/reasoning
multi-agent handoff
evaluation
guardrail
execution trace
```

Do not require LangGraph/CrewAI API syntax.
