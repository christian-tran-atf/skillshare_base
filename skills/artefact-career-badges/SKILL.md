---
name: artefact-career-badges
description: Reference for Artefact's Software Engineering career guide (2026) and evaluation grid (2026): ladder and points, badges, output versus outcome, dossier limits, evaluation process. Use when evaluating contributions for the semestrial performance review, choosing which expertise badges or cross-cutting skills to target, or preparing Artefact badge dossiers. For line-by-line evidence mapping use career-badge-mapping.
---

# Artefact SE career guide and evaluation grid (2026)

Ground badge candidacy assessments and performance-review evidence in the SE Chapter rules without forcing contributions into rigid checkbox templates. Sources read 2026-11-20: *SE Career guide 2026.pdf* ("Guide évaluation, Oct 2026") and *SE Evaluation Grid 2026 - [FR] Soft. Eng Badges.pdf*. Exact grid wording: [`references/skill-grid-2026.md`](references/skill-grid-2026.md). The previous 2025 summary is in `references/legacy/` (superseded). The line-by-line mapping procedure and rubrics are in the `career-badge-mapping` skill; the per-skill grid files and the 2025-to-2026 change log live there too (`references/grid/_changes-2026-vs-2025.md`).

## 1. Career system mechanics (2026)

- **Cadence**: evaluations every six months, **December and June**. Reviewer selection (2-4 reviewers incl. the N+1), self/peer reviews, counsellor review, evaluation committee.
- **Ladder** (points → grade): J1 0 · J2 10 · J3 20 · S1 30 · S2 45 · S3 60 · M1 80 · M2 100 · M3 120 · D1/Pr1 150. Titles: Junior SE (J0-J3), Senior SE (S1-S3), Lead SE (M1-M3), then Director SE (generalist) or Principal engineer (expert), Partner, Managing Partner. *(Note: slide 14 contains a legacy typo stating J1 = 5 pts while slide 5's ladder sets J1 = 0 pts.)*
- **Promotion**: intergrade (J2 to J3) needs points; grade change (J3 to S1) needs points **and** soft requirements (Client Development, People Management, Project Management, Communication, Business sense, Technical Conviction, assessed by self, peer and counsellor reviews). Bonus: at most 2 pts, an advance on future badges.
- **Badges**: points per level L1 4 · L2 10 · L3 16 · L4 28.
  - **Expertise badges (5)**: `Software Developer`, `Site Security & Reliability Engineer (SSRE)`, `Architect` (grid: *Cloud Architect*), `Machine Learning Engineer` (2026 grid: *ML & Agentic Engineer*), `Analytics Engineer`.
  - **Growth badges (3, guide p.8)**: `Technical Project Lead` (2025 grid: *Project Tech Lead*), `Pre-Sales Engineer`, `Engineering Manager`.
  - **2026 Grid structure & TPL/Growth gap**: The 2026 grid PDF exports **Levels 1-3 only**, omits the 3 Growth badge tables, and adds **3 pink-banded cross-cutting skills** (`Communication`, `Business sense`, `Delivery & project execution`). When evaluating a Growth badge such as `Technical Project Lead`, rate it against two labelled line sets and report coverage for each: (a) the legacy 2025 *Project Tech Lead* lines (`references/legacy/skill-grid-2025.md`; the only wording specific to the badge) and (b) the 2026 cross-cutting lines (`Delivery & project execution` + `Communication`, plus `Business sense` where framing/MVP/ROI applies), as in `career-badge-mapping`, flagging for counsellor confirmation whether Growth badges are still awarded as 4/10/16-pt badges or folded into soft requirements.
- **Level meaning** (guide p.9): L1 delivers well under supervision, technical team, chapter; L2 self-reliant and supervisor, technical and business team, chapter; L3 shares best practices, client management, tech community; L4 evangelist, client direction, growth tribe and outside.
- **Output versus outcome** (guide p.5): an *output* is what was built; an *outcome* is a result with a measurable positive impact for Artefact across three scopes: **Project delivery**, **Chapter SE**, or **Client development**.
  - **Junior (J0-J3)**: Outcome expected on *Project delivery* | Output sufficient on *Chapter SE* | N/A on *Client development*.
  - **Senior (S1-S3)**: Outcome on *Project delivery* & *Chapter SE* | Output on *Client development*.
  - **Lead (M1-M3)**: Outcome on all three.
- **Dossier** (guide p.10): **one single combined dossier** covers all badges requested in the evaluation cycle (note: older template headers said one file per badge; guide p.10 states *"un seul dossier de badge pour tous les badges demandés"*). Max **2 pages per project** (diagrams/charts excluded) and **max 3 relevant projects**. Verdicts: Strong "Yes" (~30%, awarded without oral), Oral (~60%: 20 min for L1, 30 min for L2+, with ≥2 leads), Strong "No" (~10%, counsellor should discourage premature requests). Past dossiers are typically written in French.

## 2. How the committee evaluates a badge (non-dogmatic mapping rules)

Each grid skill has four rows per level: **Expectations**, **Reach**, **Output Examples**, **Outcome Examples**.

1. **Illustrative, never exhaustive**: the examples are a non-exhaustive list of facts linked to the milestone; one does not need to tick all the boxes.
2. **Do not force-fit.**
   - Map a contribution on the underlying engineering competency, autonomy and reach (an LLM/RAG ingestion, chunking, vector search, retrieval evaluation or inference-cost optimisation pipeline can show *ML & Agentic Engineer* skills even if the grid's examples name `MLflow` or `scikit-learn`; Snowflake SQL modelling, `dbt`, data-quality guards and lineage show *Analytics Engineer* skills even inside an AI product repository).
   - If core expectations are absent (e.g. strong backlog breakdown and code reviews but no agile ceremonies or reporting-chain visibility under *Delivery & project execution*), **call out both the strengths and the exact gap** so the person can check whether non-Git evidence (meetings, chat, scratchpads, tech lead feedback) fills it.
3. **Dossier content** that carries weight: architecture diagrams, concrete metrics (ROI, cost, latency, reliability, team productivity), what failed and how the engineer pivoted, verifiable links (`!MR`, `#issue`, ADR, wiki). Cost figures must be reproducible from a billing export; withdrawn or superseded figures must not be quoted.
4. **Out-of-window continuity**: a semestrial review is about the semester window, except when the mission lead validates referencing an earlier foundational stream not yet credited for that badge. Label pre-window evidence by date, and check the previous dossier so the same work is not credited twice.
5. **Grade context**: the grade (e.g. J2) sets whether an output suffices or an outcome is expected (section 1).
