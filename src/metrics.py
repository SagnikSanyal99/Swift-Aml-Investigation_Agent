from __future__ import annotations

import pandas as pd
from .config import VERIFIED_METRICS, GRAPH_SCALE, LLM_PROTOTYPE


def verified_kpi_frame() -> pd.DataFrame:
    rows = []
    for key, value in VERIFIED_METRICS.items():
        rows.append({"KPI": key, "Value": value, "Layer": "Frozen model"})
    for key, value in GRAPH_SCALE.items():
        rows.append({"KPI": key, "Value": value, "Layer": "Graph"})
    for key, value in LLM_PROTOTYPE.items():
        rows.append({"KPI": key, "Value": value, "Layer": "AI prototype"})
    return pd.DataFrame(rows)


def ablation_effects() -> dict[str, float]:
    return {
        "actual_minus_random_topology": 0.780603 - 0.718471,
        "money_neutralized_topology_effect": 0.944459 - 0.651668,
    }

