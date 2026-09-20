# 3–4 Day Sprint Plan

## Choosing a Mode

The plan is intentionally capped. If you exceed a day's timebox, cut optional implementation—not fundamentals or quizzes.

### Practical total

```text
3-day core: about 15–17 focused hours total
4-day preferred: same core + about 3–4 hours consolidation
```

Day 1 is the heaviest day because it carries the only implementation work in
the sprint, including the one external-API segment.

Do not spend more than about one hour per day on academic reading. The readings are there to establish the mental model; the quizzes and transfer exercises prove whether you can use it.


### 3-Day Core

Use this if you truly have only three days. Complete every item marked **CORE**. Skip optional coding repetitions and framework experiments.

### 4-Day Preferred

Complete the same three core days, then use Day 4 for retrieval, transfer, and a mock CMU lab.

---

# Day 1 — Agents, LLM Boundary, Tool Loop, External API Boundary

**Timebox:** 6–6.5 hours

```text
45–60 min  official reading
60 min     agent/tool fundamentals + drawings
30 min     Day 1A quiz / remediation
75 min     deterministic implementation (Patches 1–4)
30 min     trace + changed variant + failure case
25 min     API boundary fundamentals + request/response drawing
15 min     Day 1B API quiz / remediation
35 min     one external read-only API tool (Patch 5) + two failure demos
30 min     closed-code exit gate (deterministic loop and API path)
15–30 min  buffer
```

Day 1 is the longest day in the sprint. It is the only day that carries
implementation, and the API segment is deliberately placed here rather than
given a day of its own.

**Goal:** Understand what an agent is before treating an LLM framework as the
agent, and understand what actually happens when one of its tools reaches a
service you do not own.

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

## Quiz 1A — CORE

Take the Day 1A quiz from `QUIZ_PROTOCOL.md`.

## Related to Trellis — after the quiz

Only use this section after the Day 1 quiz passes. Trellis is code you have already built, so it is the transfer example—not a shortcut around explaining the mechanism first.

Trace one concrete request: **“Create a task called Study approval boundaries.”**

```text
handle_agui_request
→ model proposes CreateTaskArgs
→ build_agent's create_task wrapper
→ tools.create_task
→ policy.check
→ idempotency.acquire
→ domain.create_task + domain.write_events
→ idempotency.complete + commit
```

Use the pinned, symbol-level links in `TRELLIS_CODE_MAP.md` under **Day 1 — Agent, state, tools, loop, and authority**. Before opening the code, predict which component chooses the action, which component has authority to allow it, what state changes, what evidence is written, and what a repeated identical tool call should do.

## Deterministic implementation — CORE

Build only after the Day 1A quiz passes:

```text
deterministic model-decision stub
→ explicit while/step loop
→ one read-only deterministic tool
→ tool-result observation
→ explicit stop condition
→ trace record
```

This is Patches 1–4 in `IMPLEMENTATION_PLAN.md`.

Do **not** add memory, RAG, LangGraph, CrewAI, a database, or a network call
here. The deterministic tool comes first so the loop can be understood with no
networking in the picture.

Trace it, run one changed input, and force one failure before going further.

---

## External API boundary — CORE

Only once the deterministic loop above traces correctly.

The point of this segment is one boundary, not API development:

```text
agent decision
→ proposed tool call
→ application validates input
→ tool constructs HTTP request
→ external API
→ HTTP response
→ validate/interpret response
→ tool result
→ agent observation
→ next agent decision
```

### Fundamentals — CORE

Be able to explain:

```text
API / API boundary
client vs server
request vs response
HTTP
GET
endpoint / URL
path parameter vs query parameter
status code, success vs non-success
JSON response body
parsing the body
timeout
network/transport failure
HTTP error response
malformed/unexpected response data
input validation before the request
response validation after the request
external data as observation/evidence, not authoritative state
```

See `FUNDAMENTALS.md` section C2.

Then draw, on paper:

```text
request → response → validation → tool result → observation
```

and state the tool contract — input, output, state read/written, authority
owner, external dependency, stop condition, failure behavior, evidence — before
any code exists.

### Quiz 1B — CORE

Take the Day 1B quiz from `QUIZ_PROTOCOL.md`. Do not inspect or write the API
tool until it passes.

### Implementation — CORE

One patch only. This is Patch 5 in `IMPLEMENTATION_PLAN.md`:

```text
one public read-only endpoint, no credentials
one GET request
at most one simple input
explicit timeout
input validation before sending
status-code check
JSON parse + minimal shape validation
bounded result returned to the agent
```

Do **not** add an API server, FastAPI, a write method, OAuth, API keys,
retries, pagination, webhooks, a generic client abstraction, a database, or a
frontend.

### Failure demos — CORE

Deliberately produce and inspect at least:

1. one network/transport failure (unreachable host or a very small timeout);
2. one non-success HTTP response (a well-formed input the service does not have).

Then name which of the five failure kinds in `FUNDAMENTALS.md` section C2 each
one was, and what evidence in the trace proves it.

### Related to Trellis — after the failure demos

Trellis reaches exactly one external service, Linear, and funnels every outbound
call through one function. Use `TRELLIS_CODE_MAP.md` under **Day 1B — The
external API boundary** to see the same five failure kinds in code you own,
plus three things a public postal-code lookup cannot show: a `200 OK` that is
still a refusal, one timeout with a deliberate no-retry rule, and an error
object that must not be logged whole.

Predict the four transfer-check answers before opening `linear_agent_api.py`.

## Exit test — CORE

Close the code. From memory:

1. draw the loop and say what state changes after every step;
2. draw the full request/response path end to end;
3. distinguish tool-input validation failure, network/transport failure,
   HTTP/API error, response-shape/data failure, and agent-loop/control-flow
   failure.

## If Day 1 runs long

Cut in this order, and stop as soon as you are back inside the timebox:

```text
1. the optional live-LLM swap (it is already the lowest-priority patch)
2. writing the API tool yourself — inspect and trace a supplied one instead
3. the deterministic loop's optional extra trace fields
```

Never cut the API concepts, the Day 1B quiz, or the two failure demos. Per
`CLAUDE.md`, implementation scope is reduced before conceptual coverage.

If the network is unavailable, the concepts, the quiz, the transport-failure
demo, and the exit test all still work; substitute a recorded response body for
the success path.

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

## Related to Trellis

Use `TRELLIS_CODE_MAP.md` under **Day 2 — Context, state, memory, evidence, and RAG**.

The most concrete Trellis example is a second user turn: `runs.create_turn` inherits server-owned canonical history, `handle_agui_request` ignores a browser-supplied transcript as authority, and `_project_prior_turn_history_for_model` changes the model's view without rewriting the durable record. Then compare that path with `get_task_history` and `resolve_task_reference`, which retrieve structured PostgreSQL evidence.

Be precise about the boundary: Trellis does **not** contain embeddings, a vector database, or a RAG pipeline. Explain which Day 2 categories Trellis does demonstrate, then state what new stages a real RAG path would need.

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

For the tool-failure scenario, reuse the Day 1 API tool and treat the external
failure kinds separately — transport failure, non-success HTTP status, and
bad/unexpected response shape are three different scenarios wearing one name.
This adds no new implementation; the failures were already demonstrated on
Day 1.

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

## Related to Trellis

Use `TRELLIS_CODE_MAP.md` under **Day 3 — Reasoning, multi-agent boundaries, evaluation, and safety**.

Trace one destructive request through the framework approval interrupt, the server-owned approval row, continuation resolution, and the deterministic policy recheck. Then map the five evaluation scenarios above to the linked Trellis tests.

Do not call Trellis multi-agent merely because it constructs browser and Linear agent profiles. They share one prompt, tool kernel, and state boundary and do not hand work to each other. Use that single-agent baseline to explain exactly what roles, handoff state, coordination, and termination rules a genuine second agent would add.

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

## Related to Trellis

Use `TRELLIS_CODE_MAP.md` under **Day 4 — Framework mapping and capstone-level trace**.

Translate Trellis back from Pydantic AI and AG-UI vocabulary into ordinary mechanisms: state, action, decision, loop, termination, authority, and evidence. Then narrate the complete `create_task` path and, for every boundary, state its input, output, mutable state, authority, and failure behavior.

For the mock transfer, design—but do not automatically implement—a read-only “list overdue tasks” behavior. Predict where its typed contract, model-visible tool, deterministic query, replay evidence, and tests would belong before opening the linked code.
