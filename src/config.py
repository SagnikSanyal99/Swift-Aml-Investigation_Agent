from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
RESULTS_DIR = PROJECT_ROOT / "results"
DATA_DIR = PROJECT_ROOT / "data"

VERIFIED_METRICS = {
    "ROC-AUC": 0.972667,
    "PR-AUC": 0.554988,
    "Precision @ 0.50": 0.246801,
    "Recall @ 0.50": 0.768501,
    "F1 @ 0.50": 0.373616,
    "Brier": 0.053497,
}

GRAPH_SCALE = {
    "Payment edges": 100_000,
    "Training edges": 80_000,
    "Test edges": 20_000,
    "Account nodes": 36_979,
    "Bank nodes": 150,
    "Country nodes": 15,
}

LLM_PROTOTYPE = {
    "Intended investigations": 100,
    "Successful persisted investigations": 32,
    "Fully cited successful findings (%)": 100,
    "Invalid evidence citations": 0,
    "Ground-truth contamination": 0,
}

