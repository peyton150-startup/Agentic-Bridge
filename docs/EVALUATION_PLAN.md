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

Scenario 3 is not one scenario once a tool reaches an external service. Split it:

```text
3a. network/transport failure   — no usable response arrived
3b. HTTP/API error              — a response arrived, non-success status
3c. response shape/data failure — success status, body unusable
```

Both failures demonstrated on Day 1 already supply 3a and 3b; 3c can be defined
on paper from the same tool contract. This costs no additional implementation.

### If the decision model is TypeSafe (optional Patch 6)

- **Scenario 2:** a Choice cannot return an option outside its set, so scenario 2 *looks* solved. It is not: arguments without a question keep defaults, and free-text/number/date arguments are never checked by the model. Keep validation in code and design scenario 2 around those arguments.
- **Scenario 5:** a Noul guardrail ("Does this request ask for an action outside the agent's authority?") is a reasonable extra check, but TypeSafe's own limitations page says adversarial content can influence it. The guardrail informs the decision; application authority rules still decide. Include one scenario where the request text tries to talk the guardrail into "no".
- **Low confidence:** define before running what happens below a threshold (stop, escalate, or ask). The threshold is a policy constant you chose, not a vendor default.

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

If TypeSafe is used, also record the decision's `confidence` and whether a low-confidence rule fired.

Do not spend the sprint building dashboards.

## Failure Classes

Use simple categories:

```text
model decision
tool-input validation
tool/environment
network/transport
HTTP/API error
response shape/data
termination
state/authority
safety/permission
low confidence (only if a confidence-gated rule exists)
application bug
```

The three external classes replace a single "external/provider" bucket on
purpose. "The API failed" does not tell you whether a request left the machine,
whether the service answered, or whether your own parsing was wrong — and those
three call for different fixes.

## Optional Extension X — Scenarios and Failure Classes

Only if Extension X is done. These are defined before running, like the five
above, and do not replace them.

### Scenarios

```text
X1-a  valid read                 GET returns 200 and the expected body
X1-b  valid create               POST returns 201 and the state contains the new item
X1-c  malformed request          422, state unchanged
X1-d  domain-invalid request     400/409, state unchanged
X2-a  valid event                2xx, exactly one side effect
X2-b  malformed event            422, no side effect
X2-c  duplicate event            2xx both times, still exactly one side effect
```

For each, "state unchanged" or "exactly one side effect" is part of the PASS
condition. A correct status with the wrong state is a FAIL.

### Failure classes by direction

Keep the three directions apart. Do not flatten them into "the API failed."

```text
Outbound (Patch 5)   our validation → transport/network → remote HTTP response
                     → remote data shape → agent/control flow

Inbound (X1)         request reaches server → routing → request/schema validation
                     → application/domain validation → domain operation
                     → response mapping

Webhook (X2)         sender → network → receiver → authenticity (concept)
                     → schema validation → duplicate/replay check
                     → business handling → acknowledgement
```

Each stage in a chain produces different evidence. Record which stage failed,
not just that a request did.

## What Evaluation Does Not Prove

Five scenarios do not prove production reliability. The exercise proves that you understand how to define behavior, execute a scenario, and use evidence to judge whether the system met the intended contract.
