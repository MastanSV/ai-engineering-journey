> **As of 2026-07-04 — Week 4 · Saturday (RESUME day, 6hr / 360 min, flexible blocks).**
> Journey paused ~May 20, resumed today. Front-load a refresher, then resume P1.

# Current Task — Refresh + resume P1 (finish EDA → baseline model)

## Block 1 — Env + memory warm-up (45 min)

- [ ] 10 min — Env check: activate `.venv`, test-import numpy/pandas/sklearn/matplotlib/mlflow. Fix anything broken first.
- [ ] 35 min — Re-read own notes: `concepts/week-02-prereading.md` (Ridge/Lasso + logistic Q&A) + `concepts/week-02-teachback-regularization.md`.

## Block 2 — Reactivate recall (60 min)

- [ ] 30 min — Anki: run all Week 0–2 decks. Note failed cards → teach-back weak spots for Tue.
- [ ] 30 min — Rerun notebooks 05 (ridge/lasso), 06 (logistic), 07 (CV) top-to-bottom.

## Block 3 — Re-enter P1 (15 min)

- [ ] Re-read `projects/05_P1_Tabular_ML/README.md`; open `Heart_Disease_Dataset.ipynb`; find where you stopped.

## ☕ Break (15 min)

## Block 4 — Finish EDA + preprocessing (120 min) [completes Day-2 leftover]

- [ ] Load `heart.csv`; shape, `df.info()`, `df.describe()`, null check
- [ ] Class balance of `target` (0/1) — decides if accuracy is misleading
- [ ] Correlation heatmap + distribution plots
- [ ] Encoding decision (true categoricals vs encoded ints) + `StandardScaler` (recall WHY Ridge/Lasso need it)
- [ ] Train/test split: 80/20, `random_state=42`, `stratify=y` (think through why)

## Block 5 — Baseline model + MLflow (90 min)

- [ ] Fit plain `LogisticRegression` baseline; predictions
- [ ] Compute precision first (+ recall, F1, confusion matrix) — reuse `week-04/01-classification-metrics.ipynb`
- [ ] MLflow experiment `p1-tabular-ml`: log params + baseline metrics as reference run

## Wrap (15 min)

- [ ] 🚀 Commit: `week-04 resume: P1 EDA + preprocessing + baseline model`
- [ ] Update `01-current-state.md` + `03-active-tasks.md` end-of-day

**DoD today:** clean stratified split done, one logged MLflow baseline run, precision computed.

> ⏱️ 20-min stuck rule active. Feynman checklist applies before any new Anki card.
