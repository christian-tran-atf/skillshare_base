#!/usr/bin/env python3
"""Collect one person's GitLab activity for ONE repository (or its wiki) in a time window.

Read-only. Talks to GitLab only through `glab api`, and to a local clone only with
`git fetch` / `git log`. Writes <out>/evidence.json (normalized, see
contribution-review/references/evidence-schema.md) and prints a short summary.

  collect.py --repo URL --start YYYY-MM-DD --end YYYY-MM-DD --out DIR
             [--local PATH] [--alias EMAIL_OR_NAME ...] [--username USER] [--no-wiki]
Dates are inclusive and evaluated in UTC.
"""
import argparse, json, re, subprocess, sys, os, tempfile, datetime as dt
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import quote

LIMITS = []          # human-readable caveats, copied into evidence.json
DEC = json.JSONDecoder()


def die(msg):
    sys.exit(f"ERROR: {msg}")


def run(cmd, timeout=180):
    return subprocess.run(cmd, capture_output=True, text=True, errors="replace", timeout=timeout)


def parse_json_stream(text):
    """`glab api --paginate` prints one JSON array per page, back to back."""
    out, i, text = [], 0, text.strip()
    while i < len(text):
        val, j = DEC.raw_decode(text, i)
        out.extend(val) if isinstance(val, list) else out.append(val)
        i = j
        while i < len(text) and text[i].isspace():
            i += 1
    return out


class Gl:
    def __init__(self, host):
        self.host, self.calls, self.failed = host, 0, 0
        self.env = dict(os.environ)
        # Reading the token from the OS keyring on every `glab` call is slow; read it once.
        r = run(["glab", "auth", "status", "--hostname", host, "--show-token"])
        m = re.search(r"Token[^:\n]*:\s*(\S+)", r.stdout + r.stderr)
        if m and not set(m.group(1)) <= {"*"}:
            self.env.update(GITLAB_TOKEN=m.group(1), GITLAB_HOST=host)

    def get(self, endpoint, paginate=True, quiet=False):
        cmd = ["glab", "api", endpoint, "--hostname", self.host] + (["--paginate"] if paginate else [])
        self.calls += 1
        for attempt in (1, 2):
            r = subprocess.run(cmd, capture_output=True, text=True, timeout=180, env=self.env)
            if r.returncode == 0:
                try:
                    data = parse_json_stream(r.stdout) if paginate else json.loads(r.stdout)
                    return data
                except Exception as e:  # malformed output
                    err = f"parse error: {e}"
            else:
                err = (r.stderr or r.stdout).strip()[:300]
        self.failed += 1
        if not quiet or self.failed < 5:
            LIMITS.append(f"API call failed: {endpoint} -> {' '.join(err.split())}")
        return None


def parse_repo_url(url):
    m = re.match(r"^https?://([^/]+)/(.+?)/?$", url.strip())
    if not m:
        die(f"not a valid repository URL: {url!r}")
    host, path = m.groups()
    wiki = False
    if "/-/" in path:
        wiki = "/-/wikis" in path
        path = path.split("/-/")[0]
    path = re.sub(r"\.git$", "", path)
    if path.endswith(".wiki"):
        wiki, path = True, path[:-5]
    if "/" not in path:
        die(f"URL has no group/project path: {url!r}")
    return host, path, wiki


def iso(d):
    return d.strftime("%Y-%m-%dT%H:%M:%SZ")


def in_window(ts, start, end):
    if not ts:
        return False
    d = dt.datetime.fromisoformat(ts.replace("Z", "+00:00")).astimezone(dt.timezone.utc).date()
    return start <= d <= end


def short(txt, n):
    txt = txt or ""
    return txt if len(txt) <= n else txt[:n] + f"…[+{len(txt) - n} chars]"


# ---------------------------------------------------------------- identity
class Identity:
    def __init__(self, user, aliases, local):
        self.user = user
        self.emails, self.names = set(), set()
        for e in (user.get("email"), user.get("commit_email"), user.get("public_email")):
            if e:
                self.emails.add(e.lower())
        self.names |= {n.lower() for n in (user.get("name"), user.get("username")) if n}
        gcfg = []
        for scope in (["--global"], ["--local"] if local else []):
            for key in ("user.email", "user.name"):
                r = run(["git", *(["-C", local] if scope == ["--local"] else []), "config", *scope, key])
                if r.returncode == 0 and r.stdout.strip():
                    gcfg.append((key, r.stdout.strip()))
        for key, val in gcfg:
            (self.emails if key == "user.email" else self.names).add(val.lower())
        for a in aliases:
            (self.emails if "@" in a else self.names).add(a.lower())

    def match(self, name, email):
        return (email or "").lower() in self.emails or (name or "").lower() in self.names

    def match_user(self, u):
        return bool(u) and u.get("id") == self.user["id"]


def remote_matches(local, host, path):
    """True if any remote of `local` points exactly at host/path (no prefix matches: foo vs foo.wiki)."""
    want = f"{host}/{path}".lower()
    for ln in run(["git", "-C", local, "remote", "-v"]).stdout.splitlines():
        parts = ln.split()
        if len(parts) < 2:
            continue
        url = re.sub(r"^(https?://|ssh://)?([^@/]+@)?", "", parts[1].lower()).replace(":", "/", 1) if "://" not in parts[1] \
            else re.sub(r"^(https?|ssh)://([^@/]+@)?", "", parts[1].lower())
        if re.sub(r"\.git$", "", url.rstrip("/")) == want:
            return True
    return False


# ---------------------------------------------------------------- commits
def commits_local(local, host, path, start, end, ident):
    if not remote_matches(local, host, path):
        LIMITS.append(f"local clone {local} has no remote matching {host}/{path}; local clone IGNORED (wrong repo?)")
        return None
    f = run(["git", "-C", local, "fetch", "--all", "--prune", "--quiet", "--tags"], timeout=300)
    if f.returncode != 0:
        LIMITS.append(f"git fetch failed in {local}: {f.stderr.strip()[:200]}; local data may be stale")
    r = run(["git", "-C", local, "log", "--branches", "--remotes", "--no-merges", "--no-renames",
             f"--since={start}T00:00:00Z", f"--until={end}T23:59:59Z",
             "--format=\x1e%H\x1f%an\x1f%ae\x1f%aI\x1f%s", "--numstat"], timeout=300)
    commits = []
    for block in r.stdout.split("\x1e")[1:]:
        head, _, stat = block.partition("\n")
        sha, an, ae, ad, subj = head.split("\x1f")
        adds = dels = files = 0
        for ln in stat.strip().splitlines():
            p = ln.split("\t")
            if len(p) == 3:
                files += 1
                adds += int(p[0]) if p[0].isdigit() else 0
                dels += int(p[1]) if p[1].isdigit() else 0
        commits.append(dict(sha=sha, author_name=an, author_email=ae, date=ad, title=subj,
                            additions=adds, deletions=dels, files=files))
    return commits


def dedupe_commits(commits):
    """Rebased or cherry-picked copies share author, author date and title: count them once."""
    seen = {}
    for c in commits:
        k = ((c["author_email"] or "").lower(), c["date"], c["title"])
        if k in seen:
            seen[k]["versions"] += 1
        else:
            seen[k] = dict(c, versions=1)
    return list(seen.values())


def commits_api(gl, pid, start, end):
    ep = (f"projects/{pid}/repository/commits?all=true&with_stats=true&per_page=100"
          f"&since={start}T00:00:00Z&until={end}T23:59:59Z")
    data = gl.get(ep)
    if data is None:
        return None
    return [dict(sha=c["id"], author_name=c.get("author_name"), author_email=c.get("author_email"),
                 date=c.get("authored_date"), title=c.get("title"),
                 additions=(c.get("stats") or {}).get("additions", 0),
                 deletions=(c.get("stats") or {}).get("deletions", 0), files=None,
                 parents=len(c.get("parent_ids") or [])) for c in data]


# ---------------------------------------------------------------- notes
def note_rec(n, mine, ident):
    return dict(id=n["id"], author=n["author"]["username"], mine=mine, created_at=n["created_at"],
                type=n.get("type") or "Note", resolvable=n.get("resolvable"), resolved=n.get("resolved"),
                length=len(n.get("body") or ""), body=short(n.get("body"), 1500 if mine else 400))


def fetch_notes(gl, base, iid, ident):
    data = gl.get(f"{base}/{iid}/notes?per_page=100&sort=asc") or []
    return [note_rec(n, ident.match_user(n["author"]), ident) for n in data if not n.get("system")]


# ---------------------------------------------------------------- main collection
def collect_project(gl, args, host, path, start, end):
    enc = quote(path, safe="")
    proj = gl.get(f"projects/{enc}", paginate=False)
    if not proj:
        die(f"cannot read project {path} on {host} (no access, or wrong URL)")
    pid = proj["id"]
    user = gl.get("user", paginate=False)
    if args.username:
        user = gl.get(f"users?username={args.username}", paginate=False)[0]
    ident = Identity(user, args.alias, args.local)
    after = iso(dt.datetime.combine(start, dt.time.min))
    ev_after, ev_before = start - dt.timedelta(days=1), end + dt.timedelta(days=1)

    # --- events (my activity feed), filtered to this project and the window
    raw = gl.get(f"users/{user['id']}/events?after={ev_after}&before={ev_before}&per_page=100") or []
    events = []
    for e in raw:
        if e.get("project_id") != pid or not in_window(e["created_at"], start, end):
            continue
        note = e.get("note") or {}
        events.append(dict(created_at=e["created_at"], action=e["action_name"], target_type=e.get("target_type"),
                           target_iid=e.get("target_iid"), target_title=e.get("target_title"),
                           noteable_type=note.get("noteable_type"), noteable_iid=note.get("noteable_iid"),
                           push=(e.get("push_data") or {}).get("commit_title"),
                           push_ref=(e.get("push_data") or {}).get("ref"),
                           push_commits=(e.get("push_data") or {}).get("commit_count")))

    # --- commits
    commits = commits_local(args.local, host, path, start, end, ident) if args.local else None
    source = "local-git"
    if commits is None:
        commits, source = commits_api(gl, pid, start, end), "api"
    commits = dedupe_commits(commits or [])
    if source == "api":
        LIMITS.append("commits read through the API (no usable local clone): the list can include superseded versions of "
                      "rebased branches; duplicates are collapsed by (email, author date, title) but counts remain an upper bound")
    all_authors = {}
    for c in commits:
        k = f"{c['author_email']}|{c['author_name']}"
        all_authors[k] = all_authors.get(k, 0) + 1
    mine = [c for c in commits if ident.match(c["author_name"], c["author_email"]) and c.get("parents", 0) < 2]
    unmatched_top = sorted(((k, v) for k, v in all_authors.items()
                            if not ident.match(*reversed(k.split("|", 1)))), key=lambda kv: -kv[1])[:8]
    mine.sort(key=lambda c: c["date"], reverse=True)

    # --- candidate MRs / issues (lists only catch author/assignee/reviewer; events and commits catch the rest)
    def listing(kind, extra):
        return gl.get(f"projects/{pid}/{kind}?scope=all&updated_after={after}&per_page=100&{extra}") or []
    mr_ids = {m["iid"]: m for q in (f"author_id={user['id']}", f"assignee_id={user['id']}", f"reviewer_id={user['id']}")
              for m in listing("merge_requests", q)}
    is_ids = {i["iid"]: i for q in (f"author_id={user['id']}", f"assignee_id={user['id']}")
              for i in listing("issues", q)}
    extra_mr = {e["target_iid"] for e in events if e["target_type"] == "MergeRequest"} | \
               {e["noteable_iid"] for e in events if e["noteable_type"] == "MergeRequest"}
    extra_is = {e["target_iid"] for e in events if e["target_type"] == "Issue"} | \
               {e["noteable_iid"] for e in events if e["noteable_type"] == "Issue"}

    # --- commit -> MR mapping: one call per known MR first, then per-commit lookups for what is left
    def mr_commit_shas(iid):
        r = gl.get(f"projects/{pid}/merge_requests/{iid}/commits?per_page=100", quiet=True)
        return iid, {c["id"] for c in r or []}
    with ThreadPoolExecutor(args.workers) as ex:
        sha_to_mrs = {}
        for iid, shas in ex.map(mr_commit_shas, sorted(set(mr_ids) | extra_mr)):
            for sha in shas:
                sha_to_mrs.setdefault(sha, set()).add(iid)
    left = [c for c in mine if c["sha"] not in sha_to_mrs]
    if len(left) > 300:
        LIMITS.append(f"{len(left)} own commits not in any known MR; per-commit MR lookup done for the 300 most recent, "
                      f"the rest have mr_iids=null (unknown, NOT 'no MR')")
    def commit_mrs(c):
        r = gl.get(f"projects/{pid}/repository/commits/{c['sha']}/merge_requests", quiet=True)
        return c["sha"], None if r is None else [m["iid"] for m in r]
    with ThreadPoolExecutor(args.workers) as ex:
        looked = dict(ex.map(commit_mrs, left[:300]))
    for c in mine:
        c["mr_iids"] = sorted(sha_to_mrs[c["sha"]]) if c["sha"] in sha_to_mrs else looked.get(c["sha"])
        extra_mr |= set(c["mr_iids"] or [])

    def detail(kind, iid):
        return gl.get(f"projects/{pid}/{kind}/{iid}", paginate=False, quiet=True)
    for kind, ids, extra in (("merge_requests", mr_ids, extra_mr), ("issues", is_ids, extra_is)):
        missing = [i for i in extra if i and i not in ids]
        with ThreadPoolExecutor(args.workers) as ex:
            for i, d in zip(missing, ex.map(lambda i: detail(kind, i), missing)):
                if d:
                    ids[i] = d

    ev_by = lambda t, i: [e for e in events if (e["target_type"] == t and e["target_iid"] == i) or
                          (e["noteable_type"] == t and e["noteable_iid"] == i)]

    def build_mr(iid):
        m = mr_ids[iid]
        notes = fetch_notes(gl, f"projects/{pid}/merge_requests", iid, ident)
        mc = [c for c in mine if iid in (c["mr_iids"] or [])]
        evs = ev_by("MergeRequest", iid)
        roles = []
        if ident.match_user(m.get("author")): roles.append("author")
        if any(ident.match_user(a) for a in m.get("assignees") or []): roles.append("assignee")
        if any(ident.match_user(a) for a in m.get("reviewers") or []): roles.append("reviewer")
        if any(n["mine"] for n in notes): roles.append("commenter")
        if mc: roles.append("committer")
        if ident.match_user(m.get("merged_by") or m.get("merge_user")): roles.append("merger")
        if any(e["action"] == "approved" for e in evs): roles.append("approver")
        why = []
        if "author" in roles and in_window(m["created_at"], start, end): why.append("authored-in-window")
        if "author" in roles and in_window(m.get("merged_at"), start, end): why.append("merged-in-window")
        if any(n["mine"] and in_window(n["created_at"], start, end) for n in notes): why.append("my-note-in-window")
        if any(in_window(c["date"], start, end) for c in mc): why.append("my-commit-in-window")
        if any(e["action"] in ("approved", "accepted", "opened", "closed") for e in evs): why.append("event-in-window")
        if not why:
            return None
        others = [n for n in notes if not n["mine"]]
        full = detail("merge_requests", iid) or m
        return dict(iid=iid, url=m["web_url"], title=m["title"], state=m["state"], draft=m.get("draft"),
                    author=m["author"]["username"], my_roles=roles, in_window_because=why,
                    created_at=m["created_at"], merged_at=m.get("merged_at"), closed_at=m.get("closed_at"),
                    source_branch=m["source_branch"], target_branch=m["target_branch"], labels=m.get("labels"),
                    milestone=(m.get("milestone") or {}).get("title"),
                    reviewers=[r["username"] for r in m.get("reviewers") or []],
                    changes_count=full.get("changes_count"), description=short(m.get("description"), 3000),
                    my_commits=[{k: c[k] for k in ("sha", "date", "title", "additions", "deletions")} for c in mc],
                    my_notes=[n for n in notes if n["mine"]],
                    feedback_received=dict(notes_by_others=len(others),
                                           diff_notes_by_others=sum(n["type"] == "DiffNote" for n in others),
                                           unresolved_threads=sum(bool(n["resolvable"]) and not n["resolved"] for n in others),
                                           others=others[:40]) if "author" in roles else None,
                    events=[(e["created_at"], e["action"]) for e in evs])

    def build_issue(iid):
        i = is_ids[iid]
        notes = fetch_notes(gl, f"projects/{pid}/issues", iid, ident)
        evs = ev_by("Issue", iid)
        roles = []
        if ident.match_user(i.get("author")): roles.append("author")
        if any(ident.match_user(a) for a in i.get("assignees") or []): roles.append("assignee")
        if any(n["mine"] for n in notes): roles.append("commenter")
        if any(e["action"] == "closed" for e in evs): roles.append("closer")
        why = []
        if "author" in roles and in_window(i["created_at"], start, end): why.append("authored-in-window")
        if "assignee" in roles and in_window(i.get("closed_at"), start, end): why.append("assigned-closed-in-window")
        if any(n["mine"] and in_window(n["created_at"], start, end) for n in notes): why.append("my-note-in-window")
        if evs: why.append("event-in-window")
        if not why:
            return None
        return dict(iid=iid, url=i["web_url"], title=i["title"], state=i["state"], author=i["author"]["username"],
                    assignees=[a["username"] for a in i.get("assignees") or []], my_roles=roles,
                    in_window_because=why, created_at=i["created_at"], closed_at=i.get("closed_at"),
                    labels=i.get("labels"), milestone=(i.get("milestone") or {}).get("title"),
                    description=short(i.get("description"), 3000),
                    my_notes=[n for n in notes if n["mine"]],
                    notes_by_others=sum(not n["mine"] for n in notes))
    with ThreadPoolExecutor(args.workers) as ex:
        mrs = [x for x in ex.map(build_mr, sorted(mr_ids)) if x]
        issues = [x for x in ex.map(build_issue, sorted(is_ids)) if x]

    # --- milestones (no author field in GitLab: report "created by me" and "contains my items" separately)
    ms_raw = gl.get(f"projects/{pid}/milestones?per_page=100&include_ancestors=true") or []
    ms_created = {e["target_title"] for e in events if e["target_type"] == "Milestone" and e["action"] == "created"}
    mine_by_ms = {}
    for kind, items in (("merge_requests", mrs), ("issues", issues)):
        for it in items:
            if it.get("milestone"):
                mine_by_ms.setdefault(it["milestone"], {"merge_requests": 0, "issues": 0})[kind] += 1
    milestones = [dict(title=m["title"], url=m.get("web_url"), state=m["state"], start_date=m.get("start_date"),
                       due_date=m.get("due_date"), updated_at=m["updated_at"], description=short(m.get("description"), 600),
                       i_created_it=m["title"] in ms_created, my_items=mine_by_ms.get(m["title"]))
                  for m in ms_raw if m["title"] in ms_created or m["title"] in mine_by_ms]

    # --- releases and pipelines
    rel = [dict(tag=r["tag_name"], name=r.get("name"), released_at=r.get("released_at"), url=r["_links"]["self"])
           for r in gl.get(f"projects/{pid}/releases?per_page=100") or []
           if ident.match_user(r.get("author")) and in_window(r.get("released_at"), start, end)]
    pl = gl.get(f"projects/{pid}/pipelines?username={user['username']}&updated_after={after}"
                f"&updated_before={iso(dt.datetime.combine(end, dt.time.max))}&per_page=100") or []
    pipelines = dict(total=len(pl), by_status={s: sum(p["status"] == s for p in pl) for s in {p["status"] for p in pl}},
                     by_source={s: sum(p.get("source") == s for p in pl) for s in {p.get("source") for p in pl}})

    direct = [c for c in mine if c["mr_iids"] == []]
    return dict(
        project=dict(id=pid, path=path, web_url=proj["web_url"], default_branch=proj.get("default_branch"),
                     description=short(proj.get("description"), 500), wiki_enabled=proj.get("wiki_enabled")),
        identity=dict(username=user["username"], id=user["id"], name=user.get("name"),
                      emails=sorted(ident.emails), names=sorted(ident.names),
                      unmatched_top_commit_authors_in_window=unmatched_top),
        commits=dict(source=source, total_in_repo_window=len(commits), mine=mine,
                     duplicates_collapsed=sum(c["versions"] - 1 for c in mine),
                     mine_without_mr=[c["sha"] for c in direct],
                     mine_mr_unknown=sum(c["mr_iids"] is None for c in mine)),
        merge_requests=mrs, issues=issues, milestones=milestones, releases=rel, pipelines=pipelines,
        events=events), ident


def collect_wiki(gl, args, host, path, start, end, ident_user=None):
    enc = quote(path, safe="")
    proj = gl.get(f"projects/{enc}", paginate=False)
    if not proj:
        die(f"cannot read project {path} on {host}")
    pid = proj["id"]
    user = gl.get("user", paginate=False)
    if args.username:
        user = gl.get(f"users?username={args.username}", paginate=False)[0]
    ident = Identity(user, args.alias, args.local)
    clone = args.local
    if clone:
        if not remote_matches(clone, host, path + ".wiki"):
            LIMITS.append(f"--local {clone} is not the wiki repo of {path}; cloning a fresh copy instead")
            clone = None
        else:
            run(["git", "-C", clone, "fetch", "--all", "--prune", "--quiet"], timeout=300)
    if not clone:
        clone = os.path.join(tempfile.mkdtemp(prefix="wiki-"), "wiki")
        r = run(["git", "clone", "--quiet", f"https://{host}/{path}.wiki.git", clone], timeout=300)
        if r.returncode != 0:
            LIMITS.append(f"wiki clone failed: {r.stderr.strip()[:200]}")
            clone = None
    pages, mine_commits, total = {}, [], 0
    if clone:
        r = run(["git", "-C", clone, "log", "--no-merges", "--no-renames", f"--since={start}T00:00:00Z", f"--until={end}T23:59:59Z",
                 "--format=\x1e%H\x1f%an\x1f%ae\x1f%aI\x1f%s", "--numstat"], timeout=120)
        for block in r.stdout.split("\x1e")[1:]:
            head, _, stat = block.partition("\n")
            sha, an, ae, ad, subj = head.split("\x1f")
            total += 1
            is_me = ident.match(an, ae)
            for ln in stat.strip().splitlines():
                p = ln.split("\t")
                if len(p) != 3: continue
                pg = pages.setdefault(p[2], dict(file=p[2], my_commits=0, others_commits=0, my_additions=0, my_deletions=0))
                if is_me:
                    pg["my_commits"] += 1
                    pg["my_additions"] += int(p[0]) if p[0].isdigit() else 0
                    pg["my_deletions"] += int(p[1]) if p[1].isdigit() else 0
                else:
                    pg["others_commits"] += 1
            if is_me:
                mine_commits.append(dict(sha=sha, date=ad, title=subj))
        for pg in pages.values():
            if pg["my_commits"]:
                s = run(["git", "-C", clone, "show", f"HEAD:{pg['file']}"])
                text = pg["file"].lower().endswith((".md", ".markdown", ".rdoc", ".adoc", ".asciidoc", ".org", ".txt"))
                pg["current_content"] = short(s.stdout, 2500) if s.returncode == 0 and text else None
                pg["url"] = f"{proj['web_url']}/-/wikis/{re.sub(r'\.md$', '', pg['file'])}"
    raw = gl.get(f"users/{user['id']}/events?after={start - dt.timedelta(days=1)}&before={end + dt.timedelta(days=1)}&per_page=100") or []
    wev = [dict(created_at=e["created_at"], action=e["action_name"], title=e.get("target_title"))
           for e in raw if e.get("project_id") == pid and (e.get("target_type") or "").startswith("WikiPage")
           and in_window(e["created_at"], start, end)]
    return dict(project=dict(id=pid, path=path, web_url=proj["web_url"] + "/-/wikis/home"),
                identity=dict(username=user["username"], emails=sorted(ident.emails), names=sorted(ident.names)),
                wiki=dict(commits_in_window_total=total, my_commits=mine_commits,
                          pages_touched=[p for p in pages.values() if p["my_commits"]],
                          pages_touched_only_by_others=len([p for p in pages.values() if not p["my_commits"]]),
                          events=wev))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True)
    ap.add_argument("--start", required=True)
    ap.add_argument("--end", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--local")
    ap.add_argument("--alias", action="append", default=[])
    ap.add_argument("--username")
    ap.add_argument("--workers", type=int, default=8)
    args = ap.parse_args()
    try:
        start, end = dt.date.fromisoformat(args.start), dt.date.fromisoformat(args.end)
    except ValueError:
        die("--start/--end must be YYYY-MM-DD")
    if end < start:
        die("--end is before --start")
    if args.local:
        args.local = os.path.expanduser(args.local)
        if not os.path.isdir(args.local):
            die(f"--local path does not exist: {args.local}")
    host, path, is_wiki = parse_repo_url(args.repo)
    gl = Gl(host)
    if gl.get("user", paginate=False, quiet=True) is None:
        die(f"cannot reach {host} with glab (not logged in, VPN down, or token expired): run `glab auth status --hostname {host}`")
    os.makedirs(args.out, exist_ok=True)
    body = collect_wiki(gl, args, host, path, start, end) if is_wiki else collect_project(gl, args, host, path, start, end)[0]
    ev = dict(meta=dict(provider="gitlab", host=host, repo=path, kind="wiki" if is_wiki else "project",
                        input_url=args.repo, window=dict(start=args.start, end=args.end, tz="UTC"),
                        collected_at=dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
                        local_path=args.local, limits=LIMITS), **body)
    with open(os.path.join(args.out, "evidence.json"), "w") as f:
        json.dump(ev, f, indent=1, ensure_ascii=False)
    # ---- summary for the caller
    s = [f"evidence: {os.path.join(args.out, 'evidence.json')}", f"repo: {host}/{path} ({ev['meta']['kind']})  window: {args.start}..{args.end} UTC",
         f"identity: {json.dumps(ev['identity'].get('emails'))} {json.dumps(ev['identity'].get('names'))}"]
    if is_wiki:
        w = ev["wiki"]
        s.append(f"wiki: {len(w['my_commits'])}/{w['commits_in_window_total']} commits mine, {len(w['pages_touched'])} pages touched, {len(w['events'])} events")
    else:
        c = ev["commits"]
        s.append(f"commits[{c['source']}]: {len(c['mine'])} mine / {c['total_in_repo_window']} in repo ({len(c['mine_without_mr'])} without MR, {c['mine_mr_unknown']} unknown)")
        s.append("merge_requests: " + ", ".join(f"{r}={sum(r in m['my_roles'] for m in ev['merge_requests'])}"
                 for r in ("author", "assignee", "reviewer", "commenter", "committer", "merger", "approver")))
        s.append("issues: " + ", ".join(f"{r}={sum(r in i['my_roles'] for i in ev['issues'])}" for r in ("author", "assignee", "commenter", "closer")))
        s.append(f"milestones: {len(ev['milestones'])}  releases: {len(ev['releases'])}  pipelines: {ev['pipelines']['total']}  events: {len(ev['events'])}")
        um = ev["identity"]["unmatched_top_commit_authors_in_window"]
        s.append("COMMIT AUTHORS NOT MATCHED TO ME (check none is me under another email): " + "; ".join(f"{k} x{v}" for k, v in um))
    incomplete = gl.failed > max(3, gl.calls // 20)
    if incomplete:
        s.insert(0, f"INCOMPLETE: {gl.failed}/{gl.calls} API calls failed (VPN? token? rate limit?). Do NOT analyse; fix and rerun.")
    s += [f"LIMIT: {l}" for l in LIMITS[:12]] + ([f"LIMIT: …{len(LIMITS) - 12} more in evidence.json"] if len(LIMITS) > 12 else [])
    print("\n".join(s))
    sys.exit(2 if incomplete else 0)


if __name__ == "__main__":
    main()
