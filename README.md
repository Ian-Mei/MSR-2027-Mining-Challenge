# MSR 2027 Mining Challenge: GitSkills

CS 520 (Fall 2026, UMass Amherst) final project. We are mining the
[GitSkills](https://arxiv.org/abs/2608.10906) dataset of agent-skill files (`SKILL.md`) on GitHub
for the [MSR 2027 Mining Challenge](https://2027.msrconf.org/track/msr-2027-mining-challenge).

- Course requirements and deadlines: [docs/requirements.md](docs/requirements.md)
- Project plan and research questions: [docs/project_plan.md](docs/project_plan.md)
- Paper draft (IEEEtran, 4 + 1 pages): [paper/main.tex](paper/main.tex)

## Dataset

GitSkills (Destefanis, Graziotin, Vaccargiu, Ortu; MSR '27) holds 3,797,117 `SKILL.md` occurrences
from 282,200 public GitHub repositories, collected in July 2026. They dedupe to 1,877,981 distinct contents.

| Source | Link | Notes |
|---|---|---|
| Hugging Face (Parquet) | https://huggingface.co/datasets/mvaccargiu/gitskills | **What we use.** One folder per table |
| Zenodo (full SQLite) | https://doi.org/10.5281/zenodo.21875637 | ~44 GB single file |
| GitHub sample | https://github.com/giuseppedestefanis/gitskills-sample | Small zip for quick looks |

Tables:

- `artifacts` (3.8M rows): one row per `SKILL.md` occurrence. Columns include repo, path, `location_class`,
  content and hash, parsed front matter (`name`, `description`), `dedup_primary`, commit history
  (first and last commit with author type), and sibling and script flags.
- `artifact_siblings` (7.3M rows): the other files in each skill's folder (scripts, references, and so on).
- `repos` (282K rows): stars, forks, language, license, created and pushed dates.
- `mining_runs` (7 rows): provenance of the collection queries.

## Setup

```bash
python -m venv .venv
source .venv/Scripts/activate      # Windows Git Bash; use .venv/bin/activate on macOS/Linux
pip install -r requirements.txt

# Small tables first, plus 2 parts of artifacts for prototyping
python scripts/download_data.py --tables repos mining_runs
python scripts/download_data.py --tables artifacts --parts 2
python scripts/explore.py
```

Data lands in `data/gitskills/data/<table>/part-*.parquet`, which git ignores. Query it with DuckDB:

```python
import sys; sys.path.insert(0, "src")
from gitskills.db import connect
con = connect()
con.sql("SELECT location_class, count(*) n FROM artifacts GROUP BY 1 ORDER BY n DESC").show()
```

## Layout

```
docs/        course requirements, project plan, meeting notes
scripts/     data download and one-off analysis scripts
src/gitskills/   shared code (DuckDB loader, helpers)
notebooks/   exploratory notebooks (clear outputs before committing)
paper/       LaTeX source for the challenge paper
data/        downloaded dataset (git-ignored)
results/     generated tables and figures (git-ignored; copy final figures to paper/figures/)
```

## Team

| Name | Role / RQ |
|---|---|
| Ian Mei | |
| | |
| | |
