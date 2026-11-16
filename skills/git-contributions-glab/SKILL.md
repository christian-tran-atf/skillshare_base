---
name: git-contributions-glab
description: GitLab CLI (glab) provider for harvesting a user's GitLab contributions (events, MRs, co-authored commits, code reviews, DiffNotes, issues, GraphQL WorkItems, milestones, and .wiki repositories) over a date window. Loaded by git-contributions or when auditing GitLab project activity via glab.
---

# GitLab Provider (`glab` + Git `log`)

Provider implementation for `git-contributions` using the `glab` CLI (REST API v4 + GraphQL) and read-only `git` commands.

## 1. Host & URL Normalization

Given a GitLab URL `https://<host>/<path>`:

1. Strip trailing `/` and `.git`.
2. **Wiki detection**:
   - If the URL contains `/-/wikis` (e.g. `https://<host>/group/proj/-/wikis/home`) or ends with `.wiki`:
     - `repo_type = wiki_repo`
     - `parent_project_path = group/proj`
     - `git_clone_url = https://<host>/group/proj.wiki.git`
   - Otherwise:
     - `repo_type = code_repo`
     - `project_path = group/proj` (supports nested subgroups: `group/sub/proj`)
3. **URL-encoded path for REST API**: replace every `/` in `project_path` with `%2F` (e.g. `artefact%2Fincident360`).
4. **Host flag**:
   - For `glab mr|issue|milestone|release|ci`: pass `-R https://<host>/<project_path>` (or set `GITLAB_HOST=<host> glab ... -R <project_path>`).
   - For `glab api`: **always** pass `--hostname <host>`. Never rely on `glab`'s default `gitlab.com` when running outside a repo directory.

## 2. Auth & Identity Resolution (Preflight)

Verify auth and capture exact identity:

```bash
glab auth status --hostname <host>
glab api --hostname <host> user | jq '{id, username, name, email, public_email}'
glab api --hostname <host> user/emails | jq 'map(.email)' 2>/dev/null || true
```

If a local checkout exists, also inspect `git -C <local_path> log --all --format="%an <%ae>" | sort -u` to collect alternate author emails belonging to the same person (e.g. `@artefact.com` vs `_external@client.com`). Build a case-insensitive regex `<EMAIL_REGEX>` matching all of the user's emails/names.

## 3. Critical `glab` Gotchas (Why Multi-Channel Discovery is Required)

1. **`assignee` misses contributions**: Issues and MRs frequently have `assignee = null` or another owner even when the user authored, co-authored, reviewed, or closed them. Never filter solely by `--assignee`.
2. **GitLab Events API date bounds are EXCLUSIVE**:
   - In `GET /projects/:id/events?after=YYYY-MM-DD&before=YYYY-MM-DD`, GitLab treats `after` as **strictly after** and `before` as **strictly before**.
   - **Rule**: To cover `[start_date, end_date]` inclusively:
     - `AFTER_EXCLUSIVE = start_date - 1 day`
     - `BEFORE_EXCLUSIVE = end_date + 1 day`
3. **`glab issue list` misses Tasks (`WorkItem`) and lacks date flags**:
   - Use REST `/issues` with `created_after` / `updated_after`, **plus** Events API (`target_type == "WorkItem"`) and GraphQL `workItems` so GitLab Tasks/WorkItems are captured alongside classic Issues.
4. **`glab api --paginate` JSON concatenation**:
   - Plain `glab api ... --paginate` outputs one JSON array *per page* back-to-back, which breaks `jq 'map(...)'` unless slurped or streamed.
   - **Always use** `glab api --hostname <host> '<endpoint>' --paginate --output ndjson | jq -s '...'` so multi-page results parse cleanly into one array.
5. **`-f` / `-F` defaults `glab api` to `POST`**:
   - For `GET` endpoints, either inline query parameters in the endpoint string or pass `-X GET` explicitly.

## 4. Exhaustive Discovery Workflow — `code_repo`

Run these channels for `project_path` (`<ENC_PATH>`) over `[START_ISO, END_ISO]` (`YYYY-MM-DDT00:00:00Z` to `YYYY-MM-DDT23:59:59Z`). Batch independent read commands in a single shell script or temp JSON dump under `/tmp/` to minimize round-trips.

### Channel A — Project Events Stream (Backbone Index)
Captures every action the user took in the window: opened/accepted/closed MRs, approvals, `DiffNote` / `DiscussionNote` / `Note` comments (with full note body!), opened/closed `Issue` and `WorkItem`, `Milestone` actions, and `WikiPage::Meta` edits.

```bash
glab api --hostname <host> \
  "projects/<ENC_PATH>/events?user=<username>&after=<AFTER_EXCLUSIVE>&before=<BEFORE_EXCLUSIVE>&per_page=100" \
  --paginate --output ndjson > /tmp/events_<repo>.ndjson
```

Summarize event counts by `[action_name, target_type]` and extract:
- All commented `noteable_type` + `noteable_iid` + `note.type` (`DiffNote`, `DiscussionNote`, `Note`) + `note.body` + `note.position` where `author_username == "<username>"`.
- All `WorkItem`, `Issue`, `MergeRequest`, and `Milestone` IIDs touched by the user.

### Channel B — Merge Requests (4 Angles, Deduplicated by `iid`)

Query MRs updated since `START_ISO` and filter activity within `[START_ISO, END_ISO]`:

1. **Authored by user**:
   ```bash
   glab api --hostname <host> \
     "projects/<ENC_PATH>/merge_requests?author_username=<username>&scope=all&updated_after=<START_ISO>&per_page=100" \
     --paginate --output ndjson
   ```
2. **Assigned to user** (catches MRs opened by someone else and handed over):
   ```bash
   glab api --hostname <host> \
     "projects/<ENC_PATH>/merge_requests?assignee_username=<username>&scope=all&updated_after=<START_ISO>&per_page=100" \
     --paginate --output ndjson
   ```
3. **Reviewed or Approved by user** (exclude self-approvals where `author.username == <username>`):
   ```bash
   glab api --hostname <host> \
     "projects/<ENC_PATH>/merge_requests?reviewer_username=<username>&scope=all&updated_after=<START_ISO>&per_page=100" \
     --paginate --output ndjson

   glab api --hostname <host> \
     "projects/<ENC_PATH>/merge_requests?approved_by_ids[]=<user_id>&scope=all&updated_after=<START_ISO>&per_page=100" \
     --paginate --output ndjson
   ```
4. **Commented on or Co-Committed by user** (unassigned & non-author MRs!):
   - Take every `MergeRequest` `noteable_iid` from Channel A comments.
   - Take every commit authored by `<EMAIL_REGEX>` in Channel E and map non-author commits to MRs via:
     ```bash
     glab api --hostname <host> "projects/<ENC_PATH>/repository/commits/<SHA>/merge_requests"
     ```
   - Fetch full metadata/description for any newly discovered MR IIDs via `projects/<ENC_PATH>/merge_requests/<iid>`.

**Separate Promotion MRs**: Flag MRs whose title/branches match environment promotion (`dev -> preprod`, `develop -> preprod`, `preprod -> prod`, `main -> prod`) into their own bucket.

### Channel C — Issues & GraphQL WorkItems (Tasks)

1. **Authored or Assigned Issues**:
   ```bash
   glab api --hostname <host> \
     "projects/<ENC_PATH>/issues?author_username=<username>&scope=all&updated_after=<START_ISO>&per_page=100" \
     --paginate --output ndjson

   glab api --hostname <host> \
     "projects/<ENC_PATH>/issues?assignee_username=<username>&scope=all&updated_after=<START_ISO>&per_page=100" \
     --paginate --output ndjson
   ```
2. **Issues & WorkItems touched via Events (closed, commented, opened Tasks)**:
   - Collect all `Issue` and `WorkItem` IIDs from Channel A (both direct actions and `note.noteable_type == "Issue"`).
   - Fetch missing details via GraphQL `workItems` (which returns both `Issue` and `Task` types, descriptions, milestones, and assignees):
     ```bash
     glab api --hostname <host> graphql -f query='
       query($fullPath: ID!, $iids: [String!]) {
         project(fullPath: $fullPath) {
           workItems(iids: $iids, first: 100) {
             nodes {
               iid
               title
               state
               createdAt
               closedAt
               webUrl
               workItemType { name }
               author { username }
               description
             }
           }
         }
       }
     ' -f fullPath="<project_path>" -F 'iids=["<iid1>","<iid2>"]'
     ```

### Channel D — Milestones & Releases

```bash
glab api --hostname <host> "projects/<ENC_PATH>/milestones?per_page=100" --paginate --output ndjson
glab api --hostname <host> "projects/<ENC_PATH>/releases?per_page=100" --paginate --output ndjson
```

Link milestones active in `[START_ISO, END_ISO]` to the user's MRs and issues (`milestone.iid`) plus Milestone open/close events from Channel A. Do not claim milestone ownership unless the user opened/closed the milestone or authored a substantial share of its issues/MRs — state exact counts (e.g. *"authored 4 of 6 MRs in milestone %47"*).

### Channel E — Code, Commits, ADRs & In-Repo Docs (Local Checkout Preferred)

1. If a local checkout exists, sync refs safely without touching the working tree:
   ```bash
   git -C "<local_path>" fetch origin --prune --quiet
   ```
   *(If no local checkout exists, use `glab api "projects/<ENC_PATH>/repository/commits?since=<START_ISO>&until=<END_ISO>&all=true&per_page=100" --paginate --output ndjson` or a temporary `--bare` clone in `/tmp`.)*
2. List the user's non-merge commits in the window across remote branches (focusing on default branch `origin/develop` or `origin/main`):
   ```bash
   git -C "<local_path>" log origin/HEAD --no-merges \
     --since="<START_ISO>" --until="<END_ISO>" \
     --perl-regexp --author="<EMAIL_REGEX>" \
     --format="%H|%ad|%an <%ae>|%s" --date=short --shortstat
   ```
3. Inspect high-signal files touched by the user:
   - In-repo documentation, runbooks, architecture records (`docs/`, `ADR*`, `README*`, `CONTRIBUTING*`, `*.sql` runbooks, `.gitlab-ci.yml`).
   - Key feature/fix MRs where reading the commit diff (`git -C "<local_path>" show --stat <sha>` or targeted diff hunks) clarifies technical depth (e.g. Clean Architecture boundaries, Snowflake SQL transactions, dbt models, evaluation harnesses, CI/CD pipelines).

## 5. Exhaustive Discovery Workflow — `wiki_repo` (`.wiki`)

GitLab's Wiki REST API (`projects/<ENC_PATH>/wikis`) returns current page snapshots **without per-line author attribution or commit timestamps**. Therefore, **always inspect the underlying `.wiki.git` Git history** to attribute wiki contributions accurately:

1. **Locate or clone the wiki Git repo**:
   - Use local `<repo>.wiki` checkout if present (run `git -C "<local_wiki_path>" fetch origin --prune --quiet`).
   - Otherwise clone read-only to `/tmp/git-contributions-wiki-<slug>` from `https://<host>/<parent_project_path>.wiki.git`.
2. **Extract user's wiki commits & diffs in the window**:
   ```bash
   git -C "<wiki_path>" log origin/HEAD \
     --since="<START_ISO>" --until="<END_ISO>" \
     --perl-regexp --author="<EMAIL_REGEX>" \
     --name-status --format="COMMIT|%H|%ad|%an <%ae>|%s" --date=short
   ```
3. **Verify authorship per page**:
   - Run `git -C "<wiki_path>" log -p --since="<START_ISO>" --until="<END_ISO>" --perl-regexp --author="<EMAIL_REGEX>" -- "<file>.md"` to read the exact sections, tables, architecture diagrams, or cost analyses written by the user (distinguishing pages created from scratch vs. sections added to shared pages).
   - Cross-check with `WikiPage::Meta` events from the parent project's Events API (Channel A) if web UI edits used a different commit author string.
   - Build web URLs as `https://<host>/<parent_project_path>/-/wikis/<slug>`.
