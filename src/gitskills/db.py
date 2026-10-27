"""DuckDB views over the downloaded GitSkills Parquet files.

Usage:
    from gitskills.db import connect
    con = connect()
    con.sql("SELECT location_class, count(*) FROM artifacts GROUP BY 1").show()
"""

from pathlib import Path

import duckdb

PARQUET_ROOT = Path(__file__).resolve().parents[2] / "data" / "gitskills" / "data"


def connect(root: Path = PARQUET_ROOT, database: str = ":memory:") -> duckdb.DuckDBPyConnection:
    """Open DuckDB with one view per downloaded table (artifacts, artifact_siblings, repos, mining_runs)."""
    con = duckdb.connect(database)
    if not root.exists():
        raise FileNotFoundError(f"{root} not found; run scripts/download_data.py first")
    for table_dir in sorted(p for p in root.iterdir() if p.is_dir()):
        glob = (table_dir / "*.parquet").as_posix()
        con.execute(f"CREATE VIEW {table_dir.name} AS SELECT * FROM read_parquet('{glob}')")
    return con
