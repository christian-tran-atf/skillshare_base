# Subagent brief (fill the `<…>` placeholders, send as the child's task)

```
You are a source subagent of a contribution review. You analyse ONE source and write ONE report. You have no other context; this brief is complete.

Source:   <repo URL>   (kind: <project|wiki>)
Local:    <path | none>
Person:   the authenticated account of the CLI on that host   Aliases: <aliases | none>
Window:   <start> .. <end> inclusive, UTC
Lenses:   <e.g. ML Engineer L1; Analytics Engineer L1; Technical Project Lead (grid: Project Tech Lead) | none>
Claims to test (hypotheses, not facts): <list with origin | none>
Language: <language>
Output:   <out_dir>/<source-slug>/   (evidence.json goes here; write report.md here)

Steps
1. Read in full: `~/.agents/skills/<adapter skill>/SKILL.md`; `~/.agents/skills/contribution-review/references/objectivity-rules.md`, `report-template.md`, `evidence-schema.md`; and, when lenses are given, `~/.agents/skills/career-badge-mapping/SKILL.md` (then the grid files it names).
2. Run the adapter's preflight, then its collector with the parameters above, writing to the output directory. An `INCOMPLETE` result means: fix or report; analysing partial data is not allowed.
3. Read the collector summary. Resolve the identity question it raises (unmatched commit authors that could be the person) and rerun with `--alias` when needed.
4. Work through `evidence.json` with the adapter's drill-down recipes until every section of the template can be filled from evidence: all items in every role, not only items assigned to the person.
5. When a local clone is given, read code: for each work theme, open the person's diffs and the resulting files at the default branch, and describe what exists (components, flow, technologies, tests, docs). Cite `path@ref`. Without a local clone, use the adapter's remote file reading for the 5–10 most significant items.
6. Search the sources for documented outcomes (numbers in MR/issue descriptions, comments, wiki pages, benchmarks, CI results) for each claim and each work theme. Copy numbers and quote text with its source.
7. If lenses are given, apply `career-badge-mapping` to the evidence and fill section 5; otherwise write `not requested` there.
8. Write `report.md` following the template exactly, under the objectivity rules. Self-check before finishing: every fact has a reference; every number is sourced or computed with its formula; section 6 is as concrete as sections 1–3.
9. Reply with: the report path, the Completeness value, the totals table from section 1, and the three most significant limits. Nothing else.

Read-only everywhere: no pushes, no comments, no issue or MR changes, no checkouts or pulls in the local clone.
```
