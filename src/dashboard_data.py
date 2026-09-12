from __future__ import annotations

import pandas as pd
from .config import GRAPH_SCALE, VERIFIED_METRICS, LLM_PROTOTYPE


def summary_cards() -> list[dict[str, str]]:
    return [
        {"label": "Payment edges", "value": f"{GRAPH_SCALE['Payment edges']:,}", "detail": "Temporal payment graph"},
        {"label": "Accounts", "value": f"{GRAPH_SCALE['Account nodes']:,}", "detail": "Graph entities"},
        {"label": "ROC-AUC", "value": f"{VERIFIED_METRICS['ROC-AUC']:.4f}", "detail": "Frozen model"},
        {"label": "PR-AUC", "value": f"{VERIFIED_METRICS['PR-AUC']:.4f}", "detail": "Frozen model"},
        {"label": "Evidence records", "value": "30,000", "detail": "Canonical evidence store"},
        {"label": "AI investigations", "value": str(LLM_PROTOTYPE['Successful persisted investigations']), "detail": "Validated prototype"},
    ]


def case_priority_data() -> pd.DataFrame:
    return pd.DataFrame({
        "Priority": ["P4_LOW", "P3_MEDIUM", "P2_HIGH", "P1_CRITICAL"],
        "Cases": [18795, 1205, 0, 0],
    })


def case_type_data() -> pd.DataFrame:
    return pd.DataFrame({
        "Case Type": ["LOW_PRIORITY_REVIEW", "MODEL_LED_CASE", "NETWORK_CONTEXT_REVIEW", "NETWORK_LED_CASE"],
        "Cases": [18745, 1239, 15, 1],
    })


def evidence_data() -> pd.DataFrame:
    return pd.DataFrame({
        "Evidence Type": ["TRANSACTION_CONTEXT", "NETWORK_CONTEXT", "MODEL_SIGNAL", "BEHAVIOR_CONTEXT"],
        "Records": [19000, 6000, 3000, 2000],
    })


def coverage_data() -> pd.DataFrame:
    return pd.DataFrame({
        "Evidence Layer": [
            "Model signal", "Transaction context", "Network context",
            "Behavior context", "Minimum evidence", "Multi-source", "GOOD/RICH"
        ],
        "Coverage (%)": [100, 100, 100, 100, 100, 100, 100],
    })


def ablation_data() -> pd.DataFrame:
    return pd.DataFrame({
        "Condition": ["A_ACTUAL", "B_CONSTANT", "C_SHUFFLED", "D_RANDOM_TOPOLOGY", "E_RANDOM_BOTH"],
        "PR-AUC": [0.780603, 0.944459, 0.943282, 0.718471, 0.651668],
    })
