# Trellis Code Map

Use this document to connect the Agentic Bridge concepts to code the learner has already built. Trellis is a **transfer case**, not an academic curriculum source. Academic teaching claims must still come only from the official CMU and UC Berkeley sources listed in `SOURCES.md`.

## Repository identity

| Field | Value |
|---|---|
| Repository | `Trellis_AI_Chatbot_Task_Manager` |
| GitHub | <https://github.com/peyton150-startup/Trellis_AI_Chatbot_Task_Manager> |
| Local checkout | `C:\Users\nicol\Trellis_AI_Agent` |
| Canonical branch analyzed | `master` |
| Commit analyzed | `11cf50bc5882b71062b65e83f436b2e9317354b1` |
| Commit state when mapped | local `HEAD` matched `origin/master` |

The links below are pinned to that commit so they keep pointing to the code that was analyzed. In a later session, first run:

```powershell
git -C C:\Users\nicol\Trellis_AI_Agent rev-parse HEAD
```

If the commit changed, use the symbol names in this document as the primary locator and refresh line links only after inspecting the new code. Do not infer current behavior from an old line number.

## What Trellis is

Trellis is an LLM-powered task manager whose central boundary is:

```text
model proposes
→ typed schema validates
→ deterministic policy decides
→ idempotency decides execute/replay/conflict
→ domain code changes state
→ PostgreSQL commits state + evidence
```

The browser and the model are not authorities. Deterministic application code and PostgreSQL own permissions, current task state, accepted conversation history, approvals, retry state, and audit evidence.

Two scope limits matter for the bridge:

- Trellis has structured database reads and history lookup, but it intentionally has **no embedding model, vector database, or RAG pipeline**. Day 2 uses its state and evidence boundaries as a comparison before asking what RAG would add.
- Trellis exposes a browser agent profile and a narrower Linear agent profile, but they do not collaborate or hand work to one another. They are two entry paths into a shared kernel, **not a multi-agent system**. Day 3 uses this as a negative example that prevents “two agent objects” from being confused with multi-agent coordination.

---

## Day 1 — Agent, state, tools, loop, and authority

### Best concrete example: create one task

Trace the request “Create a task called Study approval boundaries” through these exact locations:

1. [`handle_agui_request`](https://github.com/peyton150-startup/Trellis_AI_Chatbot_Task_Manager/blob/11cf50bc5882b71062b65e83f436b2e9317354b1/backend/app/agent.py#L680-L758) extracts the accepted user message, creates a server-owned run, loads canonical history, and starts model execution.
2. [`CreateTaskArgs`](https://github.com/peyton150-startup/Trellis_AI_Chatbot_Task_Manager/blob/11cf50bc5882b71062b65e83f436b2e9317354b1/backend/app/models.py#L437-L442) is the tool input contract. It defines the fields and types the model may propose.
3. [`build_agent`](https://github.com/peyton150-startup/Trellis_AI_Chatbot_Task_Manager/blob/11cf50bc5882b71062b65e83f436b2e9317354b1/backend/app/agent.py#L430-L500) constructs the model-facing agent and chooses which tools exist in its capability profile.
4. The [`create_task` agent wrapper](https://github.com/peyton150-startup/Trellis_AI_Chatbot_Task_Manager/blob/11cf50bc5882b71062b65e83f436b2e9317354b1/backend/app/agent.py#L528-L536) translates framework context into Trellis context and delegates to deterministic code.
5. The deterministic [`tools.create_task`](https://github.com/peyton150-startup/Trellis_AI_Chatbot_Task_Manager/blob/11cf50bc5882b71062b65e83f436b2e9317354b1/backend/app/tools.py#L396-L551) hashes the arguments, checks for a completed replay, classifies approval, checks policy, acquires an idempotency lease, calls the domain layer, writes events, completes the lease, and commits.
6. [`policy.check`](https://github.com/peyton150-startup/Trellis_AI_Chatbot_Task_Manager/blob/11cf50bc5882b71062b65e83f436b2e9317354b1/backend/app/policy.py#L95-L192) owns scope and authorization decisions; the model does not.
7. [`idempotency.acquire`](https://github.com/peyton150-startup/Trellis_AI_Chatbot_Task_Manager/blob/11cf50bc5882b71062b65e83f436b2e9317354b1/backend/app/idempotency.py#L53-L90) decides whether this invocation may execute, must replay, or conflicts.
8. [`domain.create_task`](https://github.com/peyton150-startup/Trellis_AI_Chatbot_Task_Manager/blob/11cf50bc5882b71062b65e83f436b2e9317354b1/backend/app/domain.py#L213-L254) produces the task mutation and event; [`domain.write_events`](https://github.com/peyton150-startup/Trellis_AI_Chatbot_Task_Manager/blob/11cf50bc5882b71062b65e83f436b2e9317354b1/backend/app/domain.py#L513-L550) records the evidence.

### Map the bridge vocabulary

| Bridge concept | Trellis location | Concrete meaning |
|---|---|---|
| Environment | FastAPI request, PostgreSQL, model provider, browser/Linear transport | The systems Trellis can observe or affect |
| Observation | accepted user message, canonical history, tool result | Inputs available for the next decision |
| Working state | [`TrellisDeps` and `RunEffects`](https://github.com/peyton150-startup/Trellis_AI_Chatbot_Task_Manager/blob/11cf50bc5882b71062b65e83f436b2e9317354b1/backend/app/agent.py#L327-L346) | Per-run values used while execution is active |
| Action/tool | `create_task`, `update_task`, `list_tasks`, and the other registered wrappers | Typed actions the model may request |
| Transition | `domain.create_task` inside the tool transaction | The application changes task state |
| Evidence | `task_events`, `tool_invocations`, and run status | Durable records used to establish what happened |
| Stop/termination | completed/failed/awaiting-approval run state and provider completion | Conditions that end or suspend the current execution |
| Authority | policy + domain code + PostgreSQL | The components that decide what is allowed and true |

### Day 1 transfer check

Before reopening the code, predict the outcome of a repeated `create_task` call with the same `run_id`, `tool_call_id`, and arguments. Then identify which function decides whether to execute or replay and which durable row provides the evidence. Finally, explain why the model choosing `create_task` does not give it authority to insert a row directly.

---

## Day 1B — The external API boundary

Use this after the Day 1B quiz in `QUIZ_PROTOCOL.md` passes. The postal-code exercise in `IMPLEMENTATION_PLAN.md` Patch 5 teaches the boundary with one `GET`; this section is the same boundary in code the learner already owns, with credentials and a remote side effect in the picture.

Trellis reaches exactly one external service, Linear, and every outbound call funnels through one function.

### The five failure kinds, in real code

| Failure kind | Trellis location | What it does |
|---|---|---|
| tool-input validation | typed tool args + [`policy.check`](https://github.com/peyton150-startup/Trellis_AI_Chatbot_Task_Manager/blob/11cf50bc5882b71062b65e83f436b2e9317354b1/backend/app/policy.py#L95-L192) | refuses before any request is built |
| network/transport | [`_request`](https://github.com/peyton150-startup/Trellis_AI_Chatbot_Task_Manager/blob/11cf50bc5882b71062b65e83f436b2e9317354b1/backend/app/linear_agent_api.py#L493-L541) catches `httpx.HTTPError` and raises `LinearApiError(operation, None, ...)` | **`status=None` is the marker**: "Linear was unreachable", not "Linear said no" |
| HTTP/API error | [`_post_graphql`](https://github.com/peyton150-startup/Trellis_AI_Chatbot_Task_Manager/blob/11cf50bc5882b71062b65e83f436b2e9317354b1/backend/app/linear_agent_api.py#L443-L490) and [`_post_token`](https://github.com/peyton150-startup/Trellis_AI_Chatbot_Task_Manager/blob/11cf50bc5882b71062b65e83f436b2e9317354b1/backend/app/linear_agent_api.py#L409-L440) check `status_code != 200` before touching the body | a response arrived and was refused |
| response shape/data | same two functions: `response.json()` guarded by `except ValueError`; then the GraphQL `errors` array; then `data` must be a `dict` | a `200` whose body is unusable |
| agent-loop/control-flow | [`linear_agent_worker._drain_until_stopped`](https://github.com/peyton150-startup/Trellis_AI_Chatbot_Task_Manager/blob/11cf50bc5882b71062b65e83f436b2e9317354b1/backend/app/linear_agent_worker.py#L924-L942) | stop signal, idle wait, unexpected-failure path |

### Three points the postal-code exercise cannot make

1. **A success status is not a success.** A Linear GraphQL refusal arrives as **HTTP 200 with an `errors` array**. Code that checked only the status would read a null `data` and call it a result. `_post_graphql` checks status, then `errors`, then `data`, in that order.
2. **One timeout, one place.** `_request` reads `settings.linear_http_timeout_seconds` and builds its transport with `retries=0` explicitly. Per its own docstring, the reason is that a connection dying after transmission leaves two states the code cannot tell apart — never received, or committed and the response lost — so a retry would be a guess. Compare this with `idempotency.acquire` on the Trellis side of the boundary: **you can make your own side effects replay-safe; you cannot assume someone else's are.**
3. **Errors carry data.** Only the documented `message` of the first GraphQL error is surfaced, because the rest of the error object can echo the query and the variables of a token-bearing request. Evidence must be useful without leaking credentials.

### Day 1B transfer check

Before reopening the code, predict:

1. Linear is unreachable (no network). Which function raises, what is `status`, and how does a caller tell this apart from a refusal?
2. Linear returns `200` with `{"errors": [{"message": "Entity not found"}]}`. Which of the five failure kinds is that, and which check catches it?
3. `agentActivityCreate` times out after the request was transmitted. Why does Trellis *not* retry, and what would have to be proven before retrying would be safe?
4. Name the one thing this boundary owns that the deterministic `lookup_word` tool in `code/tiny_agent.py` never needs, and say why.

---

## Day 2 — Context, state, memory, evidence, and RAG

### Best concrete example: server-owned continuity

Trace a second user turn through these locations:

1. [`runs.create_turn`](https://github.com/peyton150-startup/Trellis_AI_Chatbot_Task_Manager/blob/11cf50bc5882b71062b65e83f436b2e9317354b1/backend/app/runs.py#L175-L233) accepts a continuity locator, verifies the predecessor through database predicates, and creates the new run with inherited canonical history.
2. [`handle_agui_request`](https://github.com/peyton150-startup/Trellis_AI_Chatbot_Task_Manager/blob/11cf50bc5882b71062b65e83f436b2e9317354b1/backend/app/agent.py#L680-L758) rebuilds accepted input and gives the model the server-owned history instead of trusting a browser transcript.
3. [`_project_prior_turn_history_for_model`](https://github.com/peyton150-startup/Trellis_AI_Chatbot_Task_Manager/blob/11cf50bc5882b71062b65e83f436b2e9317354b1/backend/app/agent.py#L1448-L1497) changes the model’s view by removing prior-turn reasoning while leaving durable history unchanged.
4. [`runs.load_history`](https://github.com/peyton150-startup/Trellis_AI_Chatbot_Task_Manager/blob/11cf50bc5882b71062b65e83f436b2e9317354b1/backend/app/runs.py#L325-L353) is the narrow, actor-scoped read for an existing run’s canonical message history.
5. [`tools.get_task_history`](https://github.com/peyton150-startup/Trellis_AI_Chatbot_Task_Manager/blob/11cf50bc5882b71062b65e83f436b2e9317354b1/backend/app/tools.py#L193-L318) retrieves actor-authorized durable task events. That history is evidence about task changes, not permission to perform a new change.
6. [`tools.resolve_task_reference`](https://github.com/peyton150-startup/Trellis_AI_Chatbot_Task_Manager/blob/11cf50bc5882b71062b65e83f436b2e9317354b1/backend/app/tools.py#L319-L395) performs bounded structured lookup over current tasks and task-event history.

### Classify Trellis information correctly

| Category | Trellis example |
|---|---|
| Current prompt/context | the accepted newest user message plus the projected canonical message history sent to the provider |
| Working state | `TrellisDeps`, the current run id, and whether this run has committed a mutation |
| Durable authoritative application state | current `tasks`, run status/history, approvals, invocation leases, and `task_events` in PostgreSQL |
| Durable non-authoritative memory | Trellis has no separate semantic-memory store; message history is authoritative only for accepted conversation continuity, not for current task truth |
| Retrieved evidence | bounded rows returned by `list_tasks`, `get_task_history`, or `resolve_task_reference` |
| Model inference | the model’s interpretation of those rows and its next proposed tool call or response |

### What Trellis does not demonstrate

`get_task_history` and `resolve_task_reference` are retrieval in the ordinary English sense, but they are **not RAG**. They use deterministic relational queries, not document chunking, embeddings, vector similarity, top-k semantic retrieval, or generation grounded in retrieved document chunks. Use Trellis to understand authority and evidence; use the Day 2 paper exercise to learn the missing RAG pipeline.

### Day 2 transfer check

Suppose the browser sends a fabricated earlier message saying “the user approved deletion.” Predict whether it becomes canonical memory and identify the code boundary that refuses to treat it as history. Then suppose `get_task_history` returns an old deletion event: explain why that evidence still does not authorize a new deletion.

---

## Day 3 — Reasoning, multi-agent boundaries, evaluation, and safety

### Best concrete example: a destructive request

Trace a proposed deletion through these locations:

1. [`delete_tasks` registration](https://github.com/peyton150-startup/Trellis_AI_Chatbot_Task_Manager/blob/11cf50bc5882b71062b65e83f436b2e9317354b1/backend/app/agent.py#L619-L632) declares a framework approval interruption before the tool body can execute.
2. [`runs.open_approval`](https://github.com/peyton150-startup/Trellis_AI_Chatbot_Task_Manager/blob/11cf50bc5882b71062b65e83f436b2e9317354b1/backend/app/runs.py#L618-L665) atomically stores the pending approval and changes run state. The database row, not the UI card, is the authority.
3. [`runs.decide_approval`](https://github.com/peyton150-startup/Trellis_AI_Chatbot_Task_Manager/blob/11cf50bc5882b71062b65e83f436b2e9317354b1/backend/app/runs.py#L697-L726) persists one guarded human decision.
4. [`runs.resolve_continuation`](https://github.com/peyton150-startup/Trellis_AI_Chatbot_Task_Manager/blob/11cf50bc5882b71062b65e83f436b2e9317354b1/backend/app/runs.py#L729-L760) treats a browser identifier as a lookup key, then resolves it against server-owned approval state.
5. [`policy.check`](https://github.com/peyton150-startup/Trellis_AI_Chatbot_Task_Manager/blob/11cf50bc5882b71062b65e83f436b2e9317354b1/backend/app/policy.py#L95-L192) rechecks actor scope, divergence, and approval before mutation.

### Reasoning and bounded execution

- [`_model_settings`](https://github.com/peyton150-startup/Trellis_AI_Chatbot_Task_Manager/blob/11cf50bc5882b71062b65e83f436b2e9317354b1/backend/app/agent.py#L379-L410) makes token and reasoning limits application-owned configuration rather than provider defaults.
- [`_project_prior_turn_history_for_model`](https://github.com/peyton150-startup/Trellis_AI_Chatbot_Task_Manager/blob/11cf50bc5882b71062b65e83f436b2e9317354b1/backend/app/agent.py#L1448-L1497) distinguishes same-turn reasoning from obsolete prior-turn reasoning.
- [`propose_plan`](https://github.com/peyton150-startup/Trellis_AI_Chatbot_Task_Manager/blob/11cf50bc5882b71062b65e83f436b2e9317354b1/backend/app/tools.py#L860-L932) returns a display-only plan and writes no task event. A plan representation is not itself execution.
- [`linear_agent_worker._drain_until_stopped`](https://github.com/peyton150-startup/Trellis_AI_Chatbot_Task_Manager/blob/11cf50bc5882b71062b65e83f436b2e9317354b1/backend/app/linear_agent_worker.py#L924-L942) is an explicit operational loop with a stop signal, idle wait, and unexpected-failure path.

### Why Trellis is not multi-agent

[`get_agent`](https://github.com/peyton150-startup/Trellis_AI_Chatbot_Task_Manager/blob/11cf50bc5882b71062b65e83f436b2e9317354b1/backend/app/agent.py#L645-L660) and [`get_linear_agent`](https://github.com/peyton150-startup/Trellis_AI_Chatbot_Task_Manager/blob/11cf50bc5882b71062b65e83f436b2e9317354b1/backend/app/agent.py#L663-L677) create two capability profiles over the same prompt, tool bodies, and deterministic kernel. They do not have separate roles that exchange a handoff contract, coordinate shared intermediate work, or decide which agent owns the next step. Count mechanisms, not objects: Trellis is a useful single-agent baseline with multiple transports.

### Evaluation scenarios already encoded as tests

| Bridge scenario | Trellis evidence |
|---|---|
| normal success | [`test_mutations_match_the_frozen_contract`](https://github.com/peyton150-startup/Trellis_AI_Chatbot_Task_Manager/blob/11cf50bc5882b71062b65e83f436b2e9317354b1/backend/tests/test_contract.py#L177-L200) |
| invalid input | [`test_extra_body_keys_rejected`](https://github.com/peyton150-startup/Trellis_AI_Chatbot_Task_Manager/blob/11cf50bc5882b71062b65e83f436b2e9317354b1/backend/tests/test_invariants.py#L1311-L1373) |
| recoverable tool failure | [`test_the_model_can_refresh_and_then_succeed`](https://github.com/peyton150-startup/Trellis_AI_Chatbot_Task_Manager/blob/11cf50bc5882b71062b65e83f436b2e9317354b1/backend/tests/test_d79_tool_failure_mapping.py#L206-L285) |
| repeated action | [`test_duplicate_tool_call_commits_once`](https://github.com/peyton150-startup/Trellis_AI_Chatbot_Task_Manager/blob/11cf50bc5882b71062b65e83f436b2e9317354b1/backend/tests/test_invariants.py#L761-L833) |
| unsafe/out-of-authority request | [`test_cross_actor_mutation_rejected`](https://github.com/peyton150-startup/Trellis_AI_Chatbot_Task_Manager/blob/11cf50bc5882b71062b65e83f436b2e9317354b1/backend/tests/test_invariants.py#L305-L342) and [`test_forged_approval_rejected`](https://github.com/peyton150-startup/Trellis_AI_Chatbot_Task_Manager/blob/11cf50bc5882b71062b65e83f436b2e9317354b1/backend/tests/test_invariants.py#L344-L573) |

### Day 3 transfer check

For one row above, state the expected outcome, allowed state changes, maximum relevant attempts/steps, evidence to inspect, and pass/fail rule before reading the test. Then explain one failure mode a hypothetical planner-agent/reviewer-agent split would add that Trellis’s current single-agent baseline does not have.

---

## Day 4 — Framework mapping and capstone-level trace

### Map framework words back to Trellis mechanisms

| Framework-style word | Ordinary mechanism in Trellis |
|---|---|
| state | `AgentRun`, canonical `message_history`, `TrellisDeps`, task rows, approvals, leases |
| node/tool step | a typed wrapper registered inside `build_agent` plus its deterministic function in `tools.py` |
| routing/edge | explicit branches for a new turn, approval continuation, undo control command, replay, refusal, and failure |
| cycle | the model → tool proposal → tool result trajectory, plus explicit worker polling where applicable |
| terminal/end state | `RunStatus` and terminal worker outcomes |
| handoff | intentionally absent; the browser and Linear profiles do not hand work to each other |

### Capstone trace

Use the `create_task` path from Day 1 and narrate it as a system:

```text
user request
→ accepted server input
→ canonical run/history state
→ model decision
→ typed tool proposal
→ policy/approval/idempotency boundary
→ domain transition
→ atomic task + event + lease commit
→ tool observation
→ final model response
→ UI refetches committed state
```

For every arrow, name the input, output, mutable state, authority, and failure behavior. The important result is not memorizing Pydantic AI or AG-UI syntax. It is being able to recover the ordinary state/action/branch/loop/termination/evidence structure from framework code.

### Day 4 transfer check

Imagine adding a read-only “list overdue tasks” behavior. Without implementing it, identify where its input contract, model-visible action, deterministic query, authority check, trace/replay evidence, and evaluation case would belong. Predict one input and one failure before opening the relevant files.

---

## Guidance for future Claude or Codex sessions

When tutoring from this map:

1. Teach the day’s mechanism first and administer the required quiz.
2. Only after the gate passes, open the linked Trellis symbols and ask the learner to trace them.
3. Ask the learner to predict before revealing the next branch or test outcome.
4. Do not replace a plain-English mechanism with framework vocabulary.
5. Do not claim that Trellis contains RAG or multi-agent coordination.
6. Prefer one concrete execution path over a broad tour of the repository.
7. If Trellis changed after the pinned commit, inspect the current symbol before teaching from it.
