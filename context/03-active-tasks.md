# Active Tasks — Week 1 Sprint (Apr 27 – May 3, 2026)

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

### Thursday Apr 30 — Carryover (gradient descent) + Bias-Variance + sklearn

**🔄 Carryover from Wed (do FIRST, ~75 min):**

- [ ] Backfill Ep 3 Q3 (determinant geometry) in `week-01-prereading.md`
- [ ] Notebook `03-linreg-from-scratch-part2.ipynb` — gradient descent in pure numpy (L1→L4 method)
- [ ] 3 new Anki cards (gradient, learning rate, gradient descent)
- [ ] Commit + push notebook 03

**Today's originally planned block (Thursday, 9:00–10:30 PM):**

- [ ] 🌅 **15 min:** StatQuest Bias-Variance Tradeoff → 5 sentences
- [ ] 💻 **45 min:** Notebook → `daily-notebooks/week-01/04-linreg-sklearn.ipynb`
  - Same fake data, now use `sklearn.linear_model.LinearRegression`
  - Verify `w*`, `intercept*` match scratch implementation (within tolerance)
  - Document: "What sklearn does in 3 lines, my scratch code did in 30"
- [ ] 📝 **20 min:** Anki review + 2 new cards (bias, variance)
- [ ] 🚀 **10 min:** commit + push

**⚠️ Realistic load tonight: ~165 min** (carryover 75 + planned 90). Total budget is only 90 min. **Decision tree before starting:**

1. **Best case (high energy):** Do gradient descent carryover tonight → defer bias-variance + sklearn notebook to Fri. Adjust Fri's California housing work to Sat.
2. **Realistic case:** Do gradient descent (notebook 03) only tonight, mark bias-variance + sklearn notebook 04 as deferred to Fri.
3. **Low energy:** Do warmup + first 2 mini-topics of gradient descent only. Mark rest 🔄.

**Pick option before starting. Log decision here.**

### Friday May 1 — Real dataset + MLflow integration

- 🌅 **15 min:** StatQuest Linear Regression (main video) → 5 sentences
- 💻 **45 min:** Notebook → `daily-notebooks/week-01/05-real-dataset.ipynb`
  - Load `sklearn.datasets.fetch_california_housing()` (8 features, 20k rows)
  - 80/20 train/test split, fit LinearRegression, compute R², MSE
  - Log to MLflow with experiment name `week-01-california-housing`
- 📝 **20 min:** Anki review + 1 new card (R-squared)
- 🚀 **10 min:** commit + push

### Saturday May 2 — Diagnostics + portfolio polish (6hr)

- 🌅 **30 min:** Anki review (all Week 1 cards)
- 💻 **2hr:** Notebook → `daily-notebooks/week-01/06-diagnostics.ipynb`
  - Residual plots (predicted vs actual, residuals vs predicted)
  - Identify which features matter (coefficient magnitudes)
  - Try removing a feature, re-train, compare MSE
  - Markdown narration throughout — recruiter-readable
- 💻 **2hr:** Try TWO different models on California housing (still Week 1 territory)
  - `Ridge` (regularized linreg)
  - `Lasso` (sparsity-inducing)
  - Log both runs to MLflow → compare in UI side-by-side
- 📝 **30 min:** Curiosity bucket review — pick 1 item, explore for 30 min
- 🐦 **30 min:** Draft Twitter thread #3 in `twitter-posts/week-01-thread.md`
  - Hook idea: "Built linear regression from scratch in numpy this week. Here's what every gradient descent line actually does 🧵"
- 🚀 **30 min:** commit + push, screenshots

### Sunday May 3 — Teach-back + retro (6hr)

- 🌅 **30 min:** Anki review
- ✍️ **2hr:** **NN3 Teach-back** → `concepts/week-01-teachback-linreg.md`
  - 800 words, "Linear Regression Explained to My Non-Technical Friend"
  - Cover: what problem it solves, gradient descent intuition, bias-variance, when it fails
  - NO Google, NO ChatGPT (same rule as baseline essay)
- 💻 **1.5hr:** Optional: try California housing on **Kaggle** — submit to a beginner competition if one fits
- 📝 **30 min:** Anki — clean up cards, mark mature ones
- 📖 **1hr:** **Weekly retro** → `weekly-logs/week-01-linreg.md` (use template)
- 🐦 **30 min:** Post Twitter thread #3
- 🎤 **30 min:** Sunday mentor session — paste retro in chat

---

## ✅ Definition of Done — Week 1

- [ ] 5 weekday warmup videos watched + 5 sentences each ← 1/5 done (Ep 1)
- [ ] Notebooks 01–06 committed in `daily-notebooks/week-01/` ← 1/6 done
- [ ] Linear regression implemented from scratch (gradient descent, no sklearn)
- [ ] Same problem solved with sklearn — results match
- [ ] California housing trained, R² and MSE in MLflow
- [ ] Ridge + Lasso comparison logged in MLflow (3 runs minimum)
- [ ] Diagnostic plots committed (residuals)
- [ ] Teach-back essay written (≥ 800 words, no AI assist)
- [ ] Twitter thread #3 posted
- [ ] Week 1 retro complete
- [ ] All 5 NN dimensions hit (commits, Twitter, teach-back, Anki daily, Sunday retro)

## 🚫 Out of scope (resist the rabbit hole)

- Neural networks
- Polynomial regression / feature engineering depth
- Logistic regression (Week 2)
- Cross-validation (Week 2)
- Deep dive into eigenvalues/SVD (Week 3)
- Anything outside `daily-notebooks/week-01/`

## 🎯 Curiosity bucket rule

If you find something interesting mid-task → write it in `concepts/curiosity-bucket.md` → KEEP WORKING. Saturday afternoon has 30 min reserved for it.
