# Current State — Snapshot

> **Updated:** 2026-07-04 (Week 4 — RESUMED after pause; today = Week 4 · Saturday)
> _Update this file at the end of every working session._

## Calendar

- **Current date:** July 4, 2026 (treated as **Saturday** — 6hr day)
- **Current week:** **4 of 32** (resumed mid-sprint after ~6-week pause) — Week 3 closed (clean)
- **Current phase:** Phase 1 — Math + ML Foundations (Weeks 1–4)
- **Theme this week:** _Phase 1 Finish — Ship P1_
- **Target offer date:** December 2026

## Resume note (2026-07-04)

- Journey **paused ~May 20** (mid-Week 4, after Day 2) and **resumed July 4**.
- Calendar re-anchored: **today = Week 4 · Saturday**. Remaining Week 4 work re-flows across this weekend + next week (Jul 4 → Jul 12).
- ~6-week gap → today front-loads a **refresher block** (re-read notes, rerun Anki, rerun notebooks 05–07) before resuming P1.
- Week hours (re-anchored): Sat 6 + Sun 6 + Mon–Fri 7.5 = **19.5hr** (on target).

## Hardware

- GPU: NVIDIA Quadro T1000, 4.29 GB VRAM
- PyTorch 2.6.0 + CUDA 12.4 ✅
- Strategy: local for Phases 1–4, Colab/Kaggle for 7B+ in Phase 5

## Environment

- `C:\Temp\Learnings\ai-engineering-journey`
- Python 3.11 via uv, `.venv` active
- MLflow ✅ (used in Weeks 0–3)
- numpy + matplotlib ✅
- Ollama + llama3.2:3b ✅
- ⚠️ Re-verify env on resume (first task today): confirm imports numpy/pandas/sklearn/matplotlib/mlflow still run.

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

## Week 4 progress (live — re-anchored)

- **Day 1 (pre-pause)** — ✅ Classification-metrics notebook (`daily-notebooks/week-04/01-classification-metrics.ipynb`) + P1 scoping. **P1 = Heart Disease classification** (README written: precision + ROC-AUC priority)
- **Day 2 (pre-pause)** — 🔄 P1 notebook started (`projects/05_P1_Tabular_ML/Heart_Disease_Dataset.ipynb`, `heart.csv`) — EDA/preprocessing incomplete
- **⏸️ PAUSE ~May 20 → ▶️ RESUME July 4**
- **Sat Jul 4** — refresher + finish EDA/preprocessing + baseline model (today)
- **Sun Jul 5** — models + 5-fold CV + evaluation suite
- **Mon Jul 6** — best-model selection + MLflow finalize
- **Tue Jul 7** — logistic teach-back (part 1)
- **Wed Jul 8** — finish teach-back + Anki week-04
- **Thu Jul 9** — Gradio app.py
- **Fri Jul 10** — HF Space deploy + test
- **Sat Jul 11** — README quality bar + Loom + Twitter thread #5 + Phase 1 gate check
- **Sun Jul 12** — Week 4 retro + Phase 2 prereading + Week 5 plan

## NN status (Week 4 — live)

- **NN1** GitHub commits: _ / (count days actually worked) _(verify from git log)\_
- **NN2** Twitter: 0 / 1 thread — `week-04-thread-p1.md` not created yet
- **NN3** Teach-back: not done — `week-04-teachback-logistic.md` not created yet
- **NN4** Anki: 0 week-04 cards (`anki-cards-week-04.tsv` not created); daily reviews resume today
- **NN5** Sunday retro: not done — `retro-week-04.md` not created yet
