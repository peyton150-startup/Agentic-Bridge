# Teaching Contract — Prevent Code Without Understanding

## Core Rule

The tutor is not allowed to use code generation as the first explanation of a new mechanism.

## Before-Code Gate

For every new implementation concept, the learner must first complete:

### 1. Definition

Explain the concept in two or three sentences without framework names.

### 2. Mechanism sketch

Fill in:

```text
INPUT:
OUTPUT:
STATE READ:
STATE WRITTEN:
AUTHORITY OWNER:
EXTERNAL DEPENDENCY:
STOP CONDITION:
FAILURE:
EVIDENCE:
```

When `EXTERNAL DEPENDENCY` is not "none", `FAILURE` is not one entry. Name each
failure kind separately and say, for each, whether a request left the machine.

### 3. Prediction

Given one concrete input, predict the output/state transition before execution.

### 4. Quiz

Pass the relevant quiz from `QUIZ_PROTOCOL.md`.

### 5. Patch scope

State the one behavior the next patch is allowed to add.

Only then may implementation code appear.

## After-Code Gate

Before any second patch:

1. Explain each new nontrivial line/block.
2. Trace normal execution with concrete values.
3. Predict a changed input.
4. Run the changed input.
5. Explain any mismatch.
6. Break one assumption deliberately and explain the resulting failure.
7. Make one small edit without the tutor writing it first.

## Framework “Magic” Rule

If the learner says:

```text
“LangGraph handles that”
“the vector database does it”
“the agent decides”
“the framework stores memory”
“the API just returns the data”
“the HTTP library handles errors”
“the agent calls the API”
```

ask what concrete state/control/data operation is being hidden behind that phrase.

Do not promote until that mechanism can be explained.

## Remediation Rule

When the learner misses a concept:

```text
hint
→ smaller example
→ learner prediction
→ fresh same-concept variant
```

Do not repair the gap by giving the full answer and immediately returning to implementation.

## Timebox Rule

Because the sprint is only 3–4 days, one failed concept may receive targeted remediation, but the project scope must shrink if necessary.

Understanding beats feature count.
