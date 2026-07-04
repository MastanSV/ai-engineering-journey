# Active Tasks — Week 4 Sprint (RE-ANCHORED: Jul 4–12, 2026)

## Sprint goal

Finish and ship P1 (Heart Disease classification, Tabular ML w/ engineering rigor) on HF Spaces, passing all 6 quality-bar criteria and clearing the Phase 1 gate. Logistic teach-back closes the Week 3 gap.

## Theme: **"Phase 1 Finish — Ship P1"**

## Resume context

- Paused ~May 20 (after Week 4 Day 2), resumed Jul 4. Today = **Week 4 · Saturday**.
- Days 1–2 (pre-pause): ✅ classification-metrics notebook + P1 scoping; 🔄 P1 EDA started.

## P1 decision (logged Day 1)

**Option A — Heart Disease classification.** Dataset `heart.csv` (14-feature subset, target 0/1). Primary metric **precision** (false negative = missed sick patient) + **ROC-AUC**. Approach: Logistic Regression with Ridge/Lasso regularization. Scope in `projects/05_P1_Tabular_ML/README.md`.

## Time budget (re-anchored)

- Sat 6hr · Sun 6hr · Mon–Fri 1.5hr × 5 = 7.5hr · **Available: ~19.5hr**

## Active rules

- **30-min carryover cap:** weekday carryover >30 min → push to Saturday, not next weekday.
- **20-min stuck rule:** stuck >20 min → switch resource. Never close laptop without trying 1 alternative.
- **Feynman learning checklist:** before marking a concept "learned," write a 3-sentence zero-jargon explanation. If you can't → re-study. Only then add the Anki card.

---

## Daily breakdown

> **Self-contained rule:** every day's block contains everything needed to execute.

---

### Sat Jul 4 — RESUME: refresh + finish EDA + baseline (6hr) → see `06-current-task.md`

- [ ] Warm-up review (notes + Anki + rerun notebooks 05–07) — 105 min
- [ ] Finish P1 EDA + preprocessing (class balance, heatmap, encode/scale, stratified 80/20 split) — 120 min
- [ ] P1 baseline LogisticRegression + precision/recall/F1/confusion matrix + MLflow reference run — 90 min
- [ ] 🚀 Commit: `week-04 resume: P1 EDA + preprocessing + baseline model`

---

### Sun Jul 5 — P1 models + CV + evaluation (6hr)

- [ ] 15 min — Anki review
- [ ] 150 min — Regularized models: LogisticRegression with L2 (Ridge) and L1 (Lasso) penalties; 5-fold CV (`cross_val_score`, scoring on precision + ROC-AUC). Log each run to MLflow `p1-tabular-ml`
- [ ] 120 min — Evaluation suite: confusion matrix, precision/recall/F1, ROC curve + AUC, threshold sweep (precision-first per eval plan); side-by-side comparison table baseline vs Ridge vs Lasso
- [ ] 45 min — Buffer
- [ ] 🚀 Commit: `week-04 day: P1 models + CV + evaluation`

---

### Mon Jul 6 — Best-model selection + MLflow finalize (1.5hr, 9:00–10:30 PM)

- [ ] 15 min — Anki review
- [ ] 60 min — Pick best model (justify in markdown against precision/ROC-AUC); log final metrics + model artifact to MLflow
- [ ] 15 min — 🚀 Commit: `week-04 day: P1 best-model selection`

---

### Tue Jul 7 — Logistic teach-back (part 1) (1.5hr, 9:00–10:30 PM)

- [ ] 75 min — Start `concepts/week-04-teachback-logistic.md` (no-Google, no-AI): sigmoid, log-loss, gradient derivation
- [ ] 15 min — 🚀 Commit: `week-04 day: logistic teach-back part 1`

---

### Wed Jul 8 — Finish teach-back + Anki (1.5hr, 9:00–10:30 PM)

- [ ] 60 min — Finish teach-back (decision boundary, when to use vs not; ≥800 words total)
- [ ] 20 min — Create `concepts/anki-cards-week-04.tsv` (confusion matrix, precision, recall, F1, ROC-AUC, sigmoid, log-loss) — apply Feynman check first
- [ ] 10 min — 🚀 Commit: `week-04 day: teach-back complete + anki`

---

### Thu Jul 9 — Gradio app (1.5hr, 9:00–10:30 PM)

- [ ] 75 min — Build `projects/05_P1_Tabular_ML/app.py`: feature inputs → best model → prediction + probability
- [ ] 15 min — 🚀 Commit: `week-04 day: P1 gradio app`

---

### Fri Jul 10 — HF Space deploy (1.5hr, 9:00–10:30 PM)

- [ ] 75 min — Push to HF Space (`mastanai/p1-tabular-ml`); add `requirements.txt`; test live URL
- [ ] 15 min — 🚀 Commit: `week-04 day: P1 deployed to HF Space`

---

### Sat Jul 11 — Polish + Twitter + Phase 1 gate (6hr)

- [ ] 60 min — README to quality bar: problem, approach, results table (real numbers), architecture diagram, live HF link
- [ ] 30 min — Loom walkthrough (≤3 min), embed in README
- [ ] 45 min — NN2 Twitter thread #5 → `twitter-posts/week-04-thread-p1.md` (hook + app screenshot + eval numbers). POST LIVE, save URL
- [ ] 30 min — Anki review
- [ ] 45 min — Phase 1 gate check: all 6 quality-bar criteria vs P1; note gaps
- [ ] 150 min — Buffer / fix gate gaps
- [ ] 🚀 Commit: `week-04: P1 shipped + thread + gate check`

---

### Sun Jul 12 — Retro + Phase 2 prep (6hr)

- [ ] 15 min — Anki review
- [ ] 60 min — NN5 Week 4 retro → `weekly-logs/retro-week-04.md`
- [ ] 60 min — Phase 2 prereading (PyTorch basics: 3B1B NN Ch.1 + PyTorch 60-min blitz skim) → 5 questions in `concepts/week-04-prereading.md`
- [ ] 45 min — Week 5 plan stub in `03-active-tasks.md` + `06-current-task.md`
- [ ] 30 min — Update ALL context files + final commit
- [ ] 150 min — Buffer / curiosity bucket / rest
