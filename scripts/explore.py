"""Print the schema and row count of every downloaded GitSkills table (sanity check after download)."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from gitskills.db import connect  # noqa: E402


def main() -> None:
    con = connect()
    for (name,) in con.execute("SELECT view_name FROM duckdb_views() WHERE NOT internal ORDER BY 1").fetchall():
        rows = con.execute(f"SELECT count(*) FROM {name}").fetchall()[0][0]
        print(f"\n== {name} ({rows:,} rows in downloaded parts)")
        con.sql(f"DESCRIBE {name}").show(max_rows=50)


if __name__ == "__main__":
    main()
