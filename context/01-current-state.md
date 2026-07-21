# Current State — Snapshot

> **Updated:** 2026-07-21 (Week 6 — Tuesday; planning Wed–Sun sprint)
> _Update this file at the end of every working session._

## Calendar

- **Current date:** July 21, 2026 (Tuesday — planning day)
- **Current week:** **6 of 32**
- **Current phase:** Phase 1 → Phase 2 transition (shipping P1, then Phase 2 begins)
- **Theme this week:** _Ship & Pivot_
- **Target offer date:** December 2026

## Resume note (2026-07-04)

- Journey **paused ~May 20** (mid-Week 4, after Day 2) and **resumed July 4**.
- Calendar re-anchored: **Jul 4 = Week 4 · Saturday**.
- ~6-week gap → front-loaded a **refresher block** before resuming P1.

## Hardware

- GPU: NVIDIA Quadro T1000, 4.29 GB VRAM
- PyTorch 2.6.0 + CUDA 12.4 ✅
- Strategy: local for Phases 1–4, Colab/Kaggle for 7B+ in Phase 5

## Environment

- `C:\Temp\Learnings\ai-engineering-journey`
- Python 3.11 via uv, `.venv-1` active
- MLflow ✅ (used in Weeks 0–5)
- numpy + matplotlib + sklearn + pandas ✅
- Ollama + llama3.2:3b ✅

## Public presence

- GitHub: github.com/MastanSV/ai-engineering-journey (public, pinned)
- Twitter/X: @mastan_ai (4 threads posted total)
- HF Hub: mastanai
- Kaggle: valismastan

## Time commitment (locked)

- Mon–Fri: **9:00–10:30 PM** (1.5hr × 5 = 7.5hr)
- Sat + Sun: **6hr each**
- Weekly target: **19hr**

## Day-state tracking legend

- ✅ **Shipped** — completed within the planned day
- 🔄 **Carried** — partial; remainder rolled to next day (note why)
- ⏭️ **Deferred** — explicitly skipped, logged with reason
- ❌ **Skipped** — missed entirely, no recovery (rare; triggers re-plan)

## Week 4 summary (closed)

- ✅ EDA + preprocessing + baseline model + MLflow
- ✅ L2 (Ridge) + L1 (Lasso) models trained
- ✅ 5-fold cross-validation (precision + ROC-AUC)
- ✅ MLflow experiment logging
- ✅ Confusion matrix + classification report
- ✅ Recall-vs-precision reconciliation (switched to recall-first for screening)
- 🔄 Evaluation suite (ROC curve, threshold sweep, comparison table) → carried to Week 5

## Week 5 summary (closed)

- ✅ Evaluation suite complete (ROC curve, threshold sweep, comparison table)
- ✅ Best-model selection + MLflow finalized (recall-first + ROC-AUC justification)
- ✅ Feynman check: regularized model vs baseline for heart disease
- ✅ Logistic teach-back complete: sigmoid, log-loss, gradient, decision boundary, works/fails, regularization (≥800 words)
- ✅ Anki cards week-04 created (8 cards: confusion matrix, precision, recall, F1, ROC-AUC, sigmoid, log-loss, threshold)
- 🔄 Gradio app + HF deploy → carried to Week 6
- 🔄 README polish + Loom + Twitter #5 → carried to Week 6
- 🔄 Phase 1 gate + retro → carried to Week 6

## Week 6 progress (live)

- **Mon Jul 21** — ❌ Skipped (no session)
- **Tue Jul 22** — Planning day (schedule created)
- **Wed Jul 23** — Gradio app build
- **Thu Jul 24** — Gradio app finish + local test
- **Fri Jul 25** — HF Space deploy
- **Sat Jul 26** — README + Loom + Twitter + Phase 1 gate + retro
- **Sun Jul 27** — Phase 2 kickoff (pre-reading + perceptron notebook)

## NN status (Week 6 — live)

- **NN1** GitHub commits: 0 / target ≥4 (Wed, Thu, Fri, Sat)
- **NN2** Twitter: 0 / 1 thread — `week-05-thread-p1.md` planned for Sat Jul 26
- **NN3** Teach-back: ✅ done — `week-04-teachback-logistic_regression.md` complete
- **NN4** Anki: ✅ `anki-cards-week-04.tsv` created; daily reviews active
- **NN5** Retro: not done — `retro-week-05.md` planned Sat Jul 26
