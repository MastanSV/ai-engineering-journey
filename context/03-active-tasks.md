# Active Tasks — Week 4 Sprint (May 18–24, 2026)

## Sprint goal

By Sunday May 24, P1 (Tabular ML w/ Engineering Rigor) is deployed on HF Spaces, passes all 6 quality-bar criteria, and the Phase 1 gate is cleared. Logistic regression teach-back addresses the Week 3 gap.

## Theme: **"Phase 1 Finish — Ship P1"**

Week 3 proved I can ship under pressure (first clean week). Week 4 proves I can ship a production-quality project that passes the recruiter-stops-scrolling test.

## Week 3 carryover (explicit)

None — all DoD items shipped.

## Time budget

- Mon–Fri: 1.5hr × 5 = 7.5hr · Sat 6hr · Sun 6hr · **Available: ~19.5hr**

## Active rules

- **30-min carryover cap:** if weekday carryover >30 min → push to Saturday, not next weekday.
- **20-min stuck rule:** if stuck >20 min on a derivation/concept → switch to a different resource (blog, different video, ask mentor). Never close laptop without trying 1 alternative.
- **Feynman learning checklist (NEW):** before marking a concept "learned," write a 3-sentence explanation with zero jargon. If you can't → re-study that piece. Only then add the Anki card.

---

## Daily breakdown

> **Self-contained rule:** every day's block contains everything needed to execute. Do NOT come back to chat to fetch a link or a prompt.

---

### Mon May 18 — Classification metrics notebook + P1 scoping (1.5hr, 9:00–10:30 PM)

**Slot plan (90 min):**

- [ ] 📝 **15 min — Anki review** (all Week 1–3 cards)
- [ ] 💻 **45 min — `daily-notebooks/week-03/08-classification-metrics.ipynb`** (create)
  - Reuse logistic model from notebook 06
  - `from sklearn.metrics import confusion_matrix, classification_report, roc_auc_score`
  - Print confusion matrix, precision, recall, F1 for the binary classifier
  - Markdown: "When would you optimize for recall over precision? Give a real example."
- [ ] 📋 **30 min — P1 project scoping**
  - **Decision:** Pick dataset + problem. Two options:
    - **(A) Classification:** Heart disease / customer churn → logistic + regularization + full metrics suite → showcases Week 2–3 skills
    - **(B) Regression:** Polish California Housing across notebooks 04-05-07 into one clean project → less new work but doesn't showcase classification
  - Write problem statement, feature list, and evaluation plan in `projects/05_P1_Tabular_ML/README.md`
  - Log choice in `04-decisions-log.md`
- [ ] 🚀 **Commit:** `week-04 day-1: classification metrics notebook + P1 scoping`

---

### Tue May 19 — P1: EDA + preprocessing (1.5hr, 9:00–10:30 PM)

**Slot plan (90 min):**

- [ ] 💻 **90 min — P1 notebook: EDA + feature engineering**
  - Load dataset, describe shape, check nulls, class balance (if classification)
  - Correlation heatmap, distribution plots
  - Preprocessing pipeline: handle missing values, encode categoricals, `StandardScaler`
  - Train/test split (80/20, `random_state=42`)
- [ ] 🚀 **Commit:** `week-04 day-2: P1 EDA + preprocessing`

---

### Wed May 20 — P1: Model training + CV (1.5hr, 9:00–10:30 PM)

**Slot plan (90 min):**

- [ ] 💻 **90 min — P1 notebook: models + hyperparameter tuning**
  - Baseline model (LogisticRegression or LinearRegression depending on P1 choice)
  - Ridge + Lasso with 5-fold CV (`cross_val_score`)
  - If classification: also try different thresholds
  - Log all runs to MLflow under experiment `p1-tabular-ml`
- [ ] 🚀 **Commit:** `week-04 day-3: P1 model training + CV`

---

### Thu May 21 — P1: Evaluation + MLflow (1.5hr, 9:00–10:30 PM)

**Slot plan (90 min):**

- [ ] 💻 **90 min — P1 notebook: evaluation suite**
  - Full metrics table: MSE/R² (regression) or confusion matrix/precision/recall/F1/AUC (classification)
  - Comparison plot: model performance side-by-side
  - Best model selection with justification (markdown cell)
  - MLflow: log final metrics + model artifact
- [ ] 🚀 **Commit:** `week-04 day-4: P1 evaluation suite`

---

### Fri May 22 — Teach-back: logistic regression (1.5hr, 9:00–10:30 PM)

**Slot plan (90 min):**

- [ ] ✍️ **75 min — NN3 Teach-back essay** → `concepts/week-04-teachback-logistic.md`
  - ≥800 words, no-Google, no AI
  - Must cover: sigmoid, log-loss, gradient derivation, decision boundary, when to use vs not use
  - Addresses retro gap #1 directly
- [ ] 🚀 **15 min — Commit:** `week-04 day-5: logistic regression teach-back`

---

### Sat May 23 — P1: Deploy + polish + Twitter (6hr)

**Slot plan (360 min):**

- [ ] 💻 **120 min — P1 Gradio app + HF Space deploy**
  - Build `app.py` with Gradio: user inputs features → model predicts
  - Push to HF Space (`mastanai/p1-tabular-ml` or similar)
  - Test the live URL
- [ ] 📝 **60 min — P1 README to quality bar**
  - Problem statement, approach, results
  - Architecture diagram (Excalidraw or hand-drawn + photo)
  - Real eval numbers table
  - Link to live HF Space
- [ ] 🎥 **30 min — Loom walkthrough** (3 min max)
  - Record, upload, embed link in README
- [ ] 🐦 **45 min — NN2 Twitter thread #5** → `twitter-posts/week-04-thread-p1.md` (create)
  - Hook: what the project does, why it matters, what you learned
  - Include screenshot of Gradio app + eval numbers
  - POST LIVE, save URL
- [ ] 📝 **30 min — Anki cards** (create `concepts/anki-cards-week-04.tsv`)
  - confusion matrix, precision, recall, F1, Gradio basics
- [ ] 🚨 **30 min — Phase 1 gate check**
  - Review all 6 quality-bar criteria against P1
  - If any criterion fails → note what's missing, fix Sunday morning
- [ ] ☕ **45 min — Buffer**

---

### Sun May 24 — Retro + Phase 2 prep (6hr)

**Slot plan (360 min):**

- [ ] 📝 **15 min — Anki review**
- [ ] 🌅 **60 min — Phase 2 prereading: PyTorch basics**
  - Video: 3Blue1Brown "Neural Networks" Chapter 1 (~20 min)
  - Read: PyTorch "60 Minute Blitz" tutorial (skim, don't code yet)
  - Output: 5 questions in `concepts/week-04-prereading.md`
- [ ] 📖 **60 min — NN5 Week 4 retro** → `weekly-logs/retro-week-04.md`
- [ ] 📋 **45 min — Week 5 plan stub** in `03-active-tasks.md` and `06-current-task.md`
- [ ] 🚀 **30 min — Update ALL context files + final commit**
  - `01-current-state.md`: Week 4 final results
  - `03-active-tasks.md`: Week 5 sprint
  - `06-current-task.md`: Monday Week 5 task
- [ ] ☕ **150 min — Buffer / curiosity bucket / rest**
