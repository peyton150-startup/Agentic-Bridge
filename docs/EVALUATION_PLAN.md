# Evaluation Readiness Plan

CMU's public curriculum includes evaluation, guardrails, logging, and observability. CMU's Autonomous Agents course also emphasizes integration/testing, execution monitoring, reliability, and robustness.

The sprint therefore practices **defining evidence before running** rather than building a full evaluation platform.

## Five Required Scenarios

For the tiny Day 1 agent, define:

1. normal success;
2. invalid proposed tool input;
3. tool failure;
4. repeated-action / max-step pressure;
5. unsafe or out-of-authority request.

## For Every Scenario Record Before Execution

```text
initial state
expected allowed action(s)
expected forbidden action(s)
expected final result
allowed state change
maximum steps
expected termination reason
trace evidence to inspect
PASS condition
FAIL condition
```

## Minimal Metrics

For sprint readiness, track only:

```text
task pass/fail
steps taken
tool calls
termination reason
failure class
```

If a live LLM is used, optionally add latency and token/cost evidence if it is readily available.

Do not spend the sprint building dashboards.

## Failure Classes

Use simple categories:

```text
model decision
validation
tool/environment
termination
state/authority
safety/permission
external/provider
application bug
```

## What Evaluation Does Not Prove

Five scenarios do not prove production reliability. The exercise proves that you understand how to define behavior, execute a scenario, and use evidence to judge whether the system met the intended contract.
