# RQ3: Bundled scripts

**Owner:** Chloe

**Question:** How often do skills bundle executable files, and how widely are these skills copied?

**Experiment:** Find skills that bundle script files (.sh, .py, etc.). Analyze each script without running it and
sort it into one of three groups: read-only, modifies files or the system, or uses the network. Compare how widely
each group is copied.

## First thing to check

Does `artifact_siblings` include the scripts' contents, or only paths and flags? Run `run.py` after downloading the
table. If contents are missing, scripts must be fetched from GitHub, which changes the plan. Tell the team and the TA.

## Tasks

- [ ] Share of skills with bundled scripts, by extension (.sh, .py, .js, ...)
- [ ] Copy counts for skills with vs. without scripts
- [ ] Static classifier: read-only / modifies files or system / uses network (rules per language)
- [ ] Hand-check a sample of classified scripts; report agreement
- [ ] Compare copy spread across the three groups (with a statistical test, for example Mann-Whitney U)
- [ ] Top-copied skills vs. random sample, reported separately
- [ ] `FINDINGS.md`: answer, numbers, charts, threats to validity

**Never execute a script from the dataset.**

## Files

- `run.py`: starter script. Prints the `artifact_siblings` schema. Writes to `results/rq3_bundled_scripts/`.
