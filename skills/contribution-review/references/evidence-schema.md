# Evidence schema (what every adapter's collector writes to `evidence.json`)

Normalised across providers: *change request* = GitLab merge request / GitHub pull request. A field a provider cannot supply is `null`, never invented.

```
meta:        provider, host, repo, kind (project|wiki), input_url, window{start,end,tz}, collected_at, local_path, limits[]
identity:    username, id, name, emails[], names[], unmatched_top_commit_authors_in_window[[ "email|name", count ]]
project:     id, path, web_url, default_branch, description, wiki_enabled
commits:     source (local-git|api), total_in_repo_window,
             duplicates_collapsed (rebased/cherry-picked copies counted once),
             mine[{sha,date,title,author_name,author_email,additions,deletions,files,versions,mr_iids|null}],
             mine_without_mr[sha], mine_mr_unknown (count; mr_iids null = lookup skipped, not "no MR")
merge_requests[]:  iid,url,title,state,draft,author,my_roles[],in_window_because[],created_at,merged_at,closed_at,
             source_branch,target_branch,labels,milestone,reviewers[],changes_count,description,
             my_commits[{sha,date,title,additions,deletions}],
             my_notes[{id,created_at,type (Note|DiffNote|DiscussionNote),length,body,resolvable,resolved}],
             feedback_received{notes_by_others,diff_notes_by_others,unresolved_threads,others[]} (only when I am author),
             events[[ts,action]]
issues[]:    iid,url,title,state,author,assignees[],my_roles[],in_window_because[],created_at,closed_at,labels,milestone,
             description,my_notes[],notes_by_others
milestones[]: title,url,state,start_date,due_date,updated_at,description,i_created_it,my_items{merge_requests,issues}
releases[]:  tag,name,released_at,url
pipelines:   total, by_status{}, by_source{}
events[]:    created_at, action, target_type, target_iid, target_title, noteable_type, noteable_iid, push, push_ref, push_commits
wiki (kind=wiki): commits_in_window_total, my_commits[], pages_touched[{file,url,my_commits,others_commits,my_additions,my_deletions,current_content}],
             pages_touched_only_by_others, events[]
```
`my_roles` ∈ author, assignee, reviewer, commenter, committer, merger, approver (change requests); author, assignee, commenter, closer (issues). `in_window_because` states why the item is in the window (authored-in-window, merged-in-window, my-note-in-window, my-commit-in-window, event-in-window, assigned-closed-in-window).
