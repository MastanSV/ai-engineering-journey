# Current Task — Week 2 Sprint (May 4 – May 10, 2026)

> **Replace this file at the start of every new chat session/topic.**

## This week's mission

**When the line isn't enough.** Add regularization (Ridge + Lasso) to the California housing model, then build logistic regression from scratch for binary classification. By Sun May 10: 3-way MLflow comparison (vanilla / Ridge / Lasso), logistic regression in raw numpy with decision boundary plot, and a teach-back essay on regularization.

## Status going into Week 2

- ✅ Week 1 closed — 4/4 notebooks, teach-back 7.5/10, retro 8/10
- ⚠️ NN2 Twitter thread #3 carried into Week 2 (post Mon evening)
- 📋 New rule active: **30-min carryover cap** (`04-decisions-log.md` 2026-05-03)
- 📋 Calibration: **2 days budgeted per from-scratch notebook** (Week 1 lesson)

## Carryover from Week 1

- [ ] Twitter thread #3 → post Mon May 4
- [ ] Bias-variance precise definitions → fold into regularization intuition
- [ ] Standardize features before comparing coefficients → Week 2 prerequisite (Tue/Wed)
- [ ] Residual plots — when they earn their keep → fold into Sat diagnostics
- [ ] Normal Equation derivation → if time permits, mid-week curiosity slot

## Time budget

- Mon–Fri: **9:00–10:30 PM** (1.5hr × 5 = 7.5hr)
- Sat: **6hr**, Sun: **6hr**
- Target: **19hr**

## Daily breakdown

### Mon May 4 — Mentor + Week 1 carryover (1.5hr)

- [ ] 🎤 30 min — Mentor: confirm Week 2 plan + DoD
- [ ] 🐦 30 min — Twitter thread #3 (Week 1 linreg) — clears NN2 carryover
- [ ] 📝 15 min — Anki review
- [ ] 🌅 15 min — StatQuest: Ridge intuition → 5 sentences

### Tue May 5 — Ridge L1 + L2 (1.5hr)

- [ ] 📚 60 min — Ridge intuition (why L2 shrinks weights, why standardize first) + math (∂/∂w of MSE + λ·‖w‖²)
- [ ] 📝 15 min — 3 Anki cards (Ridge, L2, standardization)
- [ ] 🌅 15 min — StatQuest: Lasso → 5 sentences

### Wed May 6 — Notebook 05 Part A (1.5hr)

- [ ] 💻 75 min — `daily-notebooks/week-02/05-ridge-lasso-california.ipynb`
  - Load California → `StandardScaler` → fit `LinearRegression` (baseline) + `Ridge`
  - MLflow runs logged (params, metrics, model)
- [ ] 🚀 15 min — commit + push

### Thu May 7 — Notebook 05 Part B + comparison (1.5hr)

- [ ] 💻 60 min — Add `Lasso` → log to MLflow → 3-way comparison (R², MSE, coef magnitudes); screenshot UI
- [ ] 📝 15 min — 3 Anki cards (Lasso, L1, alpha/λ)
- [ ] 🌅 15 min — StatQuest: Logistic Regression → 5 sentences

### Fri May 8 — Mentor: logistic L1 + L2 (1.5hr)

- [ ] 🎤 75 min — Sigmoid intuition, why log-loss not MSE for classification, derive ∂(log-loss)/∂w by hand
- [ ] 🚀 15 min — log notes; **mid-week velocity check**

### Sat May 9 — Notebook 06 + cross-val (6hr)

- [ ] 💻 180 min — `06-logistic-from-scratch.ipynb` (L3 + L4): sigmoid, log-loss, gradient, GD loop on binary dataset; decision boundary plot
- [ ] 💻 90 min — `07-cross-validation.ipynb` (stretch): k-fold CV on California; compare to single 80/20
- [ ] 📝 30 min — 4 Anki cards (sigmoid, log-loss, logistic, k-fold CV)
- [ ] 🌅 30 min — StatQuest: ROC/AUC → 5 sentences
- [ ] 🚀 30 min — commit + push
- [ ] 🚨 30 min — **Saturday velocity check** (audit carryover-cap rule)
- [ ] ☕ 30 min — buffer / curiosity bucket review

### Sun May 10 — Teach-back + retro + Week 3 stub (6hr)

- [ ] 🌅 15 min — Anki review (all cards)
- [ ] ✍️ 120 min — **NN3 teach-back** ≥800 words, no-Google: "Regularization explained to my non-technical friend"
- [ ] 🐦 45 min — **NN2 Twitter thread #4** (5–7 tweets; image: 3-way MLflow comparison or decision boundary)
- [ ] 📖 60 min — **NN5 Week 2 retro** (template) — first retro under the 30-min cap; report whether it held
- [ ] 💻 60 min — Glossary fill (regularization, L1, L2, Ridge, Lasso, sigmoid, log-loss, logistic, ROC, AUC, k-fold CV, decision boundary)
- [ ] 📋 30 min — Write Week 3 stub in this file
- [ ] 🚀 30 min — final commit + push
- [ ] ☕ 30 min — buffer

## Definition of Done — Week 2

- [ ] Notebook 05 (Ridge + Lasso + standardization, 3-way MLflow)
- [ ] Notebook 06 (logistic from scratch, decision boundary)
- [ ] Notebook 07 (k-fold CV) — stretch
- [ ] 4 StatQuest videos × 5 sentences (Ridge, Lasso, Logistic, ROC/AUC)
- [ ] Teach-back essay ≥800 words, no-Google
- [ ] **NN2: 2 threads posted** (Mon #3, Sun #4) — no zeros this week
- [ ] ~12 new Anki cards, 7/7 reviews
- [ ] Week 2 retro with carryover-cap audit
- [ ] Glossary stubs filled

## Out of scope (resist)

- Multiclass / softmax (Week 3)
- Decision trees / random forests (Week 3)
- Neural nets (Phase 2)
- Polynomial / interaction features

## Active rules

- 30-min carryover cap (NEW — Week 2 experiment)
- Layered learning method (L1→L4)
- 3-state day tracking (✅ / 🔄 / ⏭️)
- Velocity check on Saturday
- 9:00–10:30 PM weekday slot is sacred
- No 10/10 self-scores
