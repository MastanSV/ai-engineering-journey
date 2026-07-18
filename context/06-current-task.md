> **As of 2026-07-18 — Week 5 · Saturday (6hr day, but starting with Fri carryover task).**
> Previous session (Thu): Wrote logistic teach-back part 1 (sigmoid, log-loss, gradient update rule) in `concepts/week-04-teachback-logistic_regression.md`.
> Today (first block): Finish teach-back part 2 + Anki cards. Then move to Gradio app.

# Current Task — Finish Teach-Back + Anki Cards (1.5hr block)

## What you already wrote (Blocks 1–3 done Thu)

- ✅ Sigmoid function — why not linreg for classification, sigmoid formula, z→probability conversion
- ✅ Log-loss — why not MSE, loss formula, examples
- ✅ Gradient update rule — dw/db formulas, learning rate, training loop diagram

## What's left (3 sections to add to `concepts/week-04-teachback-logistic_regression.md`)

---

## Block 1 — Decision Boundary (20 min)

Write a new `## Block 4 — Decision Boundary` section in the teach-back file.

Lines to cover:

- **What is a decision boundary?** The line (or surface) where the model is 50/50 — sigmoid output = 0.5, meaning z = wx + b = 0. On one side → predict 1, other side → predict 0.
- **Why is it a straight line?** Because wx + b = 0 is a linear equation. Logistic regression always produces a straight-line boundary (that's its limitation).
- **Threshold changes the boundary.** Default threshold = 0.5. If you lower it (e.g., 0.3 for heart disease), you shift the boundary so more patients get flagged as sick — fewer missed, more false alarms. Connect to your P1 threshold sweep work.
- **Connect to your contour plot.** You made a contour plot in `06-logistic-from-scratch.ipynb` — the colour boundary in that plot IS the decision boundary. Describe what you saw.

### 🎤 I'll ask

1. If wx + b = 2 for a patient, which side of the boundary are they on? What does the model predict?
2. Why would a hospital want to lower the threshold below 0.5? What's the trade-off?
3. Can logistic regression produce a curved decision boundary? Why or why not?

---

## Block 2 — When Logistic Regression Works / Fails (20 min)

Write a new `## Block 5 — When Logistic Regression Works and Fails` section.

Lines to cover:

- **Works well when:** classes are roughly linearly separable, features are meaningful and not too many, you need interpretable coefficients (e.g., doctor wants to know which features increase risk).
- **Fails when:** the real boundary between classes is curved/complex (e.g., XOR pattern — two features, but the classes are in opposite corners). No straight line can split them.
- **Fails when:** features are heavily correlated (multicollinearity — you saw this in California housing with rooms vs bedrooms). Coefficients become unstable.
- **Fails when:** massive class imbalance (95% healthy, 5% sick) — model learns to just say "healthy" for everything and gets 95% accuracy. Connect to your spam filter accuracy example from `01-classification-metrics.ipynb`.
- **Compared to more powerful models:** logistic regression is the "baseline" for classification, same way linear regression was for regression. Fast, transparent, and a benchmark.

### 🎤 I'll ask

1. If your data looks like two concentric circles (class 0 inside, class 1 outside), will logistic regression work? Why?
2. Name one real advantage of logistic regression over a complex model like a neural network.
3. Your heart disease dataset has 14 features — is logistic regression a reasonable choice? Why?

---

## Block 3 — Regularization's Role in Logistic Regression (20 min)

Write a new `## Block 6 — Regularization in Logistic Regression` section.

Lines to cover:

- **Same idea as linear regression.** You already explained Ridge (L2) and Lasso (L1) in your regularization teach-back. The penalty works the same way here: add λ·Σwⱼ² (Ridge) or λ·Σ|wⱼ| (Lasso) to the log-loss.
- **Why it matters here:** without regularization, if features are near-perfectly separating the classes, the weights blow up to ±infinity (the sigmoid tries to become a step function). Regularization caps this.
- **sklearn default:** `LogisticRegression()` uses L2 penalty with C=1.0 by default. C = 1/λ, so small C = heavy penalty. You discovered this during P1 — your "baseline" was already regularized.
- **L1 for feature selection:** in your P1, L1 may have zeroed out unimportant features from the 14. Check — did any coefficients go to exactly zero?
- **Connect to P1 results:** your comparison table (L2 vs L1) — which did better for heart disease? Why does that make sense given what you know about the 14 features?

### 🎤 I'll ask

1. What happens to logistic regression weights if data is perfectly separable and there's no regularization?
2. What does C=0.01 mean in terms of penalty strength? Is it heavy or light?
3. In your P1, did L1 zero out any features? What would that mean clinically?

---

## Block 4 — Word Count Check + Flow Read (5 min)

- [x] 4.1 Total word count across all 6 blocks ≥ 800 words. Count it: select all text → word count.
- [x] 4.2 Read top to bottom — does the teach-back flow as one story from "why sigmoid" to "regularization"?

---

## Block 5 — Anki Cards (20 min)

Create `concepts/anki-cards-week-04.tsv`. Same format as your existing TSV files (front;back).

Cards to write (Feynman-check each — if you can't explain it simply, re-study before writing the card):

| #   | Front (question)                                      | Back should cover                                                                                                     |
| --- | ----------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| 1   | What is a confusion matrix?                           | 2×2 grid: TP, FP, TN, FN — your spam filter example                                                                   |
| 2   | Precision vs Recall — what question does each answer? | Precision: "of all I flagged positive, how many were right?" Recall: "of all actual positives, how many did I catch?" |
| 3   | F1 score — what is it and when do you use it?         | Harmonic mean of precision & recall; use when you need a single number balancing both                                 |
| 4   | ROC-AUC — what does it measure?                       | Area under TPR vs FPR curve; 1.0 = perfect, 0.5 = random; threshold-independent                                       |
| 5   | Sigmoid function — formula + what it does             | σ(z) = 1/(1+e^−z); squashes any real number to (0,1) probability                                                      |
| 6   | Log-loss — formula + why not MSE?                     | −(1/N)Σ[y·log(p)+(1−y)·log(1−p)]; MSE makes loss surface non-convex                                                   |
| 7   | Classification threshold — what does lowering it do?  | More positives predicted → recall goes up, precision goes down                                                        |
| 8   | When does logistic regression fail?                   | Non-linear boundaries, heavy multicollinearity, extreme class imbalance                                               |

---

## Block 6 — Commit + EOD (10 min)

- [ ] 6.1 🚀 Commit: `week-05: teach-back complete + anki cards`
- [ ] 6.2 End-of-day update: `01-current-state.md`, `03-active-tasks.md`, `06-current-task.md`.

---

**DoD:** `week-04-teachback-logistic_regression.md` has 6 blocks (3 existing + 3 new), ≥800 words total. `anki-cards-week-04.tsv` has ≥8 cards, each Feynman-checked. Committed.
