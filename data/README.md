# Data and external artifacts

The repository intentionally does not commit the full synthetic payment environment, graph files, or model checkpoint by default.

## Local artifact root

Configure a local artifact directory containing the persisted project outputs from the original development environment.

Expected high-level assets include:

```text
data/
└── project_artifacts/
    ├── v2_2_1_behavioral_gnn/
    │   ├── temporal_heterogeneous_graph/
    │   ├── pyg_heterogeneous/
    │   ├── v2_2_5_matched_epoch_final/
    │   └── final_aml_cases/
    └── ...
```

Because the underlying dataset is synthetic, the omission is primarily for repository size, reproducibility hygiene, and separation of source code from generated artifacts.

The repository's `results/` directory contains the authoritative presentation-level summary tables required to reproduce the primary charts without exposing the full working dataset.
