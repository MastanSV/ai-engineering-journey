> **As of 2026-07-16 — Week 5 · Thursday (1.5hr, 9:00–10:30 PM).**
> Previous session (Wed): Best-model selection + MLflow finalize (carryover items from Tue fixed).
> Today: Anki review + logistic teach-back part 1 (sigmoid, log-loss, gradient update rule).

# Current Task — Logistic Teach-Back (Part 1)

## Reminder

Your Week 3 notebook note said: _"NOT HAPPY WITH THE UNDERSTANDING OF LOGISTIC REGRESSION. NEED TO REVISIT AGAIN."_ — Tonight is that revisit. Write to understand, not to finish fast.

**Rules:** No Google, no AI. Write in your own words as if explaining to a non-technical friend (Feynman style). Minimum depth: someone reading this should be able to implement sigmoid + log-loss + gradient step from your explanation alone.

---

## Block 0 — Warm-up (15 min)

- [ ] 0.1 Run Anki (Week 0–4 cards). Note any card you fail → revisit that concept before writing.
- [ ] 0.2 Open `daily-notebooks/week-03/06-logistic-from-scratch.ipynb` — skim your own code to refresh memory. Do NOT copy from it; just remind yourself what you built.

---

## Block 1 — Sigmoid Function (20 min)

Write in `concepts/week-04-teachback-logistic.md`.

- [ ] 1.1 **Why not plain linear regression for classification?** What goes wrong if you use y = wx + b to predict 0/1? (Hint: outputs can be 5.0 or −3.0 — not probabilities.)
- [ ] 1.2 **What is the sigmoid function?** Write the formula. Explain what it does to any input number (squashes to 0–1). Walk through: what happens at z = 0? z = +10? z = −10?
- [ ] 1.3 **Why sigmoid specifically?** What property makes it useful for binary classification? (maps to probability, smooth, differentiable)
- [ ] 1.4 **Checkpoint:** Without looking at your notebook, can you sketch the sigmoid curve shape in words (S-shape, asymptotes at 0 and 1, crosses 0.5 at z = 0)?

### 🔍 Lines I'll check on Block 1

- Does your explanation make clear **why we can't just use a straight line** for classification?
- Did you write the actual formula: σ(z) = 1 / (1 + e^(−z))?
- Did you walk through at least 3 concrete z-values showing the output?
- Can a reader who only reads your text tell what the sigmoid curve looks like?

### 🎤 Interview questions (Block 1)

1. If sigmoid outputs 0.73, what does that number mean in a heart-disease context?
2. What happens to the sigmoid output when z is a very large positive number? Very large negative?
3. Why can't we just round the linear regression output to 0 or 1 instead of using sigmoid?

---

## Block 2 — Log-Loss / Binary Cross-Entropy (30 min)

Continue in the same file.

- [ ] 2.1 **Why not MSE for classification?** What goes wrong if you use squared error with sigmoid? (Hint: the loss surface becomes non-convex — multiple valleys, gradient descent gets stuck.)
- [ ] 2.2 **Build log-loss from intuition:** If the true label is 1 and model says p = 0.99, loss should be tiny. If model says p = 0.01, loss should be huge. Which math function does this? → −log(p).
- [ ] 2.3 **Write the full formula:** L = −(1/N) Σ [y·log(p) + (1−y)·log(1−p)]. Explain each piece: what does the y·log(p) part handle? What does the (1−y)·log(1−p) part handle?
- [ ] 2.4 **Walk through 2 concrete examples:** (a) y = 1, p = 0.9 → compute the loss. (b) y = 0, p = 0.9 → compute the loss. Show the math step by step.
- [ ] 2.5 **Why clip p?** What happens to log(0)? How does eps fix it? (You answered this in your notebook — rewrite it more precisely here.)
- [ ] 2.6 **Checkpoint:** Close your notebook. Can you write the log-loss formula from memory and explain why each term exists?

### 🔍 Lines I'll check on Block 2

- Is the log-loss formula written out fully (not just named)?
- Did you show the **two-case breakdown** (when y = 1 vs when y = 0) so the reader sees the formula isn't magic?
- Are there at least 2 numeric examples with actual computed values?
- Did you explain the eps/clip guard in your own words?
- Does your MSE-for-classification explanation mention non-convexity or "multiple valleys"?

### 🎤 Interview questions (Block 2)

1. If y = 1 and p = 0.5, what is the log-loss for that single sample? What about p = 0.99?
2. Why does the formula have two terms added together instead of just −log(p)?
3. What would go wrong if you trained logistic regression using MSE instead of log-loss?
4. In the formula, when y = 0, what happens to the first term y·log(p)? Why is that useful?

---

## Block 3 — Gradient Update Rule (25 min)

Continue in the same file.

- [ ] 3.1 **What are we trying to minimize?** (log-loss). What knobs do we turn? (w and b, same as linear regression).
- [ ] 3.2 **Write the gradient formulas:**
  - dw = (1/N) · Xᵀ · (p − y)
  - db = (1/N) · Σ(p − y)
  - Explain in plain English: (p − y) is the error. We multiply by X to figure out how much each feature contributed to that error.
- [ ] 3.3 **Write the update step:** w ← w − lr · dw, b ← b − lr · db. Explain what learning rate controls (step size — your mountain-fog analogy from linreg teachback applies here too).
- [ ] 3.4 **Why does this look almost identical to linear regression's gradient?** Point out the only difference: in linreg, prediction = Xw + b. In logistic, prediction = sigmoid(Xw + b). The gradient formula structure is the same — the sigmoid is what makes it classification.
- [ ] 3.5 **Checkpoint:** Without looking at code, write the 4-line training loop pseudocode: compute z → compute p → compute gradients → update weights.

### 🔍 Lines I'll check on Block 3

- Are both gradient formulas (dw and db) written out explicitly?
- Did you explain **(p − y)** as "the error" and **Xᵀ ·** as "which features caused it"?
- Is the connection to linear regression's gradient made explicit?
- Can a reader reconstruct a training loop from your explanation alone?

### 🎤 Interview questions (Block 3)

1. If p = 0.8 and y = 1, what is (p − y)? Is the gradient pushing the weights to make p go up or down?
2. Why do we divide by N in the gradient formula?
3. What happens if the learning rate is too large? Too small? (Connect to your mountain-fog analogy.)
4. If you had to explain the entire logistic regression training loop in 3 sentences, what would you say?

---

## Block 4 — Wrap-up + Commit (5 min, use remaining buffer)

- [ ] 4.1 Re-read your teach-back top to bottom. Does it flow? Would a friend follow it?
- [ ] 4.2 Word-count check: aim for ≥400 words tonight (the remaining ≥400 comes Friday).
- [ ] 4.3 🚀 Commit: `week-05: logistic teach-back part 1`
- [ ] 4.4 End-of-day update: `01-current-state.md`, `03-active-tasks.md`, `06-current-task.md`.

---

**DoD today:** `concepts/week-04-teachback-logistic.md` exists with 3 sections (sigmoid, log-loss, gradient update rule) written in your own words, no AI, ≥400 words, at least 2 numeric examples in the log-loss section.

> ⏱️ 20-min stuck rule: if you blank on a concept >20 min, open your `06-logistic-from-scratch.ipynb` and trace through ONE code cell. Then close it and write.
