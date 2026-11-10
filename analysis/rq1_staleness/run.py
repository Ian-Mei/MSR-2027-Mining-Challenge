"""RQ1 (staleness) starter: check the commit-history columns we need.

Run from the repo root:  python analysis/rq1_staleness/run.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from gitskills.db import connect  # noqa: E402
from gitskills.paths import results_dir  # noqa: E402

OUT = results_dir("rq1_staleness")


def main() -> None:
    con = connect()
    con.sql("DESCRIBE artifacts").show(max_rows=60)
    # TODO: filter history_fetched = 1, join repos, compute gap between skill's last commit and repo's last push.


if __name__ == "__main__":
    main()
