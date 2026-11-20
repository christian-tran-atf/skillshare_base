# What changed between the 2025 skill grid and the 2026 evaluation grid

Compared line by line (normalised text) on 2026-11-20: *SE Skill Grid 2025 - [FR] Soft. Eng Tech Badges.pdf* vs *SE Evaluation Grid 2026 - [FR] Soft. Eng Badges.pdf*; and *SOFTWARE ENGINEER - CAREER SYSTEM v2025.pdf* vs *SE Career guide 2026.pdf* (title "Guide évaluation, Oct 2026").

## Grid
| Item | 2025 | 2026 |
|---|---|---|
| Levels shown | 1, 2, 3, 4 | **1, 2, 3 only** (the sheet header still reads "H1 2025 skills updates (rewording & refresh)") |
| Text of Levels 1-3 for Analytics Engineer, Software Developer, SSRE, Cloud Architect, the five generic dimensions | as published | **identical** (checked) |
| ML skill | "ML Engineer" | **"ML & Agentic Engineer"**; Levels 1-3 text identical (the "agentic" scope is not reflected in new lines) |
| Cloud Architect | page header "Cloud Architect" | same lines (the guide calls it "Architect") |
| Growth skills Technical Project Lead (grid name *Project Tech Lead*), Pre-Sales Engineer, Engineering Manager | have grid pages | **no grid page in the 2026 grid** (the 2026 career guide, p.8, still lists them as Growth expertises) |
| Cross-cutting skills | none | **new**: Communication, Business sense, Delivery & project execution (3 levels each, same four rows: Expectations, Reach, Output, Outcome; pink band like Growth in the guide) |

Consequences for a mapping:
- A lens named "Technical Project Lead" has **no 2026 grid text**. The closest 2026 grid skill is *Delivery & project execution* (manages a stream, agile ceremonies, mentors juniors, code reviews, roadmap), together with *Communication* for reporting-chain updates. State this substitution in every report, keep the 2025 `legacy-2025/grid/project-tech-lead.md` as a secondary reference, and list the question for the person to confirm with the counsellor.
- It is **not known** whether the three cross-cutting skills carry badge points or only feed the soft requirements of grade promotion (the guide's soft criteria include Communication, Business sense, Project Management, Technical Conviction). Treat them as evidence lenses and say so.
- Level 4 lines remain available only in `legacy-2025/`; do not rate against Level 4 from the 2026 grid.

## Career guide
| Item | 2025 system | 2026 guide |
|---|---|---|
| Ladder | Intern, L1 6 pts, L2 14, L3 20, L4 30, ... L11 150 | Grades **J1 0, J2 10, J3 20, S1 30, S2 45, S3 60, M1 80, M2 100, M3 120, D1/Pr1 150 pts**; salaries J1 50 k€, J2 53, J3 56, S1 60+6, S2 65+6, S3 70+6, M1 75+8, M2 80+8, M3 85+8, D1/Pr1 90+18 |
| Titles | Software Engineer, Senior, Lead, Principal / Director | Junior SE (J0-J3), Senior SE (S1-S3), Lead SE (M1-M3), then Director SE (generalist track) or Principal engineer (expert track), Partner, Managing Partner |
| Output vs outcome | not stated | **Explicit rule** (p.5): an *outcome* is a result with a measurable positive impact for Artefact (project delivery, Chapter SE, client development); an *output* is the artefact. Junior: outcome expected for project delivery, output enough for Chapter SE, N/A for client development. Senior: outcome, outcome, output. Lead: outcome on all three |
| Promotions | points + review | **Intergrade** (e.g. J2 to J3) needs points; **grade change** (e.g. J3 to S1) needs points **and** soft requirements; bonus points up to 2 pts for a very good semester (an advance on future badges) |
| Soft requirements | not in the system PDF | Criteria: Client Development, People Management, Project Management, Communication (written and oral), Business sense, Technical Conviction; assessed by self review, peer reviews, counsellor review, evaluation committee |
| Badges | 4 levels, 4/10/16/28 pts | still 4 levels, 4/10/16/28 pts; Expectations/reach per level (p.9): L1 delivers well under supervision, technical team, chapter; L2 self-reliant and supervisor, technical and business team; L3 shares best practices, client management, tech community; L4 evangelist, client direction, growth tribe and outside |
| Dossier | notes only | **p.10**: one dossier for all badges requested; max 2 pages per project and 3 relevant projects; outcomes Strong "Yes" (~30%), Oral (~60%; 20 min for level 1, 30 min for level 2+, at least 2 leads), Strong "No" (~10%); the counsellor should discourage a request without the level |
| Cadence | twice a year | evaluations every 6 months, **December and June**; eligibility after 3 months of permanent contract |
