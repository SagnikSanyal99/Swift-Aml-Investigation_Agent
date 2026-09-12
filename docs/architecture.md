# Project Structure & Data Architecture

```text
Cross-Border SWIFT AML Investigation
│
├── 1. Payment Messages
│   ├── Message identity
│   ├── Transaction identity
│   ├── Timestamp
│   ├── Currency
│   ├── Amount
│   ├── Sender
│   ├── Receiver
│   ├── Ordering / beneficiary information
│   └── Banking information
│
├── 2. Entities
│   ├── Accounts
│   ├── Banks
│   └── Countries
│
├── 3. Relationships
│   └── Account → Payment → Account
│
├── 4. Behavioral / Transaction Context
│   ├── Payment characteristics
│   ├── Historical activity
│   ├── Network characteristics
│   └── Supporting contextual signals
│
├── 5. Predictive Layer
│   └── Frozen payment-topology GNN
│
├── 6. Evidence Layer
│   ├── Model signal
│   ├── Transaction context
│   ├── Network context
│   └── Behavioral context
│
└── 7. Investigation Layer
    ├── Case
    ├── Priority
    ├── Evidence package
    ├── Investigator workflow
    └── AI-assisted analysis
```

## Data scale

| Component | Count |
|---|---:|
| Payment edges | 100,000 |
| Training edges | 80,000 |
| Test edges | 20,000 |
| Account nodes | 36,979 |
| Bank nodes | 150 |
| Country nodes | 15 |
