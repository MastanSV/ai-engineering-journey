> **As of 2026-07-15 — Week 5 · Tuesday (1.5hr, 9:00–10:30 PM).**
> Previous sessions (Week 4): EDA + baseline + L2/L1 models + CV + MLflow + confusion matrix + classification report done.
> Today: finish evaluation suite (ROC curve, threshold sweep, comparison table).

# Current Task — Finish P1 Evaluation Suite

## Block 0 — Warm-up (15 min)

- [ ] 0.1 Run Anki (Week 0–3 + any new cards). Note any card you fail.
- [ ] 0.2 Reopen `Heart_Disease_Dataset.ipynb`; restart kernel + run all cells to restore state.
- [ ] 0.3 Confirm `y_pred_l2`, `y_pred_l1`, and `positive_scores` variables are live.

---

## Block 1 — Part G: ROC curve + AUC (30 min)

- [ ] G1 Import `roc_curve` + `roc_auc_score` (already imported — confirm).
- [ ] G2 Compute ROC (fpr, tpr, thresholds) for both models using the class-1 probabilities.
- [ ] G3 Plot both ROC curves on one axes; add the diagonal "random" line. Label each curve with its AUC score.
- [ ] G4 **Checkpoint:** what does a point in the top-left corner mean? What does the diagonal represent? 1 sentence each.

---

## Block 2 — Part H: Threshold sweep (30 min)

- [ ] H1 Take your best model's class-1 probabilities. Instead of the default 0.5 cutoff, try thresholds from 0.1 to 0.9 (step 0.1).
- [ ] H2 For each threshold, compute precision + recall.
- [ ] H3 Plot precision vs recall as the threshold moves (or print a small table).
- [ ] H4 **Checkpoint:** as you lower the threshold, which goes up and which goes down — precision or recall? Why?
- [ ] H5 Pick a threshold that fits "don't miss sick patients." Write 2 sentences justifying it in a markdown cell.

---

## Block 3 — Part I: Comparison table + wrap (15 min)

- [ ] I1 Build a markdown table: rows = baseline / L2 / L1; columns = precision, recall, F1, ROC-AUC.
- [ ] I2 **Checkpoint:** did regularization beat the baseline? By how much? 1 sentence.
- [ ] W1 🚀 Commit: `week-05: P1 evaluation suite complete`
- [ ] W2 End-of-day update: `01-current-state.md` (mark Tue done).

**DoD today:** ROC curves plotted, threshold selected with justification, comparison table complete. Evaluation suite closed.

> ⏱️ 20-min stuck rule active. If ROC plot code trips you up, check: are you passing probabilities (not predictions) to roc_curve?
