# Active Tasks — Week 1 Sprint (Apr 27 – May 3, 2026)

## Sprint goal

By Sunday May 3, I have built linear regression FROM SCRATCH in numpy (gradient descent, my own loss function), re-implemented it with sklearn, trained on a real dataset, logged every run in MLflow, and can explain the bias-variance tradeoff in my own words. No magic. No black boxes.

## Theme: **"From line to model"**

Master the simplest possible ML model end-to-end. Every concept here scales to GPT-4. If linreg is fuzzy, neural nets will be impossible.

## Time budget

- Mon–Fri: **9:00–10:30 PM** (1.5hr × 5 = 7.5hr)
- Sat: **6hr** focused
- Sun: **6hr** focused (incl. retro)
- **Target total: ~19hr**

---

## Daily breakdown

### Monday Apr 27 — Linear algebra warmup + numpy refresh

- 🌅 **15 min:** 3B1B Linear Algebra Ep 1 (Vectors) → 5 sentences in `concepts/week-01-prereading.md`
- 💻 **45 min:** Numpy notebook → `daily-notebooks/week-01/01-numpy-refresher.ipynb`
  - Create vectors/matrices, reshape, broadcasting, dot product, matrix multiplication
  - 10 small exercises (no Google for syntax — use docstrings via `?` in Jupyter)
- 📝 **20 min:** Anki — review yesterday + add 3 cards from today (vector, dot product, broadcasting)
- 🚀 **10 min:** commit + push

### Tuesday Apr 28 — Linear regression intuition

- 🌅 **15 min:** 3B1B Linear Algebra Ep 2 (Linear combinations & basis) → 5 sentences
- 💻 **45 min:** Notebook → `daily-notebooks/week-01/02-linreg-from-scratch-part1.ipynb`
  - Generate fake data: y = 2x + 1 + noise (use `np.random.randn`)
  - Plot it. Eyeball-fit a line. Compute MSE manually.
  - Define the loss function as a Python function: `def mse(y_true, y_pred): ...`
- 📝 **20 min:** Anki review + 2 new cards (MSE, residual)
- 🚀 **10 min:** commit + push

### Wednesday Apr 29 — Gradient descent from scratch

- 🌅 **15 min:** 3B1B Linear Algebra Ep 3 (Linear transformations & matrices) → 5 sentences
- 💻 **45 min:** Notebook → `daily-notebooks/week-01/03-linreg-from-scratch-part2.ipynb`
  - Implement gradient descent in pure numpy (no sklearn): w, b updated by computed gradients
  - Run for 1000 iterations, plot loss curve
  - Compare your final w, b to true (2.0, 1.0)
- 📝 **20 min:** Anki review + 3 new cards (gradient, learning rate, gradient descent)
- 🚀 **10 min:** commit + push

### Thursday Apr 30 — Bias-Variance + sklearn

- 🌅 **15 min:** StatQuest Bias-Variance Tradeoff → 5 sentences
- 💻 **45 min:** Notebook → `daily-notebooks/week-01/04-linreg-sklearn.ipynb`
  - Same data, now use `sklearn.linear_model.LinearRegression`
  - Verify w*, intercept* match your scratch implementation (within tolerance)
  - Document: "What sklearn does in 3 lines, my scratch code did in 30"
- 📝 **20 min:** Anki review + 2 new cards (bias, variance)
- 🚀 **10 min:** commit + push

### Friday May 1 — Real dataset + MLflow integration

- 🌅 **15 min:** StatQuest Linear Regression (main video) → 5 sentences
- 💻 **45 min:** Notebook → `daily-notebooks/week-01/05-real-dataset.ipynb`
  - Load `sklearn.datasets.fetch_california_housing()` (8 features, 20k rows)
  - 80/20 train/test split, fit LinearRegression, compute R², MSE
  - Log to MLflow with experiment name `week-01-california-housing`
- 📝 **20 min:** Anki review + 1 new card (R-squared)
- 🚀 **10 min:** commit + push

### Saturday May 2 — Diagnostics + portfolio polish (6hr)

- 🌅 **30 min:** Anki review (all Week 1 cards)
- 💻 **2hr:** Notebook → `daily-notebooks/week-01/06-diagnostics.ipynb`
  - Residual plots (predicted vs actual, residuals vs predicted)
  - Identify which features matter (coefficient magnitudes)
  - Try removing a feature, re-train, compare MSE
  - Markdown narration throughout — recruiter-readable
- 💻 **2hr:** Try TWO different models on California housing (still Week 1 territory)
  - `Ridge` (regularized linreg)
  - `Lasso` (sparsity-inducing)
  - Log both runs to MLflow → compare in UI side-by-side
- 📝 **30 min:** Curiosity bucket review — pick 1 item, explore for 30 min
- 🐦 **30 min:** Draft Twitter thread #3 in `twitter-posts/week-01-thread.md`
  - Hook idea: "Built linear regression from scratch in numpy this week. Here's what every gradient descent line actually does 🧵"
- 🚀 **30 min:** commit + push, screenshots

### Sunday May 3 — Teach-back + retro (6hr)

- 🌅 **30 min:** Anki review
- ✍️ **2hr:** **NN3 Teach-back** → `concepts/week-01-teachback-linreg.md`
  - 800 words, "Linear Regression Explained to My Non-Technical Friend"
  - Cover: what problem it solves, gradient descent intuition, bias-variance, when it fails
  - NO Google, NO ChatGPT (same rule as baseline essay)
- 💻 **1.5hr:** Optional: try California housing on **Kaggle** — submit to a beginner competition if one fits
- 📝 **30 min:** Anki — clean up cards, mark mature ones
- 📖 **1hr:** **Weekly retro** → `weekly-logs/week-01-linreg.md` (use template)
- 🐦 **30 min:** Post Twitter thread #3
- 🎤 **30 min:** Sunday mentor session — paste retro in chat

---

## ✅ Definition of Done — Week 1

- [ ] 5 weekday warmup videos watched + 5 sentences each
- [ ] Notebooks 01–06 committed in `daily-notebooks/week-01/`
- [ ] Linear regression implemented from scratch (gradient descent, no sklearn)
- [ ] Same problem solved with sklearn — results match
- [ ] California housing trained, R² and MSE in MLflow
- [ ] Ridge + Lasso comparison logged in MLflow (3 runs minimum)
- [ ] Diagnostic plots committed (residuals)
- [ ] Teach-back essay written (≥ 800 words, no AI assist)
- [ ] Twitter thread #3 posted
- [ ] Week 1 retro complete
- [ ] All 5 NN dimensions hit (commits, Twitter, teach-back, Anki daily, Sunday retro)

## 🚫 Out of scope (resist the rabbit hole)

- Neural networks
- Polynomial regression / feature engineering depth
- Logistic regression (Week 2)
- Cross-validation (Week 2)
- Deep dive into eigenvalues/SVD (Week 3)
- Anything outside `daily-notebooks/week-01/`

## 🎯 Curiosity bucket rule

If you find something interesting mid-task → write it in `concepts/curiosity-bucket.md` → KEEP WORKING. Saturday afternoon has 30 min reserved for it.
