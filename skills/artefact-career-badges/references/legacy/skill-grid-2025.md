> **SUPERSEDED (2025).** Use `../skill-grid-2026.md`. Kept for the Growth badges and Level 4 that the 2026 grid dropped.

# Artefact SE Skill Grid 2025 — Per-Badge Reference

Distilled verbatim from `SOFTWARE ENGINEER - CAREER SYSTEM v2025.pdf` and `SE Skill Grid 2025 - [FR] Soft. Eng Tech Badges.pdf`.
Remember: **Output Examples** and **Outcome Examples** are non-exhaustive illustrations, never mandatory checkboxes.

---

## 1. Machine Learning Engineer (Expertise — shared with Data Scientists)

**Role essence**: Help ship ML and GenAI/LLM systems faster and with higher confidence in production through MLOps / LLMOps pipelines, model/LLM integration, evaluation, monitoring, and cost/performance optimization.

### Level 1 (Reach: Artefact SoftEng & DS)
- **Expectations**:
  - Implement basic MLOps / LLMOps pipelines and bring them to production.
  - Integrate models into cloud-based ML/AI environments (e.g. Vertex AI, AMLS, SageMaker, GCP Gemini, Azure OpenAI / Azure AI Foundry, Snowflake Cortex).
  - Apply fundamental ML and GenAI principles in production workflows (RAG, OCR/parsing, chunking, embeddings/vector search, structured outputs, prompt/agent workflows, retrieval/LLM evaluation).
  - Set up basic CI/CD workflows to automate ML/AI pipeline or service deployment.
  - Ensure code follows best practices for maintainability and scalability.
- **Illustrative Outputs**: MLOps/GenAI design patterns (vector stores, feature stores, warehouses); deploying/integrating models or GenAI chains/agents (OpenAI API, LangChain, LangGraph, direct SDKs); CI/CD for deployment & monitoring; experiment/evaluation tracking; REST/gRPC serving endpoints; basic performance/cost logging & monitoring; packaging for deployment.
- **Illustrative Outcomes**: ML/GenAI pipelines deployed and monitored in production; CI/CD automation reduced deployment errors; structured & reproducible evaluations/experiments; measurable cost or latency optimization.

### Level 2 (Reach: Artefact SoftEng & DS)
- **Expectations**: Design & implement end-to-end MLOps/LLMOps pipelines; optimize model serving/inference strategies for low latency, high availability, and cost efficiency; advanced monitoring/logging/alerting; scalable & resilient architectures; ML/AI-specific testing strategies (data validation, retrieval/judge evaluation, drift, integration testing); automated cost & performance monitoring; versioning, rollback, and automated retraining/refresh workflows.

---

## 2. Analytics Engineer (Expertise — shared with Data Analysts)

**Role essence**: Build data pipelines in all directions — from exploratory analysis to production transformation pipelines, from documentation and data contracts to data quality monitoring.

### Level 1 (Reach: PO, Data Engineers, Data Scientists, Data Analysts — project team)
- **Expectations**:
  - Write complex SQL queries autonomously.
  - Use main Data Engineering transformation tools (`dbt`, `sqlmesh`, Snowflake tasks/streams/dynamic tables).
  - Apply good practices in SQL and data transformation tools.
  - Debug data pipelines within own scope.
- **Illustrative Outputs**: Complex documented SQL queries explaining business logic; using modern data frameworks (`dbt`, `sqlmesh`); debugging data pipelines; writing interface contracts and data requests; basic data quality checks / tests; reviewing SQL queries.
- **Illustrative Outcomes**: Models delivered in `dbt`; source data inconsistencies identified and resolved; pipeline bugs fixed; transformations & data models easy for onboarded teammates to understand.

### Level 2 (Reach: Project team, data architect, client business people)
- **Expectations**: Mentor others on SQL/data management; master main DE tools and set them up from scratch autonomously; design smart data models for use cases; own data quality (specs met, tests/constraints enforced, accurate documentation); check query plans & optimize SQL execution time/processing costs; define & implement KPIs.

---

## 3. Technical Project Lead / Project Tech Lead (Growth)

**Role essence**: Lead technical streams and cross-expertise engineers (SE, DS, DA, DE) to frame work, ensure quality delivery, manage risks/roadblocks, and guide teammates.

### Level 1 (Reach: Artefact Consulting Manager & client tech counterparts)
- **Expectations**:
  - Ensure delivery of software engineering streams: validate prerequisites, create/structure tickets, review code, plan adoption/rollout.
  - Proactively communicate to reporting chain: regular updates on progress and roadblocks, manage expectations, address concerns.
  - Provide technical guidance and support to junior engineers (or peers on owned technical streams).
- **Illustrative Outputs**: 1:1s with project engineers / client PoC; leading or driving agile ceremonies / backlog refinement; helping break down features/PRDs into actionable tasks & milestones; defining and maintaining a clear technical backlog; tracking project issues, risks, and technical decisions (ADRs, PRDs, decision logs); constructive code reviews raising quality across the stack.
- **Illustrative Outcomes**: Streams delivered on time; positive client/team feedback on features and communication; increased team velocity and clarity; teammates aided by clear specs, reviews, and tooling.

### Level 2 (Reach: Artefact Manager/Director & client tech lead)
- **Expectations**: Frame and deliver SE streams autonomously (gather requirements, define scope, design architecture, write comprehensive design docs & ADRs, estimate effort & roadmap, ensure code quality across SQL/Python/infra, manage risks & dependencies); lead and mentor a small team of junior engineers (delegate tasks, align on *what* and *why*, identify skill gaps).

---

## 4. Software Developer (Expertise)

- **Level 1** *(Sub-system level; supervised design, autonomous implementation/testing/docs)*: API endpoints, clean code, unit tests, debugging own code, Git/Scrum workflow integration.
- **Level 2** *(Repository/system level; full-stack of a data/AI project)*: Active contribution across every layer of the stack, E2E/integration testing, reviewing peers'/juniors' PRs, breaking down user stories into technical tasks, subsystem refactoring, clear repo onboarding (`CONTRIBUTING.md`, ADRs), fast prod bug resolution, sharing best practices internally.
- **Level 3** *(Multi-system level; client tech lead reach)*: Organizes code reviews, reviews senior PRs, formalizes guidelines, repository-wide refactoring, designs simple solutions to complex multi-system problems, upskills DE/DS/DA teammates.

---

## 5. Site Security & Reliability Engineer — SSRE (Expertise)

- **Level 1** *(Task/supervised scope)*: Assist in monitoring & pipeline reliability, basic troubleshooting & incident response, support security measures (secrets/Keychain, roles/grants, network policies), implement/update CI/CD pipelines, Docker/Terraform basics, release/ops runbooks.
- **Level 2** *(Significant system components)*: Manage complex incidents & post-mortems/RCAs, design monitoring/alerting, implement security & least-privilege RBAC across environments (DEV/PP/PROD), reusable CI/CD components or Terraform modules, automate toil, mentor juniors.

---

## 6. Cloud Architect (Expertise)

- **Level 1**: Assist in designing/deploying small-scale cloud solutions, cloud infra docs, basic automation scripts, troubleshooting, cloud resource/cost reports.
- **Level 2**: Independently design & implement complex cloud solutions, disaster recovery, cloud deployment automation, cross-system integration, security/compliance, cloud cost & performance optimization.

---

## 7. Pre-Sales Engineer & Engineering Manager (Growth)

- **Pre-Sales L1**: Produce pitch content (slides, architecture, PoC, demo) autonomously from supervisor guidelines; translate technical choices into business implications for non-tech audiences.
- **Engineering Manager L1**: Contribute to a chapter sub-mandate (e.g. Kode, skills, bootcamps, templates), join interviewer pool, or coach a counselee.
