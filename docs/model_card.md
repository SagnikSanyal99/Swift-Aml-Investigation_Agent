# Model Card

## Model purpose

The predictive component evaluates whether structured payment characteristics and payment relationships contain measurable information for distinguishing higher-risk synthetic payment events.

## Final configuration

| Property | Value |
|---|---|
| Model type | Payment-topology GNN |
| Predictive features | Amount; USD-equivalent amount |
| Hidden dimension | 64 |
| Dropout | 0.20 |
| Learning rate | 0.001 |
| Weight decay | 0.0001 |
| Training rows | 80,000 |
| Test rows | 20,000 |
| Matched evaluation | 20 epochs |
| Seed | 42 |
| Status | Frozen |

## Final reproducible metrics

| Metric | Result |
|---|---:|
| ROC-AUC | 0.972667 |
| PR-AUC | 0.554988 |
| Precision @ 0.50 | 0.246801 |
| Recall @ 0.50 | 0.768501 |
| F1 @ 0.50 | 0.373616 |
| Brier | 0.053497 |

## Controlled validation

At 20 matched epochs:

| Condition | PR-AUC |
|---|---:|
| A_ACTUAL | 0.780603 |
| B_CONSTANT | 0.944459 |
| C_SHUFFLED | 0.943282 |
| D_RANDOM_TOPOLOGY | 0.718471 |
| E_RANDOM_BOTH | 0.651668 |

Key differences:

- Actual structure minus randomized structure = **0.062132**
- Money-neutralized topology effect = **0.292791**

The defensible conclusion is that the controlled experiments support an independent predictive contribution from payment topology under the synthetic experimental design.

## Intended use

Research, demonstration, workflow design, analytics experimentation, and portfolio presentation.

## Not intended for

Autonomous regulatory decisions, customer adverse action, production AML case closure, or replacement of trained investigators.

## Known limitations

- Synthetic data
- Direct account-context retrieval coverage was 0% for the validated selected cases
- AI investigation was demonstrated on 32 successful persisted cases
- Production effectiveness is not established
