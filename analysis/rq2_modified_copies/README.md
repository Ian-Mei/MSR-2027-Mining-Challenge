# RQ2: Risky modified copies

**Owner:** Euba

**Question:** Do modified copies of widely reused skills introduce command execution or network access absent
from the original (the analog of a supply-chain attack in an ecosystem without a registry)?

**Experiment:** Group copies of the most widely copied skills using exact and near-duplicate matching, and pick a
"parent" for each group by earliest commit date. Compare each modified copy with its parent and flag any added
shell commands, downloads (curl, wget), package installs, or new URLs. Report how often this happens and show examples.

This is the hardest RQ. Get a narrow version working first, then widen it.

## Tasks

- [ ] Pick the top N most-copied skills (start with N = 50) by content hash and by `name`
- [ ] Near-duplicate grouping (for example MinHash or token Jaccard); check a sample of groups by hand
- [ ] Parent = earliest first-commit date; mark groups where the order is uncertain
- [ ] Diff each modified copy against its parent; extract added lines
- [ ] Detector for added risk: shell commands, `curl`/`wget`, `| sh`, package installs, new URLs
- [ ] Hand-label a sample of flagged and unflagged diffs; report precision (and recall on the sample)
- [ ] Report with and without uncertain-parent groups; top skills vs. random sample
- [ ] `FINDINGS.md`: answer, numbers, worked examples, threats to validity

## Files

- `run.py`: starter script. Writes to `results/rq2_modified_copies/`.
