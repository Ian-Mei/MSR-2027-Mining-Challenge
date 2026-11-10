# Analysis workspaces

One folder per research question. Each owner works in their own folder, so nobody edits the same files.

| Folder | RQ | Owner(s) |
|---|---|---|
| [rq1_staleness/](rq1_staleness/) | How often do skills become outdated? | Ian, Ethan |
| [rq2_modified_copies/](rq2_modified_copies/) | Do modified copies add command execution or network access? | Euba |
| [rq3_bundled_scripts/](rq3_bundled_scripts/) | How often do skills bundle executables, and how far do they spread? | Chloe |

## Rules

- **Your folder is yours.** Put scripts, notebooks and notes for your RQ there.
- **Shared code goes in `src/gitskills/`** (for example, commit-date helpers that both RQ1 and RQ2 use).
  Tell the team in chat before you change a shared function.
- **Outputs go in `results/<rq folder>/`**, which git ignores. Every table or chart must be reproducible by
  running a script in your folder.
- **Clear notebook outputs before committing.**
- **Never run a script from the dataset.** Static analysis only (see risks in [docs/project_plan.md](../docs/project_plan.md)).
- Work on a branch named after your RQ (for example `rq2`), and open a PR into `main` when something works.

## Shared schedule

| Date | Milestone (everyone) |
|---|---|
| Thu Nov 12 | One preliminary number or chart per RQ for the TA check-in |
| Tue Nov 24 | Pipeline runs end to end on the sample (most-copied skills + random sample) |
| Sun Dec 6 | Full results, including the threshold and sample-vs-top comparisons |
| Sun Dec 13 | Final answers written up in your folder's `FINDINGS.md`; team review |
| Tue Dec 15 | Final project due, 11:55 PM EST |
