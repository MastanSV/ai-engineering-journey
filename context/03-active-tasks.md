# Active Tasks — Week 5 Sprint (Jul 15–20, 2026)

## Sprint goal

Finish and ship P1 (Heart Disease classification, Tabular ML w/ engineering rigor) on HF Spaces, passing all 6 quality-bar criteria and clearing the Phase 1 gate.

## Theme: **"Ship P1 + Close Phase 1 Gate"**

## Context

- Week 4 completed: EDA, preprocessing, baseline, L2/L1 models, 5-fold CV, MLflow logging, confusion matrix, classification report, recall-vs-precision reconciliation.
- Week 5 carries the remaining P1 delivery tasks (evaluation finish, teach-back, app, deploy, polish).

## P1 decision (logged Week 4 Day 1)

**Heart Disease classification.** Dataset `heart.csv` (14-feature subset, target 0/1). Primary metric **recall** (false negative = missed sick patient) + **ROC-AUC**. Approach: Logistic Regression with Ridge/Lasso regularization. Scope in `projects/05_P1_Tabular_ML/README.md`.

## Time budget

- Mon (done) | Tue–Fri 1.5hr × 4 = 6hr | Sat–Sun 6hr × 2 = 12hr | **Available: 18hr**

## Active rules

- **30-min carryover cap:** weekday carryover >30 min → push to Saturday, not next weekday.
- **20-min stuck rule:** stuck >20 min → switch resource. Never close laptop without trying 1 alternative.
- **Feynman learning checklist:** before marking a concept "learned," write a 3-sentence zero-jargon explanation. If you can't → re-study. Only then add the Anki card.

---

## Daily breakdown

> **Self-contained rule:** every day's block contains everything needed to execute.

---

### ✅ Mon Jul 14 — DONE

---

### Tue Jul 15 (1.5hr, 9:00–10:30 PM) — Finish evaluation suite

- [ ] 15 min — Anki review
- [ ] 60 min — Part G (ROC curve + AUC for both models, plot on one axes) + Part H (threshold sweep: precision vs recall at thresholds 0.1–0.9, pick recall-protecting threshold)
- [ ] 15 min — Part I (markdown comparison table: baseline / L2 / L1 × precision, recall, F1, ROC-AUC)
- [ ] 🚀 Commit: `week-05: P1 evaluation suite complete`

---

### Wed Jul 16 (1.5hr, 9:00–10:30 PM) — Best-model selection + MLflow finalize

- [ ] 15 min — Anki review
- [ ] 45 min — Pick best model (justify in markdown: recall-first + ROC-AUC); log final metrics + model artifact (`mlflow.sklearn.log_model`)
- [ ] 20 min — Feynman check: 3 jargon-free sentences (why regularized model did/didn't beat baseline for heart disease)
- [ ] 10 min — 🚀 Commit: `week-05: P1 best-model selected + MLflow finalized`

---

### Thu Jul 17 (1.5hr, 9:00–10:30 PM) — Logistic teach-back (part 1)

- [ ] 15 min — Anki review
- [ ] 75 min — Start `concepts/week-04-teachback-logistic.md` (no-Google, no-AI): sigmoid function, log-loss derivation, gradient update rule
- [ ] 🚀 Commit: `week-05: logistic teach-back part 1`

---

### Fri Jul 18 (1.5hr, 9:00–10:30 PM) — Finish teach-back + Anki cards

- [ ] 60 min — Finish teach-back: decision boundary, when logistic regression works/fails, regularization's role (≥800 words total)
- [ ] 20 min — Create `concepts/anki-cards-week-04.tsv` (confusion matrix, precision, recall, F1, ROC-AUC, sigmoid, log-loss, threshold) — Feynman check each card
- [ ] 10 min — 🚀 Commit: `week-05: teach-back complete + anki cards`

---

### Sat Jul 19 (6hr) — Gradio app + HF Space deploy

- [ ] 15 min — Anki review
- [ ] 120 min — Build `projects/05_P1_Tabular_ML/app.py`: feature inputs → best model pipeline → prediction + probability display
- [ ] 30 min — Local test (run `gradio app.py`, test edge cases)
- [ ] 90 min — Push to HF Space (`mastanai/p1-tabular-ml`); add `requirements.txt`; verify live URL works
- [ ] 30 min — Buffer / fix deployment issues
- [ ] 🚀 Commit: `week-05: P1 Gradio app deployed on HF Space`

---

### Sun Jul 20 (6hr) — Polish + ship + gate check + retro

- [ ] 60 min — README to quality bar: problem statement, approach, results table (real numbers), architecture diagram (Excalidraw), live HF link
- [ ] 30 min — Loom walkthrough (≤3 min), embed in README
- [ ] 45 min — Twitter thread #5 → `twitter-posts/week-05-thread-p1.md` (hook + app screenshot + eval numbers). POST LIVE, save URL
- [ ] 30 min — Anki review
- [ ] 45 min — Phase 1 gate check: all 6 quality-bar criteria vs P1; note gaps
- [ ] 60 min — Week 5 retro → `weekly-logs/retro-week-05.md`
- [ ] 30 min — Phase 2 prereading (skim Week 6 plan: DL + Transformers)
- [ ] 🚀 Commit: `week-05: P1 shipped + thread + Phase 1 gate cleared`
