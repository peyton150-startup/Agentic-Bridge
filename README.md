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
Day 1 — prerequisites + agents + LLM boundary + tool loop + external API boundary
Day 2 — memory + RAG/vector retrieval fundamentals
Day 3 — reasoning + multi-agent + evaluation/safety + final readiness gate
```

Target: roughly **5–6 focused hours per day**, except Day 1, which runs to
about **6–6.5 hours** because it carries the sprint's only required
implementation work.

### 4-day preferred

```text
Days 1–3 — same core
Day 4 — consolidation, framework vocabulary mapping, mini-capstone design, mock CMU lab
```

Target: roughly **4–5 focused hours per day**.

All essential readiness material is inside Days 1–3. Day 4 is repetition and transfer, not a new prerequisite.

### Optional Extension X (about 2.5–3 hours)

```text
X1 — serve a tiny API with FastAPI (inbound request → validation → domain function → status + JSON)
X2 — receive a simulated webhook (event → validation → deduplication → acknowledgement)
```

Available only after Gate 1B. Take it on Day 4 or after the bridge. It
completes the three-direction model: **call an API, provide an API, receive an
event**. It is not required for CMU readiness. See `docs/SPRINT_PLAN.md` →
Optional Extension X.

## What This Sprint Does NOT Require

Before CMU you do **not** need to:

- build a polished product;
- learn every LangGraph or CrewAI API;
- deploy a production vector database;
- build an API, an API server, or a reusable HTTP client (a tiny FastAPI server and webhook receiver are available as the optional Extension X, once the outbound HTTP boundary is understood; they are never required);
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
- what happens when a tool reaches an external HTTP API — validated input, request, status, parsed body, response validation, bounded result — and who owns each step;
- how to tell a tool-input validation failure, a network/transport failure, an HTTP/API error, a response-shape failure, and an agent-loop failure apart;
- the difference between context, memory, authoritative state, and retrieved evidence;
- the RAG pipeline from documents to retrieval to generated answer;
- why retrieval failure and generation failure are different;
- how planning/reasoning changes control flow and cost;
- why multiple agents require roles, coordination rules, shared-state rules, and termination rules;
- what evaluation, safety, execution monitoring, and traces are trying to prove;
- how to map CMU's LangGraph/CrewAI vocabulary back to ordinary state and control flow.

Optional, only if Extension X is taken: the difference between calling an API,
serving one, and receiving a webhook. That includes who initiates each, which
layer validates what, why a `2xx` acknowledgement is not completed work, and why
duplicate events must not cause duplicate side effects.

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
  TRELLIS_CODE_MAP.md

learning/
  LEARNING_LEDGER.md

code/
  tiny_agent.py      (Patches 1–4)
  api_tool.py        (Patch 5)
```

## Start Here

1. Read `SOURCES.md` and `docs/SOURCE_MAP.md` so you know exactly what the curriculum is based on.
2. Read `docs/SPRINT_PLAN.md` and choose 3-day or 4-day mode.
3. Read `docs/TRELLIS_CODE_MAP.md` for the pinned repository identity and the prior-work examples used after each day gate.
4. Run `FIRST_SESSION.md`.
5. Take `docs/PREREQUISITE_DIAGNOSTIC.md` before writing agent code.
6. Follow the day plan in order.

The repository begins with **documentation only** on purpose.
