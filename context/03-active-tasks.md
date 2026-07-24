# Active Tasks — Week 6 Sprint (Jul 22–27, 2026)

## Sprint goal

Ship P1 on HF Spaces (all 6 quality-bar criteria), clear Phase 1 gate, and kick off Phase 2 (DL + Transformers).

## Theme: **"Ship & Pivot"**

## Context

- Week 5 completed: evaluation suite, best-model selection, MLflow finalize, teach-back (6 blocks, ≥800 words), Anki cards week-04.
- Week 6 carries the remaining P1 delivery tasks (Gradio app, deploy, README, Loom, Twitter, gate, retro) + Phase 2 kickoff.

## P1 decision (logged Week 4 Day 1)

**Heart Disease classification.** Dataset `heart.csv` (14-feature subset, target 0/1). Primary metric **recall** (false negative = missed sick patient) + **ROC-AUC**. Approach: Logistic Regression with Ridge/Lasso regularization. Scope in `projects/05_P1_Tabular_ML/README.md`.

## Time budget

- Tue (planning only) | Wed–Fri 1.5hr × 3 = 4.5hr | Sat–Sun 6hr × 2 = 12hr | **Available: 16.5hr**

## Active rules

- **30-min carryover cap:** weekday carryover >30 min → push to Saturday, not next weekday.
- **20-min stuck rule:** stuck >20 min → switch resource. Never close laptop without trying 1 alternative.
- **Feynman learning checklist:** before marking a concept "learned," write a 3-sentence zero-jargon explanation. If you can't → re-study. Only then add the Anki card.

---

## Daily breakdown

> **Self-contained rule:** every day's block contains everything needed to execute.

---

### Wed Jul 22 (1.5hr, 9:00–10:30 PM) — Gradio app build

- [x] 15 min — Anki review
- [x] 60 min — Build `projects/05_P1_Tabular_ML/app.py`:
  - Load best model pipeline (export from notebook via `joblib.dump` if not already saved)
  - Gradio interface: 14 feature inputs (sliders/dropdowns) → prediction + probability bar
  - Add title, description, example inputs
- [x] 15 min — Verify model file exists, loads cleanly, returns prediction
- [x] 🚀 Commit: `week-06: P1 Gradio app initial build`

**Exit criteria:** `app.py` exists, model loads, returns a prediction on dummy input.

---

### Thu Jul 23 (1.5hr, 9:00–10:30 PM) — Gradio app finish + local test

- [x] 15 min — Anki review
- [x] 45 min — Local end-to-end test: `python app.py`
  - Test edge cases: all-zero inputs, max-range inputs, typical healthy/sick patient
  - Fix UI issues (labels, slider ranges, formatting)
- [x] 20 min — Prepare deploy files: `requirements.txt` (gradio, scikit-learn, joblib, pandas), verify model file < 50MB
- [x] 10 min — 🚀 Commit: `week-06: P1 Gradio app tested + deploy-ready`

**Exit criteria:** App runs clean locally, edge cases pass, deploy files ready.

---

### Fri Jul 24 (1.5hr, 9:00–10:30 PM) — HF Space deploy

- [x] 15 min — Anki review
- [x] 60 min — HF Space deploy:
  - Create Space `mastanai/p1-tabular-ml` (Gradio SDK)
  - Push `app.py`, model file, `requirements.txt`
  - Verify live URL works end-to-end
- [x] 15 min — Fix deployment issues (dependency pins, file paths)
- [x] 🚀 Commit: `week-06: P1 deployed on HF Space`

**Exit criteria:** Live HF URL returns prediction for test input.

---

### Sat Jul 25 (6hr) — README + Loom + Twitter + gate + retro

#### Morning block (3hr)

- [ ] 15 min — Anki review
- [ ] 90 min — README polish (`projects/05_P1_Tabular_ML/README.md`):
  - Problem statement + approach + dataset description
  - Results table (real eval numbers: precision, recall, F1, ROC-AUC per model)
  - Architecture diagram (Excalidraw: data → preprocessing → model → threshold → prediction)
  - Live HF demo link + local setup instructions
- [ ] 60 min — Loom walkthrough (≤3 min):
  - Script first: problem → approach → code highlights → results → live demo
  - Record (max 2 takes), upload, embed link in README
- [ ] 15 min — Buffer

#### Afternoon block (3hr)

- [ ] 45 min — Twitter thread #5 → `twitter-posts/week-05-thread-p1.md`:
  - Hook → problem → what I built → key insight → eval results → live link → CTA
  - POST LIVE, save URL
- [ ] 30 min — Phase 1 gate check (all 6 must pass):
  - ✅ Live demo on HF Space
  - ✅ 3-min Loom in README
  - ✅ Architecture diagram
  - ✅ Real eval numbers
  - ✅ Twitter thread
  - ✅ Solves a real problem (heart disease screening)
- [ ] 60 min — Week 5/6 retro → `weekly-logs/retro-week-05.md`:
  - What shipped, what slipped (Sat/Sun carryover), velocity, root cause, lessons
- [ ] 30 min — Log Phase 1 gate result in `context/04-decisions-log.md`
- [ ] 15 min — 🚀 Commits: `week-06: P1 shipped + Phase 1 gate passed` + `week-06: retro + twitter thread`

**Exit criteria:** All 6 quality-bar items pass. Retro written. Twitter posted. Gate logged.

---

### Sun Jul 26 (6hr) — Phase 2 Kickoff: Deep Learning Foundations

#### Morning block (3hr)

- [ ] 15 min — Anki review
- [ ] 45 min — Phase 2 pre-reading: neural network fundamentals
  - Topics: perceptron, multi-layer networks, activation functions (ReLU, tanh), forward pass
  - Source: 3Blue1Brown neural network series (Ch 1–2) OR fast.ai Practical DL Ch 4
- [ ] 90 min — Phase 2 pre-reading continued:
  - Backpropagation intuition (chain rule, computational graphs)
  - PyTorch basics: tensors, autograd, `nn.Module`
- [ ] 30 min — Notes: `concepts/week-06-prereading.md` (key takeaways, questions)

#### Afternoon block (3hr)

- [ ] 90 min — Create `daily-notebooks/week-06/01-perceptron-from-scratch.ipynb`:
  - Implement single perceptron (AND/OR gate) with numpy
  - Forward pass + manual gradient update
  - Visualize decision boundary
- [ ] 60 min — Scope P2 (nanoGPT): break into weekly milestones for Weeks 7–9
- [ ] 30 min — Update context files: `01-current-state.md`, `03-active-tasks.md`, `06-current-task.md`
- [ ] 🚀 Commit: `week-06: Phase 2 kickoff — perceptron from scratch`

**Exit criteria:** Pre-reading done, perceptron notebook works, P2 milestones drafted, context updated.

---

## Non-negotiables this week

| #   | Rule           | Check                           |
| --- | -------------- | ------------------------------- |
| NN1 | GitHub commits | ≥4 commits (Wed, Thu, Fri, Sat) |
| NN2 | Twitter        | Thread #5 posted by Sat         |
| NN3 | Teach-back     | ✅ Already complete             |
| NN4 | Anki           | Daily reviews (no skip)         |
| NN5 | Retro          | `retro-week-05.md` written Sat  |

## Risk & mitigation

| Risk                                | Mitigation                                               |
| ----------------------------------- | -------------------------------------------------------- |
| HF deploy fails (dependency hell)   | 30-min buffer Fri; fallback: fix Sat morning first thing |
| Loom takes too long (perfectionism) | Script first, max 2 takes, ship imperfect                |
| Phase 2 pre-reading rabbit hole     | Hard timebox 2.5hr; goal = intuition, not mastery        |
| Model export missing from notebook  | Wed first 15 min: check if `.pkl` exists, export if not  |

## Phase 1 → Phase 2 transition checklist

- [ ] P1 live on HF Space
- [ ] All 6 quality-bar items passed
- [ ] Phase 1 gate logged in `04-decisions-log.md`
- [ ] Phase 2 pre-reading complete (NN basics + backprop + PyTorch)
- [ ] P2 scope defined (nanoGPT milestones)
