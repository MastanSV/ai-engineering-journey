# Active Tasks — Week 2 Sprint (May 4 – May 10, 2026)

## Sprint goal

By Sunday May 10, I have implemented Ridge + Lasso on California housing with a 3-way MLflow comparison, built logistic regression from scratch in numpy on a binary dataset (sigmoid + log-loss + GD + decision boundary), watched 4 StatQuest videos with notes, and shipped a teach-back essay on regularization. Two Twitter threads posted (Week 1 carryover Mon + Week 2 Sun) — NN2 must hit, no zeros.

## Theme: **"When the line isn't enough"**

Week 1 proved a line can fit. Week 2 proves a line can fit _too well_ (regularization) and that some problems aren't lines at all (classification).

## Time budget

- Mon–Fri: 9:00–10:30 PM (7.5hr) · Sat 6hr · Sun 6hr · **Target 19hr**

## Day-state tracking system

(unchanged — see `07-tracking-rules.md` for ✅ / 🔄 / ⏭️ / ❌ definitions and the 30-min carryover cap)

## Daily breakdown

### Monday May 4 — Mentor + Week 1 carryover

- [ ] 🎤 Mentor session: lock Week 2 plan + DoD
- [ ] 🐦 Post Twitter thread #3 (Week 1 carryover, NN2)
- [ ] 📝 Anki review
- [ ] 🌅 StatQuest: Ridge → 5 sentences

### Tuesday May 5 — Ridge L1 + L2

- [ ] 📚 Ridge intuition + math (L1: 5-sentence why; L2: derive ∂/∂w of MSE + λ·‖w‖²)
- [ ] 📝 3 Anki cards (Ridge, L2, standardization)
- [ ] 🌅 StatQuest: Lasso → 5 sentences

### Wednesday May 6 — Notebook 05 Part A

- [ ] 💻 `05-ridge-lasso-california.ipynb` Part A: StandardScaler + LinearRegression baseline + Ridge → MLflow
- [ ] 🚀 commit + push

### Thursday May 7 — Notebook 05 Part B + 3-way comparison

- [ ] 💻 Add Lasso run → MLflow → screenshot 3-way comparison (R², MSE, coef magnitudes)
- [ ] 📝 3 Anki cards (Lasso, L1, alpha)
- [ ] 🌅 StatQuest: Logistic Regression → 5 sentences

### Friday May 8 — Mentor: logistic L1 + L2

- [ ] 🎤 Sigmoid intuition; why log-loss not MSE for classification; derive ∂(log-loss)/∂w by hand
- [ ] 🚀 mid-week velocity check (carryover cap audit)

### Saturday May 9 — Notebook 06 + cross-val + Saturday velocity check

- [ ] 💻 `06-logistic-from-scratch.ipynb` (L3+L4): sigmoid + log-loss + GD + decision boundary
- [ ] 💻 `07-cross-validation.ipynb` (stretch): k-fold CV on California
- [ ] 📝 4 Anki cards (sigmoid, log-loss, logistic, k-fold CV)
- [ ] 🌅 StatQuest: ROC/AUC → 5 sentences
- [ ] 🚨 Saturday velocity check
- [ ] 🚀 commit + push

### Sunday May 10 — Teach-back + thread #4 + retro

- [ ] 🌅 Anki review
- [ ] ✍️ NN3 teach-back essay ≥800 words, no-Google
- [ ] 🐦 NN2 Twitter thread #4
- [ ] 📖 NN5 Week 2 retro (audit carryover-cap rule)
- [ ] 💻 Glossary fill
- [ ] 📋 Week 3 stub in `06-current-task.md`
- [ ] 🚀 final commit

## Definition of Done — Week 2

- [ ] Notebook 05 (Ridge + Lasso + standardization, 3-way MLflow)
- [ ] Notebook 06 (logistic from scratch, decision boundary)
- [ ] Notebook 07 (k-fold CV) — stretch, OK to drop
- [ ] 4 StatQuest videos × 5 sentences each
- [ ] Teach-back essay ≥800 words, no AI
- [ ] **NN2: 2 threads posted** (Mon #3, Sun #4)
- [ ] ~12 Anki cards, 7/7 daily reviews
- [ ] Week 2 retro complete with carryover-cap audit
- [ ] Glossary stubs filled

## 🚫 Out of scope

- Multiclass / softmax (Week 3)
- Decision trees / random forests (Week 3)
- Neural nets (Phase 2)
- Polynomial / interaction features

## 🎯 Curiosity bucket rule

Found something interesting mid-task → write to `concepts/curiosity-bucket.md` → keep working. Sat 30-min slot reserved for review.
