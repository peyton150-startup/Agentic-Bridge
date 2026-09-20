# Agentic Bridge — Current State

## Lifecycle

**Current stage:** Day 2 — memory and RAG fundamentals

Day 0 diagnostic passed 2026-09-18; Day 1 and Gate 1 passed 2026-09-20 (see `learning/LEARNING_LEDGER.md`).

## Time Constraint

This repository is designed for a **3-day core** or **4-day preferred** sprint immediately before CMU's Agentic AI Program.

Do not expand the scope unless a diagnostic reveals a prerequisite gap that would block the program.

## What Exists

Documentation only.

## What Does Not Exist Yet

- agent framework code;
- vector database deployment;
- multi-agent orchestration;
- frontend;
- production infrastructure;
- large application codebase.

## First Implementation Target

Only after the prerequisite diagnostic and Day 1 concept gate:

```text
deterministic model decision stub
→ explicit agent loop
→ one read-only tool
→ bounded stop condition
→ traceable result
```

A live LLM is optional during the sprint. The loop must be understood **before** a provider is swapped in.

## Exit Target

At sprint end, the learner should have:

1. a passed CMU prerequisite diagnostic;
2. one tiny agent loop they can trace line by line;
3. paper/manual exercises for memory, vector retrieval, reasoning, multi-agent coordination, and evaluation;
4. a final oral/architecture readiness pass;
5. a list of weak concepts to review during CMU rather than hiding them behind frameworks.
