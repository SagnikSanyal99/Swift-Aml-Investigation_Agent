# Governance, Compliance & Ethics

## Separation of information roles

The project separates:

1. predictive model signal;
2. post-hoc investigative context;
3. validation-only synthetic ground truth;
4. investigation priority and workflow.

This reduces the risk of treating validation labels as operational evidence.

## Reproducibility controls

- Strict temporal separation
- Train-only scaling
- Frozen checkpoint
- Checkpoint SHA-256 verification
- Persisted validation tables
- Evidence-store audit
- Retrieval traces
- Case-level quality audit
- Explicit API limitation disclosure

## Frozen checkpoint

```text
706b4a48c9ea6c392ed8a4b1c0e104041e7df17be592c919bf1bef2b33c35c58
```

## Ethics

A risk score is not proof of financial crime. Investigators must review supporting evidence before any consequential action. False positives, customer impact, privacy, and fairness require additional assessment before any real-world deployment.

## AI safeguards

AI-assisted narratives must remain traceable to retrieved evidence. The AI component is assistance, not an autonomous compliance authority.

## Disclaimer

This repository is an auditable research-grade proof of concept using synthetic data. It is not a production AML monitoring platform, regulator-approved model, or autonomous financial-crime decision system.
