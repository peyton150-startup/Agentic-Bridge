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

**Q3 — loop with break:** understood `break`; predicted 2 (counted searches, not passes). Completed trace table → 3, explained "if comes after steps + 1". Correct after hint.

**Q4 — try/except KeyError:** cold content right, order wrong (put `ok` after the returned value) and added a `search:` prefix. Explained after prompt: `print` waits for `run` to finish; `run` prints during execution. Partial. (Tutor error: said four lines, there were three.)

**Q5 — composed decide/act/loop:** correct cold, `['search','result','search','result','stop']`, with an accurate full narrated trace.

**Cold transfer — mutation vs rebinding with `memory + [...]`:** correct cold (`['a','b']`, `['a','b','extra','more']`). Unsure whether `+` includes old items; resolved with "right side runs first on the old box".

**Precise weakness (resolved):** mutation vs rebinding; statement order inside a loop body; when a nested call's prints happen.

**Result:** Section A PASS (one small weakness → remediated → fresh variant correct cold).

**Still to do:** Diagnostic B–D, then First Session Steps 2 (vacuum six fields) and 3 (runtime drawing).

**Promotion:** continue

### 2026-09-18 / Day 0 — Diagnostic B (Data Structures / Algorithms), in progress

**Structure choice (5 jobs):** cold 3/5 — set, dict, queue correct; subtask-most-recent-first marked queue (→ stack), replay history marked stack (→ list; learner admitted picking stack because it was unused). Both corrected with reasons after small examples.

**Representation cost (list vs set membership, 1M items):** initial misconception — set is faster "because no duplicates". Corrected via counting checks on a 5-item list ("has to go through every entry"). Then correct: list 1M → 1M checks, 10M → 10M checks; set ≈ constant. Toy locker hash taught (letter count, last digit); learner computed `"cmu.edu"` → locker 7 correctly; asked whether the recipe is fixed (yes, within a run). Learned set and dict share the mechanism (dict locker also holds value).

**Precise weakness:** attributed set speed to uniqueness rather than direct-location lookup; growth-of-work reasoning needed concrete counting first.

**Corrected mental model:** list membership checks every item (work grows with size); set/dict compute where the item would be and look once (work ~constant). Uniqueness is a side effect.

**Hallway state-space (rooms 1–4):** said "move left to room 4" (direction + jump). Traced 2,3,4 → 3 moves. Multiple choice: state = current room, actions = left/right, goal test = "is my room 4?" all correct. Explained why "have I made 3 moves?" fails (start elsewhere → overshoot; bump → ends in room 3). Linked: max-steps is a budget, not a goal test.

**Result:** Section B PASS.

**Promotion:** continue

### 2026-09-18 / Day 0 — Diagnostic C (LLM Fundamentals)

**Nondeterminism:** correct ("probabilistic"); mechanism (sampling next token) explained. Bank charge: correct — needs same result every time.

**Authority:** "don't charge immediately; confirm, check account, check balance." Added: ownership/authority check. Learned terms authoritative state vs authority. **Misconception fixed:** said "the LLM has to check" → corrected to "code checks; LLM proposes."

**Structured output:** misconception — thought structure removes probabilistic text. Corrected: structure fixes shape (code reads `answer["amount"]`), not content. Then correct: `{"account":"4471","amount":500}` can still occur; caught by authoritative-state checks, not format.

**Long context:** cost + latency correct; proposed summarize, recent window, search-history (→ retrieval/RAG preview; corrected "like a set" to relevance ranking).

**Result:** Section C PASS (two corrected misconceptions: who checks; what structure guarantees).

### 2026-09-18 / Day 0 — Diagnostic D (AI/Agent Fundamentals), in progress

**Cold (robot vacuum six fields):** goal/env/termination "not sure"; state "context and the internet"; actions "set of actions we code to allow" (correct); transition "state and context". Multiple choice: picked nearly all options — "I have no way to distinguish them."

**Precise weakness:** cannot yet tell goal / environment / state / transition / termination apart; defaults to LLM vocabulary (context, internet) for non-LLM agents.

**Remediation given:** one question per field (grade it? where does it operate? what does it know now? what can it do? what changes after? am I done?) + filter "is this even about a vacuum?". Retry: state → B correct with reasoning; environment → chose C (vacuum's code) — wrong; said "a and b are about where it is", which is the definition of environment. Explained: environment = world outside the agent; code is inside.

**Retry with filters:** vacuum goal (a), transition (a), termination (b) all correct with reasons ("time limits or counts instead of a reason to stop").

**Cold transfer — smart thermostat, no options:** all six fields correct (goal 70°, env house/rooms, state 55° sensor reading, actions heater on/off, transition temp rises, termination "all rooms at 70?"). Taught: task agents vs continuous agents.

**LLM role ("make it cozy"):** correctly said LLM turns "cozy" into a target (65°). **Slip:** said "LLM stops the heater" → corrected: LLM proposes target; code validates range, updates state, runs same loop. On 150°: "checked against authoritative state so it doesn't hallucinate a crazy number" — correct; refined: reject regardless of cause.

**Result:** Section D PASS (large weakness → remediated → cold transfer correct).

### 2026-09-18 / Day 0 — First Session Step 3: runtime drawing (thermostat + LLM)

**Per-arrow table:** LLM→code proposal/out-of-range correct. Misconceptions fixed: (1) "deterministic code → not much can fail" → deterministic ≠ correct (55–850 typo fails every time); (2) "state tells heater" → state is data, code acts; (3) sensor arrow owner/failure unsure → observations can be wrong.

**Evidence:** stuck sensor → heater runs forever (correct). Log pattern: heater ON every step, reading unchanged → flag. Proposed rule with domain threshold ("8° takes ~2h, so flag after 1h no change"). Named: execution monitoring, stall detection, bounded loop.

**Result:** Step 3 complete.

## Day 0 Decision — 2026-09-18

Diagnostic A–D all PASS (each with remediation; final transfer items cold-correct). **Promote to Day 1.**

Recurring pattern to watch: under pressure, reverts to "the LLM does/checks X" — re-test authority split in Day 1 quiz Q2/Q3 on a new domain.

### 2026-09-18 / Day 1 — Reading: CS188 1.1 and 1.2

**1.1:** thermostat = reflex agent (correct, with reason). PEAS 3/4 — mapped P to state; corrected P = performance measure = goal.

**1.2 main ideas discussed:**
- Search problem parts + action cost: walk (3) vs teleport (5) correct; bump case arithmetic slip (4, not 5).
- World vs search state: "get to (5,3)" kept ghosts despite harmless assumption → lesson "search state depends on the problem"; "eat all dots" → position + dots eaten, correct.
- Counting states: cold answered 10 × 3 = 30 (added dots instead of ×2 each); asked whether this was combinations/permutations → taught multiplication rule / light switches; then 8, 80, "a lot bigger" correct (~10 billion for 30 dots).
- Graph vs tree: tree can loop forever (left/right) correct → link to max-step bound.

### 2026-09-18 / Day 1 — Fundamentals C: tool contract

**lookup_word contract:** proposer/allowed/no state change correct. Input first said "a document" → corrected to the `word` string. Validation: accepted "12345"; believed `"1245"` is not a string → corrected (quotes make a string); rule set to "letters only, 1–30 chars".

**Authority slip (recurring, 3rd time):** "the LLM would output not found" / "the model reads the input and starts the workflow". Resolved using learner's own traced Q5 loop: loop calls decide(); decide can't call act(); loop runs first; input triggers code. Learner restated: **"code starts it and calls the model; model returns a proposal; code validates, runs tools, continues or stops."** Legit nuance kept: model may write the final user-facing message; code orchestrates.

### 2026-09-18 / Day 1 Quiz — in progress

**Q1** (`{"tool":"lookup_word","word":"12345"}` — should it run?): answered **yes** ("proposed by model, correct tool, valid string") — **incorrect** under the agreed contract (letters only). Same pattern: treats well-formed model proposal as sufficient. Brief correction given; **resume here** with full discussion, then Q2–Q5 + transfer.

**Promotion:** in progress — authority/validation is the live CMU watch-item candidate.

---

## CMU Watch Items

Record only weaknesses that should receive extra attention during the program.

| Concept | Why weak | What I can already explain | What to watch during CMU |
|---|---|---|---|
| | | | |
