from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
required = [
    "README.md",
    "requirements.txt",
    "pyproject.toml",
    "CITATION.cff",
    "notebooks/00_FINAL_PROJECT_VALIDATION_AND_RESULTS.ipynb",
    "notebooks/01_DATA_AND_ARCHITECTURE.ipynb",
    "notebooks/02_MODEL_AND_CONTROLLED_VALIDATION.ipynb",
    "notebooks/03_EVIDENCE_AND_INVESTIGATION.ipynb",
    "notebooks/04_END_USER_DASHBOARD.ipynb",
    "src/config.py",
    "src/data_loader.py",
    "src/metrics.py",
    "src/dashboard_data.py",
    "src/dashboard.py",
    "docs/architecture.md",
    "docs/model_card.md",
    "docs/governance.md",
    "docs/business_context.md",
    "docs/investigation_workflow.md",
    "docs/audience_guide.md",
    "docs/build_roadmap.md",
    "results/verified_kpis.csv",
    "results/controlled_ablation_20_epoch.csv",
    "results/retrieval_coverage.csv",
    "results/evidence_composition.csv",
    "results/case_priority.csv",
    "results/case_type.csv",
]
missing = [p for p in required if not (ROOT / p).exists()]
if missing:
    raise SystemExit("Missing repository files:\n" + "\n".join(missing))

# Verify headline result values are represented in summary data.
kpis = list(csv.DictReader((ROOT / "results/verified_kpis.csv").open()))
kmap = {row["KPI"]: float(row["Value"]) for row in kpis}
assert abs(kmap["ROC-AUC"] - 0.972667) < 1e-9
assert abs(kmap["PR-AUC"] - 0.554988) < 1e-9
assert kmap["Payment edges"] == 100000
assert kmap["Account nodes"] == 36979
assert kmap["Ground-truth contamination"] == 0

print("Repository validation: PASS")
print(f"Checked {len(required)} required files and headline KPI consistency.")
