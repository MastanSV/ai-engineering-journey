> **As of 2026-07-05 — Week 4 · Sunday (6hr / 360 min, flexible blocks).**
> Yesterday: EDA + preprocessing + baseline LogisticRegression logged to MLflow.
> Today: regularized models + CV + full evaluation. Do micro-tasks top to bottom; never skip a Checkpoint.

# Current Task — P1 models + 5-fold CV + evaluation suite

## Block 0 — Warm-up (15 min)

- [x] 0.1 Run Anki (Week 0–2 + new cards). Note any card you fail.
- [x] 0.2 Reopen `Heart_Disease_Dataset.ipynb`; restart kernel + run all cells.
- [x] 0.3 Confirm you still have `X_train`, `X_test`, `y_train`, `y_test` (scaled + stratified) and yesterday's baseline run reproduces.

---

## Block 1 — Regularized models (150 min)

### Setup

- [x] 1.1 Import `LogisticRegression` (sklearn.linear_model) and the metric functions you'll use.

### Part A — L2 (Ridge-style)

- [x] A1 Create `LogisticRegression(penalty='l2', C=1.0)`.
- [x] A2 **Checkpoint:** `C` is the inverse of λ. To make regularization _stronger_, do you raise or lower `C`? Write 1 line.
- [x] A3 `.fit()` on training data.
- [x] A4 `.predict()` on test + `.predict_proba()` (keep the class-1 column).
- [x] A5 Print precision + ROC-AUC; jot both numbers in a markdown cell.

### Part B — L1 (Lasso-style)

- [x] B1 Create `LogisticRegression(penalty='l1', solver='liblinear')` (or `'saga'`).
- [x] B2 **Checkpoint:** why does L1 need a special solver? (One sentence — absolute-value penalty not differentiable at 0.)
- [x] B3 `.fit()`, then predict + predict_proba.
- [x] B4 Inspect `.coef_`; count how many are ~0.
- [x] B5 **Checkpoint:** list features whose coef went to ~0. Match your Lasso "feature selection" note? 1–2 sentences.
- [x] B6 Print precision + ROC-AUC; jot numbers.

### Part C — 5-fold CV

- [ ] C1 Import `cross_validate` (sklearn.model_selection).
- [ ] C2 Run on the **L2 model**: `cv=5`, `scoring=['precision','roc_auc']`.
- [ ] C3 **Checkpoint:** why CV over a single split? (One sentence — variance of the estimate.)
- [ ] C4 Compute mean AND std for each metric; write them down.
- [ ] C5 Repeat C2–C4 for the **L1 model**.
- [ ] C6 **Checkpoint:** high mean + high std tells you what? (One sentence.)

### Part D — Log to MLflow

- [ ] D1 `mlflow.set_experiment('p1-tabular-ml')`.
- [ ] D2 L2 model: `start_run()`, `log_param` (penalty, C, solver), `log_metric` (CV precision + roc_auc mean/std).
- [ ] D3 Repeat D2 for the L1 model in its own run.
- [ ] D4 Open MLflow UI; confirm both runs appear side by side.
- [ ] D5 **Checkpoint (Feynman):** 3 jargon-free sentences — which model looks better _for heart disease_ and why, given missing a sick patient is the costly error?

---

## ☕ Break (15 min)

---

## Block 2 — Evaluation suite (120 min)

### Part E — Confusion matrix

- [ ] E1 Import `confusion_matrix` + `ConfusionMatrixDisplay`.
- [ ] E2 Build the confusion matrix for the L2 model on the test set.
- [ ] E3 **Checkpoint:** in plain words, how many actually-sick patients did it label healthy (false negatives)? Why is that the number you care about most here?
- [ ] E4 Repeat E2 for the L1 model.

### Part F — Precision / recall / F1

- [ ] F1 Print `classification_report` for both models.
- [ ] F2 **Checkpoint:** for this problem, is recall or precision the metric that protects patients? Reconcile with your README (you wrote "precision first") — do you still agree, or did the numbers change your mind? 2 sentences.

### Part G — ROC curve + AUC

- [ ] G1 Import `roc_curve` + `roc_auc_score`.
- [ ] G2 Compute ROC + AUC for both models using the class-1 probabilities.
- [ ] G3 Plot both ROC curves on one axes; add the diagonal "random" line.
- [ ] G4 **Checkpoint:** what does a point in the top-left corner mean? What does the diagonal represent? 1 sentence each.

### Part H — Threshold sweep

- [ ] H1 Take your best model's class-1 probabilities. Instead of the default 0.5 cutoff, try thresholds from 0.1 to 0.9.
- [ ] H2 For each threshold, compute precision + recall.
- [ ] H3 Plot precision vs recall as the threshold moves (or print a small table).
- [ ] H4 **Checkpoint:** as you lower the threshold, which goes up and which goes down — precision or recall? Why?
- [ ] H5 Pick a threshold that fits "don't miss sick patients." Write 2 sentences justifying it in a markdown cell.

### Part I — Comparison table

- [ ] I1 Build a markdown table: rows = baseline / L2 / L1; columns = precision, recall, F1, ROC-AUC.
- [ ] I2 **Checkpoint:** did regularization beat the baseline? By how much? 1 sentence.

---

## Block 3 — Wrap + buffer (45 min)

- [ ] W1 **Feynman check:** 3 jargon-free sentences — why did the regularized model beat (or not beat) baseline here? If you can't → re-study that piece before continuing.
- [ ] W2 🚀 Commit: `week-04 day: P1 models + CV + evaluation`
- [ ] W3 End-of-day updates: `01-current-state.md` (Sun progress + NN status) and `03-active-tasks.md` (check off Sunday).
- [ ] W4 Remaining buffer: rest, or clear one Anki straggler from 0.1.

**DoD today:** 3 models logged with 5-fold CV (precision + ROC-AUC), confusion matrices, ROC curves, a justified decision threshold, and a comparison table.

> ⏱️ 20-min stuck rule active. Convergence warning on saga → think `max_iter`/scaling, don't silence blindly.
