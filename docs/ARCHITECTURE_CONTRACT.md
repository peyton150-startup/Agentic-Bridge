# Architecture Contract for the Tiny Sprint Agent

## 1. Application Owns Control Flow

The model may propose a next action. Application code decides whether that action is valid and whether execution continues.

## 2. Application Owns Authoritative State

Model text, retrieved evidence, and tool observations may influence decisions but do not become authoritative merely by being generated or observed.

## 3. Tools Have Explicit Authority

Each tool contract defines:

```text
accepted input
possible output
allowed side effects
failure behavior
```

Every sprint tool is read-only.

## 3a. External Calls Are Bounded and Sit Behind the Tool Boundary

The agent never speaks to an external service. One tool does, on the
application's behalf, under the same contract as any other tool plus:

```text
input is validated before any request is built
the method is read-only
the call has an explicit timeout
the status code is checked before the body is used
the body is parsed defensively and its shape is checked
the result handed back is bounded in size
each failure kind produces a distinct, named failure result
```

Because part of the work happens on a machine the application does not own, an
external call has five distinguishable failure kinds — tool-input validation,
network/transport, HTTP/API error, response shape/data, and agent-loop — and
the trace must make clear which one occurred.

The deterministic tool is built and understood first. Networking is added only
after the loop is traceable without it.

## 3b. External Responses Are Evidence

An external response is a claim made by another program at one moment. It is an
observation, subject to clause 2: it does not become authoritative state by
arriving, and it never grants the agent authority it did not already have.

## 4. Loop Is Bounded

Every run has an explicit maximum-step bound and a defined termination reason.

## 5. External/Probabilistic Behavior Is Isolated

The deterministic model-decision stub exists so loop/state behavior can be tested independently of model variability.

The same reasoning applies to the network: the deterministic tool exists so that
loop behavior can be tested without transport failure in the picture, and so
that a failing run can be attributed to the loop or to the external boundary
rather than to both at once.

**Swap test:** replacing the stub with a live decision model (the optional Patch 6 in `IMPLEMENTATION_PLAN.md`) should change only the decision function. Any required change to state, loop, validation, tool, or trace is evidence that this rule was violated.

## 6. Evidence Is Part of the Design

The trace must allow the learner to reconstruct why each step occurred.

## 7. Complexity Requires a Reason

Do not add memory, retrieval, planning branches, or extra agents because they are fashionable or appear in the CMU syllabus.

For each proposed addition ask:

```text
What problem does this solve?
What new state/control path appears?
What can now fail?
How would we test it?
```
