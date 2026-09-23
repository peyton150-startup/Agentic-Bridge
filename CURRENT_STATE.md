# Agentic Bridge — Current State

## Lifecycle

**Current stage:** Sprint complete — **Ready with watch items** (2026-09-23)

Day 0 diagnostic passed 2026-09-18; Day 1 (incl. Day 1B external API) and Gate 1 passed 2026-09-20; Day 2 and Gate 2 passed 2026-09-21; Day 3 work and quiz passed 2026-09-21; final readiness check Parts A–D passed 2026-09-22/23 (see `learning/LEARNING_LEDGER.md`).

The watch items to carry into the program are in the **CMU Watch Items** table at the end of the ledger.

Optional work not done: Day 4 mini-capstone, mock lab, full Pydantic AI Trellis trace (a 20-minute cut was done), and Extension X.

## Time Constraint

This repository is designed for a **3-day core** or **4-day preferred** sprint immediately before CMU's Agentic AI Program.

Do not expand the scope unless a diagnostic reveals a prerequisite gap that would block the program.

## What Exists

- documentation;
- `learning/LEARNING_LEDGER.md`, the full learning record from Day 0 onward;
- `code/tiny_agent.py` — Patches 1–4: state, one read-only deterministic tool with
  input validation, deterministic model stub, bounded loop, and trace
  (`final_answer` / `max_steps` / `model_error`);
- `code/api_tool.py` — Patch 5: `lookup_postcode`, one read-only GET to
  api.zippopotam.us with input validation, timeout, status check, JSON parse,
  shape checks, and a bounded result (`invalid_input` / `network` / `http` /
  `shape` error results). Runs standalone; not wired into `run_agent` (optional).

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
→ one read-only deterministic tool
→ bounded stop condition
→ traceable result
```

Then, and only after that loop traces correctly, one further patch:

```text
one read-only external HTTP tool
→ validated input
→ one GET request with an explicit timeout
→ status + parse + shape validation
→ bounded observation
→ two deliberate failure demonstrations
```

A live LLM is optional during the sprint and is the lowest-priority patch. The loop must be understood **before** a provider is swapped in, and the deterministic tool must be understood **before** a network call is added.

## Optional Extension X — added 2026-09-21, not started

A FastAPI server (X1) and a local simulated webhook receiver (X2) are defined as
an **optional** extension after Gate 1B, about 2.5–3 hours. They are not part of
the 3-day core or the readiness decision, and no extension code exists yet. The
core scope rule above still applies: the extension may not displace Day 3 or
Day 4 core items. See `docs/SPRINT_PLAN.md` → Optional Extension X.

## Exit Target

At sprint end, the learner should have:

1. a passed CMU prerequisite diagnostic;
2. one tiny agent loop they can trace line by line, including one tool that reaches an external API;
3. paper/manual exercises for memory, vector retrieval, reasoning, multi-agent coordination, and evaluation;
4. a final oral/architecture readiness pass;
5. a list of weak concepts to review during CMU rather than hiding them behind frameworks.
