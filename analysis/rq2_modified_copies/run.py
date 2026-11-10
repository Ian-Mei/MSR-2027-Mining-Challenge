"""RQ2 (modified copies) starter: list the most-copied skills by content hash.

Run from the repo root:  python analysis/rq2_modified_copies/run.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from gitskills.db import connect  # noqa: E402
from gitskills.paths import results_dir  # noqa: E402

OUT = results_dir("rq2_modified_copies")


def main() -> None:
    con = connect()
    con.sql("DESCRIBE artifacts").show(max_rows=60)
    # TODO: replace content_hash with the actual hash column name from the schema above.
    # top = con.sql("SELECT content_hash, count(*) AS copies FROM artifacts GROUP BY 1 ORDER BY copies DESC LIMIT 50")
    # top.df().to_csv(OUT / "top_copied.csv", index=False)


if __name__ == "__main__":
    main()
