**Posted:** May 4, 2026 . https://x.com/mastan_ai/status/2051248494036517362?s=20

**Tweet 1/6 (hook)**

```
Built linear regression from scratch in numpy this week.

No sklearn. No black boxes. Just gradient descent, one line at a time.

Here's what every line actually does 🧵
```

**Tweet 2/6 (the problem)**

```
The job: find w and b so that y ≈ w·x + b fits the data.

"Fit" = minimize Mean Squared Error:
MSE = mean((y_pred − y_true)²)

We square the errors so positives don't cancel negatives, and big misses get punished harder than small ones.
```

**Tweet 3/6 (the gradient)**

```
We can't just guess w and b. We need a *direction* to nudge them.

That's the gradient — partial derivatives of MSE w.r.t. each param:
∂MSE/∂w = -2·mean(x · (y - y_pred))
∂MSE/∂b = -2·mean(y - y_pred)

It points uphill on the loss surface. We go the opposite way.
```

**Tweet 4/6 (the loop)**

```
Gradient descent in 3 lines:

  for step in range(epochs):
      dw, db = gradients(x, y, w, b)
      w -= lr * dw
      b -= lr * db

That's it. The whole magic of "training a model" is just nudging params downhill until the loss stops dropping.
```

**Tweet 5/6 (the gotcha — learning rate)**

```
Learning rate is the size of each nudge. Tested 3 values on the same data:

• lr = 0.01  → converged to w≈3.0, b≈5.0 ✅
• lr = 0.1    → loss exploded to NaN 💥
• lr = 0.0001 → still crawling after 1000 epochs 🐌

Too big = unstable. Too small = useless. Tuning matters.

[loss curve image]
```

**Tweet 6/6 (the bridge)**

```
Then I re-did it with sklearn:

  LinearRegression().fit(X, y)

3 lines. Same answer. But now I know what those 3 lines are *doing*.

Every neural network is this same loop, just with more params and a non-convex loss. Foundations matter.

Full notebook: github.com/MastanSV/ai-engineering-journey
```

---

**Image to attach on tweet 5:** the loss curve from `daily-notebooks/week-01/03-linreg-from-scratch-part2.ipynb` (the convergence plot showing loss dropping over epochs).

**Posting order:** Post 1, then reply with 2 → 3 → 4 → 5 (with image) → 6.

**Timer:** 30 min total. If you're past 25 min and still tweaking wording — ship it. Brutal accountability rule: ugly + posted > polished + drafted.
