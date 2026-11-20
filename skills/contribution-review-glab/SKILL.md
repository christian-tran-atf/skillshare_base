---
name: contribution-review-glab
description: GitLab adapter for contribution-review. Collects one person's merge requests, issues, review comments, milestones, commits and wiki history for one repository in a time window with the glab CLI, into a normalised evidence.json. Use when a contribution-review source subagent works on a GitLab or self-hosted GitLab repository (including `.wiki` repositories).
---

Collector + drill-down recipes for **one GitLab repository or wiki**. Contract and schema: `~/.agents/skills/contribution-review/references/adapter-contract.md` and `evidence-schema.md`.

## 1. Preflight
```bash
glab auth status --hostname <host>      # must show "Logged in"; token from the keyring is fine
glab api user --hostname <host>         # proves the host is reachable (VPN) and returns the account
```
A failure here is a stop: report the exact message.

## 2. Collect
```bash
python3 ~/.agents/skills/contribution-review-glab/scripts/collect.py \
  --repo <URL> --start <YYYY-MM-DD> --end <YYYY-MM-DD> --out <out_dir>/<slug> \
  [--local <clone>] [--alias <email-or-name> ...] [--username <login>]
```
- Takes a project URL or a wiki URL (`….wiki`, `…/-/wikis/…`); the wiki form reads page history from the wiki's git repository.
- Read-only. With `--local` it checks that a remote of the clone points at the repository (a clone of another repository is ignored and reported), runs `git fetch --all --prune`, and reads history from all branches and remotes.
- Takes 1–4 minutes on a repository with several hundred commits.
- Exit `2` = `INCOMPLETE` (many API calls failed): fix the cause and rerun. Exit `1` = bad input.

**Candidate discovery** is deliberately wider than "assigned to me", because many items carry no assignee: change requests and issues authored, assigned, reviewed; items I commented on or approved (the user events feed); and every change request that contains one of my commits, including other people's branches I pushed to. An item enters the evidence only with a stated reason (`in_window_because`).

## 3. Read the summary before anything else
- `COMMIT AUTHORS NOT MATCHED TO ME` lists the top other identities in the window. The person commits under several emails (the account's email, the employer's email from `git config`); if one of these is the person, rerun with `--alias`. A name that is plainly a teammate's stays unmatched.
- `mine_mr_unknown > 0` means per-commit lookups were capped: those commits' MR links are unknown, not absent.
- Zero items in a section: say so in the report with the filters used; do not infer inactivity from one API.

## 4. Drill into `evidence.json`
```bash
E=<out_dir>/<slug>/evidence.json
jq '.merge_requests | map(select(.my_roles|index("author"))) | sort_by(.created_at)
    | .[] | [.iid,.state,.created_at[:10],(.merged_at//"-")[:10],.title,([.my_commits[].additions]|add),([.my_commits[].deletions]|add)] | @tsv' -r $E
jq '[.merge_requests[] | select((.my_roles|index("author")|not) and (.my_roles|index("committer")))] | length' $E     # contributed to others' MRs
jq '.merge_requests[] | select(.my_roles|index("commenter")) | {iid,title,notes:[.my_notes[]|{type,length,body}]}' $E   # review comments
jq '.merge_requests[] | select(.feedback_received) | {iid,title,f:.feedback_received|del(.others)}' $E               # feedback received
jq '.issues[] | select(.my_roles|index("author")) | [.iid,.state,.created_at[:10],.title] | @tsv' -r $E
jq '.milestones[] | {title,state,due_date,i_created_it,my_items}' $E
jq '.commits.mine | group_by(.date[:7]) | map({month:.[0].date[:7],n:length})' $E
```
`jq` missing → use `python3 -c` over the same JSON. Descriptions and notes in the file are truncated (`…[+N chars]`); the full text is one call away (next section).

## 5. Deeper reading with glab
```bash
glab mr view <iid> -R <URL> --comments           # full MR with discussions
glab issue view <iid> -R <URL> --comments
glab api "projects/<id>/merge_requests/<iid>/diffs?per_page=100" --hostname <host> --paginate   # a diff
glab api "projects/<id>/repository/files/<url-encoded-path>/raw?ref=<branch>" --hostname <host> # a file without a clone
glab api "projects/<id>/wikis/<slug>" --hostname <host>                                          # a wiki page
```
Project IDs are in `evidence.json` (`project.id`). With a local clone, prefer git: `git -C <clone> show <sha>`, `git -C <clone> log -p --author=<email> -- <path>`, `git -C <clone> show origin/<default_branch>:<path>`, `git -C <clone> grep <term> origin/<default_branch>`. Never `pull`, `checkout` or `reset` there. No clone and a code-heavy theme → `git clone --filter=blob:none --no-checkout <URL>.git /tmp/<slug>` and read through `git show`.

## 6. GitLab attribution notes (carry into section 6 of the report)
- **Assignee is optional**: roles are derived, not read from one field.
- **Squash merge**: the squash commit carries the MR author, while the branch's individual commits may not be reachable; MR `my_commits` come from the MR's commit list, so check `squash` before comparing commit counts.
- **Milestones have no author** in GitLab. `i_created_it` comes from the events feed; `my_items` counts only my items in the milestone. Report the two apart.
- **Approvals** come from the events feed (`approved` actions); the approvals API is not queried.
- **Events horizon**: GitLab prunes events after about 3 years; irrelevant for recent windows, noted when the window is older.
- **Dates** are UTC and inclusive; the events API is date-granular, so the collector widens by one day and filters again.
- **`changes_count`** is capped by GitLab (`"1000+"`); line counts in the report come from the person's own commits.
- **Wiki pages** carry history in git only; page authorship = `git log` on the wiki repository.
- **Bots** (renovate, pipelines, GitLab itself) show as authors in lists: they are never counted as the person.
- **Foreign remotes in a clone**: the collector counts commits only from local branches and from the remotes that point at the repository itself; remotes pointing at other projects (e.g. a stray `glab-base` remote) are ignored and named in `evidence.limits`. If a commit still seems to belong to another repository, check `git branch -a --contains <sha>` and say so in the report.
- **Blame and squash merges**: `git blame` and squash/promotion merges (`dev -> preprod -> prod`) credit the person who merged, not the one who wrote the lines; never use blame totals as authorship. Use the commit list of the branch and, when the person states that a colleague wrote a module, report both.
