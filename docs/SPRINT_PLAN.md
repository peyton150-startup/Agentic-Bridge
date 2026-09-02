# 3–4 Day Sprint Plan

## Choosing a Mode

The plan is intentionally capped. If you exceed a day's timebox, cut optional implementation—not fundamentals or quizzes.

### Practical total

```text
3-day core: about 14–16 focused hours total
4-day preferred: same core + about 3–4 hours consolidation
```

Do not spend more than about one hour per day on academic reading. The readings are there to establish the mental model; the quizzes and transfer exercises prove whether you can use it.


### 3-Day Core

Use this if you truly have only three days. Complete every item marked **CORE**. Skip optional coding repetitions and framework experiments.

### 4-Day Preferred

Complete the same three core days, then use Day 4 for retrieval, transfer, and a mock CMU lab.

---

# Day 1 — Agents, LLM Boundary, Tool Loop

**Timebox:** 5–5.5 hours

```text
45–60 min  official reading
60 min     fundamentals + drawings
30 min     quiz / remediation
90 min     tiny implementation
45 min     trace + changed variant + failure case
30 min     closed-code exit gate
15–30 min  buffer
```

**Goal:** Understand what an agent is before treating an LLM framework as the agent.

## Academic reading — CORE

From `SOURCES.md`:

1. CMU Agentic AI Program: prerequisites, learning outcomes, Modules 1–2.
2. CMU 11-768 AI Agents description.
3. Berkeley CS188: `1.1 Agents` and `1.2 State Spaces and Search Problems`.
4. Skim CMU 15-213 course description only for the “programs execute/communicate through systems” mental model.

## Fundamentals — CORE

Be able to explain:

```text
agent
performance goal
environment
observation/state
action/tool
transition/consequence
planning vs direct reaction
LLM decision vs application authority
tool input validation
loop state
stop condition
bounded execution
```

See `FUNDAMENTALS.md` sections A–C.

## Quiz — CORE

Take Day 1 quiz from `QUIZ_PROTOCOL.md`.

## Tiny implementation — CORE

Build only after the quiz passes:

```text
deterministic model-decision stub
→ explicit while/step loop
→ one read-only tool
→ tool-result observation
→ explicit stop condition
→ trace record
```

Do **not** add memory, RAG, LangGraph, CrewAI, or a database.

A live LLM call is optional. If used, it comes **after** the deterministic loop is understood.

## Exit test — CORE

Close the code and draw the loop from memory. Explain what state changes after every step.

---

# Day 2 — Memory and RAG Fundamentals

**Timebox:** 4–4.5 hours

```text
45–60 min  official reading
60 min     memory/RAG fundamentals
60–75 min  classification + vector/retrieval exercises
30 min     quiz / transfer
30 min     closed-notes exit gate
optional    tiny vector calculation only if ahead of schedule
```

**Goal:** Understand what information the agent has, where it came from, and what status it has.

## Academic reading — CORE

1. CMU Agentic AI Program: Modules 2–3 and learning outcomes around memory/RAG.
2. CMU 11-768: memory and tool use.
3. Berkeley CS188 state representation material: distinguish world information from the state representation needed for a decision.

## Fundamentals — CORE

Be able to distinguish:

```text
current prompt/context
working state
durable authoritative application state
durable non-authoritative memory
retrieved evidence
model inference
```

Understand the RAG pipeline conceptually:

```text
documents
→ chunks
→ embedding/vector representation
→ query representation
→ similarity/retrieval
→ selected evidence/context
→ generation
```

Understand:

- why chunking changes what can be retrieved;
- what top-k means conceptually;
- why retrieved text is evidence/input, not authority;
- retrieval failure vs generation failure;
- why an embedding/vector is a representation, not “understanding.”

See `FUNDAMENTALS.md` sections D–E.

## Exercises — CORE

1. Classify 10 pieces of information as context/state/memory/evidence/inference.
2. Do one small vector-similarity exercise on paper before using code.
3. Given three retrieval results, identify whether the answer failure came from retrieval or generation.

## Optional tiny code

Only if time remains and the paper exercise is correct:

- write or inspect a tiny cosine-similarity calculation over manually supplied vectors;
- trace every arithmetic step;
- change one query vector and predict ranking before running.

No vector database is required.

## Exit test — CORE

Explain the RAG pipeline without saying “the framework handles it.”

---

# Day 3 — Reasoning, Multi-Agent, Evaluation, Safety

**Timebox:** 5–5.5 hours

```text
45–60 min  official reading
60 min     reasoning/multi-agent fundamentals
60 min     evaluation + safety scenarios
45 min     single-vs-multi-agent design exercise
30 min     Day 3 quiz
60 min     final readiness check / remediation
15–30 min  buffer
```

**Goal:** Enter CMU able to discuss why an architecture is structured a certain way and how you would know whether it worked.

## Academic reading — CORE

1. CMU Agentic AI Program: Modules 4–6 and capstone outcome.
2. CMU 15-482 Autonomous Agents: architecture, planning, execution monitoring, integration/testing, reliability/robustness.
3. CMU 11-768: task decomposition, safety sandboxing, credentialing.
4. Berkeley CS188: revisit state/actions/goal test; skim MDP introduction for the idea that action choice may occur under uncertainty.

## Fundamentals — CORE

Be able to explain:

```text
direct loop vs explicit plan/decomposition
branching candidate actions/thought paths conceptually
verification step
budget/step limit
single-agent baseline
agent role
handoff
shared state
termination
execution monitoring
success criterion
failure case
guardrail
trace/evidence
```

See `FUNDAMENTALS.md` sections F–H.

## Evaluation exercise — CORE

Create five scenarios for the Day 1 tiny agent:

```text
normal success
invalid proposed tool input
tool failure
repeated/looping action pressure
unsafe/out-of-authority request
```

For each specify **before running**:

- expected outcome;
- allowed state changes;
- maximum steps;
- evidence you would inspect;
- pass/fail criterion.

## Multi-agent design exercise — CORE

Take one problem and propose:

```text
single-agent design
vs
two-agent design
```

Defend whether the second agent solves a real coordination/decomposition problem or merely adds complexity.

No multi-agent code is required.

## Final 3-day gate — CORE

Take `FINAL_READINESS_CHECK.md`.

If you pass, you are done with the bridge even if you never installed LangGraph or CrewAI.

---

# Day 4 — Optional Consolidation and Mock CMU Lab

**Timebox:** 3–4 hours

**Goal:** Reduce cognitive load during CMU's first two weeks.

## 1. Framework vocabulary map

Without coding a framework, create a table:

```text
ordinary mechanism     CMU-listed framework idea
state                  graph/workflow state
branch/decision        routing/edge
agent/tool action      node/tool step
loop continuation      cycle/next step
stop condition         terminal/end state
handoff                 multi-agent routing
```

Do not memorize API syntax.

## 2. Mini-capstone architecture

Choose one small real-world problem and write one page containing:

```text
problem
goal/success measure
environment
state
possible actions/tools
authoritative data
memory needs
whether RAG is needed
reasoning strategy
single vs multi-agent decision
termination
evaluation cases
guardrails
trace/evidence
```

## 3. Mock lab

Have the tutor give one unseen small change to the Day 1 loop.

Required order:

```text
predict
state contract
quiz
small patch
trace
failure test
teach back
```

## 4. Delayed retrieval

Retake the final quiz without opening notes.
