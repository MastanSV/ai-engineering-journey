# Current State — Snapshot

> > **Updated:** 2026-05-04 (Monday — Week 2 Day 1)
> > _Update this file at the end of every working session._

## Calendar

- **Current date:** May 4, 2026
- **Current week:** **2 of 32** (Day 1 of 7) — Week 1 closed
- **Current phase:** Phase 1 — Math + ML Foundations (Weeks 1–4)
- **Theme this week:** _When the line isn't enough_ (regularization + classification)
- **Target offer date:** December 2026

## Hardware

- GPU: NVIDIA Quadro T1000, 4.29 GB VRAM
- PyTorch 2.6.0 + CUDA 12.4 ✅
- Strategy: local for Phases 1–4, Colab/Kaggle for 7B+ in Phase 5

## Environment

- `C:\Temp\Learnings\ai-engineering-journey`
- Python 3.11 via uv, `.venv` active
- MLflow ✅ (used in Week 0)
- numpy + matplotlib ✅ (active in Week 1)
- Pre-commit hooks: ⬜ deferred to Week 1 buffer
- Ollama + llama3.2:3b ✅

## Public presence

- GitHub: github.com/MastanSV/ai-engineering-journey (public, pinned)
- Twitter/X: @mastan_ai (Tweet #1 + thread #2 done)
- HF Hub: mastanai
- Kaggle: valismastan
- Profile README: updated to "Week 1 — Linear Regression from Scratch" ✅

## Time commitment (locked)

- Mon–Fri: **9:00–10:30 PM** (1.5hr × 5 = 7.5hr)
- Sat + Sun: **6hr each**
- Weekly target: **19hr**

## Day-state tracking legend

- ✅ **Shipped** — completed within the planned day
- 🔄 **Carried** — partial; remainder rolled to next day (note why)
- ⏭️ **Deferred** — explicitly skipped, logged with reason
- ❌ **Skipped** — missed entirely, no recovery (rare; triggers re-plan)

## Week 2 progress (live)

- **Mon May 4** — Mentor session + Twitter thread #3 (Week 1 carryover) + Ridge intuition warmup
- **Tue May 5** — Ridge L1+L2 (intuition + math)
- **Wed May 6** — Notebook 05 Part A (standardize + Ridge + MLflow)
- **Thu May 7** — Notebook 05 Part B (Lasso + 3-way MLflow comparison)
- **Fri May 8** — Mentor: logistic L1+L2 (sigmoid, log-loss, derivation)
- **Sat May 9** — Notebook 06 (logistic from scratch) + Notebook 07 (k-fold CV, stretch) + Sat velocity check
- **Sun May 10** — Teach-back essay + Twitter thread #4 + Week 2 retro + Week 3 stub

## Slip ledger (Week 2 — live)

| Day          | State | Slipped item | Reason | Remainder (min) | Action |
| ------------ | ----- | ------------ | ------ | --------------- | ------ |
| _(none yet)_ |       |              |        |                 |        |

**Velocity check status:** _(updated each Saturday)_

## Week 1 results (final)

- Hours logged: **24 / 19 target** (over by 5hr — but 15 of 24 came from weekend; weekday execution was fragile)
- Notebooks shipped: 4/4 (numpy refresher, linreg part 1, GD from scratch, sklearn+California+MLflow)
- Teach-back: **7.5/10** (vs Week 0 baseline 4/10 — real-world examples for non-technical friend)
- Anki: 12 new cards, 7/7 daily reviews
- Slips: 3 weekday (Wed 🔄, Thu ⏭️, Fri 🔄) → recovered on weekend
- Mood 6/10 | Confidence Dec 2026: 7/10
- **Verdict:** Shipped scope (post-cut). Cascade pattern identified: low-energy day + first-time topic → avoidance next day → eats following day's slot.
- **Calibration rule for Week 2:** Carryover capped at 30 min; anything bigger pushes to Saturday (not next weekday).

## Week 0 results (final)

- Hours logged: 17 / 22 target
- Baseline EDA: **6.5/10** | Baseline essay: **4/10**
- Mood 7/10 | Confidence Dec 2026: 7/10
- **Verdict:** Full curriculum, no skipping

## Top gaps being addressed in Week 2

1. Regularization (Ridge L2 + Lasso L1) — main work
2. Standardization before comparing coefficients (Week 1 curiosity carryover)
3. Logistic regression from scratch (sigmoid + log-loss + GD)
4. Cross-validation (concept + 1 implementation)
5. Bias-variance precise definitions (essay gap from Week 1)
6. **Weekday execution discipline** — 30-min carryover cap is the experiment this week

## NN status (Week 2 — live)

- **NN1 GitHub commits:** target daily commits Mon–Sun
- **NN2 Twitter:** thread #3 (carryover) → Mon · thread #4 (regularization) → Sun · **must hit 2 threads, no zeros**
- **NN3 Teach-back:** regularization essay ≥800 words, no-Google → Sun May 10
- **NN4 Anki:** ~12 new cards target (Ridge, Lasso, L1, L2, sigmoid, log-loss, logistic, decision boundary, ROC, AUC, k-fold CV, standardization); 7/7 daily reviews
- **NN5 Sunday retro:** due Sun May 10 — first retro under 30-min carryover cap

## Decisions locked

- Capstone: Compliance Document QA System
- Learn-in-public: Twitter/X
- Mode: Brutal accountability (= honest data, not self-flagellation)
- DSA parallel: Week 9
- Networking: Week 5
- Applications: Week 16

## Last shipped

- **Apr 23–24:** Setup, accounts, public repo, Tweet #1
- **Apr 25:** CONTEXT system + baseline test (graded 6.5 + 4)
- **Apr 26:** Baseline fixes, MLflow hello-world, Week 0 retro, Week 1 plan locked
- **Apr 27:** Numpy refresher notebook + 3B1B Ep 1 notes + 5 Anki cards + dot product bug fix
- **Apr 28:** 3B1B Ep 2 (span/basis) notes; linreg part 1 partial (data gen + plot)
- **Apr 29:** Tue carryover completed (MSE + eyeball fit + 3-guess + 2 Anki cards + notebook 02 commit); 3B1B Ep 3 (linear transformations) notes; Anki reviewed
- **Apr 30:** _(deferred — low energy)_
- **May 1:** Mentor session — gradient descent L1 (intuition: gradient = direction, why descent vs ascent, role of lr) + L2 (derived ∂MSE/∂w and ∂MSE/∂b on paper using chain rule)
- **May 2:** Notebook 03 shipped — predict/mse/gradients (3 sanity tests pass) + GD loop converges to w≈3.0, b≈5.0 + loss curve + L4 experiments (lr=0.1 diverges, lr=0.0001 crawls); 3 Anki cards rewritten with mentor review; Ep 3 Q3 backfilled; Week 1 scope cut logged
- **May 3:** Notebook 04 (sklearn on fake data + California housing + MLflow + residual plot) shipped; teach-back essay (1170 words, no-Google) shipped; Week 1 retro shipped with slip-pattern analysis + 30-min carryover cap rule

## Blockers

- _(none)_

## Mood / Energy

- Apr 26: Mood 7/10, Confidence 7/10
- Apr 28: Mood 8/10, Confidence 7/10
- Apr 29: Mood 5/10, Confidence 7/10
- Apr 30: Mood 5/10, Confidence 7/10
- May 2: Mood 5/10, Confidence 7/10
- May 3: Mood 6/10, Confidence 7/10 (Week 1 close)

## Active rules

- No 10/10 self-scores
- 9:00–10:30 PM weekday slot is sacred
- Curiosity bucket pattern (capture, don't chase)
- Anki review = daily, before commit
- Every video paired with artifact (≥ 5 sentences or code)
- Videos ≤ 15 min each (no 90-min marathons)
- Profile sync rule: every Monday update `MastanSV/MastanSV/README.md`
- **(Apr 28):** Re-verify code correctness — when in doubt, manually compute one tiny example and check
- **(Apr 29):** **Layered learning method** — for every ML topic: L1 (intuition, 5 sentences) → L2 (math + symbol cheat sheet) → L3 (tiny code, sanity-tested) → L4 (reflection, bridge to next topic). Don't skip layers.
- **(Apr 29):** **3-state day tracking** — use ✅ / 🔄 / ⏭️ instead of binary done/not-done. Log slip reasons.
- **(Apr 29):** **Velocity check rule** — if ≥3 days/week show 🔄 OR total carryover > 1 hour → trigger re-plan on Saturday (cut scope, use buffer, or accept smaller week). Never fake-finish.
- **(May 3):** **30-min carryover cap** — at end of each weekday, write the carryover task. If it's >30 min, immediately move it to Saturday in the task file (not the next weekday). Stops Wed→Thu→Fri cascade.
