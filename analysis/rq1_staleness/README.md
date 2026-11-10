# RQ1: Staleness

**Owners:** Ian, Ethan

**Question:** How often do skills become outdated relative to the projects and tools they describe?

**Experiment:** For each skill, compare when it was last edited with the repo's recent activity and with the
versions of the tools it mentions. Count a skill as outdated when the repo or tool has moved on (for example, a
major release or N months of commits) while the skill hasn't changed. Report how common that is and how long the gaps are.

## Suggested split

- **Ian: repo staleness.** Skill last-commit date vs. repo activity (`repos.pushed_at`, commits after the skill's last edit).
- **Ethan: tool staleness.** Extract tool and version mentions from skill text, then get release dates for those tools.
  This needs data from outside the dataset (GitHub releases, PyPI, npm), so start with a short list of popular tools.

## Tasks

- [ ] Filter to `history_fetched = 1`; record how many skills and repos are skipped
- [ ] Repo staleness: gap between the skill's last edit and the repo's last push
- [ ] Define "outdated" with explicit thresholds (for example 3, 6 and 12 months) and report each
- [ ] Tool mentions: extraction rules and a hand-checked sample for precision
- [ ] Tool staleness: skills that mention a version older than the latest major release at snapshot time
- [ ] Top-copied skills vs. random sample, reported separately
- [ ] `FINDINGS.md`: answer, numbers, charts, threats to validity

## Files

- `run.py`: starter script. Writes to `results/rq1_staleness/`.
