---
name: artefact-career-badges
description: Reference for the Artefact Software Engineering Career System (v2025) and SE Technical & Growth Badges Skill Grid (2025). Use when evaluating contributions for semestrial performance reviews, choosing which expertise or growth badges to target, or preparing Artefact badge evaluation dossiers.
---

# Artefact SE Career System & Technical Badges (v2025)

Ground badge candidacy assessments and performance-review evidence mapping in Artefact's Software Engineering Chapter rules without forcing contributions into rigid checkbox templates.

Read [`references/skill-grid-2025.md`](references/skill-grid-2025.md) for the exact per-level definitions, expectations, reach, and illustrative examples across all 8 badges.

## 1. Career System Mechanics (v2025)

### Tracks & Ladder
- **Cadence**: Assessed twice a year (S1 / S2) via 360 reviews and badge dossiers presented by the counselor to the evaluation committee.
- **Role stages & points**:
  - **Software Engineer** (Learn & participate — variable evaluated on internal contributions): **L1** (6 pts), **L2** (14 pts), **L3** (20 pts).
  - **Senior Software Engineer** (Convince & coach — owner of delivery, client tech PoC, mentor for juniors; variable 50/50 internal & client impact): **L4** (30 pts), **L5** (45 pts), **L6** (60 pts).
  - **Lead Software Engineer / Technical Expert** (Pave the way): **L7** (80 pts), **L8** (95 pts).
  - **Engineering Director / Principal Engineer** (Lead the way): **L9** (110 pts), **L10** (130 pts), **L11** (150 pts).

### Badge Families & Points per Level
Every badge grants points according to the highest validated level on that badge:
- **Level 1**: 4 pts | **Level 2**: 10 pts | **Level 3**: 16 pts | **Level 4**: 28 pts

| Family | Badges |
|---|---|
| **Expertise Badges (5)** | `Software Developer`, `Architect (Cloud)`, `Machine Learning Engineer` *(shared with DS)*, `Analytics Engineer` *(shared with DA)*, `Site Security & Reliability Engineer (SSRE)` |
| **Growth Badges (3)** | `Technical Project Lead` (*Project Tech Lead*), `Pre-Sales Engineer`, `Engineering Manager` |

### Universal Meaning of Mastery Levels

| Level | Expectations | Client Reach | Artefact Reach | Transversal Anchors (People / Knowledge / Design / Delivery / Problem Solving) |
|---|---|---|---|---|
| **Level 1** | Delivers well under supervision / autonomous on well-defined tasks | Technical team | Chapter | Delivers tested & documented assets on time, provides visibility, knowledgeable on own sub-systems, fixes bugs on own sub-system. |
| **Level 2** | Self-reliant and supervisor | Technical & business team | Chapter | Fully autonomous across stack/topic, frames approach/docs/testing strategy, sizes tasks & boosts velocity, solves issues quickly, helps juniors progress. |
| **Level 3** | Shares best practices | Client management | Tech community | Defines project/company roadmap & architecture convictions, upskills confirmed engineers/DS/DA, solves complex cross-system issues. |
| **Level 4** | Evangelist | Client direction (C-level) | Growth tribe & outside | Sets Artefact standards, represents Artefact externally, advises C-level. |

## 2. How the Committee Evaluates a Badge (Non-Dogmatic Mapping Rules)

Each badge level in the Skill Grid has four sections: **Definition / Expectations**, **Reach**, **Output Examples**, and **Outcome Examples**.

1. **Illustrative, never exhaustive**: Page 10 of the Career System explicitly states that *Examples* are a *"non-exhaustive list of facts that are linked to completing this milestone, one doesn't need to tick all the boxes to reach the milestone."*
2. **Do not force-fit**:
   - Map a contribution based on **underlying engineering competency, autonomy, and reach** (e.g., an LLM/RAG document ingestion, chunking, vector search, retrieval evaluation, or inference/ingestion cost optimization pipeline legitimately demonstrates *ML Engineer* production GenAI/LLMOps skills even if the grid's older examples name `MLflow` or `scikit-learn`).
   - Similarly, Snowflake SQL modeling, `dbt` transformations, data quality/integrity guards, lineage, and analytical views demonstrate *Analytics Engineer* skills even if implemented inside an AI product repository rather than a standalone BI project.
   - Conversely, if core expectations of a badge are absent (e.g., targeting *Project Tech Lead L1* with strong backlog/ticket breakdown and code reviews, while lacking evidence on agile ceremony facilitation or reporting-chain visibility), **call out both the strengths and the exact gap** so the candidate can verify whether non-Git evidence (meetings, Slack/Teams, scratchpads, tech lead feedback) fills it.
3. **Dossier constraints (Artefact Tips & Tricks)**:
   - One separate dossier per requested badge.
   - Concise synthesis: **max 2 pages per project** (excluding diagrams/charts) and **max 3 relevant projects**.
   - High-value proof points: architecture diagrams, concrete metrics (ROI, cost reduction, latency, reliability, team productivity/velocity), what failed & how the engineer pivoted, and verifiable links (`!MR`, `#Issue`, ADR, Wiki).
4. **Out-of-window continuity**:
   - Semestrial reviews focus on the current semester's window, **except** when a multi-semester mission or tech lead explicitly validates referencing an earlier foundational stream on the same mission/badge that has not yet been credited for that specific badge (e.g. a first-time *ML Engineer L1* request building on ~1 year of GenAI product delivery). Always label pre-window evidence clearly by date so temporal boundaries stay transparent.
