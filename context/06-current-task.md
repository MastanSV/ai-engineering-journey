> **As of 2026-07-15 — Week 5 · Wednesday (1.5hr, 9:00–10:30 PM).**
> Previous session (Tue): ROC curves plotted, threshold sweep done (needs fixes), comparison report printed.
> Today: fix Tue carryover, pick best model, MLflow finalize, Feynman check.

# Current Task — Best-Model Selection + MLflow Finalize

## Block 0 — Warm-up (15 min)

- [x] 0.1 Run Anki (Week 0–4 cards). Note any card you fail.
- [x] 0.2 Reopen `Heart_Disease_Dataset.ipynb`; restart kernel + run all cells to restore state.
- [x] 0.3 Confirm `y_pred_l2`, `y_pred_l1`, `y_proba_l2`, `y_proba_l1` are live.

---

## Block 1 — Tuesday Carryover Fixes (15 min)

- [x] F1 In the threshold sweep cell: rename `df = pd.DataFrame(results)` → `threshold_df = ...` (you overwrote your original DataFrame).
- [x] F2 Re-pick your threshold: goal is "don't miss sick patients" = maximize recall → threshold should be **below** 0.5 (e.g., 0.3). Look at your table and pick.
- [x] F3 Rewrite the justification markdown: remove the "below 0.5 = random" claim. A low threshold is a cautious screening policy, not random guessing.
- [x] F4 Explain baseline = L2: check sklearn's default `penalty` and `C` for `LogisticRegression()`. Write 1 sentence in that markdown cell.
- [x] F5 **Checkpoint:** re-run the threshold cell + comparison cell to confirm no errors.

---

## Block 2 — Part I: Comparison Table (15 min)

- [x] I1 Build a markdown cell with a proper table: rows = Baseline / L2 / L1; columns = Precision, Recall, F1, ROC-AUC. Fill with actual numbers from your runs.
- [x] I2 **Checkpoint:** did regularization beat the baseline? (Hint: baseline IS L2 with same params.) Write 1 sentence.

---

## Block 3 — Best-Model Selection + MLflow (45 min)

- [ ] M1 Compare L1 vs L2: which has higher recall? Higher ROC-AUC? Write 2 sentences justifying your pick (recall-first logic).
- [ ] M2 Create a final MLflow run (`run_name='best_model_final'`). Log: penalty, C, solver, precision, recall, F1, ROC-AUC.
- [ ] M3 Log the model artifact: `mlflow.sklearn.log_model(your_best_pipeline, "model")`.
- [ ] M4 **Checkpoint:** open MLflow UI (`mlflow ui`), verify the run appears with all metrics + artifact.

---

## Block 4 — Feynman Check + Commit (10 min)

- [ ] FE1 Write 3 jargon-free sentences: "Why did/didn't regularization beat the baseline for heart disease?" (in a markdown cell or `concepts/` file).
- [ ] W1 🚀 Commit: `week-05: P1 best-model selected + MLflow finalized`
- [ ] W2 End-of-day update: `01-current-state.md`, `03-active-tasks.md`, `06-current-task.md`.

**DoD today:** Tue fixes applied, comparison table complete, best model justified + logged in MLflow with artifact, Feynman check done.

> ⏱️ 20-min stuck rule active. If `mlflow.sklearn.log_model` gives errors, check: is the pipeline fitted? Are you inside a `with mlflow.start_run():` block?
