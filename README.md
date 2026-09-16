# Evidence-Grounded AML Investigation for Cross-Border SWIFT Payments

> **An auditable AML analytics prototype connecting structured cross-border payment data, payment relationships, a frozen risk model, contextual evidence retrieval, investigator workflows, and AI-assisted case analysis.**

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue?logo=python)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.x-ee4c2c?logo=pytorch)](https://pytorch.org/)
[![PyTorch Geometric](https://img.shields.io/badge/PyTorch%20Geometric-2.x-orange)](https://pyg.org/)
[![Plotly](https://img.shields.io/badge/Plotly-Interactive%20Dashboard-3f4f75?logo=plotly)](https://plotly.com/)

---

# 01 — Executive Summary

This project demonstrates a governed investigation workflow for synthetic cross-border SWIFT payments that connects:

**Payment data → payment relationships → model signal → contextual evidence → investigation case → AI-assisted analysis → audit trail**

The core result is not a standalone classifier. It is an **auditable investigation workflow** in which predictive output is kept separate from supporting evidence and validation-only information.

### Verified outcomes

| Measure | Verified result |
|---|---:|
| Payment edges | **100,000** |
| Account nodes | **36,979** |
| Bank nodes | **150** |
| Country nodes | **15** |
| Training payment edges | **80,000** |
| Test payment edges | **20,000** |
| Frozen model ROC-AUC | **0.972667** |
| Frozen model PR-AUC | **0.554988** |
| Recall @ 0.50 | **0.768501** |
| F1 @ 0.50 | **0.373616** |
| Canonical evidence records | **30,000** |
| Selected investigation cases | **1,000** |
| Model signal coverage | **100%** |
| Transaction context coverage | **100%** |
| Network context coverage | **100%** |
| Behavioral context coverage | **100%** |
| Multi-source evidence coverage | **100%** |
| GOOD/RICH evidence coverage | **100%** |
| Explicit ground-truth contamination | **0** |
| Persisted AI investigations | **32** |
| Fully cited successful AI findings | **100%** |
| Invalid evidence citations | **0** |

### What was demonstrated

- A structured synthetic cross-border payment environment.
- A temporal payment relationship representation.
- A frozen payment-topology predictive model.
- Controlled experiments testing the contribution of payment topology.
- A canonical evidence layer covering model, transaction, network and behavioral context.
- Investigator-oriented case generation and evidence packages.
- A downstream AI-assisted investigation prototype.
- Explicit validation, immutability and evidence-isolation controls.

### What was not claimed

This is **not** a production AML monitoring platform, regulator-approved model, autonomous compliance decision system, or replacement for trained investigators.

---

# 02 — Project Overview & Business Context

## Business Situation

Cross-border payment monitoring can create investigation workloads in which a transaction score alone provides insufficient context for understanding the surrounding payment activity.

An investigator may need to move from:

> **“Why was this payment surfaced?”**

to:

> **“What surrounding evidence should I review?”**

## Business Problem

The prototype addresses five connected operational needs:

| Need | Prototype capability |
|---|---|
| Detection | Transaction-level predictive signal |
| Context | Transaction, network and behavioral information |
| Investigation | Structured case generation and prioritization |
| Evidence | Canonical multi-source evidence retrieval |
| AI assistance | Evidence-grounded downstream case analysis |

## Business Question

**Can structured SWIFT payment information be converted into an auditable investigation workflow that combines risk signal, contextual evidence, case management and AI-assisted analysis?**

## Demonstrated Answer

The prototype shows that the workflow can be constructed and validated over a synthetic cross-border payment environment.

```text
Structured SWIFT payment data
          ↓
Payment entities and relationships
          ↓
Temporal payment graph
          ↓
Frozen risk signal
          ↓
Canonical evidence
          ↓
Investigation case
          ↓
AI-assisted investigator analysis
          ↓
Audit trail and governance
```

---

# 03 — End-User Experience

The repository is organized around the people consuming the output rather than around model internals.

## Executive / Risk Leadership

Focus on:

- payment and account scale;
- model performance;
- investigation workload;
- evidence availability;
- governance controls.

## AML Operations

Focus on:

- investigation queue;
- priority distribution;
- case types;
- evidence availability;
- operational workload.

## AML Investigator

Focus on:

- individual case;
- model signal;
- transaction context;
- network context;
- behavioral context;
- supporting evidence;
- investigation workflow.

## Compliance / Model Risk

Focus on:

- temporal separation;
- frozen model integrity;
- evidence isolation;
- contamination controls;
- validation records.

## Data Science / ML

Focus on:

- graph construction;
- model metrics;
- controlled experiments;
- feature configuration;
- reproducibility.

## AI / Engineering

Focus on:

- canonical evidence store;
- evidence provenance;
- retrieval coverage;
- downstream AI analysis;
- citation validity.

## Portfolio / Interview

Focus on:

- business problem;
- end-to-end architecture;
- quantified outcomes;
- validation quality;
- governance.

---

# 04 — End-User Dashboard

The repository contains a presentation-oriented dashboard designed to move from executive KPIs to investigator-level case review.

### Dashboard capabilities

- interactive KPI cards;
- investigation queue views;
- case-type distribution;
- evidence composition;
- evidence coverage;
- model performance;
- controlled experiment results;
- governance controls;
- case selection and evidence inspection.

### Dashboard entry point

[`dashboard/index.html`](dashboard/index.html)

### Live demonstration

Enable GitHub Pages for the `dashboard/` directory and publish the dashboard as the public demonstration site.

---

# 05 — Investigation Workflow

The project explicitly separates predictive signal from investigative context.

```text
┌─────────────────────────────────────────────────────────────┐
│ 1. PAYMENT EVENT                                            │
│    Structured cross-border payment                         │
└──────────────────────────────┬──────────────────────────────┘
                               ↓
┌─────────────────────────────────────────────────────────────┐
│ 2. PAYMENT RELATIONSHIPS                                    │
│    Account-to-account payment structure                     │
└──────────────────────────────┬──────────────────────────────┘
                               ↓
┌─────────────────────────────────────────────────────────────┐
│ 3. MODEL SIGNAL                                             │
│    Frozen predictive output                                 │
└──────────────────────────────┬──────────────────────────────┘
                               ↓
┌─────────────────────────────────────────────────────────────┐
│ 4. EVIDENCE                                                 │
│    Transaction + network + behavior + model signal          │
└──────────────────────────────┬──────────────────────────────┘
                               ↓
┌─────────────────────────────────────────────────────────────┐
│ 5. INVESTIGATION CASE                                       │
│    Case + priority + evidence package                       │
└──────────────────────────────┬──────────────────────────────┘
                               ↓
┌─────────────────────────────────────────────────────────────┐
│ 6. AI-ASSISTED ANALYSIS                                     │
│    Evidence-grounded investigator support                   │
└──────────────────────────────┬──────────────────────────────┘
                               ↓
┌─────────────────────────────────────────────────────────────┐
│ 7. AUDIT TRAIL                                              │
│    Validation + provenance + governance                     │
└─────────────────────────────────────────────────────────────┘
```

---

# 06 — Project Structure & Data Dictionary

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
│   ├── index.html
│   └── README.md
│
├── docs/
│   ├── architecture.md
│   ├── business_context.md
│   ├── model_card.md
│   ├── governance.md
│   ├── investigation_workflow.md
│   ├── audience_guide.md
│   ├── build_roadmap.md
│   └── presentation_sequence.md
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
└── .github/
    └── workflows/
        ├── validate.yml
        └── pages.yml
```

## Core data domains

### Payment messages

| Domain | Examples |
|---|---|
| Message identity | Payment/message identifiers |
| Transaction identity | Transaction key |
| Timing | Authoritative creation timestamp |
| Monetary information | Amount, currency, normalized amount |
| Parties | Sender, receiver |
| Banking information | Originating / receiving institutions |
| Geographic information | Countries and related context |

### Entities

- Accounts
- Banks
- Countries

### Relationships

- Account → Payment → Account

### Context

- Payment characteristics
- Historical activity
- Network characteristics
- Supporting behavioral signals

### Evidence

- Model signal
- Transaction context
- Network context
- Behavioral context

### Investigation

- Case
- Priority
- Evidence package
- Investigation status
- Investigator workflow
- AI-assisted analysis

---

# 07 — Model Card

## Purpose

The predictive layer is intended to identify measurable signal in payment relationships and monetary characteristics within the synthetic validation environment.

## Final configuration

| Property | Final value |
|---|---|
| Model type | Payment-topology GNN |
| Predictive features | Amount + USD-equivalent amount |
| Hidden dimension | 64 |
| Dropout | 0.20 |
| Learning rate | 0.001 |
| Weight decay | 0.0001 |
| Training rows | 80,000 |
| Test rows | 20,000 |
| Matched evaluation | 20 epochs |
| Seed | 42 |
| Model status | **FROZEN** |

## Final reproducible performance

| Metric | Value |
|---|---:|
| ROC-AUC | **0.972667** |
| PR-AUC | **0.554988** |
| Precision @ 0.50 | **0.246801** |
| Recall @ 0.50 | **0.768501** |
| F1 @ 0.50 | **0.373616** |
| Brier score | **0.053497** |

These are the authoritative metrics for the persisted frozen checkpoint.

---

# 08 — Controlled Validation

The project tested whether observed payment structure carries measurable predictive information under controlled changes to the input structure.

### Matched 20-epoch results

| Condition | PR-AUC |
|---|---:|
| Actual structure | **0.780603** |
| Constant monetary input | **0.944459** |
| Shuffled monetary input | **0.943282** |
| Randomized structure | **0.718471** |
| Randomized structure + monetary input | **0.651668** |

### Key differences

**Actual structure vs randomized structure**

```text
0.780603 − 0.718471 = 0.062132
```

**Structure after monetary neutralization**

```text
0.944459 − 0.651668 = 0.292791
```

### Interpretation

The controlled experiments support an **independent predictive contribution from payment topology under the synthetic experimental design**.

This does not establish production effectiveness or imply that payment topology alone explains AML risk.

---

# 09 — Evidence & Investigation Results

For **1,000 selected investigations**, the canonical evidence layer contains:

| Measure | Result |
|---|---:|
| Canonical evidence records | **30,000** |
| Mean evidence per case | **30** |
| Median evidence per case | **30** |
| Model signal coverage | **100%** |
| Transaction context coverage | **100%** |
| Network context coverage | **100%** |
| Behavioral context coverage | **100%** |
| Minimum evidence coverage | **100%** |
| Multi-source coverage | **100%** |
| GOOD/RICH evidence coverage | **100%** |
| Explicit ground-truth contamination | **0** |

### Evidence composition

| Evidence type | Records |
|---|---:|
| Transaction context | **19,000** |
| Network context | **6,000** |
| Model signal | **3,000** |
| Behavioral context | **2,000** |

### Investigation interpretation

The evidence layer is designed so that the investigator does not receive only a model score.

```text
Model signal
+
Transaction context
+
Network context
+
Behavioral context
=
Investigation evidence package
```

### Known evidence limitation

Direct account-context coverage was **0%** in the validated retrieval population.

This limitation is disclosed explicitly. Model, transaction, network and behavioral evidence coverage remained complete for the validated cases.

---

# 10 — AI-Assisted Investigation

The downstream AI investigation component was demonstrated as a **validated prototype**.

| Measure | Result |
|---|---:|
| Intended investigations | **100** |
| Successful persisted investigations | **32** |
| Fully cited successful findings | **100%** |
| Invalid evidence citations | **0** |
| Ground-truth contamination | **0** |

The remaining workload was not completed because of API request limits.

Therefore:

> **The AI investigation component should be described as a validated prototype covering 32 persisted successful investigations, not as a completed 100-case evaluation.**

The AI layer is downstream of the canonical evidence layer and is intended to assist investigation rather than independently determine evidence.

---

# 11 — Governance, Compliance & Auditability

The project explicitly separates:

```text
Predictive signal
       ≠
Investigative context
       ≠
Validation-only ground truth
```

## Controls

| Control | Result |
|---|---|
| Temporal train/test separation | **PASS** |
| Training / test split | **80,000 / 20,000** |
| Train-only feature scaling | **PASS** |
| Frozen model checkpoint | **PASS** |
| Checkpoint SHA-256 verification | **PASS** |
| Ground-truth contamination | **0** |
| Test data used for model selection | **NO** |
| Test data used for scaling | **NO** |
| Model retrained during final validation | **NO** |
| Model weights modified during final validation | **NO** |
| API quota bypass | **NO** |

### Frozen checkpoint

```text
706b4a48c9ea6c392ed8a4b1c0e104041e7df17be592c919bf1bef2b33c35c58
```

---

# 12 — Setup, Dependencies & Reproducibility

## Environment

The project was developed and validated in Google Colab with persistent artifacts stored in Google Drive.

## Core dependencies

```text
Python
Pandas
NumPy
PyTorch
PyTorch Geometric
Plotly
IPyWidgets
```

Install from:

```bash
pip install -r requirements.txt
```

## Reproducibility principles

The repository preserves:

- explicit train/test separation;
- deterministic seed configuration;
- persisted graph artifacts;
- frozen model weights;
- validation tables;
- evidence retrieval outputs;
- case-level audits;
- checkpoint hashing;
- investigation manifests;
- final validation records.

## Data policy

Raw working datasets and model weights are intentionally excluded from the public repository by default.

See [`data/README.md`](data/README.md) for the expected artifact structure.

---

 AML / Operations review

Open:

1. [`docs/business_context.md`](docs/business_context.md)
2. [`docs/investigation_workflow.md`](docs/investigation_workflow.md)
3. [`results/case_priority.csv`](results/case_priority.csv)
4. [`results/evidence_composition.csv`](results/evidence_composition.csv)
5. [`dashboard/index.html`](dashboard/index.html)

## 30-minute technical review

Open:

1. [`notebooks/01_DATA_AND_ARCHITECTURE.ipynb`](notebooks/01_DATA_AND_ARCHITECTURE.ipynb)
2. [`notebooks/02_MODEL_AND_CONTROLLED_VALIDATION.ipynb`](notebooks/02_MODEL_AND_CONTROLLED_VALIDATION.ipynb)
3. [`docs/model_card.md`](docs/model_card.md)
4. [`results/controlled_ablation_20_epoch.csv`](results/controlled_ablation_20_epoch.csv)

## Full project review

Follow [`docs/presentation_sequence.md`](docs/presentation_sequence.md).

---

#  — Repository Validation

The repository contains automated validation under:

```text
.github/workflows/validate.yml
```

The validation layer is intended to check:

- repository structure;
- required artifacts;
- KPI consistency;
- results files;
- documentation presence.

The dashboard publication workflow is:

```text
.github/workflows/pages.yml
```

---

#  Limitations

### Synthetic environment

The payment data and validation environment are synthetic.

### Model performance

The reported frozen-model metrics should not be interpreted as production AML effectiveness.

### AI investigation scope

The AI investigation prototype covers 32 persisted successful cases rather than the intended complete 100-case workload.

### Account evidence

Direct account-context coverage is incomplete in the validated retrieval population.

### Human oversight

The system is intended to support trained investigators, not replace them.

### Regulatory use

The prototype is not a regulator-approved AML model or autonomous compliance decision system.

---

# 16 — Final Project Statement

> **Developed an evidence-grounded AML investigation architecture for cross-border SWIFT payments that combines a frozen payment-topology GNN, canonical multi-source evidence retrieval, and an LLM-assisted investigator workflow.**

The broader demonstrated workflow is:

```text
Payment data
     ↓
Payment relationships
     ↓
Frozen risk signal
     ↓
Evidence
     ↓
Investigation
     ↓
AI assistance
     ↓
Audit trail
```

The project therefore demonstrates an integrated path from structured payment information to investigator-oriented analytical support with explicit controls around evidence, model integrity, and validation.

---

# 17 — License & Citation

See:

- [`LICENSE`](LICENSE)
- [`CITATION.cff`](CITATION.cff)

---

