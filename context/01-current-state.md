# Current State — Snapshot

> **Updated:** 2026-04-29 (Wednesday — Week 1 Day 3)
> _Update this file at the end of every working session._

## Calendar

- **Current date:** April 29, 2026
- **Current week:** **1 of 32** (Day 3 of 7)
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
- **Tue Apr 28 🔄** — 3B1B Ep 2 done (span/basis); linreg part 1 partial: data gen + plot done. MSE function + eyeball fit + 2 Anki cards + commit **carried to Wed**. _Slip reason: first-time deep L1/L2 work on linreg intuition took longer than 75 min budget. Calibration data, not failure._
- **Wed Apr 29** — Tue carryover ✅ (MSE + eyeball fit + Anki + commit) + 3B1B Ep 3 + linreg part 2 (gradient descent) ← TODAY
- **Thu Apr 30** — Bias-variance video + sklearn LinearRegression
- **Fri May 1** — Linreg main video + California housing + MLflow
- **Sat May 2** — Diagnostics + Ridge/Lasso comparison + Twitter draft
- **Sun May 3** — Teach-back essay + retro + mentor session

## Slip ledger (Week 1)

| Day        | State | Slipped item                           | Reason                                                | Recovered     |
| ---------- | ----- | -------------------------------------- | ----------------------------------------------------- | ------------- |
| Tue Apr 28 | 🔄    | MSE func + eyeball fit + Anki + commit | Underestimated time for L1/L2 depth on first ML topic | Wed Apr 29 ✅ |

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

- **NN1 GitHub commits:** 🔥 streak alive (commit pending tonight)
- **NN2 Twitter:** thread #3 due Saturday
- **NN3 Teach-back:** linreg essay due Sunday May 3
- **NN4 Anki:** 7 cards in `00-Setup` + 7 cards in math/numpy refresher (14 total); daily reviews on track
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
- **Apr 28:** 3B1B Ep 2 (span/basis) notes + linreg scratch part 1 partial (data gen + plot)
- **Apr 29:** _(today — pending: Tue carryover + Day 3 work)_

## Blockers

- _(none)_

## Mood / Energy

- Apr 26: Mood 7/10, Confidence 7/10
- Apr 28: _(self-rate tonight — pending)_
- Apr 29: _(self-rate tonight — pending)_

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
