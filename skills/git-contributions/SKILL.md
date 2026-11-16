---
name: git-contributions
description: Harvest verifiable engineering contributions (milestones, issues, work items, MRs/PRs, code reviews, comments, commits, ADRs, and wiki documentation) across a list of Git repository URLs over a mandatory date window, isolating each repository in its own subagent, and optionally relate evidence to a career system or skill grid. Use when gathering contributions for performance reviews, self-evaluations, brag documents, or badge dossiers.
---

# Git Contributions Harvester (Core)

Gather an engineer's verifiable contributions across one or more Git repositories over a bounded time window. Each repository runs in an **isolated subagent** so large diffs, comments, and logs never bloat or cross-contaminate the main session.

 CLI-specific commands live in provider skills (e.g. `git-contributions-glab` for GitLab `glab`, and future `git-contributions-gh` for GitHub `gh`). Keep this core workflow provider-agnostic.

## 1. Mandatory Parameter Gate (Hard Stop)

Validate these inputs before running any CLI command or spawning any subagent. **If any mandatory parameter is missing, malformed, or ambiguous, STOP immediately and ask the user** — never guess defaults or widen a missing window.

| Parameter | Status | Validation rule |
|---|---|---|
| `repositories` | **Mandatory** | Non-empty list of repository URLs. Normalize web wiki URLs (`…/-/wikis/…` or `…/wiki`) to their Git wiki URL (`<project-url>.wiki.git`). Flag Obsidian/Markdown link typos (e.g. `[[...`) and confirm with the user before running. |
| `start_date` | **Mandatory** | Explicit start date normalized to `YYYY-MM-DD` (inclusive, `00:00:00Z`). If given as `YYYY-MM` or `YYYY-MM-*`, normalize to the 1st of that month (`YYYY-MM-01`) and state the exact bound used. |
| `end_date` | **Mandatory** | Explicit end date normalized to `YYYY-MM-DD` (inclusive, `23:59:59Z`). If given as `YYYY-MM` or `YYYY-MM-*`, normalize to the last calendar day of that month (or today if it is the current month) and state the exact bound used. `start_date <= end_date`. |
| `local_roots` | Optional | Local workspace directories to search for existing checkouts matching each remote URL (e.g. `~/para`). Enables fast, zero-clone reading of code, diffs, and in-repo docs. |
| `career_context` | Optional | Target badges/levels, career system / skill grid reference (e.g. `artefact-career-badges` skill or attached PDFs), and any reviewer/lead guidance on out-of-window context that remains relevant to frame a stream. |

## 2. Preflight (Main Agent — Once per Host)

Before fanning out subagents, run preflight once per distinct Git host in `repositories`:

1. **Select provider skill**: Match each repository host to its provider skill:
   - GitLab hosts (`gitlab*`, self-managed GitLab) → read `~/.agents/skills/git-contributions-glab/SKILL.md`.
   - Unsupported host / missing provider skill → stop and report which provider skill is missing.
2. **Verify CLI auth & resolve identity**: Run the provider's auth & identity check once per host. Capture:
   - `username` and numeric `user_id`
   - Full name and known Git commit emails (from API + local git config / commit history, since engineers often commit under both corporate and client emails).
3. **Classify targets & pair wikis**:
   - Classify each URL as `code_repo` or `wiki_repo` (ends in `.wiki` or `.wiki.git`, or points to `/-/wikis`).
   - Group a `wiki_repo` with its parent `code_repo` **only if** you want one combined project brief, **or** spawn a dedicated wiki subagent when the user listed it as its own repository entry. Default: **one subagent per normalized repository entry** (strict isolation).
4. **Resolve local checkouts (Hybrid URL + Local Read)**:
   - Remote CLI/API queries always target the canonical URL (source of truth for MRs, issues, comments, approvals, milestones).
   - For reading code, commit diffs, ADRs, and wiki pages: search `local_roots` (if provided) for a git checkout whose remote matches the target URL.
   - If found: subagent runs `git -C <local_path> fetch --all --prune --quiet` (read-only on working tree — never checkout, pull, rebase, or modify files; read refs via `origin/<default_branch>` or commit SHAs).
   - If not found and code/wiki content is needed (mandatory for `.wiki` repos): subagent clones `--bare` or shallow read-only into a temporary directory under `/tmp/git-contributions-<run>/` and cleans it up when done.
5. **Load career reference (if requested)**:
   - If mapping to Artefact badges or career track, read `~/.agents/skills/artefact-career-badges/SKILL.md` (and its `references/skill-grid-2025.md`) so you can pass a compact, tailored rubric brief for **only the targeted badges** to each subagent instead of making every subagent parse raw PDFs.

## 3. Subagent Fan-Out (Strict Per-Repository Isolation)

Spawn **one read-only subagent per repository** in parallel. Every subagent starts cold — pass a self-contained brief containing:

1. **Target**: `repo_url`, `repo_type` (`code_repo` | `wiki_repo`), `host`, `project_path`, and resolved `local_path` (if any).
2. **Window**: Exact `start_date` and `end_date` (ISO-8601 bounds), plus any explicit user note about framing context outside the window (must be labeled `[CONTEXT OUTSIDE WINDOW]` if referenced).
3. **Identity**: `username`, `user_id`, and regex of known author emails/names.
4. **Provider instructions**: Path `~/.agents/skills/git-contributions-<provider>/SKILL.md` — instruct the subagent to read and execute every discovery channel in that provider skill.
5. **Report template & objectivity contract**: Path `~/.agents/skills/git-contributions/references/report-template.md` — instruct the subagent to read and follow it verbatim.
6. **Career rubric slice (if `career_context` provided)**: Path `~/.agents/skills/artefact-career-badges/SKILL.md` + `references/skill-grid-2025.md` and the exact target badges/levels.

## 4. Non-Negotiable Collection & Objectivity Rules

Both subagents and the main aggregating agent are bound by these rules:

1. **Never rely solely on `assignee`**: Many issues and MRs have no assignee or are assigned to someone else while the user authored them, pushed commits to them, reviewed them, or drove architectural decisions in comments. Every provider MUST query across **authorship, commit authorship, review/approval, comment/discussion activity, milestone activity, and documentation/wiki history**.
2. **Separate Promotion MRs from Feature/Fix MRs**: Environment promotion MRs (`dev -> preprod`, `preprod -> prod`, release merges) are release-management signals, not feature MRs. Count and report them separately so metrics are never inflated.
3. **Evidence-first, zero invention**: Every claim requires an artifact ID (`!MR`, `#Issue`, commit short SHA, milestone ID, wiki slug/file path), date, and URL. Never extrapolate metrics (latency, cost, % gain) unless explicitly stated in an MR, issue, commit, ADR, wiki page, or user note — and cite where the number comes from.
4. **Zero glazing, zero undermining**: Ban promotional adjectives (*exceptional, groundbreaking, single-handedly, massive, seamlessly, rockstar*) and ban dismissive minimizers (*just, merely, simple, trivial*). State the technical problem, the exact action taken by the user (distinguishing solo ownership vs. co-contribution vs. review), and the observable result.
5. **Natural career/badge alignment**: Relate contributions to badge dimensions and level reach/autonomy **only where the evidence genuinely supports it**. The Skill Grid's *Expectations*, *Output Examples*, and *Outcome Examples* are illustrative anchors, not checkboxes to force-fit. Explicitly record **gaps or thin evidence** per targeted badge so the user can make an honest decision.

## 5. Main Agent Synthesis

Once all repository subagents return their reports:

1. Keep each subagent's factual inventory intact (or saved as durable artifacts if requested).
2. Cross-reference across repositories (e.g., `incident360` code + `incident360.wiki` cost/architecture docs + `cicd-components` + `snowflake-administration`) — and with non-git sources such as Scratchpads if the caller prompt requested them.
3. Produce an **Objective Synthesis**:
   - **Consolidated Metrics Table** across repositories (feature MRs vs. promotion MRs, MRs reviewed/approved, substantive review threads, issues/PRDs authored, milestones driven, ADRs/wiki pages authored).
   - **Thematic Engineering Streams** (grouping related MRs, issues, commits, and docs into coherent project narratives with exact citations).
   - **Target Badge Assessment** (if `career_context` was provided): per target badge, list **Strong Evidence**, **Partial / Supporting Evidence**, **Out-of-Window Context (if flagged by user)**, and **Evidence Gaps / Risks for Committee Review**.
