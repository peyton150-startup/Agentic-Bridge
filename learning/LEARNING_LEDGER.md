# Agentic Bridge Learning Ledger

## Purpose

Capture the few concepts that matter during a 3–4 day sprint. Do not turn this into administrative work.

## Daily Entry

### Date / Day

### Concept

### Cold Answer

```text
[answer before help]
```

### Confidence

`0–100%`

### Result

- correct / partial / incorrect

### Precise Weakness

```text
[one sentence]
```

### Corrected Mental Model

```text
[one to three sentences]
```

### Transfer Variant Result

```text
[new example + result]
```

### Promotion

- continue / remediate / mark as CMU watch item

---

## Code Comprehension Entry

For every patch:

```text
PATCH PURPOSE:
INPUT:
OUTPUT:
STATE READ:
STATE WRITTEN:
EXTERNAL DEPENDENCY:
STOP/ERROR PATH:
ONE LINE/BLOCK I COULD NOT EXPLAIN:
MY OWN SMALL MODIFICATION:
RESULT:
```

If `ONE LINE/BLOCK I COULD NOT EXPLAIN` is non-empty, no additional implementation patch should be added until it is resolved.

---

## Entries

### 2026-09-18 / Day 0 — First Session Step 1: bridge scope vs CMU scope

**Cold answer:** Q1 (prerequisites) correct. Q2 pasted CMU's tool list rather than concepts. Q3/Q4 "not sure". Had not heard of LangGraph, LangSmith/Helicone, ReAct beyond names.

**Confidence:** not given

**Result:** partial → correct after smaller example (8/8 sort).

**Precise weakness:** Could not yet derive bridge vs CMU scope from the program page; tool names were unfamiliar.

**Corrected mental model:** The bridge covers CMU's assumed prerequisites plus the plain mechanisms under its tools (state, loop, stop). CMU covers the tools/frameworks and anything built with them.

**Transfer variant result:** "agent loop + how it stops" → B; "FAISS vs Chroma choice" → C. Both correct. Learner rule: "basic building block → bridge; complicated or beyond basics → class."

**Promotion:** continue

### 2026-09-18 / Day 0 — First Session Step 2 (partial): LLM job vs code authority

**Cold answer:** "Adding an LLM" answered as API plumbing (NVIDIA key); "not sure about jobs". Vacuum sort: 4/6 — swapped item 5 (explain skip → marked C) and item 6 (motor on/off → marked L).

**Result:** partial → correct after "wrong 1 in 50?" hint; learner reasoned consequences correctly for both.

**Precise weakness:** Initially equated "adding an LLM" with integration setup rather than deciding which role it may hold.

**Corrected mental model:** LLM may interpret, propose, and explain. Code owns anything that changes the real world or the authoritative record, especially irreversible actions.

**Transfer variant result:** pending (re-test on a new domain at Day 1 quiz, Q2/Q3).

**Promotion:** continue

### 2026-09-18 / Day 0 — Diagnostic A (Python), in progress

**Q1 — list mutation vs rebinding in a function:** cold `a=[1,2]` (wrong), `b=[99]` (right). Correct after smaller no-function example (`y = x; y.append`).

**Q2 — dict mutation vs rebinding:** needed `.get(key, 0) + 1` explained (counter pattern). `s` correct cold; `r` initially "empty", then thought `"reset"` went into `s`. Correct after boxes/sticky-notes table.

**Syntax gap found:** confused by `{}` vs `[]`. Rules taught: brackets on their own = build (`{}` dict, `[]` list); name right before `[...]` = reach in (always square). Type is set by the most recent `=` assignment of that name. Learner restated correctly.

**Q3 — loop with break:** understood `break` correctly; predicted 2 (counted searches, not passes). Answer is 3. Pass-by-pass trace table given, **not yet completed** — resume here.

**Precise weakness:** mutation (change the box) vs rebinding (move the name); order of statements inside a loop body.

**Still to do:** finish Q3 trace → Q4 exceptions → Q5 composing functions → one cold mutation-vs-rebinding variant. Then Diagnostic B–D, then First Session Steps 2 (vacuum six fields) and 3 (runtime drawing).

**Promotion:** remediate (in progress)

---

## CMU Watch Items

Record only weaknesses that should receive extra attention during the program.

| Concept | Why weak | What I can already explain | What to watch during CMU |
|---|---|---|---|
| | | | |
