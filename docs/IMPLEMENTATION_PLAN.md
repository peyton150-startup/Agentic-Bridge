# Minimal Implementation Plan

## Purpose

The sprint needs **one small implementation** so the concepts are not detached theory. It does not need a complete agent platform.

That remains true of the required core (Patches 1–5). The optional Extension X
patches near the end of this file are a separate, self-contained exercise. They
do not change the agent or its tools.

## Build Only This Core

```text
AgentState
ModelDecision (deterministic stub first)
one read-only deterministic Tool
AgentLoop
TraceEvent
one read-only external HTTP Tool (added last, same contract)
```

Conceptual flow:

```text
initial request/state
→ model-decision function
→ either final response OR proposed tool action
→ validate proposed action
→ execute read-only tool
→ record observation/result
→ update loop state
→ next step
→ stop at final answer or max-step bound
```

## Order

### Patch 1 — State and decision contract

Before code, pass Day 1 concept gate.

Add only the data needed to represent:

```text
current step
request
observations/tool results
model decision
completion state
```

Do not add persistence.

### Patch 2 — One read-only action/tool

Before code, learner defines:

```text
name
input
output
allowed side effects = none
validation
failure result
```

Use a deterministic tool so the execution path is easy to trace. No network
call belongs in this patch: the loop must be understandable before transport
failure is a possibility.

### Patch 3 — Bounded loop

Add:

```text
step
→ decide
→ validate/execute if tool
→ record observation
→ continue/finish
```

Require an explicit maximum-step termination.

### Patch 4 — Trace

Record enough to explain the run:

```text
step number
input/state summary
decision kind
tool/action if any
validation result
tool result/failure
termination reason
```

### Patch 5 — One external read-only HTTP tool

Requires Patches 1–4 traced, and the Day 1B quiz in `QUIZ_PROTOCOL.md` passed.

This patch exists to make one boundary concrete:

```text
validated input
→ HTTP request
→ external service
→ HTTP response
→ response validation
→ bounded tool result
→ observation
```

Before code, the learner states the tool contract and predicts the exact
request and the expected response:

```text
name
input (one simple value)
input validation rule
method               = GET
endpoint/URL shape   (which part is path, which part is query)
timeout
allowed side effects = none
success condition    (which status codes count)
parse step
required response fields
bounded output returned to the agent
failure result for each failure kind
```

Choose the endpoint to fit these constraints:

```text
public and read-only
no credentials or API key
one GET request
a small JSON response
a documented non-success status for a well-formed input the service does not have
```

A public postal-code lookup of the form `https://api.zippopotam.us/us/{code}`
satisfies all of them: the code is a path parameter, a valid-looking but
nonexistent code returns `404`, and the body is a few fields. Any equivalent
endpoint is fine. The endpoint is an exercise fixture, not a curriculum source;
the source rule in `SOURCES.md` governs teaching claims, not the address the
exercise happens to call.

The patch must include, and no more than:

```text
input validation before the request is built
an explicit timeout
a status-code check
a JSON parse guarded against a body that is not JSON
a minimal check that the fields being read are present
a bounded result (a short summary, not the whole body)
a distinct failure result per failure kind
```

Then demonstrate, deliberately:

```text
one network/transport failure
one non-success HTTP response
```

and classify each against the five failure kinds in `FUNDAMENTALS.md`
section C2.

### Optional Patch 6 — Live LLM swap

Lowest priority in the sprint. Only if time remains after Patch 5.

The learner first states what behavior is provider-specific and what application contract must remain stable.

Do not redesign the core around the provider.

If Day 1 is running long, this patch is the first thing to cut. Patch 5 teaches
the same external-boundary lesson — request, response, timeout, failure
classification — without provider SDK syntax becoming the lesson.

#### Candidate provider: TypeSafe (optional, not curriculum)

TypeSafe returns decisions, not text, so it can replace only the **model-decision function**:

```text
Choice: final answer | call <tool name>
optional Choice per tool argument (closed sets only)
```

Before swapping, the learner predicts:

```text
what changes:        the decision function body
what must not change: AgentState, loop, validation, tool, trace
what code still owns: the final answer text, every free-text/number/date argument
```

Traps to find from evidence:

- an argument with no question silently keeps its default, so validation is still required;
- `confidence` is a new input — decide in code what happens when it is low (for example, stop with termination reason `low_confidence`).

If the swap forces changes outside the decision function, the contract in `ARCHITECTURE_CONTRACT.md` §5 was leaking. Record that as the finding.

SDK syntax lives in `SOURCES.md` → Non-Curriculum Tooling Reference and is not a lesson.

## Optional Extension X — Serving an API and Receiving a Webhook

Not part of the core. Only after Gate 1B has passed and the core days are safe.
The concepts are in `FUNDAMENTALS.md` C3–C4, the gates in `QUIZ_PROTOCOL.md`
(Extension X1/X2), and the time budget in `SPRINT_PLAN.md`.

The extension adds one direction per patch:

```text
outbound REST  — Patch 5 (core, already built)
inbound REST   — Patch X1
webhook        — Patch X2
```

It does **not** touch `tiny_agent.py` or `api_tool.py`. It has its own domain
module. One reason: `tiny_agent.py` runs its demo when imported. The main reason
is that the lesson is "HTTP adapter ≠ business logic," and that is easiest to
see in a module written for it.

### Dependencies

`fastapi`, `httpx` (required by `TestClient`), and `pytest`. Nothing else. For
syntax, use only the official FastAPI pages listed in `SOURCES.md`.

### Patch X1 — A minimal FastAPI service

Requires the Extension X1 quiz passed.

Before code, the learner predicts, for each endpoint:

```text
method
path
where each input comes from   (path / query / body)
schema validation that runs
domain validation that runs
the function that owns the operation
expected status code
expected response body
what happens for invalid input
```

Shape (names may change; the split may not):

```text
plain-Python domain module (no FastAPI import)
  an in-memory glossary: term → definition
  a domain check for a term (letters only, bounded length)
  get_term(term)          → definition, or a "not found" result
  add_term(term, text)    → added, or a domain error (invalid / already exists)

FastAPI adapter module
  GET  /health            → 200, a tiny fixed JSON body
  GET  /terms/{term}      → 200 with the definition, or 404
  POST /terms             → request model {term, definition}
                            201 on creation
                            422 on a malformed body (framework)
                            400 on a domain-invalid term
                            409 if the term already exists
```

Route handlers only receive input, call a domain function, and map the result or
error to a status. They must not contain the business rules.

Target: about 25–35 nontrivial lines across both modules. No database, no auth,
no async code beyond what FastAPI requires, no frontend.

### Patch X1 tests

`TestClient` + pytest. Deterministic, no network, in-memory state reset before
each test. Tests must prove behavior:

```text
GET /health                         → 200 and the expected body
POST /terms valid                   → 201, then GET /terms/{term} → 200 with it
GET /terms/{unknown}                → 404
POST /terms missing a field         → 422, glossary unchanged
POST /terms domain-invalid term     → 400, glossary unchanged
POST /terms existing term           → 409, original definition unchanged
```

"Glossary unchanged" is the important assertion. The status alone does not prove
that nothing happened to state.

### Patch X2 — A local, simulated webhook receiver

Requires X1 traced and closed-code explained, and the Extension X2 quiz passed.

No real provider is used. The tests act as the producer.

```text
POST /webhooks/events
envelope   {event_id, event_type, payload}
known type "term.suggested", payload {term, definition}
side effect: append the suggestion to an in-memory review queue
```

The side effect is deliberately **not idempotent**, since appending twice gives
two entries. That way deduplication by `event_id` is what prevents the
duplicate, not an accident of the domain. The suggestion goes to a review queue,
not straight into the glossary, because an external event is evidence rather
than authority.

Before code, the learner predicts the status, response body, and queue contents
for:

```text
1. a valid event
2. a malformed envelope
3. the same valid event delivered twice
4. an unknown event_type   (decide beforehand: reject, or acknowledge and ignore,
                            and say what the producer will do next in each case)
```

The receiver must:

```text
validate the envelope before any state changes
check event_id against an in-memory set of applied IDs
apply the side effect at most once per event_id
record the event_id only after the side effect is applied
return a 2xx acknowledgement for both accepted and duplicate events
```

State this in a comment where the set is defined: the in-memory set is **not**
durable production deduplication. It is lost on restart and not shared across
processes.

Target: about 15–25 nontrivial lines. No signing code, no queue, no retries, no
background task, no persistence.

### Patch X2 tests

```text
valid event                  → 2xx, review queue has exactly 1 entry
malformed envelope           → 422, review queue empty
same event_id sent twice     → both 2xx, second marked duplicate,
                               review queue still has exactly 1 entry
```

### After each extension patch

The standard after-code gate from `TEACHING_CONTRACT.md` applies, plus:

```text
closed-code: redraw the inbound (X1) or webhook (X2) path and name, at each step,
             what FastAPI did and what your own Python did
altered variant: one small change made by the learner, predicted first
             (e.g. X1: add a query parameter; X2: add a second event type)
failure: classify one unseen failure against the C3/C4 failure lists
```

## Do Not Build During the Core Sprint

- database memory;
- vector DB;
- hosted observability;
- LangGraph implementation;
- CrewAI implementation;
- multi-agent runtime;
- frontend;
- authentication;
- deployment.

These are either CMU course topics or unnecessary for readiness. Extension X
does not lift any of them. It still has no database, no authentication, no
deployment, and no frontend.

Also excluded from Extension X: OAuth, Redis/Celery/Kafka or any queue, a generic
event bus, GraphQL, gRPC, WebSockets, server-sent events, microservices, cloud
deployment, and production webhook signing without a real provider
specification. Those are possible later extensions, not bridge work.

Specifically excluded from Patch 5, so the API exercise stays one boundary
rather than an API course. The first item and "webhooks or callbacks" are still
excluded from Patch 5 and from the core. They now exist **only** as the optional
Extension X above, which is a separate exercise taken after Gate 1B. The reason
for the exclusion has not changed: the outbound boundary must be understood on
its own before the direction is reversed.

- an API server of any kind, including FastAPI;
- `POST`/`PUT`/`PATCH`/`DELETE`;
- OAuth or any auth flow;
- API keys, unless genuinely unavoidable;
- retries or backoff;
- pagination;
- webhooks or callbacks;
- a generic/reusable API client abstraction;
- persistence of responses;
- any dependency beyond what one GET request needs.

## Day 2 / Day 3 Implementation Style

Memory, RAG, reasoning, and multi-agent topics may remain **paper exercises / tiny isolated calculations** during this bridge.

That is deliberate. The goal is to make CMU's abstractions understandable, not to prebuild the course.
