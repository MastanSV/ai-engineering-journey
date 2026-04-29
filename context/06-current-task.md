# Current Task — Week 1 Day 4 (Thursday April 30, 2026)

> **Replace this file at the start of every new chat session/topic.**

## This week's mission

**Master linear regression end-to-end.** From numpy scratch → sklearn → real California housing dataset, all logged in MLflow. By Sunday I can teach linreg to a non-technical friend in 800 words.

## Carryover from Wed Apr 29 🔄

Heavy carryover today. Do FIRST.

- [ ] Backfill Ep 3 Q3 in `concepts/week-01-prereading.md` — determinant = area scaling factor (det=0 destroys info; negative = mirror)
- [ ] Notebook `03-linreg-from-scratch-part2.ipynb` — gradient descent from scratch, L1→L4 method
- [ ] 3 new Anki cards: gradient, learning rate, gradient descent
- [ ] Commit + push for notebook 03

**Slip lesson (Wed):** Stacking carryover + new heavy topic + Anki + commit into one 90-min weekday slot is unrealistic. For Week 2 plan, budget 2 days per "from-scratch" notebook.

## Realistic load decision (pick before starting)

Total realistic time tonight = 75 (carryover) + 90 (planned) = 165 min. Budget = 90 min.

| Option           | What you do tonight                                                 | What slips                                  |
| ---------------- | ------------------------------------------------------------------- | ------------------------------------------- |
| A. High energy   | Gradient descent + bias-variance video + sklearn notebook 04 (rush) | Anki/commit possibly to Fri                 |
| B. **Realistic** | Gradient descent (notebook 03) + 3 Anki cards + commit              | Bias-variance + sklearn notebook 04 → Fri   |
| C. Low energy    | Notebook 03 first 2 mini-topics only                                | Rest of notebook 03 + everything else → Fri |

**Recommended: Option B.** Notebook 03 is the foundation for the rest of the week. Quality on this one matters. Bias-variance is conceptual — easier to slot into Fri.

**Logged decision:** _(fill in when starting tonight)_

## Today's planned block (Thursday, 9:00–10:30 PM)

If Option B chosen:

### 🌅 (skip warmup tonight — substitute with Wed carryover backfill)

- [ ] Fix Ep 3 Q3 (determinant) — 5 min

### 💻 Gradient descent from scratch (75 min)

Create: `daily-notebooks/week-01/03-linreg-from-scratch-part2.ipynb`

L1→L4 mini-topic structure (will send detailed breakdown when you ping "ready for gradient descent"):

- L1 — Intuition: "I have MSE — how do I lower it without guessing?"
- L2 — Math: gradient of MSE w.r.t. `w` and `b` (partial derivatives)
- L3 — Code: GD loop in pure numpy, sanity checked on the fake data from notebook 02
- L4 — Reflection: loss curve, what learning rate too big/small does

### 📝 Anki (5 min — quick add only)

Add 3 cards (no review tonight — done Wed):

- "What is a gradient?" / "Vector of partial derivatives. Points in direction of steepest increase of the loss."
- "What is learning rate?" / "Step size in gradient descent. Too big = diverge; too small = slow convergence."
- "What is gradient descent?" / "Iterative algorithm: nudge parameters opposite the gradient to lower the loss."

### 🚀 Commit (5 min)

Suggested message: `week-01 day4: gradient descent from scratch (notebook 03) + Wed carryover`

If Option A or C chosen → adjust accordingly.

## End-of-session checklist

- [ ] Mark today's items ✅ / 🔄 / ⏭️ in `03-active-tasks.md`
- [ ] If anything 🔄 → update slip ledger in `01-current-state.md`
- [ ] **Velocity check pre-warning:** if Thu = 🔄, that's 3/3 weekday slips — Sat re-plan is mandatory
- [ ] Self-rate mood/energy (Wed + Thu) in `01-current-state.md`
