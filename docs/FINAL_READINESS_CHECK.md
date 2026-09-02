# Final CMU Readiness Check

Take this at the end of Day 3. No notes for the first pass.

## Part A — 10-Minute Architecture Reconstruction

Draw a small LLM agent containing:

```text
user/request
application state
model decision
one tool
tool result/observation
loop
termination
trace
```

Label authority and failure boundaries.

## Part B — 15 Core Questions

1. What makes an agent more than a single LLM call?
2. What are environment, state/observation, action, and goal?
3. Why is model output not automatically authoritative?
4. What must be validated before a model-proposed tool action executes?
5. Why must a loop have a termination/budget rule?
6. Context vs durable state vs memory: what is the difference?
7. Draw the RAG pipeline.
8. What is an embedding/vector doing in that pipeline?
9. Retrieval failure vs generation failure?
10. How can chunking or top-k change behavior?
11. What does explicit planning/decomposition add to control flow?
12. What new problems appear when a second agent is added?
13. Why compare multi-agent to a single-agent baseline?
14. What should be decided before an evaluation run starts?
15. What trace evidence would you inspect when an agent fails?

## Part C — Unseen Transfer

The tutor supplies one unfamiliar problem.

You must define:

```text
performance goal
environment
state
actions/tools
authoritative data
whether memory is needed
whether RAG is needed
reasoning/control strategy
single vs multi-agent choice
termination
evaluation scenario
safety boundary
```

## Part D — CMU Vocabulary Recognition

Be able to give a one- or two-sentence **mechanism-level** description of:

```text
agentic AI
memory
tool use
reasoning loop
RAG
embedding
vector database
ReAct (high level)
Tree-of-Thought (high level)
LangGraph (what kind of problem it helps represent)
CrewAI (what kind of multi-agent organization it represents)
guardrail
logging/observability
evaluation
```

You do not need framework API syntax.

## Decision

### Ready

You can explain and transfer the mechanisms, even if implementation depth is still small.

### Ready with watch items

You understand the architecture but have one or two weaker vocabulary/mechanics areas. Record them and begin CMU.

### Not ready

Only if a **prerequisite** remains broken — e.g. Python tracing, basic data structures, basic agent/state/action reasoning, or inability to understand the tiny loop.

Do not delay CMU because you have not independently mastered advanced RAG, multi-agent frameworks, or Tree-of-Thought. Those are part of the program.
