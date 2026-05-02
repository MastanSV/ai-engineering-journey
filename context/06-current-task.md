# Current Task — Week 1 Day 7 (Sunday May 3, 2026)

> **Replace this file at the start of every new chat session/topic.**

## This week's mission

**Master linear regression end-to-end.** Scratch GD ✅ already shipped Sat. Today: bridge from scratch → sklearn → real California housing dataset (all logged in MLflow), then teach it to a non-technical friend in 800 words. **Last day of Week 1 — Sunday is sacred.**

## Status going into today

- ✅ Notebook 03 (gradient descent from scratch) shipped Sat May 2
- ✅ 17 Anki cards (gradient, learning rate, gradient descent rewritten with mentor review)
- ✅ Ep 3 Q3 (determinant) backfilled
- ✅ Week 1 scope cut logged (`04-decisions-log.md` 2026-05-02): merged sklearn + California into one notebook; Ridge/Lasso → Week 2

## Carryover from Sat May 2

_None — Sat shipped clean ✅._

## Today's plan (Sunday, ~6.5hr) — POST-SCOPE-CUT

### 🌅 Warmup (30 min, 9–9:30 AM-ish)

- [ ] **15 min:** StatQuest Bias-Variance Tradeoff → 5 sentences in `concepts/week-01-prereading.md`
- [ ] **15 min:** Anki review (all 17 cards)

### 💻 Merged notebook (150 min)

Create: `daily-notebooks/week-01/04-sklearn-california-mlflow.ipynb`

**Part A — sklearn on the same fake data (45 min)**

- Import `sklearn.linear_model.LinearRegression`
- Use the SAME fake data as notebooks 02 + 03 (seed 42, n=100, true w=3 b=5, noise σ=2)
- Fit `LinearRegression()` — verify `model.coef_ ≈ 3.0`, `model.intercept_ ≈ 5.0`
- Verify within tolerance of your scratch GD result (`w_hat`, `b_hat`)
- Markdown narration: "What sklearn does in 3 lines, my scratch code did in 30. Same answer."

**Part B — California housing, the first real dataset (60 min)**

- `from sklearn.datasets import fetch_california_housing` (8 features, ~20k rows)
- 80/20 train/test split with `train_test_split(..., random_state=42)`
- Fit `LinearRegression` on train
- Predict on test → compute MSE + R² (`from sklearn.metrics import mean_squared_error, r2_score`)
- 🚨 **Sanity check:** print `model.coef_` for each feature — sign + magnitude should make some intuitive sense (e.g., higher income → higher house price → positive coefficient on `MedInc`)

**Part C — MLflow + 1 residual plot (45 min)**

- Set experiment name `week-01-california-housing`
- Wrap each fit (Part A and Part B) in `with mlflow.start_run():`
- Log: params (n_features, train_size), metrics (mse, r2), model artifact
- After fitting Part B: 1 plot — predicted vs actual on test set (perfect predictions = diagonal line; random scatter = bad fit)
- Open MLflow UI, screenshot the comparison

**2 new Anki cards:** R-squared, residual plot

### ✍️ Teach-back essay — NN3 (120 min)

File: `concepts/week-01-teachback-linreg.md`

- **800 words minimum**, "Linear Regression Explained to My Non-Technical Friend"
- **NO Google, NO ChatGPT, NO mentor help** (same rule as baseline essay)
- Must cover:
  - What problem linreg solves (1 paragraph)
  - The line equation `y = wx + b` and what `w` and `b` mean (1 paragraph)
  - Loss / MSE — why we square the errors (1 paragraph)
  - **Gradient descent intuition** — blindfolded-on-bowl analogy or your own (2 paragraphs — this is the heart)
  - Bias-variance tradeoff (1 paragraph — uses the warmup video)
  - When linreg fails (1 paragraph — non-linear relationships, multicollinearity)

### 📖 Weekly retro — NN5 (45 min)

File: `weekly-logs/week-01-linreg.md` (use template from `templates/retro-template.md`)

**Required sections:**

- Hours logged vs target (~19hr target)
- What shipped vs DoD checklist
- **Slip pattern analysis** — 3 weekday slips. WHY? Honest answer. (Hint: first-time topics took ~2× estimate)
- Score on each of the 5 NNs
- 1 calibration rule for Week 2 (e.g., "budget 2 days per from-scratch notebook")
- Mood/confidence honest score (no 10/10)

### 🐦 Twitter thread #3 — NN2 (30 min)

File: `twitter-posts/week-01-thread.md`

- 5–7 tweets, reuse teach-back material
- Hook: "Built linear regression from scratch in numpy this week. Here's what every gradient descent line actually does 🧵"
- Include 1 image: loss curve from notebook 03 (the convergence plot)
- Post live

### 🚀 Commit + push (15 min)

Single commit message:
