---
name: career-badge-mapping
description: Relate evidence of someone's work to Artefact's Software Engineering evaluation grid (2026) and career guide as honest, citable data points for a performance review or badge dossier. Use when evidence (git activity, notes, documents) must be mapped to ML & Agentic Engineer, Analytics Engineer, Software Developer, SSRE, Cloud Architect or the cross-cutting skills (Communication, Business sense, Delivery & project execution), or when a report needs the grid's wording. Technical Project Lead, Pre-Sales and Engineering Manager are only in the 2025 legacy grid.
---

Turns **evidence** into **data points** against the skill grid. The mapping reports what the evidence supports; the person decides which badge level to claim.

**Grid version**: *SE Evaluation Grid 2026 - [FR] Soft. Eng Badges.pdf* and *SE Career guide 2026.pdf* (read 2026-11-20). The 2025 grid and career system remain in `references/legacy-2025/`. What changed: `references/grid/_changes-2026-vs-2025.md` (read it once: levels 1-3 only, ML Engineer renamed, three Growth grids dropped, three cross-cutting skills added).

## Inputs
- **Lenses**: the badges or skills under review, by their **2026 grid name**: `ML & Agentic Engineer` (the 2025 name `ML Engineer` and the guide's `Machine Learning Engineer` mean the same skill), `Analytics Engineer`, `Software Developer`, `Site Security & Reliability Engineer`, `Cloud Architect`, `Communication`, `Business sense`, `Delivery & project execution`. If a lens has no level, assess L1 as the baseline and record any L2 signals separately. Levels above 3 are not in the 2026 grid: do not rate against them.
- **Legacy lens** `Technical Project Lead` (grid name *Project Tech Lead*), `Pre-Sales Engineer`, `Engineering Manager`: the 2026 career guide still lists them as Growth badges, but the 2026 grid has no page for them. Rate the evidence against **two labelled line sets** and report coverage for each: (a) the legacy 2025 lines of that badge (`references/legacy-2025/grid/project-tech-lead.md`, Levels 1-3; the only wording specific to the badge), and (b) the 2026 cross-cutting lines that overlap it: `Delivery & project execution` (streams, ceremonies, mentoring, code reviews, roadmap) plus the `Communication` lines for reporting-chain updates. State in the report header that (a) is a superseded grid and (b) is a cross-reference, and put "is this Growth badge still requestable, and which grid applies in 2026?" in the questions for the person.
- **Grade** (optional, e.g. J2): sets what the guide expects, see "Output and outcome" below.
- **Evidence**: items that each carry an ID or link (MR/issue URLs, commits, wiki pages, notes file + date, supplied files).
- **Claims** (optional): statements the person or a third party made, e.g. "the ingestion pipeline cut costs". A claim is a hypothesis; evidence confirms or fails to confirm it.

## Load only what the lenses need
1. `references/grid/_general-levels.md`: the five generic dimensions (People, Knowledge, Design & Documentation, Delivery & Project Management, Problem Solving) at levels 1-3.
2. `references/grid/<skill>.md` for each lens: `ml-agentic-engineer`, `analytics-engineer`, `software-developer`, `ssre`, `cloud-architect`, `communication`, `business-sense`, `delivery-project-execution`. Quote lines verbatim, with their level. Cross-cutting grids have the same four rows (Expectations, Reach, Output examples, Outcome examples) but their Expectations rows are paragraphs, not bullets.
3. `references/career-guide-2026.md` for level semantics, points, output/outcome rule, dossier limits (2 pages per project, 3 projects, one dossier for all badges) and the evaluation process.

## Mapping procedure
1. **Collect lines**: for each lens, the Expectations, Output Examples, Outcome Examples and Reach lines of the target level (and of the next level when L2 signals are requested). Count the lens-specific lines (Expectations + Output + Outcome + Reach); the generic dimensions are counted apart and shared by all lenses.
2. **Match each evidence item to the lines it speaks to.** One item can speak to several lines and to several lenses. An item that matches nothing stays unmatched and goes in the report as such.
3. **Rate each (line, evidence) pair** with the rubric below. Write the justification as a plain fact: what the artifact shows.
4. **Rate outcomes separately** (see below). A capability and its measured effect are different data points.
5. **Reach**: from who interacted with the work (reviewers, commenters, requesters) state the audience observed: project team, other chapters, client technical staff, client management. Only list roles the evidence names or the person supplied (label supplied roles "stated by the person"; a repository never says who is senior).
6. **Gaps**: every line of the target level without an item rated `DEMONSTRATED` or `PARTIAL` is listed as a gap. A gap is information, so it stays in the output.

## Strength rubric (per line)
| Rating | Holds when |
|---|---|
| `DEMONSTRATED` | An artifact the person authored (code, MR, doc, issue, review) shows the capability, within the window, at a cited link; no interpretation needed to connect them. |
| `PARTIAL` | The artifact shows part of the line, or the person's share of a team result is unclear, or the capability is shown at smaller scope than the line states. |
| `ADJACENT` | Related skill; the connection needs argument. Report it, labelled as a stretch. |
| `NOT FOUND` | This source holds nothing for the line. Not a verdict on the person: other sources may hold it. |

## Output and outcome (career guide 2026, p.5)
The guide distinguishes an **output** (what you built) from an **outcome** (a result with a measurable positive impact for Artefact, on project delivery, Chapter SE or client development). Tag every data point `OUTPUT` or `OUTCOME` and name the scope (project delivery, Chapter SE, client development). With a grade given: Junior = outcome on project delivery, output enough for Chapter SE, client development N/A; Senior = outcome on project delivery and Chapter SE, output on client development; Lead = outcome on all three. Report an output that the grade would need as an outcome as `OUTPUT ONLY (outcome expected at this grade)`.

## Outcome rubric (effects such as cost, latency, adoption, time saved)
| Rating | Holds when |
|---|---|
| `MEASURED` | A number with a before/after or baseline, in a cited source. Copy the number, unit, and source. |
| `STATED` | A text asserts the effect with no measurement. Quote it with its author and date. |
| `ABSENT` | The source has no statement of the effect. Say what artifact would hold it (billing export, dashboard, benchmark) so the person can fetch it. |

When a primary export is supplied (billing CSV, metrics dump), **recompute** the quoted figures from it: say which reproduce exactly, which do not, what the baseline leaves out, and whether the compared scopes are alike. A figure the sources withdrew or superseded is reported as `SUPERSEDED`, never as `MEASURED`.

## Rules
- **Fit the grid to the evidence, never the evidence to the grid.** The grid's examples are illustrative, so a real accomplishment with no matching line is reported under "Other notable work", not bent into a line.
- **Level honesty**: label each pair with the lowest level whose wording it satisfies; a pair that satisfies a higher-level line is labelled with that level and carries the note "wording met, badge level is the person's call".
- **Same standard in both directions**: a weak or partial result is written as plainly as a strong one; no softening, no inflating.
- **Attribution**: when the person states that part of a result is a colleague's or an AI assistant's, keep the rating of what the artifacts show and add the attribution note; never raise a rating on the person's say-so alone.
- **Names**: the grid skill is called `ML & Agentic Engineer` (2026); the owner's "Technical Project Lead" is the legacy grid's *Project Tech Lead* (2025 wording) cross-referenced with `Delivery & project execution` and `Communication` (2026).
- **Output** per data point: `[lens · level · dimension] "<grid line verbatim>" ← <fact> (<evidence id/link>) → <rating> · OUTPUT|OUTCOME (<scope>)`.
