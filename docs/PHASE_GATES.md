# Sprint Gates

## Gate 0 — CMU Prerequisites

Pass `PREREQUISITE_DIAGNOSTIC.md`.

---

## Gate 1 — Day 1 Agent / Tool Loop

Without notes:

1. Define agent, environment, state/observation, action, and goal/termination.
2. Draw the tiny loop.
3. State what the model may propose vs what the application owns.
4. Trace one tool call with concrete values.
5. Explain invalid tool input behavior.
6. Explain max-step termination.
7. On a changed domain, define one read-only tool contract.

**Pass:** mechanism is correct without framework vocabulary carrying the explanation.

---

## Gate 1B — Day 1 External API Tool Boundary

Taken after Gate 1 and after the API failure demos. Without notes:

1. Draw the full path: agent decision → proposed tool call → input validation →
   HTTP request → external service → HTTP response → response validation →
   tool result → observation → next decision.
2. Name the client and the server, and say which side you own.
3. Identify the path parameter and the query parameter in an endpoint, and say
   what each is for.
4. Explain why a `404` is a successful conversation and an unsuccessful lookup.
5. State which validation runs before the request and which runs after, and
   what each prevents.
6. Explain what the timeout bounds and why the loop depends on it.
7. Distinguish the five failure kinds — tool-input validation, network/transport,
   HTTP/API error, response shape/data, agent-loop/control-flow — and say, for a
   failure you were not shown, which one it is and what evidence proves it.
8. Explain why the response is an observation rather than authoritative state or
   a permission grant.

**Pass:** the learner can classify an unseen failure correctly and can explain
why the external call sits behind the tool boundary instead of in front of it.

Failing this gate is not a reason to extend the sprint. Record it as a CMU
watch item and continue to Day 2.

---

## Gate 2 — Day 2 Memory / RAG

Without notes:

1. Classify context, working state, authoritative state, memory, evidence, inference.
2. Draw the RAG pipeline.
3. Explain embeddings/vectors conceptually.
4. Explain how chunking/top-k can affect retrieval.
5. Distinguish retrieval failure from generation failure.
6. Explain why retrieved content is not a permission grant.
7. Complete one changed vector/retrieval example.

---

## Gate 3 — Day 3 Reasoning / Multi-Agent / Evaluation

Without notes:

1. Explain why an explicit planning/decomposition strategy changes control flow.
2. Name at least two costs of extra reasoning steps/branches.
3. Define a two-agent handoff contract.
4. Explain one multi-agent failure mode not present in the single-agent baseline.
5. Define success/failure for an unseen agent scenario before it runs.
6. Identify what an execution trace would need to diagnose a failure.
7. Explain sandboxing/credentialing at the authority level.

---

## Gate X — Optional Extension: Serving an API and Receiving Events

Only if Extension X was taken. Requires Gate 1B. **Not required for promotion.**
Without notes:

1. State the three-direction model: outbound REST, inbound REST, webhook. Say
   who initiates each and why.
2. Draw the inbound path from client to JSON response. Mark what FastAPI did
   and what your own Python did.
3. Place an unseen failure in the right inbound layer: routing, schema, domain,
   operation, or response mapping.
4. Explain why a `201` does not prove the domain operation was correct.
5. Draw the webhook path. Explain why a `2xx` acknowledgement is not completed
   processing.
6. Explain why duplicates and reordering happen without anything being broken,
   and how an `event_id` check keeps a non-idempotent side effect to one.
7. Explain why an event is evidence rather than authority, and what signature
   verification protects (concept only).

**Pass:** 6 of 7, including item 6. Failing Gate X is not a CMU watch item for
readiness purposes. Note it and move on.

---

## Final Promotion Rule

The learner does not need perfect vocabulary.

Promote to CMU readiness when they can:

```text
TRACE the tiny implementation
EXPLAIN all core concepts
TRANSFER them to one unseen example
DEFEND one architecture/evaluation decision
```

If the learner cannot do one of those, record it as a CMU watch item rather than extending the bridge indefinitely.
