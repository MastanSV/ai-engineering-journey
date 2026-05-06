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
