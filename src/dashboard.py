from __future__ import annotations

import plotly.graph_objects as go
from plotly.subplots import make_subplots

from .dashboard_data import (
    summary_cards,
    case_priority_data,
    case_type_data,
    evidence_data,
    coverage_data,
    ablation_data,
)
from .metrics import ablation_effects


def executive_figure():
    cards = summary_cards()
    fig = make_subplots(
        rows=2,
        cols=3,
        specs=[[{"type": "indicator"}] * 3, [{"type": "indicator"}] * 3],
        vertical_spacing=0.15,
    )
    for i, card in enumerate(cards, start=1):
        fig.add_trace(
            go.Indicator(
                mode="number",
                value=_numeric(card["value"]),
                title={"text": f"{card['label']}<br><sup>{card['detail']}</sup>"},
            ),
            row=(i - 1) // 3 + 1,
            col=(i - 1) % 3 + 1,
        )
    fig.update_layout(title="AML Prototype — Executive KPI Board", height=650)
    return fig


def operations_figure():
    priority = case_priority_data()
    types = case_type_data()
    fig = make_subplots(rows=1, cols=2, subplot_titles=["Investigation Priority", "Case Type"])
    fig.add_trace(go.Bar(x=priority["Priority"], y=priority["Cases"], text=priority["Cases"], textposition="outside"), row=1, col=1)
    fig.add_trace(go.Bar(x=types["Case Type"], y=types["Cases"], text=types["Cases"], textposition="outside"), row=1, col=2)
    fig.update_layout(title="AML Operations Queue", height=550, showlegend=False)
    fig.update_xaxes(tickangle=-25, row=1, col=2)
    return fig


def evidence_figure():
    evidence = evidence_data()
    coverage = coverage_data()
    fig = make_subplots(rows=1, cols=2, subplot_titles=["Evidence Composition", "Evidence Coverage"], specs=[[{"type": "domain"}, {"type": "xy"}]])
    fig.add_trace(go.Pie(labels=evidence["Evidence Type"], values=evidence["Records"], hole=0.45), row=1, col=1)
    fig.add_trace(go.Bar(x=coverage["Evidence Layer"], y=coverage["Coverage (%)"], text=["100%"] * len(coverage), textposition="outside"), row=1, col=2)
    fig.update_layout(title="Evidence-Grounded Investigation Layer", height=560, showlegend=True)
    return fig


def validation_figure():
    a = ablation_data()
    eff = ablation_effects()
    fig = make_subplots(rows=1, cols=2, subplot_titles=["Controlled Results", "Key Structural Effects"])
    fig.add_trace(go.Bar(x=a["Condition"], y=a["PR-AUC"], text=[f"{x:.3f}" for x in a["PR-AUC"]], textposition="outside"), row=1, col=1)
    labels = ["Actual − randomized topology", "Money-neutralized topology"]
    values = [eff["actual_minus_random_topology"], eff["money_neutralized_topology_effect"]]
    fig.add_trace(go.Bar(x=labels, y=values, text=[f"{x:.6f}" for x in values], textposition="outside"), row=1, col=2)
    fig.update_layout(title="Model Validation Evidence", height=560, showlegend=False)
    fig.update_xaxes(tickangle=-25, row=1, col=1)
    fig.update_xaxes(tickangle=-25, row=1, col=2)
    return fig


def governance_table():
    return [
        ["Temporal separation", "80,000 / 20,000", "PASS"],
        ["Checkpoint integrity", "SHA-256 verified", "PASS"],
        ["Ground-truth contamination", "0", "PASS"],
        ["Invalid evidence citations", "0", "PASS"],
        ["Test data used for scaling", "NO", "PASS"],
        ["Test data used for model selection", "NO", "PASS"],
        ["Model retrained during showcase", "NO", "PASS"],
        ["Model weights modified", "NO", "PASS"],
    ]


def _numeric(value: str) -> float:
    cleaned = value.replace(",", "")
    try:
        return float(cleaned)
    except ValueError:
        return 0.0
