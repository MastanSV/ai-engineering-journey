# Current Task — Week 1 Day 2 (Tuesday April 28, 2026)

> **Replace this file at the start of every new chat session/topic.**

## This week's mission

**Master linear regression end-to-end.** From numpy scratch → sklearn → real California housing dataset, all logged in MLflow. By Sunday I can teach linreg to a non-technical friend in 800 words.

## Today's block (Tuesday, 9:00–10:30 PM)

### 🌅 Warmup (15 min)

- Watch: 3Blue1Brown — Linear Algebra Essence **Episode 2: Linear combinations, span, basis** (https://www.youtube.com/watch?v=k7RM-ot2NWY)
- Append to `concepts/week-01-prereading.md` a section `## Ep 2: Linear combinations, span, basis`
- Write **5 sentences in your own words**:
  1. What is a linear combination of two vectors?
  2. What does "span" mean?
  3. What is a basis (and why are î and ĵ called basis vectors)?
  4. Where will I use span/basis in AI engineering?
  5. One question I still have

### 💻 Linreg from scratch — Part 1: data + loss (45 min)

Create: `daily-notebooks/week-01/02-linreg-from-scratch-part1.ipynb`

Cells to build:

1. **Markdown:** Title + "Goal: hand-build linear regression so I never treat it as a black box"
2. **Generate fake data:**
   - 100 samples
   - True relationship: `y = 2*x + 1 + noise`
   - Use `np.random.seed(42)` first for reproducibility
   - Use `np.random.randn(100)` for noise
3. **Plot:** scatter `x` vs `y` with proper title, xlabel, ylabel, figsize
4. **Eyeball-fit:** by visual inspection, guess `w` and `b`. Plot your guessed line on top of the scatter.
5. **MSE function:** define `def mse(y_true, y_pred): ...` returning the mean squared error. Compute MSE for your eyeballed prediction.
6. **Try 3 different (w, b) guesses:** print MSE for each. Which is lowest?
7. **Markdown reflection:** "What is gradient descent going to do that I just did manually?"

### 📝 Anki (20 min)

- Review all due cards (`00-Setup` + `01-Math-Foundations`)
- Add 2 new cards to `01-Math-Foundations`:
  - "What is MSE? (formula in words)" / "average of squared differences between predicted and true values"
  - "What is a residual?" / "the difference (y_true − y_pred) for one sample"

### 🚀 Commit (10 min)
