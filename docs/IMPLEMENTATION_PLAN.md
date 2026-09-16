# Minimal Implementation Plan

## Purpose

The sprint needs **one small implementation** so the concepts are not detached theory. It does not need a complete agent platform.

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

These are either CMU course topics or unnecessary for readiness.

Specifically excluded from Patch 5, so the API exercise stays one boundary
rather than an API course:

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
