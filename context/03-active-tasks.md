# Active Tasks — Week 1 Sprint (Apr 27 – May 3, 2026)

> **STATUS: Week 1 closed May 3, 2026.** This file is now read-only history. See `06-current-task.md` for Week 2 sprint.

## Sprint goal

By Sunday May 3, I have built linear regression FROM SCRATCH in numpy (gradient descent, my own loss function), re-implemented it with sklearn, trained on a real dataset, logged every run in MLflow, and can explain the bias-variance tradeoff in my own words. No magic. No black boxes.

## Theme: **"From line to model"**

Master the simplest possible ML model end-to-end. Every concept here scales to GPT-4. If linreg is fuzzy, neural nets will be impossible.

## Time budget

- Mon–Fri: **9:00–10:30 PM** (1.5hr × 5 = 7.5hr)
- Sat: **6hr** focused
- Sun: **6hr** focused (incl. retro)
- **Target total: ~19hr**

---

## Day-state tracking system

Each task in the daily breakdown is marked at end-of-day with one of:

| Symbol | Meaning                                                                    |
| ------ | -------------------------------------------------------------------------- |
| ✅     | **Shipped** — completed within the planned day                             |
| 🔄     | **Carried** — partially done, remainder rolled to next day (must note WHY) |
| ⏭️     | **Deferred** — explicitly chose to skip; logged with reason                |
| ❌     | **Skipped** — missed with no recovery (rare; triggers re-plan)             |

**Why this matters:**

- Honest 🔄 logging gives calibration data → time estimates sharpen by Week 4
- Sunday retro reads patterns (which days slip? which task types?)
- Brutal accountability ≠ self-blame. It means honest data.

**Slip rules:**

1. When a task carries to next day → add it to next day's plan AS THE FIRST item, with `(carryover)` tag
2. Log the reason in the day's entry — _underestimated time_ / _got stuck on X_ / _energy low_
3. Note recovery in the slip ledger in `01-current-state.md`

**Velocity check (Saturday review):**

- ≥3 days with 🔄 in a week, OR
- total carryover > 1 hour

→ trigger re-plan: (a) cut scope, (b) use Sat/Sun buffer, or (c) accept smaller week. **Never fake-finish.**

**Recovery patterns that work:**

- Carryover from weekday → fold into next weekday's first 30 min
- Carryover from Friday → use Saturday's 6hr block
- Carryover from Saturday → defer to Week 2's buffer (or cut)

---

## Daily breakdown

### Monday Apr 27 — Linear algebra warmup + numpy refresh ✅ DONE

- [x] 🌅 3B1B Ep 1 (Vectors) → 5 sentences logged
- [x] 💻 `daily-notebooks/week-01/01-numpy-refresher.ipynb` shipped
- [x] 📝 Anki: reviewed `00-Setup`, created `01-Math-Foundations`, 5 cards added
- [x] 🚀 Commits pushed (incl. dot product bug fix)
- **Mentor notes:** dot product bug caught + fixed. Broadcasting explanation needs sharpening but numerical answer correct. Streak: 5 days alive.

### Tuesday Apr 28 — Linreg intuition 🔄 PARTIAL

- [x] ✅ 🌅 3B1B Ep 2 (Linear combinations / span / basis) → 5 sentences in `concepts/week-01-prereading.md`
- [🔄] 💻 Notebook `02-linreg-from-scratch-part1.ipynb` — completed mini-topics 1–3 (intuition, equation, data gen). Mini-topics 4–5 (MSE function + eyeball fit) **carried to Wed Apr 29**.
- [🔄] 📝 Anki: 2 new cards (MSE, residual) **carried to Wed**
- [🔄] 🚀 Commit + push **carried to Wed** (single commit will cover full notebook)

**Slip reason:** First-time deep L1/L2 work on linreg intuition. Took extra time to build the symbol cheat sheet, sanity checks, and "why fake data" rationale. The depth was the right call — _calibration data, not failure_.

**Recovery:** Wed Apr 29 first 30 min before regular Wed agenda.

### Wednesday Apr 29 — Carryover + Gradient descent 🔄 PARTIAL

**🔄 Carryover from Tue (DONE):**

- [x] ✅ Mini-topic 4: MSE function + 4 sanity tests
- [x] ✅ Mini-topic 5: 3 eyeball guesses + plot + reflection
- [x] ✅ 2 Anki cards (MSE, residual)
- [x] ✅ Commit + push notebook 02

**Today's planned block (Wednesday, 9:00–10:30 PM):**

- [x] ✅ 🌅 3B1B Linear Algebra Ep 3 (Linear transformations & matrices) → 5 sentences in `concepts/week-01-prereading.md` (Q3 on determinant left blank — backfilled Thu)
- [⏭️] 💻 Notebook `03-linreg-from-scratch-part2.ipynb` (gradient descent) → **deferred to Thu**
- [x] ✅ 📝 Anki: reviewed all due cards
- [⏭️] 📝 Anki: 3 new cards (gradient, learning rate, gradient descent) → **deferred to Thu** (depends on notebook 03)
- [⏭️] 🚀 Commit + push for notebook 03 → **deferred to Thu**

**Slip reason:** Tue carryover (~30 min) + warmup ate the planned slot. Gradient descent is a heavy topic (L1→L4 takes ~75 min on its own); didn't want to rush it just to mark a checkbox. _Quality over speed — the rule is honest data, not fake-finishing._

**Recovery:** Thu Apr 30. Carryover load is significant (full notebook 03 + 3 new Anki + commit) — stack it BEFORE the planned Thu sklearn work. May need to defer Thu's sklearn notebook into Fri or trim Sat scope. **Velocity check ticking: 2/2 weekday slips so far this week** — if Thu also slips, trigger Saturday re-plan.

### Thursday Apr 30 — ⏭️ DEFERRED

- [⏭️] Entire slot deferred — low energy. Chose not to rush gradient descent foundation. All carryover items (Wed GD notebook + Thu bias-variance + Thu sklearn notebook 04) rolled forward to Fri/Sat/Sun.

### Friday May 1 — 🔄 PARTIAL (mentor session, no notebook code)

- [x] ✅ 🌅 Gradient descent **L1 (intuition)** in mentor session — answered the 5 questions in own words (gradient = direction of steepest uphill, why descent vs ascent, role of learning rate, blindfolded-on-bowl analogy)
- [x] ✅ 🌅 Gradient descent **L2 (math)** in mentor session — derived ∂MSE/∂w and ∂MSE/∂b step-by-step using chain rule + power rule + partial derivatives; sign sanity check on n=1 example passed
- [🔄] 💻 Notebook 03 code (L3) + 3 Anki cards + commit **carried to Sat May 2**
- [🔄] 💻 California housing notebook + MLflow → carried to Sun

**Slip reason:** Mentor walkthrough on intuition + derivation took the full slot. Foundation work — math is now in head, not just notes. _Worth the time._

**Recovery:** Sat May 2 — notebook code + Anki + commit (done ✅).

### Saturday May 2 — ✅ SHIPPED (gradient descent + scope cut)

- [x] ✅ Backfill Ep 3 Q3 (determinant geometry) in `week-01-prereading.md`
- [x] ✅ Notebook `03-linreg-from-scratch-part2.ipynb` — gradient descent from scratch (L3 code + L4 reflection)
  - 5 cells: imports + reuse data from notebook 02; predict + mse helpers; gradients function with 3 sanity tests; GD loop; loss curve plot
  - All sanity tests passed: gradient ≈ 0 at truth, negative at (0,0), positive at (10,10)
  - Final w_hat ≈ 3.0, b_hat ≈ 5.0, MSE near noise floor (~4)
  - L4 experiments: lr=0.1 diverged (NaN), lr=0.0001 crawled (didn't converge in 1000 epochs); reflection on convex bowl vs neural net non-convex surface
- [x] ✅ 3 Anki cards rewritten with mentor review (gradient = rate of change of loss w.r.t. each param; learning rate = step size; gradient descent = iterative w ← w − lr·dw)
- [x] ✅ **Velocity check + scope cut decision** logged in `04-decisions-log.md` (2026-05-02): merge sklearn + California into one Sun notebook, drop Ridge/Lasso to Week 2
- [x] ✅ Commit + push (`week-01: gradient descent from scratch (notebook 03) + Wed carryover cleared + scope cut`)
- [⏭️] Diagnostics notebook 06 (full) → dropped, replaced with 1 residual plot in Sun merged notebook
- [⏭️] Ridge/Lasso comparison → moved to Week 2 buffer
- [⏭️] Curiosity bucket review → next week
- [⏭️] Twitter thread #3 draft → moved to Sun

### Sunday May 3 — Bias-variance + merged sklearn/California/MLflow + teach-back + retro (~6.5hr) — POST-SCOPE-CUT PLAN

- [✅] 🌅 **15 min:** StatQuest **Bias-Variance Tradeoff** → 5 sentences in `concepts/week-01-prereading.md`
- [✅] 📝 **15 min:** Anki review (all 17 cards)
- [✅] 💻 **150 min:** **Merged notebook** → `daily-notebooks/week-01/04-sklearn-california-mlflow.ipynb`
  - **Part A (45 min):** sklearn on **same fake data** from notebook 02 → verify `LinearRegression()` gives w ≈ 3.0, b ≈ 5.0 (matches scratch GD); markdown: "sklearn in 3 lines = my scratch in 30"
  - **Part B (60 min):** Load `fetch_california_housing()` (8 features, ~20k rows) → 80/20 split → fit LinearRegression → compute R² + MSE on test set
  - **Part C (45 min):** Wrap A + B in MLflow runs (experiment `week-01-california-housing`); log params, metrics, model; 1 residual plot (predicted vs actual) for Part B
  - 2 new Anki cards: R-squared, residual plot
- [✅] ✍️ **120 min: NN3 Teach-back** → `concepts/week-01-teachback-linreg.md`
  - 800 words, "Linear Regression Explained to My Non-Technical Friend"
  - Cover: what problem it solves, gradient descent intuition, bias-variance, when it fails
  - **NO Google, NO ChatGPT** (same rule as baseline essay)
- [✅] 📖 **45 min: NN5 Weekly retro** → `weekly-logs/week-01-linreg.md` (use template)
  - **Required:** slip pattern analysis (3 weekday slips → calibration lesson for Week 2)
  - Score self on the 5 NN dimensions
- [⏩] 🐦 **30 min: NN2 Twitter thread #3** in `twitter-posts/week-01-thread.md` then post
  - Reuse teach-back content; 5–7 tweets
  - Hook: "Built linear regression from scratch in numpy this week. Here's what every gradient descent line actually does 🧵"
- [✅] 🚀 **15 min:** commit + push (single commit covering all Sun artifacts)
- [✅] 🎤 **30 min (optional):** Sunday mentor session — paste retro in chat

---

## ✅ Definition of Done — Week 1 (post-scope-cut May 2)

- [✅] 3B1B Eps 1, 2, 3 watched + notes (Ep 3 Q3 backfilled May 2)
- [✅] Notebook 01 (numpy refresher) shipped
- [✅] Notebook 02 (linreg part 1: data + MSE + eyeball fit) shipped
- [✅] Notebook 03 (gradient descent from scratch) shipped — **no sklearn used** ✅
- [✅] StatQuest Bias-Variance video + 5 sentences (Sun)
- [✅] Merged notebook 04 (sklearn on fake data + California housing + MLflow + 1 residual plot) (Sun)
- [✅] sklearn results match scratch GD within tolerance (Sun, in notebook 04 Part A)
- [✅] California housing R² + MSE logged in MLflow (Sun, in notebook 04 Part C)
- [✅] Teach-back essay ≥800 words, no AI assist (Sun)
- [⏩] Twitter thread #3 posted (Sun)
- [✅] Week 1 retro complete with slip pattern analysis (Sun)
- [✅] All 5 NN dimensions hit (NN1 commits ✅, NN2 Twitter Sun, NN3 teach-back Sun, NN4 Anki ✅ 17 cards, NN5 retro Sun)

**Dropped from original DoD (moved to Week 2 buffer or later):**

- ~~Notebooks 05 + 06 as separate files~~ → merged into notebook 04
- ~~Ridge + Lasso comparison (3 MLflow runs)~~ → Week 2 (regularization deep-dive)
- ~~Full diagnostics notebook with feature-importance experiments~~ → Week 2 buffer

## 🚫 Out of scope (resist the rabbit hole)

- Neural networks
- Polynomial regression / feature engineering depth
- Logistic regression (Week 2)
- Cross-validation (Week 2)
- Deep dive into eigenvalues/SVD (Week 3)
- Anything outside `daily-notebooks/week-01/`

## 🎯 Curiosity bucket rule

If you find something interesting mid-task → write it in `concepts/curiosity-bucket.md` → KEEP WORKING. Saturday afternoon has 30 min reserved for it.
