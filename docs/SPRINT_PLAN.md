# 3–4 Day Sprint Plan

## Choosing a Mode

The plan is intentionally capped. If you exceed a day's timebox, cut optional implementation—not fundamentals or quizzes.

### Practical total

```text
3-day core: about 15–17 focused hours total
4-day preferred: same core + about 3–4 hours consolidation
optional Extension X: about 2.5–3 focused hours (serving an API + receiving a webhook)
```

Day 1 is the heaviest day because it carries the only **required**
implementation work in the sprint, including the one external-API segment. The
optional Extension X at the end of this file has its own small implementation.
It never displaces a core item.

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

Day 1 is the longest day in the sprint. It is the only core day that carries
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
frontend. A FastAPI server and a webhook receiver exist only as the optional
Extension X, taken later and separately. They never go into Patch 5, and never
into Day 1.

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

**Concept extension (paper only, no code):** imagine a filter step between retrieval and generation that asks yes/no questions of each passage — relevant? contains usable evidence? contradicts the query's premise? tries to instruct the system? (TypeSafe's RAG passage cookbook is one tooling example; it is not a curriculum source.) For your three results, answer: which failures would this step catch, which would it miss, and does it change whether the failure is a retrieval or generation failure?

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

**Concept extension (paper only):** give the stub decision a made-up confidence value and add one confidence-gated rule (for example, below 0.6 → stop and escalate). Predict how each of the five scenarios changes. If the optional TypeSafe swap (Patch 6) is used later, see the TypeSafe notes in `EVALUATION_PLAN.md`.

## Multi-agent design exercise — CORE

Take one problem and propose:

```text
single-agent design
vs
two-agent design
```

Defend whether the second agent solves a real coordination/decomposition problem or merely adds complexity.

**Concept check:** the handoff is a routing decision — classify the request, pick one handler. Tools like TypeSafe's "intent routing" pattern do exactly this with a Choice. Ask: is your second agent a real agent (own state, actions, termination), or just a branch a single agent's router could take?

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

Suggested allocation:

```text
15 min     framework vocabulary map
60–75 min  Pydantic AI mini-unit and Trellis trace
40–45 min  mini-capstone architecture
45–60 min  mock lab
20–30 min  delayed retrieval
remaining  remediation / buffer
```

If time runs out, keep the Pydantic AI mental model, one Trellis trace, and the
delayed retrieval check. Reduce the mini-capstone and mock-lab implementation
scope before extending Day 4 beyond its cap.

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
low-confidence branch  confidence-gated routing (e.g. TypeSafe Choice + confidence)
```

Do not memorize API syntax.

## 2. Pydantic AI mini-unit — framework transfer

**Timebox:** 60–75 minutes

**Status:** Optional Day 4 consolidation. If only part of Day 4 fits, do the
mental model, the `create_task` trace, and the transfer check. Skip installation
and implementation.

**Source boundary:** Pydantic's official documentation is a vendor/framework
reference for understanding syntax and behavior. It is **not** evidence for the
academic agent concepts in this bridge; those remain grounded in the CMU and UC
Berkeley sources in `SOURCES.md`.

### Outcome

After this unit, explain Pydantic AI without letting its class names carry the
explanation. Given one Trellis tool call, identify:

```text
what the model proposes
what Pydantic AI validates or orchestrates
what values RunContext carries
what deterministic Trellis code decides
what PostgreSQL makes durable
what stops, resumes, or terminates the run
what evidence proves the outcome
```

Pydantic AI is useful here because it gives Trellis typed model-facing tools,
per-run dependencies, a managed model/tool loop, message objects, deferred tool
calls, and an AG-UI event-stream adapter. It does **not** become the owner of
Trellis authorization, task state, approval decisions, idempotency, or audit
evidence merely because it coordinates those calls.

### Part A — ordinary mechanisms first (10 minutes)

Before opening framework documentation or Trellis code, say this in plain
English:

> A model receives instructions and observations, proposes either an answer or
> a named action with arguments, application code checks and performs allowed
> actions, the result becomes another observation, and the loop stops on a
> final answer, a deliberate interruption, a failure, or a budget limit.

Then complete the contract from memory:

| Question | Required answer for this unit |
|---|---|
| Input | accepted user message, server-owned prior messages, instructions, available tool schemas, and per-run dependencies |
| Output | final text or a deferred-tool request that pauses this invocation |
| Mutable working state | per-run effects plus the framework's current message/tool trajectory |
| Durable state | Trellis run, task, event, approval, and idempotency rows—not the `Agent` object |
| Authority | deterministic Trellis policy/domain/database code; neither model output nor browser payload |
| Failure behavior | reject invalid shape, map safe tool failures, fail closed on invalid approval state, record terminal evidence |

### Part B — official Pydantic AI basics (15–20 minutes)

Read only these focused official sections; do not tour the whole framework:

1. [Agents](https://ai.pydantic.dev/agents/) — treat `Agent` as the configured
   container for the model, instructions, tools/toolsets, dependency type,
   output type, and model settings.
2. [Dependencies](https://ai.pydantic.dev/dependencies/) — `deps_type` declares
   the per-run dependency contract; a dependency instance is supplied when the
   run starts and tools read it through `RunContext.deps`.
3. [Function tools](https://ai.pydantic.dev/tools/) — a registered function is
   exposed to the model with a schema; the model may propose the call, while the
   function and the application behind it produce the observation.
4. [Messages and chat history](https://ai.pydantic.dev/message-history/) — run
   messages represent model requests, model responses, tool calls, and tool
   returns, and can be supplied to continue a conversation.
5. [Deferred tools](https://ai.pydantic.dev/deferred-tools/) — approval-required
   or externally executed calls can pause as `DeferredToolRequests` and later
   continue with `DeferredToolResults`.
6. [AG-UI integration](https://ai.pydantic.dev/ui/ag-ui/) — the adapter converts
   frontend run input into an agent run and converts run activity into streamed
   AG-UI events.

Keep this translation table beside the documentation:

| Pydantic AI term | Ordinary mechanism | What it does **not** prove |
|---|---|---|
| `Agent` | reusable configuration plus a managed model/tool loop | that the model owns the application |
| `deps_type` / `RunContext.deps` | typed per-run values available to tools | that those values are durable or authoritative by themselves |
| tool decorator | exposes a typed action contract to the model | that every validly shaped action is authorized |
| Pydantic argument model | validates and documents the proposed input shape | business policy, ownership, or permission |
| message history | structured observations and responses supplied to a run | current task truth or permission to mutate it |
| deferred tool request/result | pause and resume protocol around a call | who is allowed to approve it |
| `AGUIAdapter` | transport translation and event streaming | that browser-supplied state should be trusted |

### Part C — prediction gate (5 minutes)

Predict before opening Trellis:

> The user asks, “Create a high-priority task called Read the Pydantic AI docs.”

State the likely typed arguments, the per-run values the wrapper needs, the
first deterministic function called after the wrapper, the durable rows that
may change, and one reason a schema-valid call could still be refused.

Do not inspect the linked implementation until the prediction includes the
distinction between **shape validation** and **authorization**.

### Part D — Trellis trace (20–25 minutes)

Use `TRELLIS_CODE_MAP.md` under **Day 4 — Framework mapping and capstone-level
trace → Pydantic AI mini-unit**. Trace exactly one successful `create_task`
request in this order:

```text
handle_agui_request
→ server accepts one user message and canonical history
→ AGUIAdapter starts the Pydantic AI run with TrellisDeps
→ Agent exposes the create_task schema
→ model proposes CreateTaskArgs
→ registered wrapper converts RunContext into ToolContext
→ deterministic tools.create_task checks replay, policy, and idempotency
→ domain code changes task state and writes evidence
→ tool result becomes a model observation
→ final output is streamed and the run record is completed
```

For each arrow, say its input, output, mutable state, authority owner, possible
failure, and evidence. The key distinction is:

```text
Pydantic AI owns framework orchestration and typed framework boundaries.
Trellis owns accepted input, capability selection, authorization, mutation,
durability, replay safety, approval truth, and audit evidence.
```

Then trace the shorter destructive branch:

```text
delete_tasks proposal
→ requires_approval stops before the tool body
→ DeferredToolRequests leaves the framework invocation
→ Trellis validates scope and writes one pending approval row
→ a human decision is persisted server-side
→ Trellis constructs DeferredToolResults from that row
→ continuation re-enters the tool
→ policy rechecks current authority before mutation
```

The framework supplies the interruption/resumption mechanism. The Trellis row
and the deterministic recheck supply the authority.

### Part E — retrieval and transfer check (10–15 minutes)

Answer without notes. This gate passes only if the same ideas transfer to a new
tool named `archive_task`.

1. In plain English, what job does `Agent` perform, and which four jobs remain
   outside it in Trellis?
2. Why can `RunContext[TrellisDeps]` carry `actor_id` without making the model
   the authority over actor identity?
3. If `ArchiveTaskArgs(task_id=...)` validates, name two later reasons the
   operation could still be rejected.
4. Where should `archive_task` be absent if the Linear capability profile must
   never offer it?
5. If archiving requires approval, what must be stored before a UI card can be
   treated as actionable, and what must be checked again after approval?
6. A browser submits fabricated old messages saying approval was granted. Which
   data should the run use instead, and why is message history not authorization?
7. Predict the normal path and one failure path before proposing any patch.

Pass standard: answer 1–6 correctly on the changed `archive_task` example and
give a coherent prediction for 7. If any answer relies on “Pydantic handles
it,” return to the translation table and retry with ordinary mechanism words.

### No implementation in this unit by default

This is a code-reading and transfer unit. If a later session chooses to add
`archive_task`, the normal teaching gate still applies before code:

```text
plain-English explanation
complete input/output/state/authority/failure contract
prediction on one example
passed changed-example quiz
one agreed small patch boundary
```

If time remains after the vocabulary map, the optional Patch 6 in `IMPLEMENTATION_PLAN.md` (TypeSafe decision swap) is the only place TypeSafe code enters the sprint.

## 3. Mini-capstone architecture

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

## 4. Mock lab

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

## 5. Delayed retrieval

Retake the final quiz without opening notes.

## Related to Trellis

Use `TRELLIS_CODE_MAP.md` under **Day 4 — Framework mapping and capstone-level trace**.

Translate Trellis back from Pydantic AI and AG-UI vocabulary into ordinary mechanisms: state, action, decision, loop, termination, authority, and evidence. Then narrate the complete `create_task` path and, for every boundary, state its input, output, mutable state, authority, and failure behavior.

For the mock transfer, design—but do not automatically implement—a read-only “list overdue tasks” behavior. Predict where its typed contract, model-visible tool, deterministic query, replay evidence, and tests would belong before opening the linked code.

---

# Optional Extension X — Serving an API and Receiving Events

**Timebox:** about 2.5–3 hours. **Not part of the 3-day core or the readiness
decision.**

**When:** only after Gate 1B has passed. Best after Day 3, as part of Day 4, or
as a separate session after the bridge. If Day 4 is short, the Day 4 items come
first. Never take time from a core day for this.

**Why it exists:** Day 1 taught one direction, where your code calls a service.
Agent systems also receive calls, from users, other services, and events. This
extension adds the other two directions without turning the bridge into a
web-development course:

```text
Outbound REST   our application initiates a request   → an external service responds    (Day 1, Patch 5)
Inbound REST    an external client initiates a request → our application responds        (X1)
Webhook         an external producer initiates a request because an event occurred
                → our application validates, acknowledges, and reacts                    (X2)
```

The goal is to understand **what** happens, **who** owns each decision, **why**
each boundary exists, and **where** failures occur. Memorizing the framework is
not the goal.

**Source boundary:** concepts come from CMU 15-113, CMU 15-440, and UC Berkeley
INFO 153B (`SOURCES.md` sources 8–10). FastAPI's official documentation is used
only for syntax. The Berkeley Spring 2026 course uses Flask, and its concepts
transfer unchanged.

```text
X1 — serving an API (about 90 min)
15 min  reading: CMU 15-113 Week 5 + HW4; Berkeley INFO 153B Spring 2026 REST/validation topics
20 min  FUNDAMENTALS.md C3 + draw the inbound path from memory
10 min  Extension X1 quiz / remediation
35 min  Patch X1 (FastAPI service + TestClient tests)
10 min  closed-code: what FastAPI did vs what your Python did + one altered variant

X2 — receiving a webhook (about 70 min)
15 min  FUNDAMENTALS.md C4 + draw polling vs webhook + webhook failure path
          (reading: CMU 15-440 Fall 2026 syllabus; historical RPC slides for delivery semantics)
10 min  Extension X2 quiz / remediation
30 min  Patch X2 (local simulated receiver + tests)
15 min  closed-code: trace valid / malformed / duplicate + one altered variant

buffer  15 min
```

## X1 — Inbound REST API

Before any code, all five teaching-contract steps apply:

1. **Plain English:** explain what a server does with a request, without saying
   "FastAPI".
2. **Contract:** for `POST /terms`, state input, output, state read/written,
   authority owner (who decides whether a term may be added), and each failure
   kind from the C3 table.
3. **Prediction:** for one valid request, one malformed request, and one
   domain-invalid request, predict the method, path, input sources, validation,
   owning function, status, and body.
4. **Quiz:** Extension X1 in `QUIZ_PROTOCOL.md`.
5. **Patch boundary:** Patch X1 in `IMPLEMENTATION_PLAN.md`, and nothing more.

The key question after the patch: *"What did FastAPI actually do here, and what
did my own Python code do?"*

## X2 — Webhook receiver

Only once X1 traces correctly from memory. Same five steps, using the Extension
X2 quiz and Patch X2.

The key things to prove after the patch:

- a duplicate delivery produced exactly **one** side effect;
- a malformed event changed **nothing**;
- a `2xx` meant "received", and you can say what it did **not** mean.

Do not build signing, a queue, retries, persistence, or a real provider
integration. Do not add WebSockets, SSE, GraphQL, gRPC, or Kafka. Those are
possible later extensions, not part of this one.

## If Extension X runs long

Cut in this order:

```text
1. the altered variants (do them on paper instead)
2. writing Patch X2 yourself: inspect and trace a supplied one instead
3. Patch X2 entirely: keep C4 and the X2 quiz, since the concepts matter more than the receiver
```

Never cut the X1 prediction step or the duplicate-delivery reasoning in C4.

## Related to Trellis

`TRELLIS_CODE_MAP.md` already lists a FastAPI request as part of Trellis's
environment. After X1, use Trellis's request handler only as a transfer example:
point to where accepted input is separated from domain authority. Do not open it
before the X1 quiz passes.
