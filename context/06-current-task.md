# Current Task — Week 1 Day 3 (Wednesday April 29, 2026)

> **Replace this file at the start of every new chat session/topic.**

## This week's mission

**Master linear regression end-to-end.** From numpy scratch → sklearn → real California housing dataset, all logged in MLflow. By Sunday I can teach linreg to a non-technical friend in 800 words.

## Carryover from Tue Apr 28 🔄

Do FIRST tonight (~30 min). Already in flight, mostly done — just close the loop:

- [x] Mini-topic 4 done: `mse()` function + 4 sanity tests pass
- [x] Mini-topic 5 done: 3 eyeball guesses + 3-line plot + reflection
- [x] 2 Anki cards added (MSE, residual)
- [ ] Commit + push notebook 02 with proper message

**Slip lesson:** L1/L2 depth on a _first_ ML topic takes 2x estimated time. Budget accordingly for gradient descent tonight.

## Today's block (Wednesday, 9:00–10:30 PM) — Mini-topic 6: Gradient descent

### 🌅 Warmup (15 min)

- Watch: 3Blue1Brown — Linear Algebra Ep 3 (Linear transformations & matrices) — https://www.youtube.com/watch?v=kYB8IZa5AuE
- Append to `concepts/week-01-prereading.md` a section `## Ep 3: Linear transformations & matrices`
- Write **5 sentences in your own words**:
  1. What is a linear transformation?
  2. How does a 2x2 matrix represent one?
  3. What does the determinant tell you geometrically?
  4. Where will I use this in AI engineering? (Hint: every neural net layer is `Wx + b`)
  5. One question I still have

### 💻 Gradient descent from scratch (45 min)

Create: `daily-notebooks/week-01/03-linreg-from-scratch-part2.ipynb`

Layered learning approach (same as Day 2):

- **L1 — Intuition:** What problem does GD solve? "I have MSE — how do I lower it without guessing?"
- **L2 — Math:** Gradient of MSE w.r.t. `w` and `b`. Symbol cheat sheet.
- **L3 — Code:** GD loop in pure numpy. Sanity check: does final `w, b` ≈ `(2.0, 1.0)`?
- **L4 — Reflection:** What does the loss curve teach me? What if learning rate is too big/small?

(Detailed mini-topic breakdown comes when you ping "ready for Wed mini-topic 6")

### 📝 Anki (20 min)

- Review all due cards (`00-Setup` + math/numpy)
- Add 3 new cards:
  - "What is a gradient?" / "Vector of partial derivatives — points in direction of steepest increase"
  - "What is learning rate?" / "Step size in gradient descent. Too big = diverge; too small = slow"
  - "What is gradient descent?" / "Iterative algorithm: nudge parameters opposite the gradient to lower the loss"

### 🚀 Commit (10 min)

Suggested message: `week-01 day3: linreg scratch part 2 (gradient descent) + Tue carryover`

## End-of-session checklist

- [ ] Mark all today's items ✅ / 🔄 / ⏭️ in `03-active-tasks.md`
- [ ] If anything 🔄 → add reason and recovery plan in `01-current-state.md` slip ledger
- [ ] Self-rate mood/energy in `01-current-state.md`
- [ ] Note one thing that surprised you (curiosity bucket if it's a tangent)
