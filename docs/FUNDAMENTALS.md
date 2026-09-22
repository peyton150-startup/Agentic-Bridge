# Fundamentals to Know Before CMU

This file is a **readiness checklist**, not a complete textbook.

## A. Agent Fundamentals — Berkeley CS188 + CMU agent courses

### Agent

An agent acts in an environment to pursue a goal/performance objective. For readiness, always be able to name:

```text
goal/performance measure
environment
observations/state
actions
consequences/transitions
termination or policy
```

### Planning vs reflexive/direct behavior

A direct/reflexive choice maps the current situation to an action. Planning reasons about possible action sequences or consequences before selecting what to do.

### LLM-based agent

CMU 11-768 describes LLM agents as systems using LLMs to perceive, reason, plan, and act through sustained interaction with external environments. The useful readiness idea is:

> the LLM participates in the agent; it does not erase the surrounding environment, state, tools, permissions, and termination logic.

---

## B. LLM Boundary Fundamentals — CMU Module 1 + CMU 15-213 systems perspective

Know these distinctions:

```text
model request ≠ application state
model response ≠ validated domain value
successful provider response ≠ correct task result
probabilistic output ≠ arbitrary application behavior
```

The application still needs a contract for what values it accepts and what it will do with them.

### Stable vs variable

A useful design goal is:

```text
variable model behavior
inside
stable application boundaries
```

Tests should isolate deterministic application logic from genuinely model-dependent behavior where possible.

---

## C. Tool / Action Loop Fundamentals — CMU Modules 1–2 + CS188

Think of a tool as an **action the software can execute**.

Before execution, know:

```text
who proposed it
whether that action is allowed
argument schema/validation
what state may change
what result/observation returns
what failure looks like
```

A minimal loop is conceptually:

```text
observe state/request
→ choose/propose action
→ validate
→ execute action/tool
→ receive observation/result
→ update loop state
→ continue or terminate
```

Always define a bound such as a maximum number of steps for a learning implementation.

---

## C2. External API / HTTP Tool Fundamentals — CMU Agentic AI Program (external APIs/tools) + CMU 15-213 systems/networking

Section C describes any action the software can execute. A tool that calls an external service is the **same contract**, plus one new fact: part of the work happens on a machine you do not own, reached over a network that can fail.

Do this only after the deterministic tool loop in section C is understood. Networking is a second mechanism, not a replacement for the first.

### What an API is in this architecture

An API is a published boundary that another program agrees to answer across. In an agent, that boundary sits **inside one tool**, behind the tool contract. The agent does not talk to the API; the application's tool does.

```text
client   = your application/tool — sends the request
server   = the external service — sends the response
request  = what you send (method, URL, parameters)
response = what comes back (status, body)
```

`HTTP` is the protocol both sides agree on. `GET` is the read-only method: it asks for a representation of a resource and is not supposed to change anything on the server. Choosing `GET` is how the tool's "allowed side effects = none" promise reaches across the boundary.

### Endpoint anatomy

```text
https://api.example.org/us/15213?units=metric
\___/   \_____________/\_______/\___________/
scheme        host        path      query
```

An **endpoint** is the address of a resource. A **path parameter** is part of that address (`/us/15213` — "the US postal code 15213"): it selects *which* thing. A **query parameter** (`?units=metric`) modifies or filters the request: it says *how* you want it. Both come from your input; only one is part of the resource's identity.

### Status codes

The status code is the server's verdict on the request. It is separate from whether the body contains what you wanted.

```text
2xx  success
4xx  the request was wrong (bad address, not found, not permitted)
5xx  the server failed while handling a request that may have been fine
```

`200 OK` and `404 Not Found` are both complete, successful *conversations*. Only one of them carries the data you asked for. A tool that ignores the status and parses the body anyway will hand an error page to the agent as if it were data.

### JSON response bodies and parsing

Most read APIs answer with JSON: text in a structured format that your language can turn into dictionaries, lists, strings, and numbers. Two separate things can go wrong:

```text
parsing   — the text is not valid JSON at all
shape     — it parsed fine, but the keys/fields you needed are not there
```

Valid JSON is not a promise of the right JSON.

### Timeout

A request with no timeout can hang for as long as the network lets it. An explicit timeout converts "waiting forever" into "a failure you can handle," which is what makes the loop's step bound meaningful. A tool without a timeout has an unbounded step.

### The full path, both directions

```text
agent decision
→ proposed tool call
→ application validates the input          (nothing has left the machine yet)
→ tool builds the HTTP request
→ network
→ external service
→ HTTP response (status + body)
→ tool checks the status
→ tool parses the body
→ tool validates the shape of the parsed data
→ bounded tool result
→ observation recorded in loop state
→ next agent decision
```

You should be able to draw this from memory and say, at every arrow, what crosses it and who owns the decision at that point.

### Two validations, not one

```text
BEFORE the request
  is the input well-formed and allowed?
  a bad input fails here, and no request is sent at all

AFTER the response
  did the status indicate success?
  did the body parse?
  are the fields I need present and of the expected kind?
  is the result small enough to hand back as an observation?
```

Skipping the first sends malformed or unauthorized requests outward. Skipping the second lets a stranger's output flow straight into the agent's context.

### Five distinct failure kinds

These fail in different places, produce different evidence, and call for different responses. Being able to tell them apart is the point of the exercise.

| Failure kind | Where it happens | Did a request leave? | Typical evidence |
|---|---|---|---|
| tool-input validation | application, before the call | no | rejected input + reason |
| network/transport | between client and server | yes, no usable answer | timeout, DNS failure, refused connection |
| HTTP/API error | server answered | yes | non-success status code |
| response shape/data | client, after the answer | yes | parse error, or missing/unexpected fields |
| agent-loop/control-flow | the loop around the tool | possibly many | step count, repeated identical actions, termination reason |

"The tool failed" is not a diagnosis. Naming which of these five it was is.

### Why external data is evidence, not authority

A response is a **claim made by someone else's program at one moment in time**. It is an observation the loop records, exactly like the deterministic tool's result — not authoritative application state, and never a grant of new permission. It can be wrong, stale, truncated, or hostile, and it is outside your control.

The chain of ownership does not change when a network appears in the middle of it:

```text
the model               proposes an action
the application         validates and authorizes it
the tool                performs the external interaction, bounded
the external service    returns data
the tool/application    interprets and bounds the result
the loop                decides what happens next
```

The external service is the only participant here you do not own. That is precisely why it sits behind a tool boundary instead of in front of one.

---

## Optional Extension X — Serving an API and Receiving Events

**Not part of the 3-day core.** Sections C3 and C4 are needed only for the
optional Extension X in `SPRINT_PLAN.md`. They require Gate 1B, because they
reuse C2's vocabulary with the direction reversed. The CMU readiness decision
does not depend on them.

### The main recall model: three directions

```text
Outbound REST   our application initiates a request   → an external service responds
Inbound REST    an external client initiates a request → our application responds
Webhook         an external producer initiates a request because an event occurred
                → our application validates, acknowledges, and reacts
```

At the HTTP level all three look alike: a method, a path, maybe a body, a status,
a response. What changes is **who starts the conversation, why, and which side
owns the decision at each step**. A webhook receiver is not a new technology.
It is an ordinary endpoint, usually `POST`, that another system calls when
something happens.

---

## C3. Inbound API / Server Fundamentals — CMU 15-113 (server-side development, HW4) + UC Berkeley INFO 153B (REST, routes, status codes, validation)

In C2 your tool was the **client** and someone else's service was the
**server**. Here the positions swap: your program is the server, and someone
else, such as a browser, a script, `curl`, or another service, is the client.

```text
consuming an API = your code sends requests and interprets responses   (C2)
providing an API = your code receives requests and decides responses   (C3)
```

CMU 15-113's HW4 describes the backend's job in these terms: it receives requests
at endpoints, validates user input, does server-side processing, keeps secrets
out of the client, returns JSON, and returns helpful errors rather than crashing.

### The inbound path

```text
client
→ HTTP request (method + path + query + headers + body)
→ server listening on a host/port
→ routing: which handler owns this method + path?
→ request parsing: path/query values extracted, JSON body deserialized
→ schema validation: is the input the right shape and type?
→ application/domain function: do the business rules allow this?
→ result or domain error
→ mapping to an HTTP status
→ JSON response (serialized)
→ client
```

You should be able to draw this from memory and say who owns each arrow.

### Vocabulary, mechanism first

```text
endpoint / route    a method + path the server has agreed to answer
                    (FastAPI calls a method + path pair a "path operation")
GET                 read a representation; should not change server state
POST                submit data for processing, often creating something
path parameter      part of the resource's identity:   /terms/agent
query parameter     modifies or filters the request:  /terms?limit=5
request body        structured data sent with the request, usually JSON
headers             metadata about the request (content type, credentials);
                    recognition level only in this unit
serialization       turning program values into JSON text for the response
deserialization     turning JSON text from the request into program values
```

The endpoint anatomy from C2 does not change. C2 taught you to **build** these
addresses. Here you **interpret** them.

### Two validations, owned by different layers

```text
schema validation   "Is this a well-formed request?"
                    required fields present, types correct, JSON parseable.
                    Owned by the request model / framework boundary.

domain validation   "Is this allowed and sensible for our application?"
                    term not already defined, value within a business rule.
                    Owned by ordinary application code.
```

A request can pass schema validation and still be refused by the domain. A
well-shaped request is not an authorized or correct one. This is the same lesson
as C2's "valid JSON is not a promise of the right JSON", seen from the other side.

### Status codes you must be able to choose

```text
200 OK            the request succeeded and here is the result
201 Created       the request succeeded and created something new
400 Bad Request   the request was well-formed, but the application rejects it
404 Not Found     the resource named in the path does not exist
409 Conflict      the request conflicts with current state (e.g., already exists)
422               request data failed schema validation (FastAPI's default for
                  invalid input, a framework behavior, not a universal rule)
```

The **status** is the server's verdict. The **JSON body** is the detail. A client
should be able to tell success from failure from the status alone, before it
reads the body.

### HTTP success is not domain correctness

`201 Created` means your server said it created something. It does not prove the
right thing was created, or that the business rule was the right rule. Transport
success, protocol success, and domain correctness are three separate claims.

### The transport layer should not become the domain layer

Keep the route handler thin:

```text
route handler (HTTP adapter)       ordinary Python (domain)
  receive parsed, validated input  → apply business rules
  call the domain function         → change authoritative state
  map result/error to a status     ← return result or raise a domain error
```

If the business rules live inside the route handler, you cannot test them
without HTTP, reuse them from another entry point (such as a webhook, a CLI, or
an agent tool), or tell a framework failure from a business failure. Agent
systems depend on exactly this separation. The same domain function may be
reached by a human's HTTP request, a webhook, or a model-proposed tool call, and
it must enforce the same rules for all three.

### Ownership boundary

```text
the client            chooses what to request
HTTP                  transports it
the server framework  routes and parses it
schema validation     rejects malformed input
application code      owns the business rules
domain/state layer    owns authoritative changes
the server framework  maps the result back to HTTP
```

The question to answer on every trace: **"What did the framework actually do
here, and what did my own Python code do?"**

### Request/response lifetime, API contract, OpenAPI

- A server **listens** on a host and port and handles each request separately.
  In this unit, each request is synchronous: the client waits until the server
  sends the response.
- An **API contract** is the published promise: which methods and paths exist,
  what each accepts, what each returns, and which statuses mean what.
- **OpenAPI** is a machine-readable format for writing that contract down.
  FastAPI generates one from your code and serves interactive documentation from
  it. Recognition level only: the generated document describes the contract but
  does not enforce your business rules.
- **CORS** (recognition only): a browser rule that decides whether a page served
  from one origin may call a backend on another. CMU HW4 mentions it for split
  frontend/backend deployments. This extension has no browser frontend, so it
  does not arise.

### Inbound failure kinds

| Failure kind | Where it happens | Who owns the fix | Typical evidence |
|---|---|---|---|
| never reached the server | client/network | client or operator | connection refused, timeout on the client side |
| routing | server framework | API contract | 404/405 for an unknown path or wrong method |
| request/schema validation | framework boundary | request model | 422 with field-level errors |
| application/domain validation | your application code | business rules | 400/409 with a domain reason |
| domain operation | your state layer | domain code | state not changed as expected, or a 500 |
| response mapping | route handler | adapter code | the right action but the wrong status/body |

"The API failed" is not a diagnosis here either.

---

## C4. Webhook / Event-Driven HTTP Fundamentals — CMU 15-440 Distributed Systems (communication, RPC semantics, failure) + CMU 15-113 + UC Berkeley INFO 153B (asynchronous task queues)

Only after C3 makes sense.

### Direction

```text
Polling (client decides when)          Webhook (producer decides when)
  your code: "anything new?"             producer detects an event
  service:   "no"                        producer POSTs to your receiver URL
  your code: "anything new?"             receiver validates the event
  service:   "yes, here"                 receiver acknowledges
                                         your application reacts
```

With polling, your code controls timing and often asks when nothing has changed.
With a webhook, you **subscribe** once by registering a receiver URL, and the
producer **calls back** when an event occurs. That is callback communication
across a network. It is an established distributed-systems idea, not a web
invention: historical CMU 15-440 material (Spring 2014, "Distributed Filesystems
2 — AFS, Coda, callbacks") shows a file server calling back its clients when
cached data changes. That lecture is historical support. It is not the current
Fall 2026 syllabus.

```text
event producer     the external system where the event happened
event receiver     your endpoint (the consumer/subscriber)
subscription       the registration: "send events of type X to this URL"
webhook endpoint   the receiver's ordinary HTTP route, usually POST /webhooks/...
event envelope     the fields every event carries:
                   event_id   (identity, used for deduplication)
                   event_type (what happened, used for routing to a handler)
                   payload    (the details)
acknowledgement    the receiver's 2xx response: "I received this"
```

### Acknowledgement is not completion

A `2xx` from the receiver means **"received and accepted."** It does not mean
the downstream work finished or succeeded. Receivers often acknowledge quickly
and do slower work afterwards, because the producer is waiting and may treat a
slow answer as a failure. Berkeley INFO 153B covers the mechanism behind "do it
later": asynchronous task queues. In this extension, recognizing that
acknowledgement and processing can be separate is enough. No queue is built.

### Delivery is not once, and not in order

CMU 15-440 covers Remote Procedure Calls in its current Fall 2026 schedule. The
public historical lecture slides (Spring 2014, Lecture 6 — RPC) make the
underlying point directly. A sender that gets
no answer cannot tell whether the request was lost, was processed and the reply
was lost, or is still in flight. It must choose between two options:

```text
retry        → the receiver may see the same request more than once
don't retry  → the request may never be processed
```

Exactly-once delivery is not achievable in general. Webhook producers usually
retry, so a receiver must assume:

```text
the same event may arrive more than once       (duplicate delivery)
an event may arrive late, or after a later one  (no ordering guarantee)
an event may never arrive                       (so it is not the only source of truth)
```

### Idempotent handling

An operation is **idempotent** if doing it twice has the same effect as doing it
once. "Set status to paid" is idempotent. "Append a row" or "add 10 points" is
not. The receiver makes a non-idempotent side effect safe by remembering which
`event_id`s it has already applied:

```text
event arrives
→ event_id already applied?  yes → acknowledge again, do nothing else
                             no  → apply the side effect once, record the event_id
```

The historical CMU 15-440 RPC slides describe the same idea for at-most-once
RPC: the server must be able to identify requests and keep a record of those it
has handled. A **replay** is a duplicate
sent on purpose, possibly by an attacker. The same identity check detects it,
though production systems also check authenticity and timestamps. An in-memory
set of seen IDs is enough to teach the idea. It is **not** durable production
deduplication, because it is lost on restart and not shared between server
processes.

### An event is evidence, not authority

A webhook payload is a claim made by another program. The rule from C2 and
`ARCHITECTURE_CONTRACT.md` §3b still applies: it is an observation that your
application interprets, not a command that edits your authoritative state by
arriving. Validate it before any state changes, then let your own domain rules
decide what it is allowed to cause.

### Authenticity, at the concept level

Anyone who learns the receiver URL can POST to it. Production receivers normally
verify that the sender is really the producer. A common approach is a signature
computed with a secret shared at subscription time and checked by the receiver
before it trusts the body. CMU 15-440 lists the security challenges of
distributed programs as a course objective, and CMU 15-113 requires that secrets
stay on the backend, out of code and out of the repository.

Two rules for this bridge:

1. Know **what** authentication protects: it answers "did this really come from
   the producer, unmodified?", which schema validation cannot answer.
2. Use the specific provider's official verification procedure when there is a
   real provider. Do not invent homemade cryptography. The local exercise has no
   real provider, so it does not implement signing.

### Webhook failure path

```text
sender          producer never sent it, or sent it to the wrong URL
network         request lost or timed out; producer may retry → duplicates
receiver        not running or not reachable
authenticity    (concept) sender cannot be verified → reject before trusting the body
schema          envelope malformed → reject; nothing changes
duplicate/replay event_id already applied → acknowledge, no second side effect
business        valid event, but the domain refuses or fails to apply it
acknowledgement receiver's reply lost or too slow → producer retries → duplicate
```

Each line produces different evidence and needs a different fix.

---

## D. State and Memory Fundamentals — CMU Module 2 + CS188 state representation

Do not use “memory” for every piece of retained information.

Be able to classify:

### Current context
Information placed into the present model interaction.

### Working state
Application data needed while the current run proceeds.

### Authoritative durable state
Application-owned truth that persists and may control real behavior.

### Non-authoritative durable memory
Persisted information that may help future decisions but still requires policy/validation before influencing authoritative state.

### Retrieved evidence
External or stored material selected for the current decision.

### Model inference
A conclusion generated by the model; not automatically a stored fact.

Berkeley's distinction between world state and the state representation needed for planning is useful here: store/represent what the decision process actually needs, not everything merely because it is available.

---

## E. RAG / Vector Retrieval Fundamentals — CMU Module 3

Know the pipeline:

```text
source documents
→ split/chunk
→ embedding/vector representation
→ store/index
→ represent query
→ compare/retrieve
→ select evidence
→ place evidence in model context
→ generate answer
```

### Embedding/vector
A numeric representation used so similarity/retrieval operations can compare items in a vector space.

### Chunking
How source material is divided before representation/retrieval. Boundaries matter because retrieval returns chunks, not an abstract perfect fact.

### Top-k
A retrieval policy that keeps some number of highest-ranked candidates.

### Two different failure stages

```text
retrieval failure:
needed evidence was not selected

vs

generation failure:
useful evidence was present but the model produced a poor answer
```

Never treat retrieved text as permission to expand tool authority.

---

## F. Reasoning / Planning Fundamentals — CMU Modules 2 and 4 + Berkeley CS188 search

CMU publicly lists ReAct and Tree-of-Thought among the reasoning patterns used in the program. Before the course you do not need implementation mastery.

You should understand the system-level question:

> Does the reasoning strategy create additional decision steps, candidate paths, actions, verification, or branching — and what does that cost?

Use Berkeley search vocabulary to reason about:

```text
current state
possible actions
candidate paths
cost/budget
goal test
```

More reasoning is not automatically better. It can increase steps, latency, failure opportunities, and cost.

---

## G. Multi-Agent Fundamentals — CMU Modules 4–5

Before adding a second agent, define:

```text
role
input
output
shared state
allowed actions
handoff condition
failure behavior
termination
```

Always keep a single-agent baseline in mind.

A multi-agent design is justified only if role separation/coordination provides a concrete benefit that outweighs new handoff and shared-state failure modes.

---

## H. Evaluation, Safety, and Observability — CMU Module 6 + CMU 15-482 + CMU 11-768

### Evaluation
Define what success means **before** running the system.

At minimum be ready to reason about:

```text
task success
correct state changes
bounded execution
latency/steps
failure class
```

### Safety / guardrails
CMU 11-768 explicitly highlights safety sandboxing and credentialing. The readiness principle is that the model should not receive more authority than the application intends to grant.

### Execution monitoring
CMU 15-482 emphasizes execution monitoring and integrated testing for reliable/robust agents.

A useful trace should let you reconstruct:

```text
what the system observed
what action was proposed
what was validated
what executed
what result returned
why it continued/stopped
```
