# Current State — Snapshot

> **Updated:** 2026-05-02 (Saturday — Week 1 Day 6)
> _Update this file at the end of every working session._

## Calendar

- **Current date:** May 2, 2026
- **Current week:** **1 of 32** (Day 6 of 7)
- **Current phase:** Phase 1 — Math + ML Foundations (Weeks 1–4)
- **Theme this week:** _From line to model_
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

## Week 1 progress (live)

- **Mon Apr 27 ✅** — 3B1B Ep 1 + numpy refresher + 5 Anki cards (incl. dot product bug fix)
- **Tue Apr 28 🔄** — 3B1B Ep 2 done (span/basis); linreg part 1 partial (data + plot done; MSE + eyeball fit + Anki + commit carried to Wed)
- **Wed Apr 29 🔄** — Tue carryover ✅ + 3B1B Ep 3 (linear transformations) ✅ + Anki review ✅; gradient descent notebook + 3 new Anki cards + commit **carried to Thu**
- **Thu Apr 30 ⏭️** — Slot deferred (low energy); gradient descent rolled forward
- **Fri May 1 🔄** — Mentor session covered gradient descent **L1 (intuition) + L2 (derivation)**; notebook code + Anki + commit carried to Sat
- **Sat May 2 ✅** — Notebook 03 (gradient descent from scratch, L3 code + L4 reflection) shipped + 3 Anki cards + Ep 3 Q3 (determinant) backfilled + Week 1 scope cut decided ← TODAY
- **Sun May 3** — Bias-variance + merged sklearn/California/MLflow notebook + teach-back essay + retro + Twitter thread (post-scope-cut plan)

## Slip ledger (Week 1)

| Day        | State | Slipped item                                                                      | Reason                                                                                            | Recovered                                                   |
| ---------- | ----- | --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| Tue Apr 28 | 🔄    | MSE func + eyeball fit + Anki + commit                                            | Underestimated time for L1/L2 depth on first ML topic                                             | Wed Apr 29 ✅                                               |
| Wed Apr 29 | 🔄    | Gradient descent notebook 03 + 3 Anki cards + commit; Ep 3 Q3 (determinant) blank | Tue carryover + warmup ate the slot; gradient descent needs full L1→L4 cycle, didn't want to rush | Sat May 2 ✅                                                |
| Thu Apr 30 | ⏭️    | Entire Thu slot (GD carryover + bias-variance + sklearn notebook 04)              | Low energy; chose not to rush gradient descent foundation                                         | GD recovered Sat May 2; bias-variance + sklearn → Sun May 3 |
| Fri May 1  | 🔄    | Notebook 03 code + Anki + commit; California housing + MLflow                     | Mentor session covered L1 (intuition) + L2 (derivation); code/Anki carried to Sat                 | Code recovered Sat May 2; California → Sun May 3            |

**Velocity check status: 3 weekday slips → re-plan triggered Sat May 2.** Scope cut logged in `04-decisions-log.md` (2026-05-02): merge sklearn (notebook 04) + California housing (notebook 05) + lite diagnostics into one Sunday notebook; drop Ridge/Lasso (Week 2); drop full diagnostics notebook 06 (Week 2 buffer); bias-variance video → Sun warmup.

**Calibration lesson:** First-time ML topics need ~2× the time I estimated. For Week 2 plan, budget 2 days per "from-scratch" notebook.

## Week 0 results (final)

- Hours logged: 17 / 22 target
- Baseline EDA: **6.5/10** | Baseline essay: **4/10**
- Mood 7/10 | Confidence Dec 2026: 7/10
- **Verdict:** Full curriculum, no skipping

## Top gaps being addressed in Week 1

1. Pandas/numpy idioms (active practice — 2/6 notebooks done)
2. Core ML vocabulary (loss, gradient, generalization, bias, variance)
3. Plot hygiene (figsize, labels, comparable axes, narration)
4. **Time estimation calibration** (NEW — surfaced by Tue 🔄)

## NN status (Week 1 — live)

- **NN1 GitHub commits:** 🔥 streak alive — Sat commit covers notebook 03 + Q3 backfill + context updates
- **NN2 Twitter:** thread #3 → Sunday (was Sat — moved due to scope cut)
- **NN3 Teach-back:** linreg essay due Sun May 3
- **NN4 Anki:** 17 cards total (14 + 3 new: gradient, learning rate, gradient descent); reviews on track
- **NN5 Sunday retro:** due May 3

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

## Blockers

- _(none)_

## Mood / Energy

- Apr 26: Mood 7/10, Confidence 7/10
- Apr 28: Mood 8/10, Confidence 7/10
- Apr 29: Mood 5/10, Confidence 7/10
- Apr 30: Mood 5/10, Confidence 7/10
- May 2: Mood 5/10, Confidence 7/10

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
