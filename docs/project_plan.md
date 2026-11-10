# Project plan

The 1-page plan we submitted on Canvas (Oct 8, 2026), kept up to date as the plan changes.
We answer the research questions; we are not writing the MSR paper.

## Dataset(s)

- GitSkills, Hugging Face Parquet mirror `mvaccargiu/gitskills` (snapshot: July 2026 collection; HF revision `ebab17454a7c236f8f26b183567f1a126f42e3f8`, pinned in scripts/download_data.py).

## Research questions

Challenge direction 5, **maintenance and trust**. Skills can instruct agents to run commands, access external
resources, and execute bundled scripts, and they are copied between repositories without formal review.

| RQ | Question | Owner(s) |
|---|---|---|
| **RQ1** | How often do skills become outdated relative to the projects and tools they describe? | Ian, Ethan |
| **RQ2** | Do modified copies of widely reused skills introduce command execution or network access absent from the original (the analog of a supply-chain attack in an ecosystem without a registry)? | Euba |
| **RQ3** | How often do skills bundle executable files, and how widely are these skills copied? | Chloe |

## Experiments

**RQ1.** For each skill, compare when it was last edited with the repo's recent activity and with the versions
of the tools it mentions. Count a skill as outdated when the repo or tool has moved on (for example, a major
release or N months of commits) while the skill hasn't changed. Report how common that is and how long the gaps are.

**RQ2.** Group copies of the most widely copied skills using exact and near-duplicate matching, and pick a
"parent" for each group by earliest commit date. Compare each modified copy with its parent and flag any added
shell commands, downloads (curl, wget), package installs, or new URLs. Report how often this happens and show examples.

**RQ3.** Find skills that bundle script files (.sh, .py, etc.). Analyze each script without running it and sort
it into one of three groups: read-only, modifies files or the system, or uses the network. Compare how widely
each group is copied.

## Risks and mitigations

| Risk | Mitigation |
|---|---|
| We can't tell which version is the original | Use the earliest commit date; report results with and without uncertain groups |
| Running untrusted scripts is unsafe | Static analysis only; if anything must run, use a disposable sandbox with no network access |
| The dataset is too large to process in time | Start with the most-copied skills plus a random sample; scale up if there's time |
| "Outdated" is subjective | Define it with explicit thresholds; show how results change under several thresholds |
| Missing or rewritten git history | Skip affected repos in the timing analysis (`history_fetched = 1` only) and report how many were skipped |
| Highly copied skills might not represent the full dataset | Analyze highly copied skills and a random sample separately; state which group each result represents; compare |
