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
