# Adapter contract (how to plug a new CLI)

An adapter is a skill named `contribution-review-<cli>` (e.g. `-gh`). The orchestrator, the report template and the mapping never change; only the adapter does.

An adapter provides:
1. **Preflight**: one command that proves the CLI is installed, authenticated for the host, and reaches it. Failure text says what to fix.
2. **Collector**: `scripts/collect.<ext> --repo URL --start D --end D --out DIR [--local PATH] [--alias X]…` that is read-only, writes `DIR/evidence.json` following `references/evidence-schema.md`, prints a short summary, and exits `2` when too many calls failed (`INCOMPLETE`), `1` on bad input.
   Coverage required: commits (all my identities), change requests in every role, issues in every role, review and discussion comments, milestones, wiki/docs history, plus whatever signals the provider holds (releases, pipelines/actions).
3. **Identity resolution**: the CLI account plus every email and name the person commits under, with the commit authors left unmatched surfaced in the summary.
4. **Skill body**: how to run the preflight and collector, how to drill into `evidence.json`, extra CLI commands for deeper reading, and the provider's attribution caveats.

Then add a row to the routing table in `contribution-review/SKILL.md`.

Provider notes to carry into `-gh`: `gh api` replaces `glab api`; a PR's reviews come from `/pulls/{n}/reviews` and inline comments from `/pulls/{n}/comments`; GitHub has no events-by-user endpoint with project filter, so use `/search/issues?q=involves:<user>+repo:<r>+updated:<range>` for the candidate set; wiki is `<repo>.wiki.git`; milestones also lack an author.
