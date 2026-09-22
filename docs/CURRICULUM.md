# Curriculum — Compressed for 3–4 Days

The original bridge used seven implementation phases. That is intentionally replaced by a **three-day core** because the purpose is readiness, not pre-completion of CMU's seven-week program.

## Day 0

Prerequisite diagnostic:

```text
Python
algorithms/data structures
LLM fundamentals
AI/agent fundamentals
```

## Day 1

```text
agent model
LLM as external/probabilistic component
tool/action contract
bounded control loop
authority
trace

then, once the deterministic loop traces:

API/HTTP boundary behind one tool
request/response, status, JSON parsing
validation before the request and after the response
timeout
five distinguishable failure kinds
external data as observation, not authority
```

## Day 2

```text
context vs state vs memory
RAG pipeline
embeddings/vector representation
retrieval behavior
retrieval vs generation failure
```

## Day 3

```text
reasoning/planning as control flow
multi-agent roles/handoffs/termination
evaluation before execution
guardrails/permissions
execution monitoring / traces
```

## Optional Day 4

```text
framework vocabulary mapping
Pydantic AI mini-unit: Agent, typed dependencies/tools, runs/history,
deferred approval, AG-UI, and the Trellis integration
mini-capstone architecture
mock CMU lab
final delayed retrieval
```

The Pydantic AI unit is a framework-transfer exercise, not a new academic
source or an API-memorization requirement. Learn each ordinary mechanism
first, read the matching official Pydantic AI documentation, and then trace
the pinned Trellis implementation in `TRELLIS_CODE_MAP.md`.

## Optional Extension X (after Gate 1B, about 2.5–3 hours)

```text
three directions: outbound REST, inbound REST, webhook
serving an API: routing, schema vs domain validation, status + JSON, thin adapter
receiving a webhook: acknowledgement vs processing, duplicates, idempotency,
                     no ordering guarantee, event as evidence, authenticity (concept)
```

Not required for readiness. Concepts come from CMU/Berkeley and syntax from the
official FastAPI docs.

See `SPRINT_PLAN.md` for the full sequence and `FUNDAMENTALS.md` for the concept checklist.
