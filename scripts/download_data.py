"""Download the GitSkills Parquet mirror from Hugging Face into data/gitskills/.

Examples:
    python scripts/download_data.py                       # repos + mining_runs only (small)
    python scripts/download_data.py --tables artifacts    # all artifact parts
    python scripts/download_data.py --tables artifacts --parts 2   # first 2 parts (for prototyping)
    python scripts/download_data.py --tables all
"""

import argparse
from pathlib import Path

from huggingface_hub import HfApi, hf_hub_download

REPO_ID = "mvaccargiu/gitskills"
# Pinned dataset snapshot; report this in the paper (challenge requirement).
REVISION = "ebab17454a7c236f8f26b183567f1a126f42e3f8"
TABLES = ["artifacts", "artifact_siblings", "repos", "mining_runs"]
DATA_DIR = Path(__file__).resolve().parent.parent / "data" / "gitskills"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--tables", nargs="+", default=["repos", "mining_runs"],
                        help=f"tables to fetch, or 'all' (choices: {', '.join(TABLES)})")
    parser.add_argument("--parts", type=int, default=None,
                        help="only fetch the first N Parquet parts per table")
    args = parser.parse_args()

    tables = TABLES if "all" in args.tables else args.tables
    unknown = set(tables) - set(TABLES)
    if unknown:
        parser.error(f"unknown table(s): {', '.join(sorted(unknown))}")

    files = HfApi().list_repo_files(REPO_ID, repo_type="dataset", revision=REVISION)
    for table in tables:
        parts = sorted(f for f in files if f.startswith(f"data/{table}/") and f.endswith(".parquet"))
        if args.parts is not None:
            parts = parts[: args.parts]
        print(f"{table}: {len(parts)} part(s)")
        for f in parts:
            hf_hub_download(REPO_ID, f, repo_type="dataset", revision=REVISION, local_dir=DATA_DIR)

    print(f"Done. Files are under {DATA_DIR / 'data'}")


if __name__ == "__main__":
    main()
