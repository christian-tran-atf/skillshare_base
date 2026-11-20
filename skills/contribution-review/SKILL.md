---
name: contribution-review
description: Audit one person's contributions (merge/pull requests, issues, review comments, milestones, wiki documentation, commits, code) across a list of repositories in a time window, one isolated subagent per repository, returning objective reports plus an aggregate. Use when asked to gather evidence of my work for a performance review, badge dossier, brag document or retrospective from GitLab/GitHub repositories. Requires the repository list and the start and end dates.
---

A **contribution review** is a fan-out/fan-in: one **source subagent** per repository gathers and reports facts in isolation, this agent verifies the reports and aggregates them. Provider specifics (glab, gh, …) live in **adapter skills**; everything here is provider-agnostic.

## Inputs

| Input | Rule |
|---|---|
| `repos` | **Mandatory.** List of repository URLs. A wiki is a repository of its own (`….wiki`, `…/-/wikis/…`). Each entry may carry `local=<path>`: an up-to-date clone for code reading. |
| `start`, `end` | **Mandatory.** `YYYY-MM-DD`, both inclusive, evaluated in UTC. |
| `lenses` | Optional. Badges or skills for the mapping, by their 2026 grid name, e.g. `ML & Agentic Engineer L1`, `Analytics Engineer L1`, `Delivery & project execution L1` (a legacy `Technical Project Lead` request is mapped to that skill, see `career-badge-mapping`). Absent → facts-only reports. |
| `grade` | Optional. The person's grade (e.g. `J2`); sets whether the guide expects an output or an outcome. |
| `context` | Optional. Facts the person supplies (roles and seniority of colleagues, who wrote what, AI-assistant use). Reports label them *stated by the person*; they never raise a rating on their own. |
| `supplied_files` | Optional. Local exports to cross-check figures (billing CSV, metrics, the previous badge dossier). Read-only; children recompute the quoted figures and say which reproduce. |
| `claims` | Optional. Statements to test against the evidence (see `references/objectivity-rules.md`). |
| `aliases` | Optional. Extra emails or names the person commits under. |
| `language` | Optional. Report language. Default English; quotes stay verbatim. |
| `out_dir` | Optional. Default `./contribution-review/<start>_<end>/`. |

URLs give the **platform truth** (issues, MRs, review comments, milestones, approvals live on the server, not in git). A `local` clone adds **code truth** (full diffs, surviving code, architecture) and is read-only: the adapter fetches but never pulls or checks out.

## Process

### 1. Gate
Stop and ask the user when `repos`, `start` or `end` is missing, when `end < start`, or when a URL is not `https://<host>/<group>/…/<project>`. Name every offending entry. Nothing launches before the gate is clean.

### 2. Route
For each repository, take the host and pick the adapter from the table. Wiki URLs normalise to `<project>.wiki`; identical sources collapse into one. A project and its wiki listed together stay two sources, and the project source skips its own wiki.

| Host | Adapter skill |
|---|---|
| a GitLab instance (e.g. `gitlab-si.dataiv.loc`, `gitlab.com`) | `contribution-review-glab` |
| `github.com` | `contribution-review-gh` (not yet written; see `references/adapter-contract.md`) |

A host with no adapter → tell the user which adapter is missing and run the rest.

### 3. Launch one subagent per source, in parallel
Build each brief from `references/subagent-brief.md` (fill the placeholders; the child has no other context). Every source gets its own subagent so that one repository's volume never enters another's context. Each child writes `<out_dir>/<source-slug>/report.md` and returns the path plus a ten-line digest.

### 4. Verify each report
A report is accepted when all of these hold:
- every section of `references/report-template.md` is present;
- the header's `Completeness` field is not `INCOMPLETE`;
- three or more cited items, picked at random, match `evidence.json` (id, date, role, numbers);
- every metric in the text appears in the evidence or is flagged as computed with its formula;
- the collection date is compared with the window end (a window still open at collection time is stated in the header), and commits reached through a remote that is not the repository itself are excluded (see the adapter's attribution notes);
- when `supplied_files` are given, the cost or volume figures quoted for the claims were recomputed from them.

A failed report goes back to its child with the specific mismatch (resume that child); it is never patched here.

### 5. Aggregate
Fill `references/aggregate-template.md` and write `<out_dir>/AGGREGATE.md`. Totals are summed from the reports' tables. Ratings are copied as the children wrote them; where this agent disagrees, both ratings appear with the reason. Close with the open questions only the person can answer.

### 6. Hand back
Return the path of `AGGREGATE.md`, the sources that failed or are incomplete, and the questions for the person.

## Rules
- Facts and judgements stay in separate sections of every report; `references/objectivity-rules.md` binds this agent and every child.
- This agent reads reports and spot-checks evidence; the raw API volume stays in the children and in `evidence.json`.
