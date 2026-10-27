# Project plan

> The 1-page plan we submitted on Canvas goes here, kept up to date as the plan changes.

## Dataset(s)

- GitSkills, Hugging Face Parquet mirror `mvaccargiu/gitskills` (snapshot: July 2026 collection; HF revision `ebab17454a7c236f8f26b183567f1a126f42e3f8`, pinned in scripts/download_data.py).

## Research questions

<!-- Pick 2–3. Candidate directions from the challenge call: -->

- **RQ1:**
- **RQ2:**
- **RQ3:**

<details>
<summary>Candidate directions from the challenge call</summary>

1. **Adoption and linguistic evolution.** How fast the format spreads and which projects adopt it first; a
   taxonomy of skill purposes; linguistic drift across monthly cohorts; agent-authored skills; the natural
   language a skill is written in.
2. **Shared format.** Vendor-neutral vs. tool-specific locations (`location_class`) over time; whether skill
   text addresses one named tool or any agent.
3. **Reuse without a package manager.** 50.5% of files are verbatim copies. How concentrated reuse is; the
   mechanisms that move skills (catalogs, scaffolding); clone-genealogy patterns.
4. **Metrics for natural-language instructions.** Size, churn, age, clone coverage, and readability compared
   with code; quality indicators; which `description` properties go with reuse.
5. **Maintenance and trust.** Staleness; modified copies that add command execution or network access
   (a supply-chain analog); bundled executables and how far they spread.

</details>

## Experiments

| RQ | Data / columns | Method | Output |
|---|---|---|---|
| RQ1 | | | |
| RQ2 | | | |
| RQ3 | | | |

## Risks and mitigations

| Risk | Mitigation |
|---|---|
| Full dataset is large (44 GB SQLite; millions of rows with full text) | Use the Parquet mirror with DuckDB; prototype on `--parts 2`; push filters and projections down |
| Commit history exists for only a subset of files | Report coverage; restrict time-based RQs to `history_fetched = 1` |
| Verbatim duplicates skew counts | Report both occurrence-level and distinct-content (`dedup_primary = 1`) numbers |
| Manual labeling (taxonomy) is subjective | Two annotators, codebook, report Cohen's kappa on an overlap sample |
| 4-page limit | Fix RQs early and cut scope rather than squeezing text |
