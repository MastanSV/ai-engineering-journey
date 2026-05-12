# Active Tasks — Week 3 Sprint (May 11–17, 2026)

## Sprint goal

By Sunday May 17, I have built logistic regression from scratch in numpy (sigmoid + log-loss + GD + decision boundary), shipped the regularization teach-back essay (≥800 words, no AI), posted Twitter thread #4, implemented k-fold CV on California housing, and written an honest retro. The 20-min stuck rule must be tested at least once.

## Theme: **"Classification shipped"**

Week 2 proved I can learn regularization on weekdays. Week 3 proves I can ship the logistic regression notebook that froze me — and catch up on 3 missed NNs.

## Week 2 carryover (explicit)

| Item                                | Original day | Why it slipped                  | Landing day       |
| ----------------------------------- | ------------ | ------------------------------- | ----------------- |
| Logistic derivation (L2 math)       | Fri May 8    | Video-question mismatch → froze | Tue May 12        |
| Notebook 06 (logistic from scratch) | Sat May 9    | Couldn't derive → closed laptop | Wed–Thu May 13–14 |
| Teach-back essay (regularization)   | Sun May 10   | Sun/Mon skipped entirely        | Fri May 15        |
| Twitter thread #4                   | Sun May 10   | Sun/Mon skipped entirely        | Sat May 16        |
| Notebook 07 (k-fold CV)             | Sat May 9    | Blocked by notebook 06          | Sat May 16        |
| Glossary fill                       | Sun May 10   | Sun skipped                     | Sat May 16        |

## Time budget

- Mon: 0hr (missed — travel) · Tue–Fri: 9:00–10:30 PM (6hr) · Sat 6hr · Sun 6hr · **Available: ~18hr**

## Active rules

- **30-min carryover cap:** if weekday carryover >30 min → push to Saturday, not next weekday.
- **20-min stuck rule (NEW):** if stuck >20 min on a derivation/concept → switch to a different resource (blog, different video, ask mentor). Never close laptop without trying 1 alternative.

---

## Daily breakdown

> **Self-contained rule:** every day's block contains everything needed to execute. Do NOT come back to chat to fetch a link or a prompt.

---

### Mon May 11 — ❌ Skipped (travelling)

---

### Tue May 12 — Retro + logistic derivation + Anki (1.5hr, 9:00–10:30 PM)

**Slot plan (90 min):**

- [ ] ✅ 📖 **15 min — Commit Week 2 retro** (`weekly-logs/retro-week-02-logisticreg.md`)
  - Retro is written. Commit immediately → break the 3-day streak gap.
- [ ] 📝 **15 min — Add 4 Anki cards** to `concepts/anki-cards-week-02.tsv`:
  - Sigmoid function — what does it take as input? | Sigmoid takes log-odds (z = w·x + b), NOT odds. σ(z) = 1/(1+e^(-z)). σ(0)=0.5, σ(large+)→1, σ(large−)→0. | week-02 logistic-regression
  - Log-loss formula and why it exists | L = −[y·log(p) + (1−y)·log(1−p)]. Punishes confident wrong predictions harshly. Log-loss IS negative log-likelihood from MLE. | week-02 logistic-regression
  - Decision boundary — precise definition | The line (or hyperplane) where p = 0.5, i.e., where w·x + b = 0. One side → class 1, other side → class 0. | week-02 logistic-regression
  - Why is logistic regression called "regression"? | The model regresses a continuous probability (0 to 1). Classification (threshold at 0.5) is a separate step AFTER. Core output is probability, not a class label. | week-02 logistic-regression
- [ ] ✍️ **45 min — Logistic L2 derivation on paper** → write up in `concepts/week-02-prereading.md` under new heading "### Logistic L2 — derivation"
  - **Step 1:** Sigmoid derivative. Start from `σ(z) = 1/(1+e^(-z))`. Use quotient rule. Target: `σ'(z) = σ(z)·(1 − σ(z))`
  - **Step 2:** Write log-loss: `L = −[y·log(p) + (1−y)·log(1−p)]` where `p = σ(w·x + b)`
  - **Step 3:** Chain rule: `∂L/∂w = ∂L/∂p · ∂p/∂z · ∂z/∂w`. Work each piece.
  - **Step 4:** Final answer should simplify to: `∂L/∂w = (p − y)·x`
  - **Sanity check:** if `p > y` (overpredicted), gradient is positive → `w` decreases. ✅
  - **🚨 20-min stuck rule:** If you can't get past Step 1 in 20 min, read this blog: https://eli.thegreenplace.net/2016/the-softmax-function-and-its-derivative/ (only the sigmoid section). Then retry.
- [ ] 🚀 **15 min — Commit + push + update context files**
  - Commit message: `week-03 day-2: retro committed, logistic derivation, 4 anki cards`
  - Update `01-current-state.md` Week 3 progress row for Tue

---

### Wed May 13 — Notebook 06 Part A: sigmoid + log-loss (1.5hr, 9:00–10:30 PM)

**Slot plan (90 min):**

- [ ] 💻 **75 min — `daily-notebooks/week-02/06-logistic-from-scratch.ipynb`** (create file; no sklearn for the model)
  - **Cell 1 — imports:**
    ```python
    import numpy as np
    import matplotlib.pyplot as plt
    from sklearn.datasets import make_classification
    ```
  - **Cell 2 — fake binary data:**
    ```python
    X, y = make_classification(n_samples=200, n_features=2, n_redundant=0,
                               n_clusters_per_class=1, random_state=42)
    ```
    Scatter plot colored by class.
  - **Cell 3 — sigmoid function + sanity tests:**
    ```python
    def sigmoid(z): return 1 / (1 + np.exp(-z))
    # Test: sigmoid(0) ≈ 0.5, sigmoid(10) ≈ 1.0, sigmoid(-10) ≈ 0.0
    ```
  - **Cell 4 — log-loss function + sanity tests:**
    ```python
    def log_loss(y, p, eps=1e-15):
        p = np.clip(p, eps, 1 - eps)
        return -np.mean(y * np.log(p) + (1 - y) * np.log(1 - p))
    # Test: perfect → loss ≈ 0; random 0.5 → loss ≈ 0.693 (= ln 2)
    ```
  - **Cell 5 — gradient function + 3 sanity tests:**
    - At truth (should be near zero)
    - At zero weights (should be non-zero)
    - At flipped weights (should be large)
  - **Cell 6 — markdown:** "What does `eps` guard against? What would happen without it?"
- [ ] 🚀 **15 min — Commit:** `week-03 day-3: notebook 06 part A (sigmoid + log-loss + sanity tests)`

---

### Thu May 14 — Notebook 06 Part B: GD + decision boundary (1.5hr, 9:00–10:30 PM)

**Slot plan (90 min):**

- [ ] 💻 **75 min — Continue `06-logistic-from-scratch.ipynb`**
  - **Cell 7 — GD loop:** lr=0.1, epochs=1000; track loss every 50 epochs; print final weights + bias
  - **Cell 8 — loss curve plot** (epochs vs loss — should decrease smoothly)
  - **Cell 9 — decision boundary plot:** mesh grid over feature space, color regions by predicted class, scatter training points on top
  - **Cell 10 — accuracy:** compute train accuracy with threshold=0.5
  - **Cell 11 — markdown reflection:**
    1. What did you clip/guard against (the `eps`)?
    2. What if classes were perfectly separable — what happens to the weights?
    3. What's the analog of the "convex bowl" from linreg?
- [ ] 🚀 **15 min — Commit:** `week-03 day-4: notebook 06 part B (GD loop + decision boundary + reflection)`

---

### Fri May 15 — Teach-back essay: regularization (1.5hr, 9:00–10:30 PM)

**Slot plan (90 min):**

- [ ] ✍️ **75 min — NN3 teach-back essay** → `concepts/week-02-teachback-regularization.md` (create file)
  - **Title:** "Regularization Explained to My Non-Technical Friend"
  - **Length:** ≥800 words
  - **🚨 Rule:** NO Google, NO ChatGPT, NO mentor. Write from memory only.
  - **Must cover (1 paragraph each):**
    1. The overfitting problem — why perfect train fit can be useless
    2. Bias-variance tradeoff (precise definitions — close the Week 1 gap)
    3. The shrinkage idea — why penalizing big weights helps
    4. Ridge (L2) — what it does, when to use it
    5. Lasso (L1) — what it does differently, feature selection
    6. Standardization — why you must do it first
    7. When regularization doesn't help
- [ ] 🚀 **15 min — Commit:** `week-03 day-5: teach-back essay regularization (NN3)`

---

### Sat May 16 — Notebook 07 + Twitter #4 + glossary + ROC/AUC (6hr)

**Slot plan (360 min):**

- [ ] 📝 **15 min — Anki review** (all Week 1 + 2 cards)
- [ ] 💻 **90 min — `daily-notebooks/week-02/07-cross-validation.ipynb`** (create file)
  - Reuse California housing setup from notebook 05
  - `from sklearn.model_selection import cross_val_score`
  - 5-fold CV on baseline LinearRegression → print mean ± std of R²
  - 5-fold CV on Ridge and Lasso (same alphas as notebook 05)
  - Compare to single 80/20 R² from notebook 05
  - Markdown: "How much did the single-split estimate over/underclaim?"
  - Log to MLflow under `week-02-ridge-lasso` experiment, run name `linreg-5fold-cv`
- [ ] 🌅 **30 min — StatQuest: ROC and AUC**
  - **Video:** https://www.youtube.com/watch?v=4jRBRDbJemM (~16 min)
  - **Output:** append 5 sentences to `concepts/week-02-prereading.md`:
    1. What does the ROC curve plot on its X and Y axes?
    2. What does each point on the ROC curve represent?
    3. What does AUC = 0.5 mean? AUC = 1.0? AUC = 0?
    4. Why is AUC threshold-independent — and why is that useful?
    5. When would you NOT use AUC (think: heavy class imbalance)?
- [ ] 📝 **30 min — 3 Anki cards** (append to `anki-cards-week-02.tsv`):
  - k-fold cross-validation | Split train into k folds; rotate which fold is held out; average score across k runs. Reduces variance of single-split estimate. | week-03 evaluation
  - ROC curve | Plot of True Positive Rate (y) vs False Positive Rate (x) at every classification threshold. | week-03 evaluation
  - AUC | Area Under the ROC Curve. 1.0 = perfect, 0.5 = random. Threshold-independent measure of classifier quality. | week-03 evaluation
- [ ] 🐦 **45 min — NN2 Twitter thread #4** → `twitter-posts/week-02-thread-regularization.md` (create file)
  - 5–7 tweets, reuse teach-back material
  - **Hook:** "Built linear regression last week. This week, broke it on purpose with Ridge and Lasso. Here's what regularization actually does to your weights 🧵"
  - Include 3-way coefficient plot from notebook 05
  - **POST LIVE before moving on.** Save URL in the file.
- [ ] 💻 **60 min — Glossary fill** in `context/05-glossary.md`
  - Write own-words definitions for: regularization, L1, L2, Ridge, Lasso, alpha/λ, standardization, sigmoid, log-loss, logistic regression, decision boundary, ROC, AUC, k-fold cross-validation
  - Delete the `_to fill Week 2._` placeholders
- [ ] 🚨 **30 min — Saturday velocity check**
  - Open `01-current-state.md` slip ledger
  - Count weekday slips; check 30-min cap and 20-min stuck rule compliance
  - Write §5 audit note in retro draft
- [ ] 🚀 **30 min — Commit:** `week-03 day-6: notebook 07 CV + thread #4 + glossary fill + roc/auc notes + 3 anki`
- [ ] ☕ **30 min — Buffer / curiosity bucket** (`concepts/curiosity-bucket.md`)

---

### Sun May 17 — Retro + Week 4 stub (6hr)

**Slot plan (360 min):**

- [ ] 📝 **15 min — Anki review** (all cards)
- [ ] 📖 **60 min — NN5 Week 3 retro** → `weekly-logs/retro-week-03.md`
  - Use template from `templates/retro-template.md`
  - **Required:** §5 — did the 20-min stuck rule fire? What happened?
  - Score all 5 NNs
- [ ] 📋 **60 min — Week 4 plan stub** in `06-current-task.md`
  - Week 4 topics: decision trees, random forests, multiclass (softmax), ensemble intro
  - Or if Week 3 has carryover, absorb it here
- [ ] 💻 **60 min — Project 01 review** — revisit `projects/01_Linear_Regression_House_Price/` and assess against the 6-criterion quality bar from roadmap
- [ ] 🚀 **30 min — Final commit:** `week-03 day-7: retro + week 4 stub`
- [ ] ☕ **135 min — Buffer / catch-up / rest**

---

## Definition of Done — Week 3

- [ ] Notebook 06 (logistic from scratch: sigmoid, log-loss, GD, decision boundary)
- [ ] Notebook 07 (k-fold CV on California housing)
- [ ] Logistic derivation written up (sigmoid derivative + log-loss gradient)
- [ ] Teach-back essay ≥800 words, no AI (regularization)
- [ ] **NN1:** 6/6 remaining commits (Tue–Sun)
- [ ] **NN2:** Thread #4 posted
- [ ] **NN3:** Teach-back essay shipped
- [ ] **NN4:** ~7 new Anki cards, 6/6 daily reviews
- [ ] **NN5:** Week 3 retro committed
- [ ] Glossary stubs filled
- [ ] 20-min stuck rule tested at least once

## 🚫 Out of scope (Week 4)

- Multiclass / softmax
- Decision trees / random forests
- Neural nets (Phase 2)
- Polynomial / interaction features
- New projects

## 🎯 Curiosity bucket rule

Found something interesting mid-task → write to `concepts/curiosity-bucket.md` → keep working. Sat 30-min slot reserved for review.
