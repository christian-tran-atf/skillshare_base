# Artefact SE evaluation grid 2026: all skills, Levels 1-3, verbatim

Generated from `SE Evaluation Grid 2026 - [FR] Soft. Eng Badges.pdf` (read 2026-11-20). **Output Examples** and **Outcome Examples** are non-exhaustive illustrations, never mandatory checkboxes. Levels 1-3 only (the 2026 career guide still describes four badge levels). Technical Project Lead, Pre-Sales Engineer and Engineering Manager have no 2026 grid; see `legacy/skill-grid-2025.md` (2025, superseded) and `../SKILL.md`. Same content, one file per skill, in the `career-badge-mapping` skill.

## Generic level definitions (apply to every skill)

> Source: *SE Evaluation Grid 2026 - [FR] Soft. Eng Badges.pdf*, page 1 header block ("High level definition of each level"). Wording is identical to the 2025 grid for Levels 1-3; Level 4 does not appear in the 2026 grid (2025 Level 4 lines: `../legacy-2025/grid/_general-levels.md`). The 2026 guide still describes four badge levels (4/10/16/28 pts).

### People

**Level 1**
- I deliver autonmously a well defined task.

**Level 2**
- I am fully autonomous and can make juniors progress on this topic.

**Level 3**
- I upskill confirmed DE & other profiles (DA/DS/DC) on this topic (vulgarisation, good practices).

### Knowledge

**Level 1**
- I am knowledgeable on the sub-systems & technologies I work on.

**Level 2**
- I have knowledge on several technologies & good practices on this topic.

**Level 3**
- I have knowledge on most technologies & complex optimizations on this topic.

### Design & Documentation

**Level 1**
- I delivered tested & documented assets.

**Level 2**
- I create the approach & frame documention, testing strategy etc on this topic.

**Level 3**
- I have and share convictions regarding architecture, documentation & approach on this topic.

### Delivery & Project Management

**Level 1**
- I deliver tasks on time & provide visibility.

**Level 2**
- I increase delivery on this topic when jumping in.
- I size tasks in terms of time & complexity on this topic to drive priorities.

**Level 3**
- I am able to boost velocity on the project when needed.
- I define roadmap on this topic for the project/company.

### Problem Solving

**Level 1**
- I fix bugs on my sub-system.

**Level 2**
- I can solve many issues on this topic quickly.

**Level 3**
- I can solve complex issues on this topic quickly with efficient solution & find improvements to prevent this to happen again.



---

## ML & Agentic Engineer (was "ML Engineer" in 2025)

> Kind: expertise (shared with Data Scientists; the career guide still calls it Machine Learning Engineer)

> Source: *SE Evaluation Grid 2026 - [FR] Soft. Eng Badges.pdf* (the sheet header still reads "H1 2025 skills updates (rewording & refresh)"). **Only Levels 1-3 appear in the 2026 grid**; the 2026 career guide still states four badge levels (4/10/16/28 pts). Level 4 lines of the 2025 grid, where they existed, are in `../legacy-2025/grid/ml-engineer.md`. Examples are non-exhaustive: nobody ticks every box. Each bullet is one line of a grid cell (the 2025 extraction merged some wrapped Outcome lines).

### Expectations

**Level 1**
- I implement basic MLOps pipelines and bring them to production
- I integrate models into cloud-based ML environments (Vertex AI, AMLS, SageMaker, GCP Gemini, Azure Open AI)
- I apply fundamental ML and GenAI principles in production workflows
- I set up basic CI/CD workflows to automate ML model deployment
- I ensure that my code follows best practices for maintainability and scalability

**Level 2**
- I design and implement end-to-end MLOps pipelines
- I optimize model serving strategies for low latency, high availability, and cost efficiency
- I implement advanced monitoring, logging, and alerting for ML systems
- I build scalable, resilient ML architectures to support high-traffic and multi-model serving
- I apply ML-specific testing strategies, including data validation, model drift detection, and integration testing
- I deploy and configure automated cost and performance monitoring for ML workloads
- I implement model versioning, rollback strategies, and automated retraining workflows

**Level 3**
- I design and implement enterprise-grade MLOps architectures for complex, large-scale projects
- I ensure the security, compliance, and auditability of ML models in production (GDPR, AI Act, SOC2)
- I lead MLOps implementation for mission-critical AI systems, ensuring scalability and reliability
- I advise clients on MLOps best practices, governance strategies, and ML lifecycle
- I evaluate, benchmark, and integrate new MLOps tools and emerging technologies
- I implement advanced model explainability and fairness assessment techniques (SHAP, LIME, AI governance frameworks)
- I coordinate with DevOps, SecOps, and Data teams to ensure ML pipelines align with enterprise standards
- I mentor junior engineers in MLOps practices

### Reach

**Level 1**
- Artefact softeng and DS

**Level 2**
- Artefact softeng and DS

**Level 3**
- Artefact or client's lead data scientist

### Output examples

**Level 1**
- I used MLOps design patterns (vector stores, feature stores, data lakes, data warehouses)
- I deployed pre-trained models to cloud platforms
- I set up basic CI/CD pipelines to automate model deployment and monitoring
- I tracked ML experiments using MLflow, Kubeflow, or Weights & Biases
- I deployed and exposed model serving endpoints via REST or gRPC
- I built and fine-tuned off-the-shelf models (e.g., scikit-learn, Prophet).
- I developed basic GenAI agents/chains using OpenAI API, LangChain, or LangGraph
- I set up basic logging and monitoring for model performance tracking

**Level 2**
- I packaged ML models for scalable deployment
- I implemented model version tracking and performance monitoring using MLflow or Weights & Biases
- I automated model retraining and deployment workflows
- I designed and implemented feature stores to improve data efficiency in ML pipelines
- I deployed and monitored automated retraining pipelines with drift detection
- I implemented blue-green deployments to ensure seamless model updates
- I designed and deployed multi-model serving architectures to handle concurrent predictions
- I optimized ML inference pipelines for cost and performance (e.g., batch vs. real-time inference, GPU vs. CPU optimization)
- I integrated logging, alerting, and monitoring solutions (e.g., Prometheus, Datadog, OpenTelemetry)

**Level 3**
- I led the adoption of a "walking skeleton" approach to incrementally improve MLOps workflows
- I designed and implemented advanced model governance strategies (audit logging, version control, explainability)
- I ensured compliance and security of ML pipelines (data encryption, IAM roles, secret management)
- I optimized ML deployment workflows to handle thousands of concurrent model inferences efficiently
- I developed custom MLOps automation tools to streamline model lifecycle management
- I integrated bias detection and fairness assessment into ML model validation
- I conducted internal MLOps training to upskill engineering teams
- I benchmarked and recommended emerging MLOps tools and practices to enhance production readiness

### Outcome examples

**Level 1**
- ML pipelines deployed successfully and monitored in production
- CI/CD automation reduced deployment errors
- ML experiments are structured and reproducible

**Level 2**
- Model retraining and versioning ensure reliability over time
- Blue-green deployments minimize downtime
- Inference pipelines optimized for cost and performance

**Level 3**
- Large-scale ML deployment workflows are efficient and secure.
- Governance and automation improved MLOps reliability.
- Teams upskilled and adopting best MLOps practices.


---

## Analytics Engineer

> Kind: expertise (shared with Data Analysts)

> Source: *SE Evaluation Grid 2026 - [FR] Soft. Eng Badges.pdf* (the sheet header still reads "H1 2025 skills updates (rewording & refresh)"). **Only Levels 1-3 appear in the 2026 grid**; the 2026 career guide still states four badge levels (4/10/16/28 pts). Level 4 lines of the 2025 grid, where they existed, are in `../legacy-2025/grid/analytics-engineer.md`. Examples are non-exhaustive: nobody ticks every box. Each bullet is one line of a grid cell (the 2025 extraction merged some wrapped Outcome lines).

### Expectations

**Level 1**
- I write complex SQL queries in autonomy
- I use the main DE tools (dbt, sqlmesh)
- I apply good practices in SQL and in the data transformation tools I use
- I debug data-pipelines on my scope

**Level 2**
- I mentor one or more people (DA, DE, ...) on creating and optimizing SQL or data management
- I master the main DE tools and am able to set them up from scratch by my own
- I design smart data model for my use cases
- I own data quality, ensuring that specifications have been met and that documentation is accurate

**Level 3**
- I define the data strategy for my client: data governance, naming convention, data migration...
- I know which tool to use in each situation and have convictions on most of them
- I manage data from sources to exposure
- I am in contact with data owners to define data specifications
- I have convictions around datagov tools on the market

### Reach

**Level 1**
- Product owner, Data Engineers, Data scientist, Data Analyst (project team)

**Level 2**
- project team, data architect, client business people

**Level 3**
- Client business and tech management

### Output examples

**Level 1**
- I wrote complex queries and document them to explain the business logic behind.
- I used modern data frameworks on my project (dbt, sqlmesh).
- I debugged data pipelines.
- I wrote interface contracts and data requests.
- I wrote basic data quality checks...

**Level 2**
- I reviewed several SQL queries
- I checked query plan and optimize SQL queries;
- I enforced consistency and integrity using tests and constraints;
- I documented and implemented KPIs;
- I identified relevant business KPIs;
- I set up from scratch a dbt project or other tool;
- I trained junior profiles on dbt

**Level 3**
- I defined and implemented a data governance strategy
- I defined a data domain with a data owner
- I audit the data quality of a data platform
- I handled a migration from one data tool to a better one
- I setup data lineage pipelines; design advanced data checks and monitoring
- I deploy datagov tool in production
- I upskilled the team working with me (DE/DS/DA, artefact and client).

### Outcome examples

**Level 1**
- Created 5 dbt models in 2 weeks
- Identified 15 inconsistencies in source data
- Corrected 3 bugs in a data pipeline in 1 week
- People onboarded don't have a hard time understanding my transformations & the data used

**Level 2**
- Successfully optimized an SQL query, reducing its execution time by 50%.
- Improved efficiency in a dbt project, resulting in a 20% decrease in processing costs. 10 potential bugs from reaching production thanks to data quality tests.
- Optimized (KPIs) that align with client Service Level Objectives (SLOs) and Service Level Agreements (SLAs), on query execution times.
- Junior fully autonomous on the tool used in 2 months

**Level 3**
- Implemented a data strategy that enabled the development of 5 data use cases
- Reduced time to market of UC by 20%
- Increased adoption & usage of data products
- The client trusts me to lead any analytics engineering subject.


---

## Software Developer

> Kind: expertise

> Source: *SE Evaluation Grid 2026 - [FR] Soft. Eng Badges.pdf* (the sheet header still reads "H1 2025 skills updates (rewording & refresh)"). **Only Levels 1-3 appear in the 2026 grid**; the 2026 career guide still states four badge levels (4/10/16/28 pts). Level 4 lines of the 2025 grid, where they existed, are in `../legacy-2025/grid/software-developer.md`. Examples are non-exhaustive: nobody ticks every box. Each bullet is one line of a grid cell (the 2025 extraction merged some wrapped Outcome lines).

### Expectations

**Level 1**
- I design efficient software projects sub-systems with supervision of a senior/lead engineer.
- I implement these sub-systems in autonomy once design has been approved by the lead.
- I test & document these sub-systems in autonomy based on the guidelines provided.

**Level 2**
- I master the implementation of all the stack of a given data project
- I am responsible for the respect of best practices (ETL or EL, databases, APIs)

**Level 3**
- I define implementation best practices at project level and share them internally to the software engineering team at Artefact.
- I have the right intuitions on how to tackle any kind of matter.

### Reach

**Level 1**
- Artefact team (PO, Lead, Fellow Developpers); client tech team.
- Sub-system level (class, function).

**Level 2**
- Artefact team; client tech team.
- System level (repository).

**Level 3**
- Client tech lead Multi-system level (backend+front+data and organizing the split and interactions)

### Output examples

**Level 1**
- I added API endpoints to a service.
- I debugged my code by myself.
- I apply the clean code rules (short atomic functions, clear var and func naming, understandable code at first sight).
- I write unit tests where its necessary.integrate in the product team workflow (gitflow, scrum, etc)

**Level 2**
- I contributed actively on every step of the project stack; wrote end-to-end integration testing; reviewed PR of junior engineers; ensured documentation is written.
- I broke down a user stories (with functional requirements) into technical tasks.
- I reviewed juniors' PRs.
- I understood and refactored code at a subs-system level.
- I upskilled the juniors I'm working with.

**Level 3**
- I organised code reviews; reviews PR of senior engineers; formalises knowledge and advocate for best practices when sizing projects; documents best practices and guidelines.
- I understood and refactored code at a repository level.
- I upskilled the team working with me (DE/DS/DA, artefact and client).
- I designed complex but simple multi-system solutions.

### Outcome examples

**Level 1**
- My senior does not have a hard time reviewing my PR.
- Sub-systems delivered in time.
- Sub-system improved & issues prevented based on my suggestion.
- People onboarded don't have a hard time understanding the code I produced.

**Level 2**
- The repo I am responsible for is clear and i can easily onboard new engineers.
- Bugs are fixed quickly in production Increased response time of the API by XX ms

**Level 3**
- Complicated & critical software engineering topic tackled efficiently & pushed to production.
- The client trusts me to lead any subject.
- Improved velocity & synergies in the project


---

## Site Security & Reliability Engineer (SSRE)

> Kind: expertise

> Source: *SE Evaluation Grid 2026 - [FR] Soft. Eng Badges.pdf* (the sheet header still reads "H1 2025 skills updates (rewording & refresh)"). **Only Levels 1-3 appear in the 2026 grid**; the 2026 career guide still states four badge levels (4/10/16/28 pts). Level 4 lines of the 2025 grid, where they existed, are in `../legacy-2025/grid/ssre.md`. Examples are non-exhaustive: nobody ticks every box. Each bullet is one line of a grid cell (the 2025 extraction merged some wrapped Outcome lines).

### Expectations

**Level 1**
- I assist in monitoring and maintaining system and pipeline reliability.
- I perform basic troubleshooting and incident response.
- I support senior engineers in implementing security measures.
- I have a basic understanding of system administration and networking.
- I am familiar with monitoring tools and incident management processes.
- I implement CI/CD pipelines with senior supervision.

**Level 2**
- I manage and resolve complex incidents.
- I implement and maintain security and reliability measures.
- I mentor junior engineers.
- I am proficient in system administration, networking, and security protocols.
- I design and implement monitoring and alerting systems.

**Level 3**
- I lead the team in designing and implementing reliability strategies.
- I oversee the development and deployment of security measures.
- I coordinate with other teams to ensure system reliability and security.
- I have advanced knowledge of system architecture, security, and reliability engineering, security architecture, risk management, and compliance.
- I drive strategic reliability and security initiatives.

### Reach

**Level 1**
- Limited to specific tasks and supervised projects

**Level 2**
- Responsible for significant components of the system

**Level 3**
- Influence across multiple teams and projects

### Output examples

**Level 1**
- I resolved minor incidents
- I generated system monitoring reports.
- I updated documentation of a release process.
- I implemented/updated CI/CD pipelines.
- I deployed infrastructure using terraform.
- I implemented basic Airflow DAGs.

**Level 2**
- I defined alert thresholds of alert policies of a web service.
- I automated a key system process.
- I conducted a security audit and provided a report.
- I performed root cause analysis and a post mortem for failures
- I implemented terraform modules for several users

**Level 3**
- I was the point of contact of the client's security executive.
- I designed and led the rollout of a new incident response plan.
- I developed and delivered training on security best practices.
- I managed a project to migrate systems to a new platform.
- I am knowledgeable on latest security news and trends.

### Outcome examples

**Level 1**
- Reduced the frequency of minor service disruptions.
- Provided timely information for identifying potential issues.
- Improved team efficiency through clearer documentation.

**Level 2**
- Faster detection and resolution of critical incidents.
- Increased system uptime and reduced manual effort.
- Removed all critical vulnerabilities from a docker image Reduced build times

**Level 3**
- Improved the team's incident response efficiency and reduced downtime.
- Increased security awareness and reduced security vulnerabilities.
- Successfully transitioned to a more scalable and reliable platform.


---

## Cloud Architect

> Kind: expertise (the career guide calls it Architect)

> Source: *SE Evaluation Grid 2026 - [FR] Soft. Eng Badges.pdf* (the sheet header still reads "H1 2025 skills updates (rewording & refresh)"). **Only Levels 1-3 appear in the 2026 grid**; the 2026 career guide still states four badge levels (4/10/16/28 pts). Level 4 lines of the 2025 grid, where they existed, are in `../legacy-2025/grid/cloud-architect.md`. Examples are non-exhaustive: nobody ticks every box. Each bullet is one line of a grid cell (the 2025 extraction merged some wrapped Outcome lines).

### Expectations

**Level 1**
- I assist in designing and implementing cloud-based solutions.
- I perform basic cloud infrastructure management and monitoring.
- I support senior architects in cloud migration projects.
- I have a basic understanding of cloud computing concepts and services.
- I have familiarity with cloud platforms (e.g., AWS, Azure, Google Cloud).
- I follow established cloud architecture guidelines.

**Level 2**
- I independently design and implement complex cloud solutions.
- I manage cloud infrastructure and ensure security and compliance.
- I mentor junior cloud engineers.
- I am proficient in cloud architecture, networking, and security.
- I design scalable and resilient cloud solutions.

**Level 3**
- I lead the cloud architecture team in designing and implementing cloud strategies.
- I oversee the development and deployment of cloud solutions.
- I coordinate with other teams to ensure cloud infrastructure reliability and security.
- I have advanced knowledge of cloud architecture, security, and compliance.
- I have strong leadership and project management skills.
- I drive strategic cloud initiatives (platform vision).

### Reach

**Level 1**
- Limited to specific tasks and supervised projects

**Level 2**
- Responsible for significant components of the cloud infrastructure

**Level 3**
- Influence across multiple teams and projects

### Output examples

**Level 1**
- I successfully deployed small-scale cloud solutions.
- I contributed to documentation of cloud environments.
- I assisted in troubleshooting cloud infrastructure issues.
- I developed basic scripts for cloud automation.
- I created reports on cloud resource utilization.

**Level 2**
- I led the design and deployment of major cloud projects.
- I designed and implemented cloud disaster recovery plans.
- I automated cloud deployment processes.
- I integrated cloud services with existing systems.
- I conducted cloud performance testing and optimization.

**Level 3**
- I successfully led cross-functional cloud projects.
- I defined cloud architecture standards and best practices.
- I led the evaluation and selection of cloud technologies.
- I developed cloud migration strategies and plans.
- I conducted cloud training and knowledge sharing sessions.
- I managed cloud projects and ensured timely delivery.

### Outcome examples

**Level 1**
- Enhanced client's understanding of basic cloud concepts.
- Reduced the deployed cloud solutions downtime.
- Reduced time spent on manual cloud tasks.
- Provided insights into cloud cost optimization.

**Level 2**
- Ensured high availability and resilience of cloud infrastructure.
- Streamlined cloud operations and reduced deployment time.
- Strengthened cloud security posture and compliance.
- Improved data flow and interoperability between systems.
- Optimized cloud resource usage and reduced costs.

**Level 3**
- Improved the team's expertise in cloud technologies.
- Enabled smooth and successful cloud migrations.
- Enhanced cloud knowledge and skills across the organization.
- Delivered cloud projects on time and within budget.


---

## Communication

> Kind: cross-cutting skill, new in the 2026 grid

> Source: *SE Evaluation Grid 2026 - [FR] Soft. Eng Badges.pdf* (the sheet header still reads "H1 2025 skills updates (rewording & refresh)"). **Only Levels 1-3 appear in the 2026 grid**; the 2026 career guide still states four badge levels (4/10/16/28 pts). The skill did not exist in the 2025 grid. Examples are non-exhaustive: nobody ticks every box. Each bullet is one line of a grid cell (the 2025 extraction merged some wrapped Outcome lines).

### Expectations

**Level 1**
- Can articulate their own work clearly. Writes concise, professional emails and meeting notes. Can answer direct questions using an "answer-first" approach.

**Level 2**
- Masters pyramidal communication (answer-first, MECE). Can vulgarize complex technical topics for non-technical audiences. Can write a simple storyline for a deck or document.

**Level 3**
- Can write the full storyline for a complex deck or proposal. Inspires and engages audiences. Proactively communicates milestones and shares information from leadership to foster transparency.

### Reach

**Level 1**
- Immediate team members and direct counterparts.

**Level 2**
- Project team, client business people, and data architects.

**Level 3**
- Client business and tech management, client C-levels, and the wider Artefact team.

### Output examples

**Level 1**
- Clear stand-up updates.
- Well-documented code and PRs.
- Answering questions clearly within their scope.

**Level 2**
- Leading a technical workshop for a mixed audience.
- Writing the technical approach for a proposal.
- Clearly explaining project advancements on behalf of the team.

**Level 3**
- Writing the complete narrative for a winning commercial proposal.
- Presenting project successes and team achievements to the wider group.
- Efficiently delegating slide production with clear messaging.

### Outcome examples

**Level 1**
- Team members are always clear on your progress.
- Seniors don't have a hard time reviewing your work.
- Meetings are efficient because your contributions are concise.

**Level 2**
- Client stakeholders trust your technical explanations.
- Junior or consultant team members understand the 'why' behind technical tasks.
- Project risks are clearly communicated and understood.

**Level 3**
- Wins client buy-in on major strategic decisions.
- Establishes Artefact as a thought leader.
- The team feels informed, credited for their work, and aligned with leadership's vision.


---

## Business sense

> Kind: cross-cutting skill, new in the 2026 grid

> Source: *SE Evaluation Grid 2026 - [FR] Soft. Eng Badges.pdf* (the sheet header still reads "H1 2025 skills updates (rewording & refresh)"). **Only Levels 1-3 appear in the 2026 grid**; the 2026 career guide still states four badge levels (4/10/16/28 pts). The skill did not exist in the 2025 grid. Examples are non-exhaustive: nobody ticks every box. Each bullet is one line of a grid cell (the 2025 extraction merged some wrapped Outcome lines).

### Expectations

**Level 1**
- Understands the immediate business context of their tasks. Performs sanity checks on data and results. Can explain the business benefit of their work (e.g., why refactoring matters).

**Level 2**
- Can design an MVP approach, prioritizing high-value features. Identifies unstated needs and relevant KPIs. Can confidently lead a framing session or client workshop.

**Level 3**
- Has a strong impact in discovery meetings, adapting on the fly to client needs. Designs innovative solutions to unsolved problems. Has a clear vision of their industry and how Artefact can deliver value.

### Reach

**Level 1**
- Project team (POs, Analysts, fellow engineers).

**Level 2**
- Project stakeholders, client business owners, data architects.

**Level 3**
- Client leadership (Head of Data, CDO, CTO), Artefact partners.

### Output examples

**Level 1**
- Take into account end-user vision & need when making technical choices.
- Identifying a data quality issue.
- Explaining the business logic behind a data transformation.

**Level 2**
- Designing the KPI evaluation process for a model.
- Creating an MVP roadmap.
- Contributing to ROI estimations for a project.

**Level 3**
- Designing a novel data solution for a client's problem.
- Leading a discovery meeting that uncovers a major new opportunity.
- Authoring a white paper or internal standard on a key industry topic.

### Outcome examples

**Level 1**
- Features delivered have a clear and direct link to business needs.
- Suspicious results are caught early, preventing rework.
- Time is focused on tasks that align with MVP priorities.

**Level 2**
- Engineering work is directly tied to measurable business value.
- Projects are launched faster by focusing on core features.
- The client trusts you to translate their needs into a technical plan.

**Level 3**
- Artefact is positioned as a strategic partner, not just a supplier.
- New, high-value business opportunities are created.
- Methodologies are reused across projects, increasing efficiency and impact.


---

## Delivery & project execution

> Kind: cross-cutting skill, new in the 2026 grid

> Source: *SE Evaluation Grid 2026 - [FR] Soft. Eng Badges.pdf* (the sheet header still reads "H1 2025 skills updates (rewording & refresh)"). **Only Levels 1-3 appear in the 2026 grid**; the 2026 career guide still states four badge levels (4/10/16/28 pts). The skill did not exist in the 2025 grid. Examples are non-exhaustive: nobody ticks every box. Each bullet is one line of a grid cell (the 2025 extraction merged some wrapped Outcome lines).

### Expectations

**Level 1**
- Reliably delivers assigned tasks on time. Proactively provides visibility on progress and roadblocks. Follows established priorities and agile practices.

**Level 2**
- Can manage a small project or an entire stream autonomously. Actively contributes to agile ceremonies and decision-making. Mentors junior members to improve their delivery quality.

**Level 3**
- Can manage the technical side of any project autonomously. Designs the long-term project strategy and roadmap. Implements tools and best practices that improve velocity across the project.

### Reach

**Level 1**
- The individual's own work and the immediate project team.

**Level 2**
- A project stream or small team, client tech leads.

**Level 3**
- An entire project, multiple teams, client sponsors.

### Output examples

**Level 1**
- Breaking down a feature into technical sub-tasks.
- Providing accurate updates in stand-ups.
- Preparing for meetings you organize so they are efficient.

**Level 2**
- Defining the tasks for an entire sprint.
- Performing constructive, high-quality code reviews.
- Designing a simple project architecture.

**Level 3**
- Designing the long-term technical roadmap.
- Implementing new collaborative tools or processes.
- Standing your ground on technical quality to prevent long-term project debt.

### Outcome examples

**Level 1**
- Your work is delivered on time and meets quality standards.
- Project leads have full visibility and are never surprised.
- The project moves forward smoothly without bottlenecks caused by your tasks.

**Level 2**
- Project streams are delivered autonomously with high quality.
- The velocity and code quality of the entire team increases.
- Juniors are upskilled and become more autonomous.

**Level 3**
- Complex projects are delivered successfully and sustainably.
- Team members don't work in silos and collaboration is high.
- The project's technical foundation is robust, secure, and built to last.


---
