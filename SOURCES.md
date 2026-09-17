# Academic Sources and Scope

Checked: 2026-09-02

## Strict Source Rule

The learning content in this repository is grounded only in official **Carnegie Mellon University computer-science / School of Computer Science material** and official **UC Berkeley EECS / CS course material**.

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

## Deliberate Omissions

The prior version referenced broader CMU material and practitioner/social sources. Those have been removed from this sprint.

This repository also does not pretend that the public CMU Agentic AI landing page contains the private labs, assignments, or complete lecture notes. It prepares only from what CMU and Berkeley make publicly available.

## Non-Curriculum Tooling Reference

**These are not curriculum sources.** They may be used only for the syntax and behavior of an optional tool, never as evidence for a teaching claim.

### TypeSafe (Jev System One model)

https://docs.typesafe.ai/llms.txt

Checked: 2026-09-17. Used only for:

- how to call the SDK (`pip install typesafe-sdk`, Python ≥ 3.10, `TYPESAFE_API_KEY`);
- what it returns: a Choice (one option from a set), a Noul (probability of yes), or a Score (ordered levels), each with probabilities and confidence;
- its documented limits (`/model-jaggedness/jev-1.13.md`): no text generation, weak at math/dates/multi-hop reasoning, and influenced by adversarial content.

Its calibration claims are the vendor's and are not verified here. Thresholds must be treated as policy choices and checked against scenarios.

Where it appears in this repo: `docs/IMPLEMENTATION_PLAN.md` (Patch 5), `docs/ARCHITECTURE_CONTRACT.md` (§5), `docs/EVALUATION_PLAN.md`, and `docs/SPRINT_PLAN.md` (Days 2–4, concept only).
