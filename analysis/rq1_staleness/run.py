"""RQ1 (staleness), repo side: gap between a skill's last edit and its repo's last push.

A skill is "stale at T months" when the repo kept being pushed to for more than T months after
the skill's last commit. Only skills with fetched history (history_fetched = 1) are used.

Run from the repo root:  python analysis/rq1_staleness/run.py
Writes results/rq1_staleness/{repo_gap.csv, repo_staleness_summary.csv, repo_gap_hist.png}.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

import matplotlib  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

from gitskills.db import connect  # noqa: E402
from gitskills.paths import results_dir  # noqa: E402

OUT = results_dir("rq1_staleness")
THRESHOLDS_MONTHS = [3, 6, 12]
DAYS_PER_MONTH = 30.44
SNAPSHOT = "2026-07-09"  # GitSkills discovered_at date

GAP_SQL = """
SELECT a.repo_full_name,
       a.path,
       a.location_class,
       a.dedup_primary,
       CAST(a.last_commit_at AS TIMESTAMP) AS skill_last_commit,
       CAST(r.pushed_at AS TIMESTAMP)      AS repo_pushed_at,
       date_diff('second', CAST(a.last_commit_at AS TIMESTAMP), CAST(r.pushed_at AS TIMESTAMP)) / 86400.0 AS gap_days
FROM artifacts a
JOIN repos r ON a.repo_full_name = r.full_name
WHERE a.history_fetched = 1
  AND a.last_commit_at IS NOT NULL
  AND r.pushed_at IS NOT NULL
"""


def main() -> None:
    con = connect()

    total, with_hist = con.sql(
        "SELECT count(*), count(*) FILTER (WHERE history_fetched = 1) FROM artifacts"
    ).fetchall()[0]
    print(f"artifacts loaded: {total:,}; with history: {with_hist:,} ({with_hist / total:.1%}); "
          f"skipped: {total - with_hist:,}")

    con.execute(f"CREATE TEMP TABLE gaps AS {GAP_SQL}")
    neg = con.sql("SELECT count(*) FROM gaps WHERE gap_days < 0").fetchall()[0][0]
    print(f"skill edited after repo pushed_at (negative gap, clipped to 0): {neg:,}")

    stale_cols = ",\n  ".join(
        f"avg(CASE WHEN gap_days > {t * DAYS_PER_MONTH} THEN 1 ELSE 0 END) AS stale_{t}m"
        for t in THRESHOLDS_MONTHS
    )
    summary = con.sql(f"""
        SELECT coalesce(location_class, 'ALL') AS location_class,
               count(*) AS n,
               count(DISTINCT repo_full_name) AS repos,
               median(greatest(gap_days, 0)) AS median_gap_days,
               quantile_cont(greatest(gap_days, 0), 0.75) AS p75_gap_days,
               {stale_cols}
        FROM gaps
        GROUP BY ROLLUP (location_class)
        ORDER BY location_class = 'ALL' DESC, n DESC
    """).df()
    print(summary.to_string(index=False, float_format=lambda x: f"{x:.3f}"))

    summary.to_csv(OUT / "repo_staleness_summary.csv", index=False)

    # Most skills are only a few months old, so the share above is capped by skill age (right-censoring).
    # Fairer rate: among skills last edited at least T months before the snapshot, how many went stale.
    print(f"\nAge-conditioned (skill last edited >= T months before snapshot {SNAPSHOT}):")
    rows = []
    for t in THRESHOLDS_MONTHS:
        n, rate = con.sql(f"""
            SELECT count(*), avg(CASE WHEN gap_days > {t * DAYS_PER_MONTH} THEN 1 ELSE 0 END)
            FROM gaps WHERE skill_last_commit <= TIMESTAMP '{SNAPSHOT}' - INTERVAL {t} MONTH
        """).fetchall()[0]
        rows.append((t, n, rate))
        print(f"  T = {t:>2} months: eligible {n:,}, stale {rate:.1%}")
    with open(OUT / "repo_staleness_age_conditioned.csv", "w") as f:
        f.write("threshold_months,eligible,stale_share\n")
        f.writelines(f"{t},{n},{rate}\n" for t, n, rate in rows)
    gaps = con.sql("SELECT * FROM gaps").df()
    gaps.to_csv(OUT / "repo_gap.csv", index=False)

    fig, ax = plt.subplots(figsize=(6, 3.5))
    ax.hist(gaps["gap_days"].clip(lower=0) / DAYS_PER_MONTH, bins=60, range=(0, 30))
    for t in THRESHOLDS_MONTHS:
        ax.axvline(t, linestyle="--", linewidth=1, color="gray")
    ax.set_xlabel("Months between skill's last edit and repo's last push")
    ax.set_ylabel("Skills")
    ax.set_yscale("log")
    ax.set_title(f"Repo staleness (n = {len(gaps):,}, sample of 2 artifact parts)")
    fig.tight_layout()
    fig.savefig(OUT / "repo_gap_hist.png", dpi=150)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
