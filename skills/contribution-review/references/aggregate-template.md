# Aggregate template

```markdown
# Contribution review · <start> → <end>

## A. Scope and completeness
Table: source · kind · adapter · report path · Completeness · key limits. Sources skipped or failed, with reason.

## B. Cross-source inventory (summed from the reports' tables, no recomputation from memory)
| Source | MRs authored | MRs committed-to | MRs reviewed | Issues authored | Issues commented | Milestones | Wiki pages | Commits | +/− lines |
Totals row. A note where sources overlap (same MR counted once).

## C. Per-lens evidence pack
For each lens (e.g. ML & Agentic Engineer L1). Open with a coverage table: lens-specific target-level lines (Expectations + Output + Outcome + Reach) × DEMONSTRATED / PARTIAL / ADJACENT / NOT FOUND (ABSENT outcomes count as NOT FOUND); the five generic dimensions are counted apart and shared. Tag every data point OUTPUT or OUTCOME with its scope (project delivery, Chapter SE, client development) and, when a grade is given, flag an output where the guide expects an outcome.
1. Data points rated DEMONSTRATED, grouped by grid dimension, each with source refs.
2. PARTIAL and ADJACENT data points, labelled as such.
3. Outcomes: MEASURED / STATED / ABSENT / SUPERSEDED, each with the number and source, or the artifact that would hold it. Figures recomputed from supplied files are listed with the result of the check (reproduced exactly / approximately / not reproduced, what the baseline leaves out, whether the compared scopes are alike).
4. Gaps against the target level.
5. Claims tested: verdicts from the reports.
6. Observed reach (who interacted with this work, as named in the evidence).

## D. Cross-source themes and projects
Candidate projects for the dossier (max 3 per badge): facts, size, window, repo refs.

## E. Counter-evidence and caveats
Merged from the reports, plus disagreements between this agent and a child (both ratings shown).

## F. Questions for the person
```
