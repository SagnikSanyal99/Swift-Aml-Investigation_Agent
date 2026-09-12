from pathlib import Path
import pandas as pd


def load_csv(path: str | Path, required_columns: list[str] | None = None) -> pd.DataFrame:
    """Load a CSV and optionally validate required columns."""
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(path)
    df = pd.read_csv(path)
    if required_columns:
        missing = [c for c in required_columns if c not in df.columns]
        if missing:
            raise ValueError(f"{path.name}: missing columns {missing}")
    return df


def load_results(results_dir: str | Path) -> dict[str, pd.DataFrame]:
    results_dir = Path(results_dir)
    files = {
        "kpis": "verified_kpis.csv",
        "ablation": "controlled_ablation_20_epoch.csv",
        "retrieval": "retrieval_coverage.csv",
        "evidence": "evidence_composition.csv",
        "priority": "case_priority.csv",
        "case_type": "case_type.csv",
    }
    return {
        key: load_csv(results_dir / filename)
        for key, filename in files.items()
        if (results_dir / filename).exists()
    }
