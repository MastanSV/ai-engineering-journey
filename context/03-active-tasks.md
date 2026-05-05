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

> **Self-contained rule:** every day's block contains everything needed to execute — video URLs, prompt questions, file paths, copy/paste artifacts, success criteria. Do NOT come back to chat to fetch a link or a prompt.

---

### Mon May 4 — Mentor + Week 1 carryover (1.5hr, 9:00–10:30 PM)

**Slot plan (90 min):**

- [x] ✅ 🎤 **30 min — Mentor session (9:00–9:30):** Week 2 plan + DoD confirmed. No scope concerns from Week 1 retro.
- [x] ✅ 🐦 **30 min — Twitter thread #3 (9:30–10:00):** posted → https://x.com/mastan_ai/status/2051248494036517362
- [x] ✅ 📝 **15 min — Anki review (10:00–10:15):** all Week 1 cards reviewed.
- [ ] 🌅 **15 min — StatQuest: Ridge (10:15–10:30)**
  - **Video:** StatQuest — Regularization Part 1: Ridge (L2) Regression, Clearly Explained!!!
  - **Link:** https://www.youtube.com/watch?v=Q81RR3yKn30
  - **Length:** ~16 min (slightly over the 15-min rule — acceptable, canonical video)
  - **Output file:** `concepts/week-02-prereading.md` (create new file)
  - **5 sentences to answer:**
    1. What problem does Ridge solve that vanilla linear regression doesn't?
    2. What does the L2 penalty `λ·Σwⱼ²` do to the weight values during training?
    3. Why does Ridge shrink weights toward zero but never _exactly_ to zero?
    4. Why must features be standardized before applying Ridge?
    5. When would you reach for Ridge over Lasso?

**End-of-day required (≤5 min):**

- [ ] 🚀 Commit + push: `week-02 day-1: thread #3 posted, ridge intuition notes, anki reviewed`
- [ ] 📋 Update `01-current-state.md` Week 2 progress row for Mon (✅ / 🔄 / ⏭️)
- [ ] 🧮 Carryover audit: if anything 🔄, write remainder in min. **>30 min → push to Sat block, NOT Tue.**

---

### Tue May 5 — Ridge L1 + L2 (1.5hr, 9:00–10:30 PM)

**Slot plan (90 min):**

- [✅] 📚 **60 min — Ridge intuition + math** in `concepts/week-02-prereading.md`
  - **L1 (intuition, 5 sentences):**
    1. In your own words, what is regularization trying to prevent?
    2. Geometric picture: what does adding `λ·Σwⱼ²` to the loss surface look like?
    3. Why is the penalty applied to weights only, not to the bias `b`?
    4. What happens at λ=0? At λ→∞?
    5. Why does Ridge work best when many features each contribute a little?
  - **L2 (math derivation):**
    - Write the Ridge loss: `L = mean((y - (w·x + b))²) + λ·Σwⱼ²`
    - Derive `∂L/∂wⱼ` step by step using chain rule + power rule
    - Show the update becomes: `wⱼ ← wⱼ - lr·(∂MSE/∂wⱼ + 2λ·wⱼ)`
    - Sanity check: at λ=0, you recover plain GD. ✅
- [✅] 📝 **15 min — 3 Anki cards** (add to `concepts/anki-cards-week-02.tsv` — create file with TSV header `Front\tBack\tTags`):
  - Front: "Ridge regression" | Back: "Linear regression with L2 penalty (λ·Σwⱼ²) added to loss; shrinks all weights toward zero, never to zero." | Tags: week-02 regularization
  - Front: "L2 regularization" | Back: "Penalty term `λ·Σwⱼ²` added to loss. Discourages large weights. Differentiable everywhere → gradient-friendly." | Tags: week-02 regularization
  - Front: "Why standardize before Ridge/Lasso?" | Back: "L1/L2 penalty treats all weights equally; if features are on different scales, large-scale features get unfairly penalized for being large." | Tags: week-02 standardization
- [ ] 🌅 **15 min — StatQuest: Lasso**
  - **Video:** StatQuest — Regularization Part 2: Lasso (L1) Regression, Clearly Explained!!!
  - **Link:** https://www.youtube.com/watch?v=NGf0voTMlcs
  - **Length:** ~8 min
  - **Output:** append 5 sentences to `concepts/week-02-prereading.md`:
    1. How does Lasso's penalty differ from Ridge's, mathematically?
    2. Why can Lasso drive weights _exactly_ to zero (the geometric/diamond intuition)?
    3. What does that property buy you in practice (think: feature selection)?
    4. When does Lasso outperform Ridge? When is it worse?
    5. What is "Elastic Net" in one sentence?

**End-of-day:** commit + push (`week-02 day-2: ridge math + lasso intuition + 3 anki`); update state file; carryover audit.

---

### Wed May 6 — Notebook 05 Part A: Standardize + Ridge (1.5hr)

**Slot plan (90 min):**

- [ ] 💻 **75 min — `daily-notebooks/week-02/05-ridge-lasso-california.ipynb`** (create file + folder)
  - **Cell 1 — imports:**
    ```python
    import numpy as np, pandas as pd, matplotlib.pyplot as plt, mlflow
    from sklearn.datasets import fetch_california_housing
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    from sklearn.linear_model import LinearRegression, Ridge
    from sklearn.metrics import mean_squared_error, r2_score
    ```
  - **Cell 2 — load + split + standardize:**
    ```python
    data = fetch_california_housing(as_frame=True)
    X, y = data.data, data.target
    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)
    scaler = StandardScaler().fit(X_tr)
    X_tr_s = scaler.transform(X_tr); X_te_s = scaler.transform(X_te)
    ```
  - **Cell 3 — MLflow setup:**
    ```python
    mlflow.set_experiment("week-02-ridge-lasso")
    ```
  - **Cell 4 — baseline LinearRegression run** (log params: model_type, n_features; metrics: train_mse, test_mse, train_r2, test_r2; log model)
  - **Cell 5 — Ridge run** (try `alpha=1.0`); same logging pattern
  - **Cell 6 — markdown narration:** "Did Ridge improve test MSE? By how much? Did the coefficient magnitudes shrink? Show before/after."
  - **🚨 Sanity check:** baseline test R² should match Week 1 notebook 04 (~0.58). If not, you mis-split.
- [ ] 🚀 **15 min — commit + push:** `week-02 day-3: notebook 05 part A (standardize + ridge + mlflow)`

**End-of-day:** update state file; carryover audit.

---

### Thu May 7 — Notebook 05 Part B + 3-way comparison (1.5hr)

**Slot plan (90 min):**

- [ ] 💻 **60 min — Add Lasso to notebook 05**
  - **Cell 7 — imports:** `from sklearn.linear_model import Lasso`
  - **Cell 8 — Lasso run** (try `alpha=0.1`; if all coefs zero, lower alpha); same MLflow logging pattern
  - **Cell 9 — 3-way comparison plot:** bar chart of `|coefficient|` per feature for LinearRegression vs Ridge vs Lasso
  - **Cell 10 — MLflow UI screenshot:** open `mlflow ui` in terminal, screenshot the 3-run comparison table; save as `daily-notebooks/week-02/mlflow-comparison.png`
  - **Cell 11 — markdown:** "Which features did Lasso zero out? Does that make domain sense for housing prices?"
- [ ] 📝 **15 min — 3 Anki cards** (append to `anki-cards-week-02.tsv`):
  - Front: "Lasso regression" | Back: "Linear regression with L1 penalty (λ·Σ|wⱼ|); can drive weights exactly to zero → built-in feature selection." | Tags: week-02 regularization
  - Front: "L1 vs L2 — key behavioral difference" | Back: "L1 produces sparse solutions (some weights = 0). L2 shrinks all weights but keeps them non-zero." | Tags: week-02 regularization
  - Front: "alpha (λ) parameter" | Back: "Strength of the regularization penalty. α=0 → vanilla regression. α→∞ → all weights = 0." | Tags: week-02 regularization
- [ ] 🌅 **15 min — StatQuest: Logistic Regression**
  - **Video:** StatQuest — Logistic Regression
  - **Link:** https://www.youtube.com/watch?v=yIYKR4sgzI8
  - **Length:** ~8 min
  - **Output:** append 5 sentences to `concepts/week-02-prereading.md`:
    1. Why can't we just use linear regression for binary classification (probabilities < 0 or > 1)?
    2. What does the sigmoid function do, in one sentence?
    3. What is "log-loss" (cross-entropy) and why is it used instead of MSE for classification?
    4. What does the "decision boundary" mean geometrically?
    5. Is logistic regression a "regression" or "classification" algorithm? Defend the name.

**End-of-day:** commit (`week-02 day-4: notebook 05 part B (lasso) + 3-way comparison + logistic intuition`); state update; carryover audit.

---

### Fri May 8 — Mentor: logistic L1 + L2 (1.5hr)

**Slot plan (90 min):**

- [ ] 🎤 **75 min — Mentor session: logistic regression deep-dive**
  - **L1 (intuition) — 5 questions to answer in own words during mentor:**
    1. Sigmoid: why this specific shape `1/(1+e^-z)`? What property makes it useful?
    2. If MSE worked for linreg, why does it fail for classification?
    3. Geometric picture of log-loss: what does it punish, and how harshly?
    4. What is the "decision boundary" in 2D? Is it always a straight line in logistic regression?
    5. Why is the loss surface for logistic regression _convex_ — and why does that matter?
  - **L2 (math) — derive on paper:**
    - Sigmoid: `σ(z) = 1/(1+e^-z)`; show that `σ'(z) = σ(z)·(1-σ(z))`
    - Log-loss for one example: `L = -[y·log(p) + (1-y)·log(1-p)]` where `p = σ(w·x + b)`
    - Derive `∂L/∂w` using chain rule. Final answer should simplify beautifully to: `(p - y)·x`
    - Sign sanity check: if `p > y` (overpredicted), gradient is positive → `w` decreases. ✅
  - **Capture all derivations** in `concepts/week-02-prereading.md` under heading "Logistic L2 — derivation"
- [ ] 🚀 **15 min — mid-week velocity check + carryover audit**
  - Open `01-current-state.md` Week 2 progress + slip ledger
  - Count weekday slips so far this week
  - If ≥2 slips OR any single carryover >30 min not yet pushed to Sat → flag in retro draft

**End-of-day:** commit (`week-02 day-5: logistic regression L1+L2 mentor notes`).

---

### Sat May 9 — Notebook 06 + cross-val + Saturday velocity check (6hr)

**Slot plan (360 min):**

- [ ] 💻 **180 min — `daily-notebooks/week-02/06-logistic-from-scratch.ipynb`** (no sklearn for the model)
  - **Cell 1 — imports:** `numpy`, `matplotlib`, `from sklearn.datasets import make_classification` (allowed for data only)
  - **Cell 2 — fake binary data:** `X, y = make_classification(n_samples=200, n_features=2, n_redundant=0, n_clusters_per_class=1, random_state=42)`; scatter plot colored by class
  - **Cell 3 — sigmoid + sanity test:**
    ```python
    def sigmoid(z): return 1 / (1 + np.exp(-z))
    # Test: sigmoid(0) ≈ 0.5, sigmoid(10) ≈ 1.0, sigmoid(-10) ≈ 0.0
    ```
  - **Cell 4 — log-loss function + sanity test:**
    ```python
    def log_loss(y, p, eps=1e-15):
        p = np.clip(p, eps, 1 - eps)
        return -np.mean(y * np.log(p) + (1 - y) * np.log(1 - p))
    # Test: perfect predictions → loss ≈ 0; random 0.5 → loss ≈ 0.693 (= ln 2)
    ```
  - **Cell 5 — gradient function + sanity tests** (3 cases: at truth, at zero weights, at flipped weights)
  - **Cell 6 — GD loop:** lr=0.1, epochs=1000; track loss every 50 epochs
  - **Cell 7 — loss curve plot**
  - **Cell 8 — decision boundary plot:** mesh grid over feature space, color by predicted class
  - **Cell 9 — L4 reflection (markdown):** What did you have to clip/guard against (the `eps` in log_loss)? What if classes were perfectly separable? What's the analog of the "convex bowl" picture from linreg?
- [ ] 💻 **90 min (stretch) — `daily-notebooks/week-02/07-cross-validation.ipynb`**
  - Reuse California housing setup from notebook 05
  - `from sklearn.model_selection import cross_val_score`
  - 5-fold CV on baseline LinearRegression → print mean ± std of R²
  - Compare to single 80/20 R² from notebook 05; markdown reflection: "How much did the single-split estimate over/underclaim?"
  - Log to MLflow under same `week-02-ridge-lasso` experiment with run name `linreg-5fold-cv`
- [ ] 📝 **30 min — 4 Anki cards** (append to `anki-cards-week-02.tsv`):
  - Front: "Sigmoid function" | Back: "σ(z) = 1/(1+e^-z). Squashes any real number into (0,1) so it can be read as a probability." | Tags: week-02 logistic
  - Front: "Log-loss / cross-entropy" | Back: "L = -[y·log(p) + (1-y)·log(1-p)]. Convex in logistic regression's params → GD finds global min." | Tags: week-02 logistic
  - Front: "Logistic regression" | Back: "Linear model + sigmoid → probability for binary classification. Loss = log-loss, not MSE." | Tags: week-02 logistic
  - Front: "k-fold cross-validation" | Back: "Split train into k folds; rotate which fold is held out; average score across k runs. Reduces variance of single-split estimate." | Tags: week-02 evaluation
- [ ] 🌅 **30 min — StatQuest: ROC and AUC**
  - **Video:** StatQuest — ROC and AUC, Clearly Explained!
  - **Link:** https://www.youtube.com/watch?v=4jRBRDbJemM
  - **Length:** ~16 min
  - **Output:** append 5 sentences to `concepts/week-02-prereading.md`:
    1. What does the ROC curve plot on its X and Y axes?
    2. What does each point on the ROC curve represent?
    3. What does AUC = 0.5 mean? AUC = 1.0? AUC = 0?
    4. Why is AUC threshold-independent — and why is that useful?
    5. When would you NOT use AUC (think: heavy class imbalance)?
- [ ] 🚀 **30 min — commit + push** (`week-02 day-6: notebook 06 logistic from scratch + notebook 07 cv + roc/auc notes + 4 anki`)
- [ ] 🚨 **30 min — Saturday velocity check + carryover-cap audit**
  - Open `01-current-state.md` slip ledger
  - For each weekday slip: was the carryover ≤30 min? If not, was it pushed to Sat?
  - Write a 3-sentence note in `weekly-logs/retro-week-02-regularization.md` (create scaffold from `templates/retro-template.md`) — section 5 audit
- [ ] ☕ **30 min — buffer / curiosity bucket review** (`concepts/curiosity-bucket.md`)

---

### Sun May 10 — Teach-back + thread #4 + retro + Week 3 stub (6hr)

**Slot plan (360 min):**

- [ ] 🌅 **15 min — Anki review** (all Week 1 + Week 2 cards, ~24 total)
- [ ] ✍️ **120 min — NN3 teach-back essay** → `concepts/week-02-teachback-regularization.md`
  - **Title:** "Regularization Explained to My Non-Technical Friend"
  - **Length:** ≥800 words
  - **🚨 Rule:** NO Google, NO ChatGPT, NO mentor help. Same rule as baseline + Week 1.
  - **Must cover (1 paragraph each unless noted):**
    1. The overfitting problem — why a model that fits training data perfectly can be useless
    2. Bias-variance tradeoff (precise definitions this time — close the Week 1 essay gap)
    3. The shrinkage idea — why penalizing big weights helps
    4. Ridge (L2) — what it does, when to use it (2 paragraphs — this is the heart)
    5. Lasso (L1) — what it does differently, why it's a feature selector
    6. Standardization — why you must do this first (one mistake to never make)
    7. When regularization doesn't help (very small datasets where you're under-fit, not over-fit)
- [ ] 🐦 **45 min — NN2 Twitter thread #4** → `twitter-posts/week-02-thread.md`
  - 5–7 tweets, reuse teach-back material
  - **Hook (tweet 1):** "Built linear regression last week. This week, broke it on purpose with Ridge and Lasso. Here's what regularization actually does to your weights 🧵"
  - **Tweet 2:** the overfitting problem (1 sentence) + why "more fit" isn't always better
  - **Tweet 3:** Ridge — "shrinks all weights toward zero, never to zero" + the L2 math `λ·Σwⱼ²`
  - **Tweet 4:** Lasso — "drives some weights _exactly_ to zero" → built-in feature selection + L1 math `λ·Σ|wⱼ|`
  - **Tweet 5:** the gotcha — "must standardize first or the penalty is unfair to large-scale features"
  - **Tweet 6 (with image):** the 3-way coefficient comparison plot from notebook 05 — `daily-notebooks/week-02/mlflow-comparison.png`
  - **Tweet 7:** "Same data. Three models. Three different stories about which features matter. Tomorrow: logistic regression from scratch. Notebook: github.com/MastanSV/ai-engineering-journey"
  - **POST LIVE before moving on.** Save URL in the thread file.
- [ ] 📖 **60 min — NN5 Week 2 retro** → `weekly-logs/retro-week-02-regularization.md`
  - Use template from `templates/retro-template.md`
  - **Required:** §5 carryover-cap audit — did the rule hold? How many >30-min spillovers were pushed to Sat? If rule failed, why?
  - Score self on all 5 NNs (no 10s)
- [ ] 💻 **60 min — Glossary fill** in `context/05-glossary.md` — write own-words definitions for: regularization, L1, L2, Ridge, Lasso, alpha/λ, standardization, sigmoid, log-loss, logistic regression, decision boundary, ROC, AUC, k-fold cross-validation. Delete the `_to fill Week 2._` markers as you go.
- [ ] 📋 **30 min — Week 3 stub** in `06-current-task.md` (replace this file with Week 3 mission + carryover from Week 2)
- [ ] 🚀 **30 min — final commit + push** (`week-02 day-7: teach-back essay + thread #4 + retro + glossary fill + week 3 stub`)
- [ ] ☕ **30 min — buffer / mentor session if needed**

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
