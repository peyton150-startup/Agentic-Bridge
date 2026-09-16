# CMU Alignment — What to Prepare vs What to Leave for the Program

## Public CMU Prerequisites

CMU's Agentic AI Program explicitly expects functional knowledge of:

```text
Python
algorithm design
data structures
LLMs
AI
```

The bridge therefore begins with a diagnostic instead of assuming BuildLens covered every prerequisite equally.

## Public CMU Module Sequence

```text
Module 1 — Foundations of Agentic AI and LLM Capabilities
Module 2 — Agent Architecture: Memory, Tools, and Reasoning Loops
Module 3 — RAG Agents and Vector Databases
Module 4 — Tree-of-Thought Reasoning and Multi-Agent Concepts
Module 5 — Multi-Agent Workflows with CrewAI and LangGraph
Module 6 — Evaluation, Guardrails, Logging, and Observability
Module 7 — Capstone Project
```

## Bridge Target

The bridge does **not** attempt to master these modules first.

It targets the minimum useful pre-understanding:

| CMU area | Before CMU you should already understand | Leave for CMU depth |
|---|---|---|
| LLM foundations | model call is probabilistic external behavior; context/request/response; structured application contract | deeper model/provider techniques |
| Agent architecture | state, action/tool, control loop, stop condition, authority | richer agent patterns |
| External tools/APIs | one tool's HTTP boundary: validated input, GET, timeout, status, parsed body, response validation, bounded observation, and the failure kinds that boundary makes distinguishable | integration breadth, provider SDKs, production API engineering |
| Memory | context vs durable state vs non-authoritative memory | advanced memory strategies |
| RAG | document → representation → retrieve → context → answer; retrieval vs generation failure | framework/vector DB implementation depth |
| Structured reasoning | planning/decomposition changes control flow and budget | Tree-of-Thought implementation depth |
| Multi-agent | roles, shared state, handoffs, termination, single-agent baseline | CrewAI/LangGraph orchestration depth |
| Evaluation/safety | explicit success criteria, failure cases, traces, guardrails | CMU's complete toolchain and practices |
| Capstone | define problem, agentic justification, architecture, evaluation | complete project construction/presentation |

## Why Berkeley CS188 Is Included

CMU's program is LLM-agent focused, but Berkeley CS188 supplies a compact classical agent vocabulary that prevents “agent = chatbot with tools” thinking:

```text
performance goal
environment
state / observation
actions
transition/consequence
goal / policy / planning
```

That vocabulary is useful when CMU later introduces LLM-based tools, reasoning, and multi-agent coordination.

## Why CMU 15-213 Is Included

Only as a reminder that model/tool calls still execute through ordinary software and systems boundaries:

```text
program
→ API/network/process boundary
→ external behavior
→ response/error
→ application interpretation
```

Day 1's single external API tool is where this stops being a metaphor. One GET
request is enough to make the boundary real.

Do not turn the sprint into a systems course, and do not turn the API exercise
into an API course. One endpoint, one request, one set of failure kinds.
