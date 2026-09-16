# Evidence-Grounded AML Investigation for Cross-Border SWIFT Payments
![Python](https://img.shields.io/badge/Python-3.11%2B-blue?logo=python)
![React](https://img.shields.io/badge/React-18+-blue?logo=react)
![FastAPI](https://img.shields.io/badge/FastAPI-Production-green?logo=fastapi)
![OpenAI](https://img.shields.io/badge/OpenAI-API-412991?logo=openai&logoColor=white)

> A governed AML analytics prototype connecting structured SWIFT payment data, payment relationships, a frozen risk model, contextual evidence retrieval, investigator workflow, and AI-assisted case analysis.
## Executive summary

The project demonstrates an auditable investigation architecture for synthetic cross-border SWIFT payments. The final validated system connects payment data to payment relationships, generates a frozen predictive signal, attaches contextual evidence, creates investigation cases, and provides a downstream AI-assisted investigation prototype.

### Verified outcomes

| Area | Result |
|---|---:|
| Payment edges | **100,000** |
| Account nodes | **36,979** |
| Training edges | **80,000** |
| Test edges | **20,000** |
| Frozen model ROC-AUC | **0.972667** |
| Frozen model PR-AUC | **0.554988** |
| Recall @ 0.50 | **0.768501** |
| Canonical evidence records | **30,000** |
| Selected investigation cases | **1,000** |
| Model signal coverage | **100%** |
| Transaction context coverage | **100%** |
| Network context coverage | **100%** |
| Behavioral context coverage | **100%** |
| Multi-source evidence coverage | **100%** |
| GOOD/RICH evidence coverage | **100%** |
| Explicit ground-truth contamination | **0** |
| Successful persisted AI investigations | **32** |
| Fully cited successful AI findings | **100%** |
| Invalid evidence citations | **0** |

## The project story

```text
Structured SWIFT payment data
            ↓
Payment entities and relationships
            ↓
Temporal payment graph
            ↓
Frozen risk signal
            ↓
Canonical multi-source evidence
            ↓
Investigation case
            ↓
AI-assisted investigator analysis
            ↓
Audit trail and governance
```

## Repository structure

```text
aml-swift-aml-investigation/
│
├── README.md
├── requirements.txt
├── pyproject.toml
├── CITATION.cff
├── LICENSE
├── .gitignore
│
├── notebooks/
│   ├── 00_FINAL_PROJECT_VALIDATION_AND_RESULTS.ipynb
│   ├── 01_DATA_AND_ARCHITECTURE.ipynb
│   ├── 02_MODEL_AND_CONTROLLED_VALIDATION.ipynb
│   ├── 03_EVIDENCE_AND_INVESTIGATION.ipynb
│   └── 04_END_USER_DASHBOARD.ipynb
│
├── src/
│   ├── config.py
│   ├── data_loader.py
│   ├── metrics.py
│   ├── dashboard_data.py
│   └── dashboard.py
│
├── dashboard/
│   └── README.md
│
├── docs/
│   ├── architecture.md
│   ├── model_card.md
│   ├── governance.md
│   ├── business_context.md
│   ├── investigation_workflow.md
│   ├── audience_guide.md
│   └── build_roadmap.md
│
├── results/
│   ├── verified_kpis.csv
│   ├── controlled_ablation_20_epoch.csv
│   ├── retrieval_coverage.csv
│   ├── evidence_composition.csv
│   ├── case_priority.csv
│   └── case_type.csv
│
├── data/
│   └── README.md
│
├── scripts/
│   └── validate_repository.py
│
└── .github/workflows/
    └── validate.yml
```

## Presentation sequence

See `docs/presentation_sequence.md` for a concise audience-by-audience demonstration sequence.

## Main notebook

Open:

**`notebooks/00_FINAL_PROJECT_VALIDATION_AND_RESULTS.ipynb`**

This is the recommended presentation entry point. It is designed to communicate the project to executives, banking operations leaders, investigators, analytics teams, model-risk reviewers, AI engineers, recruiters, and interviewers.

## Interactive presentation dashboard

The repository includes a standalone interactive dashboard in `dashboard/index.html`. The included GitHub Pages workflow can publish it as the public demonstration site after Pages is enabled for the repository.

## End-user dashboard

The dashboard is designed around user roles rather than model internals:

- Executive / Risk Leadership
- AML Operations
- AML Investigator
- Compliance / Model Risk
- Data Science / ML
- AI / Engineering
- Portfolio / Interview

The dashboard moves from KPI summary to workload, evidence, model validation, governance, and investigator-level case inspection.

## Important project boundary

This repository is a research-grade prototype using synthetic data. It is not a production AML monitoring platform, regulator-approved model, autonomous compliance decision system, or replacement for trained investigators.

The predictive model is frozen. Investigation evidence is maintained separately from model signal. Synthetic ground truth is used for validation only and is not treated as operational evidence.

## LLM prototype boundary

The AI-assisted investigation layer was demonstrated on **32 persisted successful investigations**. It should be presented as a validated prototype rather than a completed 100-case evaluation because the remaining workload was constrained by API request limits.

## Final project statement

> Developed an evidence-grounded AML investigation architecture for cross-border SWIFT payments that combines a frozen payment-topology GNN, canonical multi-source evidence retrieval, and an LLM-assisted investigator workflow.

## Reproducibility

The repository separates source code, persisted results, documentation, and external data. Raw project data and model weights are intentionally not included by default. See `data/README.md` for the expected local artifact structure.
