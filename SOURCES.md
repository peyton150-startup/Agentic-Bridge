# Academic Sources and Scope

Checked: 2026-09-02 (core). Sources 8–10 and the FastAPI reference checked 2026-09-21.

## Strict Source Rule

Academic teaching claims in this repository are grounded only in official
**Carnegie Mellon University computer-science / School of Computer Science
material** and official **UC Berkeley EECS / CS course material**. There is one
named exception: UC Berkeley School of Information's INFO 153B, a computing
course on back-end web architecture, used only for the optional Extension X
(source 10). The framework references at the end of this file are used only for
framework syntax and behavior.

No blogs, news explainers, Reddit, X/Twitter, social media, vendor tutorials, or third-party course summaries are curriculum sources.

## Carnegie Mellon University

### 1. CMU School of Computer Science Executive Education — Agentic AI Program

https://execonline.cs.cmu.edu/agentic-ai-program

Primary source for:

- prerequisite expectation: Python, algorithm design, data structures, LLMs, AI;
- seven-module progression;
- learning outcomes;
- memory, tools, structured reasoning;
- RAG, embeddings, vector databases;
- multi-agent workflows and coordination;
- external APIs/tools;
- evaluation and safety;
- LangChain/LCEL, CrewAI, LangGraph, ReAct, Tree-of-Thought;
- FAISS/Chroma/Pinecone;
- logging/observability/evaluation tooling;
- capstone orientation.

### 2. CMU Language Technologies Institute — 11-768 AI Agents

https://www.lti.cs.cmu.edu/misc-pages/intranet-course-info.html

Used for the LLM-agent mental model:

- autonomous systems using LLMs to perceive, reason, plan, and act;
- multi-step interaction with external environments;
- instruction following;
- tool use;
- memory;
- task decomposition;
- safety sandboxing;
- credentialing;
- modern agent frameworks.

### 3. CMU Computer Science Department — 15-482 Autonomous Agents

https://www.csd.cs.cmu.edu/academics/fall-courses

Current Fall 2026 CSD listing. Used for:

- complete integrated-agent thinking;
- agent architectures;
- reasoning/planning;
- execution monitoring;
- uncertainty;
- integration and testing;
- reliability and robustness;
- explanation of agent behavior.

### 4. CMU Computer Science Department — 15-213 Introduction to Computer Systems

https://www.cs.cmu.edu/~213/

Used only for the systems mental model beneath Python/agent abstractions:

- how programs execute and communicate;
- performance and robustness;
- networking;
- concurrent computation;
- reasoning beneath application APIs.

## UC Berkeley

### 5. UC Berkeley EECS — CS 188 Introduction to Artificial Intelligence

Course page:
https://www2.eecs.berkeley.edu/Courses/CS188/

Official textbook:
https://inst.eecs.berkeley.edu/~cs188/textbook/

Especially:

https://inst.eecs.berkeley.edu/~cs188/textbook/search/agents.html
https://inst.eecs.berkeley.edu/~cs188/textbook/search/state.html
https://inst.eecs.berkeley.edu/~cs188/textbook/mdp/

Used for:

- rational agents;
- environment, sensors/observations, actions;
- planning agents;
- state spaces;
- action/transition models;
- start states and goal tests;
- uncertainty and policy concepts.

### 6. UC Berkeley EECS — CS 61A

https://www2.eecs.berkeley.edu/Courses/CS61A/

Used for the prerequisite check around:

- procedural/control/data abstraction;
- functions and program structure;
- managing program complexity;
- basic algorithmic reasoning.

### 7. UC Berkeley EECS — CS 61B

https://www2.eecs.berkeley.edu/Courses/CS61B/

Used for the prerequisite check around:

- data structures;
- abstract data types;
- searching/sorting concepts;
- elementary software-engineering reasoning.

## Optional Extension X Sources — Serving an API and Receiving Events

These support only the optional Extension X (`FUNDAMENTALS.md` C3–C4). No CMU
or Berkeley course packages "FastAPI webhooks" as one topic. The concepts come
from the courses below, and FastAPI syntax comes only from its official
documentation (see Non-Academic Framework Reference).

### 8. CMU Computer Science — 15-113 Effective Coding with AI (Fall 2026)

Course page: https://www.cs.cmu.edu/~113/
HW3 — Explore an API: https://www.cs.cmu.edu/~113/hw3.html
HW4 — Backend + Frontend: https://www.cs.cmu.edu/~113/hw4.html

The schedule lists Week 4 "Getting started with APIs" (HW3) and Week 5
"Server-side development" (HW4). Used for:

- consuming an API vs building a backend that serves one;
- endpoints ("a specific URL on your backend that does something");
- JSON requests/responses; frontend → backend communication;
- server-side input validation and helpful error responses;
- keeping API keys/secrets on the backend in environment variables, never in code or the repository;
- local testing, including `curl`;
- CORS (recognition only);
- Flask or FastAPI as the suggested Python backend frameworks. HW4 names both. It does not require either.

### 9. CMU Computer Science — 15-440 Distributed Systems

Current (Fall 2026) syllabus: https://courseweb.sp.cs.cmu.edu/15-440/fall-2026/syllabus/
Current schedule: https://courseweb.sp.cs.cmu.edu/15-440/fall-2026/schedule/

Current learning objectives include writing programs that interoperate using
well-defined protocols, debugging highly concurrent code across machines, using
network communication primitives, understanding the general properties of
networked communication, employing paradigms such as RPC, and identifying the
security challenges of distributed programs. The current schedule includes
Communication, Time and Synchronization, and Remote Procedure Calls. Used for:

- communication between programs across a network under a defined protocol;
- latency, imperfect communication, and failure as normal conditions;
- why ordering across machines cannot be assumed;
- protection from accidental or malicious senders (security challenges).

**Historical supporting material, not the current syllabus:** the public
Spring 2014 offering of the same course,
https://www.cs.cmu.edu/~dga/15-440/S14/syllabus.html. Used only for:

- Lecture 6, RPC (https://www.cs.cmu.edu/~dga/15-440/S14/lectures/06-rpc.pdf):
  at-least-once vs at-most-once semantics, "exactly-once" as impossible in
  practice, at-least-once suited only to idempotent operations, and at-most-once
  requiring request identification plus a record of handled requests. This is
  the basis for duplicate delivery and idempotent handling;
- Lecture 8, "Distributed Filesystems 2 — AFS, Coda, callbacks"
  (https://www.cs.cmu.edu/~dga/15-440/S14/lectures/08-dfs2.pdf): callbacks as an
  established distributed-systems communication pattern.

### 10. UC Berkeley School of Information — INFO 153B Back-End Web Architecture

Catalog: https://www.ischool.berkeley.edu/courses/info/153b
Spring 2026 public course site: https://groups.ischool.berkeley.edu/i253/sp26/

The **catalog description** names Python, FastAPI, Docker, relational/NoSQL
databases, and Celery/Redis. It also describes building APIs as microservices.
The **Spring 2026 implementation uses Flask, not FastAPI** ("Build RESTful APIs
using Python (Flask)"). Do not describe the Spring 2026 labs as FastAPI labs.

Used only for framework-neutral concepts taught in Spring 2026:

- REST APIs, routes, and HTTP methods (GET, POST, PUT, DELETE);
- JSON request/response handling;
- HTTP status codes (200, 201, 400, 404);
- input validation (schema validation) and error handling;
- CRUD;
- asynchronous task queues (Redis/rq), for recognition that acknowledging work and doing it can be separate;
- system design.

## Deliberate Omissions

The prior version referenced broader CMU material and practitioner/social sources. Those have been removed from this sprint.

This repository also does not pretend that the public CMU Agentic AI landing page contains the private labs, assignments, or complete lecture notes. It prepares only from what CMU and Berkeley make publicly available.

## Non-Academic Framework Reference

The optional Day 4 Pydantic AI mini-unit uses only the framework's official
documentation for framework syntax and behavior:

- Agents: https://ai.pydantic.dev/agents/
- Dependencies and `RunContext`: https://ai.pydantic.dev/dependencies/
- Function tools: https://ai.pydantic.dev/tools/
- Messages and chat history: https://ai.pydantic.dev/message-history/
- Deferred tools and approvals: https://ai.pydantic.dev/deferred-tools/
- AG-UI integration: https://ai.pydantic.dev/ui/ag-ui/

These are vendor documentation links, not academic curriculum sources. They
may explain what a Pydantic AI API does; claims about agent concepts, planning,
memory, multi-agent coordination, evaluation, and safety must still be grounded
in the official CMU and UC Berkeley sources above.

### FastAPI (optional Extension X only)

Official documentation, checked 2026-09-21. Framework syntax and behavior only:

- First Steps (path operations, automatic `/docs` and `/openapi.json`): https://fastapi.tiangolo.com/tutorial/first-steps/
- Path Parameters: https://fastapi.tiangolo.com/tutorial/path-params/
- Query Parameters: https://fastapi.tiangolo.com/tutorial/query-params/
- Request Body (Pydantic models; how FastAPI decides path vs query vs body): https://fastapi.tiangolo.com/tutorial/body/
- Response Status Code (`status_code=` on the decorator): https://fastapi.tiangolo.com/tutorial/response-status-code/
- Handling Errors (`HTTPException`; `RequestValidationError` for invalid request data, default 422): https://fastapi.tiangolo.com/tutorial/handling-errors/
- Testing (`TestClient`, built on HTTPX, used with pytest): https://fastapi.tiangolo.com/tutorial/testing/
- OpenAPI Webhooks: https://fastapi.tiangolo.com/advanced/openapi-webhooks/

The OpenAPI Webhooks page is easy to misread. `app.webhooks` **documents
webhooks that your application sends** to other systems. It is available in
FastAPI 0.99.0 and later. FastAPI does not send them for you, and it is not how
you **receive** a webhook. A receiver is an ordinary path operation, usually
`POST`. Extension X builds a receiver and does not use `app.webhooks`.

FastAPI documentation is a framework reference, **not** the source of the
general computer-science concepts in C3–C4. Those come from sources 8–10.

## Non-Curriculum Tooling Reference

**These are not curriculum sources.** They may be used only for the syntax and behavior of an optional tool, never as evidence for a teaching claim.

### TypeSafe (Jev System One model)

https://docs.typesafe.ai/llms.txt

Checked: 2026-09-17. Used only for:

- how to call the SDK (`pip install typesafe-sdk`, Python ≥ 3.10, `TYPESAFE_API_KEY`);
- what it returns: a Choice (one option from a set), a Noul (probability of yes), or a Score (ordered levels), each with probabilities and confidence;
- its documented limits (`/model-jaggedness/jev-1.13.md`): no text generation, weak at math/dates/multi-hop reasoning, and influenced by adversarial content.

Its calibration claims are the vendor's and are not verified here. Thresholds must be treated as policy choices and checked against scenarios.

Where it appears in this repo: `docs/IMPLEMENTATION_PLAN.md` (Patch 6, the optional model swap), `docs/ARCHITECTURE_CONTRACT.md` (§5), `docs/EVALUATION_PLAN.md`, and `docs/SPRINT_PLAN.md` (Days 2–4, concept only).
