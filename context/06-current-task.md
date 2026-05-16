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
