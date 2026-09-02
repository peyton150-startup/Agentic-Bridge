# First Session — 60–90 Minute Readiness Baseline

## Rule

Do not install LangGraph, CrewAI, a vector database, or any other agent framework in this session.

Do not ask an AI assistant to generate application code.

## 1. Read the Official Program Shape

Read the CMU Agentic AI Program overview and its public prerequisites, learning outcomes, Modules 1–7, and listed applied tools. The exact official link is in `SOURCES.md`.

Then write, without copying:

```text
What does CMU expect me to know before the program?
What does CMU intend to teach during the program?
What therefore belongs in this 3–4 day bridge?
What should be left for CMU?
```

## 2. Define an Agent Before LLM Vocabulary

Using the Berkeley CS188 agent model, describe:

```text
goal / performance measure
environment
state / observation
actions
transition or consequence
termination / goal condition
```

Then explain where an LLM could participate in that system without becoming the entire system.

## 3. Draw One LLM-Agent Runtime

Draw:

```text
user request
→ application state
→ model decision
→ validated action/tool
→ environment/state change or observation
→ application state
→ model continuation or stop
→ final result
```

For every arrow identify:

- representation crossing the boundary;
- who owns authoritative state;
- one possible failure;
- one piece of evidence you would inspect.

## 4. Take the Prerequisite Diagnostic

Complete `docs/PREREQUISITE_DIAGNOSTIC.md`.

Record only concepts that genuinely need remediation. Do not turn a weak point into another week-long course.

## 5. Promotion

If the diagnostic passes, update `CURRENT_STATE.md` to:

```text
Current stage: Day 1 — agent foundations and tool loop
```

Then follow `docs/SPRINT_PLAN.md`.

## Prompt for an AI Tutor/Coding Assistant

```text
Read README.md, CURRENT_STATE.md, SOURCES.md, docs/SPRINT_PLAN.md,
docs/TEACHING_CONTRACT.md, docs/QUIZ_PROTOCOL.md, docs/PHASE_GATES.md,
and learning/LEARNING_LEDGER.md.

This is a 3–4 day readiness sprint before Carnegie Mellon SCS Executive
Education's Agentic AI Program. The academic source boundary is strict:
use only the CMU and UC Berkeley computer-science materials listed in SOURCES.md
for teaching claims in this repository.

Do not generate application code before I pass the relevant concept gate.
Before any code, require me to explain the mechanism, draw input/output/state/
authority/failure, predict behavior, and answer a short quiz. Keep patches small
enough that I can trace every nontrivial line. If I cannot explain a line, stop
and remediate before adding more code.

Start with FIRST_SESSION.md and the prerequisite diagnostic.
```
