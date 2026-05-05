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
- [] 📝 **15 min — 3 Anki cards** (add to `concepts/anki-cards-week-02.tsv` — create file with TSV header `Front\tBack\tTags`):
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
