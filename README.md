# Agentic Bridge — 3–4 Day CMU Readiness Sprint

## Purpose

Agentic Bridge is a **short readiness sprint** to complete after BuildLens and immediately before Carnegie Mellon University School of Computer Science Executive Education's Agentic AI Program.

It is **not** a substitute for the CMU program and it should not attempt to pre-complete the seven-week curriculum. The goal is narrower:

> Enter CMU already able to reason about an agent as a software system, understand the vocabulary and core mechanisms in Modules 1–6, and trace one tiny agent loop that you personally understand.

CMU publicly states that participants should have functional knowledge of **Python, algorithm design, data structures, LLMs, and AI**. Its program then progresses through LLM capabilities; memory, tools, and reasoning loops; RAG and vector databases; Tree-of-Thought and multi-agent concepts; CrewAI/LangGraph; and evaluation, guardrails, logging, and observability.

## Time Budget

Choose one mode.

### 3-day core

```text
Day 1 — prerequisites + agents + LLM boundary + tool loop
Day 2 — memory + RAG/vector retrieval fundamentals
Day 3 — reasoning + multi-agent + evaluation/safety + final readiness gate
```

Target: roughly **5–6 focused hours per day**.

### 4-day preferred

```text
Days 1–3 — same core
Day 4 — consolidation, framework vocabulary mapping, mini-capstone design, mock CMU lab
```

Target: roughly **4–5 focused hours per day**.

All essential readiness material is inside Days 1–3. Day 4 is repetition and transfer, not a new prerequisite.

## What This Sprint Does NOT Require

Before CMU you do **not** need to:

- build a polished product;
- learn every LangGraph or CrewAI API;
- deploy a production vector database;
- master Tree-of-Thought algorithms;
- build a sophisticated multi-agent system;
- reproduce CMU labs;
- create a frontend.

Those would consume the limited preparation window and create framework familiarity without necessarily creating understanding.

## The Non-Negotiable Learning Rule

**No implementation code before understanding the mechanism it is meant to express.**

Every code-bearing step follows:

```text
1. explain the concept in plain English
2. state input → output → state → authority → failure
3. predict what the small patch should do
4. pass a short concept quiz
5. inspect/write one small patch
6. trace the patch line by line
7. run a changed variant
8. explain one failure from evidence
```

If Step 4 fails, do not move to Step 5.

See `docs/TEACHING_CONTRACT.md` and `docs/QUIZ_PROTOCOL.md`.

## End State

Before starting CMU, you should be able to explain from memory:

- what an agent is in terms of environment, state, actions, goals, and feedback;
- what an LLM contributes and what it does **not** own;
- how a model/tool control loop starts, continues, and terminates;
- why tool output and model output are inputs that application code must interpret;
- the difference between context, memory, authoritative state, and retrieved evidence;
- the RAG pipeline from documents to retrieval to generated answer;
- why retrieval failure and generation failure are different;
- how planning/reasoning changes control flow and cost;
- why multiple agents require roles, coordination rules, shared-state rules, and termination rules;
- what evaluation, safety, execution monitoring, and traces are trying to prove;
- how to map CMU's LangGraph/CrewAI vocabulary back to ordinary state and control flow.

## Repository Map

```text
README.md
CURRENT_STATE.md
FIRST_SESSION.md
CLAUDE.md
SOURCES.md

docs/
  CMU_ALIGNMENT.md
  SPRINT_PLAN.md
  PREREQUISITE_DIAGNOSTIC.md
  FUNDAMENTALS.md
  TEACHING_CONTRACT.md
  QUIZ_PROTOCOL.md
  IMPLEMENTATION_PLAN.md
  ARCHITECTURE_CONTRACT.md
  EVALUATION_PLAN.md
  PHASE_GATES.md
  DESIGN_REVIEW_RUBRIC.md
  FINAL_READINESS_CHECK.md
  SOURCE_MAP.md

learning/
  LEARNING_LEDGER.md
```

## Start Here

1. Read `SOURCES.md` and `docs/SOURCE_MAP.md` so you know exactly what the curriculum is based on.
2. Read `docs/SPRINT_PLAN.md` and choose 3-day or 4-day mode.
3. Run `FIRST_SESSION.md`.
4. Take `docs/PREREQUISITE_DIAGNOSTIC.md` before writing agent code.
5. Follow the day plan in order.

The repository begins with **documentation only** on purpose.
