# Repository Build Roadmap

## Step 1 — Freeze the project story

Use `00_FINAL_PROJECT_VALIDATION_AND_RESULTS.ipynb` as the canonical narrative notebook. Do not change the final model result while packaging the project.

## Step 2 — Separate evidence from presentation

Keep raw/generated datasets and model weights outside the public repository. Commit verified summary tables, documentation, and reproducible visualization code.

## Step 3 — Present the data architecture

Show the payment-message structure, entities, relationships, contextual information, predictive output, evidence layer, and investigation layer.

## Step 4 — Present model validation

Present the frozen model metrics and the matched 20-epoch controlled experiment. Treat `0.554988` PR-AUC as the final reproducible model metric.

## Step 5 — Present investigation evidence

Show the 30,000-record evidence store, the evidence composition, coverage results, case queue, and investigator workflow.

## Step 6 — Present AI assistance honestly

Show the 32 persisted successful investigations and 100% citation validity for successful cases. Clearly disclose that the 100-case target was not completed because of API limits.

## Step 7 — Present governance

Show temporal separation, frozen checkpoint integrity, ground-truth isolation, evidence contamination checks, and immutability.

## Step 8 — Build end-user views

Provide separate views for leadership, AML operations, investigators, model risk, data science, AI/engineering, and interview audiences.

## Step 9 — GitHub quality control

Run `python scripts/validate_repository.py` before committing. Confirm that the summary tables, notebook, documentation, and source package are internally consistent.

## Step 10 — Public positioning

Present the repository as an auditable research-grade proof of concept, not a production AML decision engine.
