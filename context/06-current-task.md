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
