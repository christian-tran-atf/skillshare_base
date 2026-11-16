# Objectivity rules (bind the orchestrator and every source subagent)

The reader will paste these findings into a review of one person. The report is **evidence**, written as an auditor would: the same standard whether the finding helps or hurts.

## Traceability
- Every statement of fact carries an **evidence reference**: MR/issue URL or `!iid`/`#iid`, commit SHA (8 chars), wiki page, file path with ref, or note ID. A statement without a reference does not enter the facts sections.
- A number is either read from the source (cite where) or **computed** (state the formula and the inputs). Round nowhere; keep units.
- Dates are ISO and UTC.

## Attribution
- **Mine** means authored by the person (matched by account or by commit identity), or an action the platform records as theirs. Work of teammates in the same MR, squash-merge sums, bot commits, and generated code are **not** counted as theirs; say when attribution is mixed.
- Roles are reported as the platform records them: *author, assignee, reviewer, commenter, committer, merger, approver, closer*. A missing *assignee* field does not make work "not mine": roles come from authorship, commits, notes and events together.
- Pairing or AI-assisted authorship visible in trailers (`Co-authored-by`) is reported as a fact when present.

## Facts and judgements stay apart
- Facts sections hold: what exists, who did what, when, how big, what the text says. They contain no evaluation.
- Judgements live only in the *Candidate mappings* section, each tied to fact IDs and rated with the rubric from `career-badge-mapping`.
- Register: neutral and numeric. Adjectives of praise or criticism are replaced by the number or the quote that justifies them.

## Symmetry
- The report lists **counter-evidence** with the same care as supporting evidence: requested changes and rework on the person's MRs, abandoned or reverted work, open items, review comments that were minor, outcomes with no measurement, windows with no activity.
- A thin result stays thin: "no evidence found in this source" is a valid and useful answer.
- Context that would change a reader's interpretation (small repository, team size, other contributors' share) is given once, factually.

## Claims are hypotheses
A claim from the person or a third party (a tech lead's opinion, a remembered cost figure) is reported as `CLAIM` with its origin. The report states what the sources do and do not support: `SUPPORTED` (cite), `PARTLY` (cite and say what is missing), `NOT FOUND IN THIS SOURCE`. The claim's wording never leaks into the facts sections.

## Limits
Every collection gap is stated in the header: failed calls, truncated lists, a stale or missing local clone, identities that might be unmatched, the retention horizon of platform events, a window with no data. A report that hides a limit is rejected.
