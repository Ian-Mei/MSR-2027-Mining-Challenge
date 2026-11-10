"""RQ3 (bundled scripts) starter: check whether artifact_siblings holds script contents.

Run from the repo root:  python analysis/rq3_bundled_scripts/run.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from gitskills.db import connect  # noqa: E402
from gitskills.paths import results_dir  # noqa: E402

OUT = results_dir("rq3_bundled_scripts")


def main() -> None:
    con = connect()
    con.sql("DESCRIBE artifact_siblings").show(max_rows=60)
    # If there is no content column above, scripts must be fetched from GitHub. Tell the team.
    # TODO: count siblings by file extension and save to OUT / "extensions.csv".


if __name__ == "__main__":
    main()
