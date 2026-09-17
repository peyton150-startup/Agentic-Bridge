# Minimal Implementation Plan

## Purpose

The sprint needs **one small implementation** so the concepts are not detached theory. It does not need a complete agent platform.

## Build Only This Core

```text
AgentState
ModelDecision (deterministic stub first)
one read-only Tool
AgentLoop
TraceEvent
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

Use a deterministic tool so the execution path is easy to trace.

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

### Optional Patch 5 — Live LLM swap

Only if time remains.

The learner first states what behavior is provider-specific and what application contract must remain stable.

Do not redesign the core around the provider.

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

## Day 2 / Day 3 Implementation Style

Memory, RAG, reasoning, and multi-agent topics may remain **paper exercises / tiny isolated calculations** during this bridge.

That is deliberate. The goal is to make CMU's abstractions understandable, not to prebuild the course.
