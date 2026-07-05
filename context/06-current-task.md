> **As of 2026-07-05 — Week 4 · Sunday (6hr / 360 min, flexible blocks).**
> Yesterday: EDA + preprocessing + baseline LogisticRegression logged to MLflow. Today: regularized models + CV + full evaluation.

# Current Task — P1 models + 5-fold CV + evaluation suite

## Block 0 — Warm-up (15 min)

- [ ] Anki review (Week 0–2 + any new cards). Note stragglers.
- [ ] Reopen `Heart_Disease_Dataset.ipynb`; confirm yesterday's split + baseline run still reproduce.

## Block 1 — Regularized models (150 min)

- [ ] Fit **L2 (Ridge-style)** LogisticRegression — recall the `penalty` + `C` params (remember: `C` is the _inverse_ of λ, so small `C` = strong regularization). Think through what that means before you set it.
- [ ] Fit **L1 (Lasso-style)** LogisticRegression — needs a solver that supports L1 (`liblinear` or `saga`). After fitting, inspect which coefficients went to (near) zero → tie back to your Lasso "feature selection" note.
- [ ] **5-fold CV** with `cross_val_score` / `cross_validate`. Score on **precision** and **roc_auc** (per your eval plan), not just accuracy — the class balance you found yesterday tells you why accuracy alone lies.
- [ ] Log every run to MLflow experiment `p1-tabular-ml`: params (`penalty`, `C`, solver) + CV mean/std of each metric.

> ⏱️ 20-min stuck rule: if a solver error or convergence warning blocks you >20 min, switch approach (scale check? different solver? `max_iter`?) — don't freeze.

## ☕ Break (15 min)

## Block 2 — Evaluation suite (120 min)

- [ ] Confusion matrix for each model on the test set — read it in plain language (how many sick patients missed?).
- [ ] Precision, recall, F1 (`classification_report`).
- [ ] ROC curve + AUC (`roc_curve`, `roc_auc_score`); plot the curves together.
- [ ] **Threshold sweep:** vary the decision threshold, watch precision vs recall trade off. Pick a threshold that matches your "precision-first / missing a sick patient is costly" reasoning — and justify it in a markdown cell.
- [ ] **Comparison table (markdown):** baseline vs L2 vs L1, side by side on precision / recall / F1 / ROC-AUC.

## Block 3 — Wrap + buffer (45 min)

- [ ] Feynman check: in 3 jargon-free sentences, why did the regularized model beat (or not beat) the baseline here? If you can't → re-study before moving on.
- [ ] 🚀 Commit: `week-04 day: P1 models + CV + evaluation`
- [ ] End-of-day: update `01-current-state.md` (Sun progress + NN status) and `03-active-tasks.md` (check off Sunday).

**DoD today:** 3 models logged to MLflow with 5-fold CV precision + ROC-AUC, a comparison table, and a justified decision threshold.
