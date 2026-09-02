# CMU Prerequisite Diagnostic

CMU publicly lists functional knowledge of **Python, algorithm design, data structures, LLMs, and AI** as prerequisites.

This diagnostic is intentionally short. It identifies blockers; it does not award mastery.

## A. Python — must pass

Without running code first, solve small exercises involving:

- function calls and return values;
- list/dict mutation vs rebinding;
- `if`/loop control flow;
- exceptions/error paths;
- composing two or three functions.

**Pass condition:** predict output/state correctly on at least 4 of 5 fresh examples and explain why.

If weak, review the relevant abstraction/control concepts from Berkeley CS61A before proceeding.

## B. Data Structures / Algorithms — must pass

Explain when you would use:

```text
list
set
dictionary/map
queue
stack
```

Then answer:

1. Why can representation choice change the cost of an operation?
2. Given a small state-space problem, what are the state, actions, goal test, and frontier/search idea?
3. What does it mean to compare an algorithm by the operations it performs as input grows?

**Pass condition:** correct practical choice and reasoning on 4 of 5 examples.

If weak, use Berkeley CS61B and CS188 official material for targeted review.

## C. LLM Fundamentals — must pass

Explain in plain English:

- prompt/context vs generated output;
- why an LLM response is not guaranteed to be identical across runs;
- why generated text should not automatically become authoritative application state;
- what “structured output” is trying to accomplish;
- one way a long context can affect an application design.

**Pass condition:** no major misconception about model output being deterministic or authoritative.

## D. AI / Agent Fundamentals — must pass

Using Berkeley CS188 vocabulary, identify for a hypothetical assistant:

```text
performance goal
environment
state/observation
actions
transition/consequence
goal/termination
```

Then explain why adding an LLM does not remove the need for these concepts.

## Diagnostic Decision

```text
ALL FOUR PASS
→ begin Day 1

ONE SMALL WEAKNESS
→ targeted remediation, then a fresh variant

MULTIPLE MAJOR WEAKNESSES
→ do not try to compensate by adding frameworks;
  use the sprint primarily for prerequisite repair
```
