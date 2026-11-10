"""Shared paths for analysis outputs."""

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
RESULTS_ROOT = REPO_ROOT / "results"


def results_dir(rq: str) -> Path:
    """Return results/<rq>/, creating it if needed (git ignores results/)."""
    out = RESULTS_ROOT / rq
    out.mkdir(parents=True, exist_ok=True)
    return out
