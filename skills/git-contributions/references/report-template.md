# Subagent Repository Contribution Report Template

Read and follow this template strictly when reporting contributions for a single repository.

## Objectivity & Anti-Bias Rules

1. **Verifiable citations only**: Every listed contribution must carry its exact identifier (`!iid`, `#iid`, commit `sha`, wiki `slug`, file path), ISO date (`YYYY-MM-DD`), and URL.
2. **Role precision**: State your exact role on each item:
   - `authored` (opened the MR/issue and wrote the primary changes)
   - `co-authored` (pushed commits to someone else's MR, or others pushed substantial commits to yours — name co-contributors)
   - `reviewed` (left inline `DiffNote` / `DiscussionNote` review feedback or approved)
   - `commented` (participated in issue/MR design, debugging, or testing discussion without authoring the MR)
   - `release-promotion` (merged `develop -> preprod`, `preprod -> prod`, etc.)
3. **Neutral engineering prose**:
   - Write factual statements: *"<Action> on <subsystem> (<artifact>), <observable effect>."*
   - Do **not** flatter (*"masterfully", "crucial", "impressive", "spearheaded"*) and do **not** downplay (*"only a small fix", "just config"*).
   - Quote quantitative figures (cost, latency, test counts, data volume) **only** when present in the repository text, diffs, comments, wiki pages, or supplied exports, citing the exact source. If a later commit/wiki/issue corrects or withdraws an earlier figure, mark the earlier figure `[SUPERSEDED]` and report the reconciled number.
   - Distinguish **Output** (artifact delivered) from **Outcome** (measurable impact on *Project delivery*, *Chapter SE*, or *Client development* per the 2026 SE Career Guide p.5).
4. **Window discipline**: Only count artifacts with activity by the target user inside `[start_date, end_date]` in the primary inventory. If an older artifact (or a post-window follow-up) is essential to understand an in-window item, label it explicitly as `[OUTSIDE WINDOW: YYYY-MM-DD]`.
5. **Non-forced badge signals**: Tag an item with a candidate badge/dimension **only** when there is a clear technical link. Leave routine chores untagged rather than stretching them to fit a grid example.

---

## Markdown Output Structure

Return your report in this exact structure:

```markdown
# Contribution Report — <project_path> (`code_repo` | `wiki_repo`)

- **Repository URL**: <url>
- **Local Checkout Used**: <path | temporary clone | none>
- **Time Window**: <start_date> to <end_date> (inclusive)
- **Resolved Identity**: <username> (id: <user_id>) | git emails matched: <emails>

## 1. Quantitative Summary (In-Window Only)

| Metric | Count | Notes |
|---|---:|---|
| Feature / Fix / Refactor MRs authored (merged / open / closed) | X (m / o / c) | Excludes environment promotion MRs |
| Environment promotion MRs (`dev->pp`, `pp->prod`, etc.) | X | Listed separately |
| Other authors' MRs with commits by user (co-contributed) | X | |
| MRs reviewed (with substantive comments / approval-only) | X (c / a) | Excludes self-approvals on own MRs |
| Review & discussion comments (`DiffNote` / `DiscussionNote` / `Note`) | X | |
| Issues & Work Items authored | X | Specify PRDs / specs vs. bug/task tickets |
| Issues & Work Items closed or contributed to (non-author) | X | |
| Milestones created / closed / actively delivered | X | |
| Non-merge commits on default/target branches | X | |
| Documentation & ADR artifacts (in-repo docs / wiki pages) | X | Created vs. updated |

## 2. Milestones & Streams
For each milestone with user contributions in the window:
- **Milestone `%<iid>` — <Title>** (<state>, <start_date> → <due_date>, <url>)
  - User's contributions inside this milestone: authored MRs (`!...`), authored/closed issues (`#...`), role (driver vs. contributor).

## 3. Merge Requests — Authored & Co-Contributed
Group into logical technical themes if >8 MRs, otherwise chronological. Separate Feature/Fix MRs from Promotion MRs.
- **`!<iid>` — <Title>** (<state>, merged/updated `YYYY-MM-DD`, role: `authored` | `co-authored`, <url>)
  - **What & Why**: Concise technical description grounded in MR description + commit diff (`files changed`, architectural layer).
  - **Testing / Ops / Docs**: Tests added, runbooks/ADRs updated, or environment rollout details if present.
  - **Measurable Outcome**: Any explicit metric documented in the MR/commits/comments (or `None stated`).

*(Include a compact single line summarizing the count and list of `!<iid>` for environment promotion MRs.)*

## 4. Code Reviews & Technical Discussions (on Others' MRs & Issues)
Highlight substantive reviews (architecture, correctness, data integrity, SQL/Snowflake safety, testing harnesses, security, performance) separately from routine approvals.
- **`!<iid>` / `#<iid>` — <Title>** (author: `@<other>`, `YYYY-MM-DD`, <url>)
  - **Contribution**: Exact technical feedback, bug caught, SQL/test harness proposed, or design trade-off raised (cite note date/type).
  - **Outcome**: Whether adopted/resolved or left as follow-up.

## 5. Issues, PRDs & Problem Framing
- **`#<iid>` — <Title>** (type: `Issue` | `Task/WorkItem`, state: `<state>`, role: `authored` | `commented` | `closed`, `YYYY-MM-DD`, <url>)
  - **Scope**: Whether it is a full PRD/tech spec, vertical-slice breakdown, bug diagnosis, or operational ticket, and key technical substance.

## 6. Documentation, ADRs & Wiki Contributions
*(Primary section for `.wiki` repositories; also captures `docs/`, `ADRs/`, `README.md`, `CONTRIBUTING.md`, runbooks in code repos.)*
- **`<path or wiki slug>` — <Title>** (`created` | `updated`, commits: `<sha1>, ...`, `YYYY-MM-DD`, <url>)
  - **Substance**: Technical content authored by the user (verified via `git log -p` / `git show` so edits to others' pages only credit the user's diff), including architecture diagrams, cost/benchmark analyses, runbooks, or onboarding guides.

## 7. Career & Badge Signal Mapping (Evidence-Only, 2026 Evaluation Grid)
*(Include only when `career_context` was supplied in the brief. Use 2026 grid names — e.g. `ML & Agentic Engineer`, `Analytics Engineer`, and for legacy `Technical Project Lead` map both to 2026 `Delivery & project execution` + `Communication` and secondary 2025 `Project Tech Lead`.)*
For each target badge / skill:
### <Badge / Skill Name — Target Level>
- **Relevant Evidence from this Repo (`OUTPUT` vs `OUTCOME` + scope)**:
  - `<Artifact ID>` (`OUTPUT` | `OUTCOME — Project delivery / Chapter SE / Client development`): <How this concrete engineering work relates to the 2026 role's definition, expectations, autonomy, technical depth, or reach — without forcing exact Evaluation Grid example phrasing>.
- **Thin / Missing Signals & Counter-Evidence in this Repo**:
  - <Aspects of this badge/level that do NOT appear in this repository, or caveats such as unshipped side branches, skipped quality gates, or unresolved review threads>.

## 8. Uncertainties & Verification Notes
- Any API pagination limits hit, inaccessible endpoints, ambiguous co-authorship, or `[OUTSIDE WINDOW]` context referenced.
```
