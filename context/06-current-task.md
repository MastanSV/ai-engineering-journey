# Current Task — Sunday April 26, 2026

> **Replace this file at the start of every new chat session/topic.**

## Today's Goal

Close out Week 0. Ship Sunday deliverables (MLflow hello-world, weekly retro, Twitter thread #2). Walk into Monday with a graded baseline + Week 1 sprint plan locked.

---

## Carryover from Saturday (close these FIRST, ~30 min)

### Part 1 EDA — Verdict & Next Step

Mentor graded Part 1 at **6.5/10**. Three bug fixes shipped:

- ✅ Q3 denominator fix (`/df.shape[1]`)
- ✅ Q12 correlation heatmap added
- ✅ Q17 self-assessment markdown cell added

- [ ] Final commit + push: `baseline part 1: Q3 fix + Q12 heatmap + Q17 self-assessment`

### Part 2 Essay — Errata Action (DO NOT REWRITE BODY)

Mentor graded Part 2 at **4/10**. Essay preserved as Week 0 reference point. Will rewrite Week 4.

- ✅ Append `## Errata (added Apr 26)` section to `part02_whatisml.txt` listing the 5 errors **in your own words**:
  1. Plain English ≠ ML in general (only LLMs)
  2. Supervised vs unsupervised = labels vs no labels (NOT data type)
  3. Train/test split = held-out unseen exam, not "study more chapters"
  4. Overfitting = memorizing noise, not just "fails on test"
  5. ML doesn't "work on its own" — humans in every loop
- ✅ Add 4 Anki cards (see Part 2 grading notes in chat) → `00-Setup` deck
- ✅ Commit + push: `baseline part 2: errata + lessons learned`

---

## Sunday primary work

### 🔴 Must

- [ ] **MLflow hello-world** — `daily-notebooks/mlflow-hello/01_first_run.ipynb`
  - Install: `uv pip install mlflow`
  - Log a dummy sklearn LogisticRegression on iris: params, metrics (accuracy), model artifact
  - Launch UI: `mlflow ui` — screenshot the run page → save to repo
  - Commit: `mlflow: first tracked run`

- [ ] **Week 1 pre-reading** (~90 min, take notes in `concepts/week-01-prereading.md`)
  - 3Blue1Brown — Linear Algebra Essence, episodes 1, 2, 3
  - StatQuest — Bias-Variance Tradeoff
  - StatQuest — Linear Regression (main video)
  - For each: 3 bullets in your own words + 1 question you still have

- [ ] **Weekly retro** — `weekly-logs/week-00-setup.md`
  - Use template (see below)
  - Honest scores, actual hours logged, what slipped, what worked

- [ ] **🎤 Sunday retro with mentor** — paste retro file in chat, get Week 1 sprint plan back

### 🟡 Should

- [ ] Twitter thread #2 — Week 0 wrap → draft in `twitter-posts/week-00-thread.md`
  - Hook: "Week 0 of becoming an AI Engineer in 8 months. Here's what brutally honest baseline grading looks like 🧵"
  - 5–7 tweets. Include the 6.5/10 and 4/10 scores. Vulnerability = engagement.
- [ ] Pre-commit hooks (`ruff`, `ruff-format`, `detect-private-key`, `nbqa-ruff`)
- [ ] 3 Anki reviews due today

---

## Weekly retro template (paste into `weekly-logs/week-00-setup.md`)

```markdown
# Week 00 — Setup & Baseline (Apr 23–26, 2026)

## Hours logged

- Thu: ** / Fri: ** / Sat: ** / Sun: **
- **Total: \_\_ hrs** (target was 18–22)

## NN scorecard

- NN1 GitHub commits: \_\_ / 4 days
- NN2 Twitter: \_\_ / 1 thread
- NN3 Teach-back: ✅ Feynman essay (graded 4/10)
- NN4 Anki: ** cards added, ** reviews completed
- NN5 Sunday retro: ✅ this doc

## Baseline scores

- Part 1 EDA: 6.5/10
- Part 2 Essay: 4/10

## What worked

-

## What slipped

-

## Top 3 gaps for Week 1

1.
2.
3.

## Mood/energy (1–10): \_\_

## Confidence I'll hit Dec 2026 offer (1–10): \_\_
```
