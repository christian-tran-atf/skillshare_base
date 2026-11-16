# Report template (one per source)

Fill every section. An empty section says `none found`, with where it was looked for. Length: as long as the evidence needs; tables for inventories, prose only for themes.

```markdown
# <source> · <start> → <end>

## 0. Header
- Source: <URL> (kind: project | wiki) · provider/adapter: <name> · local clone: <path @ HEAD sha | none>
- Person: <account> · identities matched: <emails/names> · unmatched authors worth checking: <list | none>
- Window: <start>..<end> UTC · collected: <timestamp> · evidence file: <path>
- Completeness: COMPLETE | PARTIAL | INCOMPLETE — <limits, verbatim from evidence.limits and anything found while reading>
- Claims received: <list, each tagged CLAIM> | none
- Lenses: <list> | none

## 1. Activity inventory (facts only)
Counts table: item type × role (authored / contributed commits / reviewed / commented / approved / merged / assigned) with totals.

| Type | Count | Notes |
|---|---|---|

Then one table per type, newest first. Columns: ref+link · title · state · my role(s) · dates (created → merged/closed) · size (+/− lines of my commits; files) · one-line what.
- Merge/pull requests authored · MRs where I committed but did not author · MRs reviewed or commented · approvals · issues authored · issues assigned or commented · milestones (created by me / containing my items, kept apart) · wiki pages · releases · direct commits without an MR · pipelines run by me (counts by status).
Long tables: the 40 largest or most recent rows here; the rest remain in `evidence.json` (say so).

## 2. Work themes (facts only)
3–7 clusters of related items. For each: what was built or changed (technical, specific: components, files, technologies), item refs, my share, size, and any **documented** outcome with its source. Code read from the local clone is cited as `path@ref`.

## 3. Collaboration and review signals (facts only)
- Reviews given: count, share of inline (diff) comments vs general, 3 representative comments quoted verbatim with link; who was reviewed (roles if known).
- Feedback received on my MRs: notes by others, inline notes, unresolved threads, MRs with rework visible; 3 representative quotes verbatim, including critical ones.
- Documentation, specs, ADRs, decision records I wrote: refs.
- People interacted with, and their roles where stated.

## 4. Claims tested
| Claim (origin) | Verdict | Evidence | What is missing |
|---|---|---|---|

## 5. Candidate mappings (judgements, per lens)
Per `career-badge-mapping`: one line per data point, then the gaps list per lens, then "Other notable work".
`[lens · level · dimension] "<grid line>" ← <fact> (<ref>) → <rating>` · outcomes rated MEASURED / STATED / ABSENT.

## 6. Counter-evidence, caveats, attribution limits
Everything that weakens or qualifies sections 1–5, each with its ref.

## 7. Questions only the person can answer
Missing outcomes, context, off-platform work, which artifact would hold a missing number.
```
