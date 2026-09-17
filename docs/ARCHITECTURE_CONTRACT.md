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

The core sprint tool is read-only.

## 4. Loop Is Bounded

Every run has an explicit maximum-step bound and a defined termination reason.

## 5. External/Probabilistic Behavior Is Isolated

The deterministic model-decision stub exists so loop/state behavior can be tested independently of model variability.

**Swap test:** replacing the stub with a live decision model (for example the optional TypeSafe Patch 5 in `IMPLEMENTATION_PLAN.md`) should change only the decision function. Any required change to state, loop, validation, tool, or trace is evidence that this rule was violated.

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
