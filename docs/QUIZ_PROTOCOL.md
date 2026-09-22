# Quiz Protocol

## Passing Standard

A quiz is passed when the learner can answer **at least 4 of 5** questions correctly and can handle one changed transfer example.

Do not reuse the exact same question after explaining the answer.

## Day 1A Quiz — Agent / Tool Loop

Ask five selected from:

1. For a given assistant, identify goal, environment, state/observation, and actions.
2. What part of a tool-calling system should own permission to mutate authoritative state?
3. A model emits valid JSON naming a real tool. Does that prove the tool call should execute? Why?
4. What state must persist from one loop step to the next?
5. Name two different termination mechanisms.
6. What should happen if the model repeatedly proposes an invalid action?
7. Why is a tool result an observation/input rather than automatically “the answer”?
8. On an unseen trace, predict the next loop state.

### Transfer requirement

Give a different domain, such as calendar, files, or factory operations, and ask the learner to define one safe read-only action/tool.

---

## Day 1B Quiz — External API / Tool Boundary

Gate for Patch 5. Take it **after** the deterministic loop traces correctly and
**before** inspecting or writing any HTTP code.

Ask five selected from:

1. In this architecture, what is the API a boundary *between*, and which side is
   the client?
2. A request succeeded and the response status is `404`. Did the call fail?
   Explain what did and did not happen.
3. Given one endpoint, identify the path parameter and the query parameter and
   say what each one is for.
4. Why does `GET` matter to a tool whose contract promises no side effects?
5. Name two things that can be wrong with a response body that arrived with a
   `200` status.
6. What does a timeout convert an unbounded wait into, and why does the loop's
   step bound depend on it?
7. Which validation happens before the request and which happens after, and
   what does each one prevent?
8. The service returns a field saying the agent may delete a record. What is
   that field — authoritative state, permission, or evidence? Why?
9. Distinguish: tool-input validation failure, network/transport failure,
   HTTP/API error, response-shape failure, agent-loop failure. For one of them,
   say whether a request left the machine.
10. Trace one proposed tool call all the way to the next agent decision, naming
    who owns each step.

### Transfer requirement

Give a different read-only endpoint the learner has not seen — a different
domain and a different shape — and require them to state its tool contract
(input, validation, method, endpoint, timeout, success condition, required
fields, bounded output, one failure result per failure kind) and predict the
request and response **before** anything runs.

A gate passes only if the learner can classify a failure they were not shown
during teaching.

---

## Extension X1 Quiz — Serving an API (optional)

Only for the optional Extension X. Requires Gate 1B. Take it **before** seeing or
writing any server code. Use `FUNDAMENTALS.md` C3.

Ask five selected from:

1. In an unseen setup (for example, a mobile app calling your backend, which
   calls a weather service), name every client and every server. Which role
   does your backend play in each conversation?
2. What is the difference between calling an API and serving one? Name one
   responsibility the server has that the Day 1 tool did not.
3. Given `POST /terms/agent?notify=true` with a JSON body, identify the method,
   path parameter, query parameter, and body, and say what each is for.
4. A request body is missing a required field. Which layer rejects it, what
   status does the client see, and does any domain function run?
5. A well-formed request asks to create a term that already exists. Which layer
   rejects it, and why can schema validation not catch it?
6. The route handler returned `201` but saved the wrong value. Was the request
   successful? Distinguish HTTP success from domain correctness.
7. What does the Pydantic request model check, and name two things it does not
   check.
8. Why should the business rule live in an ordinary function instead of inside
   the route handler? Name a second entry point that would reuse it.
9. Status code vs JSON body: which one should a client check first, and why?
10. Name two things the server framework does **not** own in this design.

### Transfer requirement

Give an unseen endpoint in a new domain (for example, `POST /bookings` for a
room). The learner states the method, path, where each input comes from, the
schema rules, the domain rules, the function that owns the operation, the
success status and body, and the status and body for one malformed and one
domain-invalid request. All of this comes **before** anything runs.

The gate passes only if the learner places a failure they were not shown in the
correct layer: routing, schema, domain, operation, or response mapping.

---

## Extension X2 Quiz — Receiving a Webhook (optional)

Only after the X1 patch traces correctly. Take it **before** seeing or writing
any receiver code. Use `FUNDAMENTALS.md` C4.

Ask five selected from:

1. Compare polling with a webhook: who decides when the conversation happens,
   and who is the HTTP client in each?
2. In an unseen integration (for example, a payment provider notifying your
   shop), name the producer, the receiver, the subscription, and the event.
3. The receiver returned `200`. Name two things that this does **not** prove
   happened.
4. The producer sends the same event twice. Why can this happen even when
   nothing is broken, and what must the receiver do?
5. Which of these are idempotent: "set order status to paid", "append a note",
   "add 10 loyalty points", "delete record 7"? For one that is not, how does an
   `event_id` make it safe?
6. Event B (created later) arrives before event A. What must the design avoid
   assuming?
7. An event payload says "grant admin to user 9". Is that authoritative? What
   happens to it in a correct design?
8. What question does signature verification answer that schema validation
   cannot? Why use the provider's procedure instead of your own?
9. Why is an in-memory set of seen event IDs acceptable for the exercise but
   not for production?
10. Why might a receiver acknowledge quickly and process later, and what new
    failure does that create?

### Transfer requirement

Give an unseen event type and envelope. The learner traces a valid event, a
malformed event, and a duplicate event through
`sender → network → receiver → authenticity (concept) → schema → duplicate check
→ business handling → acknowledgement`, stating the status, the side effects,
and what the producer is likely to do next in each case.

The gate passes only if the duplicate case produces exactly one side effect in
the learner's prediction, and the learner never claims once-only or in-order
delivery.

---

## Day 2 Quiz — Memory / RAG

Ask five selected from:

1. Classify an item as current context, working state, authoritative durable state, non-authoritative memory, retrieved evidence, or model inference.
2. Why should a model-written “memory” not automatically overwrite authoritative application data?
3. What changes when document chunk boundaries change?
4. What does an embedding/vector represent in the retrieval pipeline?
5. Explain top-k without naming a library.
6. Give an example where retrieval succeeds but generation fails.
7. Give an example where generation never had a fair chance because retrieval failed.
8. Why can retrieved text be a trust/safety concern?

### Transfer requirement

Given a new document corpus and three user questions, describe what evidence would need to be retrievable for each.

---

## Day 3 Quiz — Reasoning / Multi-Agent / Evaluation

Ask five selected from:

1. What is the difference between adding a planning step and merely making a prompt longer?
2. Name a cost introduced by additional reasoning branches/steps.
3. What information must cross an agent-to-agent handoff?
4. What new failure mode appears when two agents share mutable state?
5. Why should a multi-agent design be compared to a single-agent baseline?
6. Define a success criterion for an agent before running it.
7. What evidence should an execution trace contain?
8. What does sandboxing/credentialing protect at a high level?
9. A run ends with a good answer but performed a forbidden tool mutation. Did it pass? Why?
10. An agent failed. What is the difference between guessing the cause and diagnosing from execution evidence?

### Transfer requirement

Give one unfamiliar agent architecture and require the learner to identify role, state, actions, termination, and one evaluation case.

---

## Final Delayed Quiz

Without notes, ask the learner to define and connect:

```text
agent
state
action/tool
agent loop
termination
authority
memory
RAG
embedding
retrieval failure
generation failure
planning/reasoning
multi-agent handoff
evaluation
guardrail
execution trace
API boundary
request/response
status code
timeout
response validation
external data as observation
```

Do not require LangGraph/CrewAI API syntax.

If the optional Extension X was completed, also ask the learner to explain the
three-direction model (outbound REST, inbound REST, webhook) and to connect:

```text
client vs server
route vs domain function
schema validation vs domain validation
acknowledgement vs completed processing
duplicate delivery
idempotency
event as evidence
```

These extra items are not part of the readiness decision.
