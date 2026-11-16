---
name: career-badge-mapping
description: Relate evidence of someone's work to Artefact's Software Engineering career system and skill grid (expertise and growth badges) as honest, citable data points for a performance review or badge dossier. Use when evidence (git activity, notes, documents) must be mapped to ML Engineer, Analytics Engineer, Software Developer, SSRE, Architect, Technical Project Lead, Pre-Sales or Engineering Manager lines, or when a report needs the grid's wording.
---

Turns **evidence** into **data points** against the skill grid. The mapping reports what the evidence supports; the person decides which badge level to claim.

## Inputs
- **Lenses**: the badges under review, e.g. `ML Engineer L1`. If a lens has no level, assess L1 as the baseline and record any L2 signals separately.
- **Evidence**: items that each carry an ID or link (MR/issue URLs, commits, wiki pages, notes file + date).
- **Claims** (optional): statements the person or a third party made, e.g. "the ingestion pipeline cut costs". A claim is a hypothesis; evidence confirms or fails to confirm it.

## Load only what the lenses need
1. `references/grid/_general-levels.md`: the five generic dimensions (People, Knowledge, Design & Documentation, Delivery & Project Management, Problem Solving) per level.
2. `references/grid/<skill>.md` for each lens: `ml-engineer`, `analytics-engineer`, `software-developer`, `ssre`, `cloud-architect`, `project-tech-lead`, `pre-sales-engineer`, `engineering-manager`. Quote lines verbatim, with their level.
3. `references/career-system.md` only for level semantics, points or dossier conventions.

## Mapping procedure
1. **Collect lines**: for each lens, the Expectations, Output Examples, Outcome Examples and Reach lines of the target level (and of the next level when L2 signals are requested).
2. **Match each evidence item to the lines it speaks to.** One item can speak to several lines and to several lenses. An item that matches nothing stays unmatched and goes in the report as such.
3. **Rate each (line, evidence) pair** with the rubric below. Write the justification as a plain fact: what the artifact shows.
4. **Rate outcomes separately** (see below). A capability and its measured effect are different data points.
5. **Reach**: from who interacted with the work (reviewers, commenters, requesters) state the audience observed: project team, other chapters, client technical staff, client management. Only list roles that the evidence names.
6. **Gaps**: every line of the target level without an item rated `DEMONSTRATED` or `PARTIAL` is listed as a gap. A gap is information, so it stays in the output.

## Strength rubric (per line)
| Rating | Holds when |
|---|---|
| `DEMONSTRATED` | An artifact the person authored (code, MR, doc, issue, review) shows the capability, within the window, at a cited link; no interpretation needed to connect them. |
| `PARTIAL` | The artifact shows part of the line, or the person's share of a team result is unclear, or the capability is shown at smaller scope than the line states. |
| `ADJACENT` | Related skill; the connection needs argument. Report it, labelled as a stretch. |
| `NOT FOUND` | This source holds nothing for the line. Not a verdict on the person: other sources may. |

## Outcome rubric (effects such as cost, latency, adoption, time saved)
| Rating | Holds when |
|---|---|
| `MEASURED` | A number with a before/after or baseline, in a cited source. Copy the number, unit, and source. |
| `STATED` | A text asserts the effect with no measurement. Quote it with its author and date. |
| `ABSENT` | The source has no statement of the effect. Say what artifact would hold it (billing export, dashboard, benchmark) so the person can fetch it. |

## Rules
- **Fit the grid to the evidence, never the evidence to the grid.** The grid's examples are illustrative, so a real accomplishment with no matching line is reported under "Other notable work", not bent into a line.
- **Level honesty**: label each pair with the lowest level whose wording it satisfies; a pair that satisfies a higher-level line is labelled with that level and carries the note "wording met, badge level is the person's call".
- **Same standard in both directions**: a weak or partial result is written as plainly as a strong one; no softening, no inflating.
- **Names**: the owner's "Technical Project Lead" is the grid's *Project Tech Lead*; use the grid's wording when quoting.
- **Output** per data point: `[lens · level · dimension] "<grid line verbatim>" ← <fact> (<evidence id/link>) → <rating>`.
