# Academic Sources and Scope

Checked: 2026-09-02

## Strict Source Rule

Academic teaching claims in this repository are grounded only in official
**Carnegie Mellon University computer-science / School of Computer Science
material** and official **UC Berkeley EECS / CS course material**. The optional
framework reference at the end of this file is used only for framework syntax
and behavior.

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
