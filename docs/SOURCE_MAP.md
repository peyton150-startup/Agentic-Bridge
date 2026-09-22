# Source Map — Fundamental → Official Academic Source

Use this file to audit the sprint. Every major teaching section is tied to an official CMU or UC Berkeley computer-science source.

| Sprint fundamental | Official source basis | Why it is in the bridge |
|---|---|---|
| CMU prerequisites | CMU SCS Executive Education Agentic AI Program | The program explicitly expects Python, algorithm design, data structures, LLMs, and AI. |
| Agent / environment / actions / goals | UC Berkeley CS188 Agents + State Spaces | Gives a precise agent model before LLM-specific framework vocabulary. |
| LLM-based agent, tool use, memory, task decomposition | CMU LTI 11-768 AI Agents | Direct CMU course description of LLM agents interacting with external environments. |
| Memory, tools, reasoning loops | CMU Agentic AI Program Module 2 | Direct preparation vocabulary for the second program module. |
| RAG, embeddings, vector databases | CMU Agentic AI Program Module 3 + learning outcomes | Direct preparation vocabulary for retrieval-based agents. |
| State representation for decisions | UC Berkeley CS188 State Spaces | Reinforces representing the information needed for decision/planning rather than treating all available information as equivalent state. |
| Planning / candidate actions / goals | UC Berkeley CS188 Search + CMU Agentic AI Modules 2/4 | Supplies a classical control model for reasoning about LLM planning strategies. |
| External API/tool boundary behind a tool contract | CMU Agentic AI Program (external APIs/tools, Modules 1–2) | The program's own scope includes agents acting through external APIs and tools. The core teaches the boundary, not API development. API development appears only in the optional Extension X below. |
| Request/response, status, timeout, transport failure | CMU 15-213 Introduction to Computer Systems (networking, robustness) | Keeps the external call an ordinary program/network boundary with ordinary failure modes rather than an opaque capability. |
| Multi-agent roles and coordination | CMU Agentic AI Modules 4–5 | Direct preparation vocabulary for CMU's multi-agent progression. |
| LangGraph / CrewAI recognition | CMU Agentic AI Program applied tools + Module 5 | Recognition only; API mastery is intentionally left to CMU. |
| Evaluation / guardrails / logging / observability | CMU Agentic AI Module 6 | Directly mirrors the public CMU module. |
| Safety sandboxing / credentialing | CMU LTI 11-768 AI Agents | Grounds authority/permission questions in CMU agent-course concerns. |
| Execution monitoring / reliable integrated agents | CMU CSD 15-482 Autonomous Agents | Reinforces that agent quality includes integration, testing, monitoring, reliability, and robust behavior. |
| Program/network/external-system mental model | CMU 15-213 Introduction to Computer Systems | Keeps model/tool calls connected to ordinary software execution, communication, performance, and robustness. |
| Python abstraction | UC Berkeley CS61A | Supports the prerequisite diagnostic for functions, control/data abstraction, and program structure. |
| Data structures / software engineering | UC Berkeley CS61B | Supports the prerequisite diagnostic for representation/data-structure choices and elementary software engineering. |

## Optional Extension X — Academic Concepts

These rows support only `FUNDAMENTALS.md` C3–C4 and the optional Extension X.
They do not change the core.

| Extension concept | Official source basis | Why it is in the extension |
|---|---|---|
| Server/backend responsibility; consuming vs providing an API | CMU 15-113 Week 5 + HW4; UC Berkeley INFO 153B (catalog + Spring 2026) | Reverses Day 1's client role, so the learner can reason about both ends of an HTTP boundary. |
| REST routes, HTTP methods, JSON, status codes (200/201/400/404) | UC Berkeley INFO 153B Spring 2026; CMU 15-113 HW4 | Gives the inbound vocabulary and the status choices the extension exercise uses. |
| Schema validation vs error handling; server-side input validation | UC Berkeley INFO 153B Spring 2026 (validation, error handling); CMU 15-113 HW4 | Grounds "schema validation ≠ domain validation" and "return helpful errors, don't crash". |
| Secrets stay on the backend; local testing with `curl` | CMU 15-113 HW3 + HW4 | Grounds the authenticity/secret discussion and local, deterministic testing. |
| Distributed communication, protocols, latency, failure, concurrency | CMU 15-440 Fall 2026 syllabus + schedule | Makes webhook behavior an ordinary distributed-systems problem rather than framework behavior. |
| Duplicate delivery, idempotency, no exactly-once | CMU 15-440 Spring 2014 Lecture 6 (RPC), **historical** | The course's own at-least-once / at-most-once analysis is the basis for deduplicating by event ID. |
| Callback communication | CMU 15-440 Spring 2014 Lecture 8 (AFS/Coda callbacks), **historical** | Shows a callback is an established distributed-systems pattern. |
| Ordering across machines cannot be assumed | CMU 15-440 Fall 2026 (Time and Synchronization) | Grounds "do not assume events arrive in order". |
| Sender authenticity as a security concern | CMU 15-440 Fall 2026 objectives (security challenges); CMU 15-113 HW3/HW4 (secrets) | Concept level only. No signing is implemented. |
| Asynchronous/background work (acknowledge vs process) | UC Berkeley INFO 153B Spring 2026 (asynchronous task queues) | Recognition only. No queue is built. |

Berkeley precision: the INFO 153B **catalog** names FastAPI, and the **Spring
2026 course teaches Flask**. Its concepts are framework-neutral. That is why the
course is used here, and it is never cited as a FastAPI source.

## Optional Extension X — Framework Syntax (not academic sources)

| Framework behavior | Official FastAPI documentation page |
|---|---|
| App object, path operations, `/docs`, `/openapi.json` | First Steps |
| Path parameters / query parameters | Path Parameters; Query Parameters |
| Pydantic request-body models; path vs query vs body resolution | Request Body |
| `status_code=` on a path operation | Response Status Code |
| `HTTPException`; default 422 for invalid request data | Handling Errors |
| `TestClient` with pytest | Testing |
| `app.webhooks` documents **outbound** webhooks only | OpenAPI Webhooks |

FastAPI documentation explains what FastAPI does. It is not evidence for any
general computer-science claim in this repository.

## Excluded on Purpose

No blog, social-media, practitioner-forum, vendor-tutorial, news-article, or third-party curriculum source is needed for this readiness sprint.
