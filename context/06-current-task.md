# Current Task — Saturday April 25, 2026

> **Replace this file at the start of every new chat session/topic.**

## Today's Goal

Complete and submit the baseline test (Part 1 EDA + Part 2 Feynman) by end of day. Get brutal grading from mentor. Use the score to calibrate the Week 1 starting point.

---

## Part 1 — Titanic numpy/pandas EDA (2 hr hard stop)

**Path:** `daily-notebooks/baseline-test/part1_eda.ipynb`
**Dataset:** `seaborn.load_dataset("titanic")` saved to `titanic.csv`

### Setup cell (paste at top of notebook)

```python
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = sns.load_dataset("titanic")
df.to_csv("titanic.csv", index=False)
df = pd.read_csv("titanic.csv")
df.head()
```

### Section A — Loading & Inspection (15 min)

1. Load `titanic.csv` into `df`.
2. Print: shape, column names, dtypes, `head(5)`, `tail(5)`.
3. How many rows have any missing values? Which columns have missing values, and what fraction for each?
4. Memory footprint of the DataFrame? Optimize one column's dtype to reduce memory.

### Section B — Descriptive Stats (20 min)

5. Overall survival rate (%)?
6. Mean age of survivors vs non-survivors. Is the difference big?
7. Survival rate by class (1st/2nd/3rd) + bar chart.
8. Survival rate by sex + bar chart.
9. Survival rate by class AND sex (grouped). Surprising patterns?

### Section C — Feature Engineering (25 min)

10. Create `age_group` with bins: Child (<13), Teen (13–19), Adult (20–59), Senior (60+). Handle missing ages explicitly.
11. Create `family_size` = `sibsp` + `parch` + 1. Survival rate by `family_size`?
12. Extract title (Mr / Mrs / Miss / etc.) from `name` via string ops. Top 5 titles.

### Section D — Outliers & Distributions (20 min)

13. Histogram of `fare`. Normally distributed? Skewed?
14. Identify fare outliers via IQR. How many?
15. Age distribution: survivors vs non-survivors (overlay or side-by-side). Observations?

### Section E — Interpretation (15 min) ← the real test

16. Markdown cell: 5 bullets summarizing findings, briefing-a-PM style. No jargon. What to investigate next?
17. Markdown cell: 3 things I do NOT yet know how to do, that are needed to turn this EDA into a predictive model. **Honest.**

### Rules

- ⏱️ **2-hour hard stop.**
- ✅ Syntax lookups OK.
- ❌ Solution lookups NOT OK.
- ✅ Add markdown explanation cells between code blocks.

### Grading rubric (mentor)

- Correctness of answers
- Code cleanliness (pandas idioms, no unnecessary loops)
- Plot quality (titles, labels, clarity)
- Q17 honesty (shallow self-assessment → harder grilling)

---

## Part 2 — Feynman Essay (1 hr hard stop)

**Path:** `concepts/baseline-feynman-what-is-ml.md`
**Title:** _"What Is Machine Learning — Explained to My Non-Technical Friend"_
**Word count:** 500 ± 50 words

### Cover at least 6 of these 8

1. What problem does ML solve that regular programming doesn't?
2. A concrete everyday example (Netflix, spam filter, etc.) in friend's language.
3. What "training" means in plain English.
4. Supervised vs unsupervised — example of each.
5. Why we split into train/test ("studying vs exam" analogy is fine).
6. What "overfitting" means — relatable metaphor.
7. Why ML is suddenly everywhere NOW (hardware / data / algorithms?).
8. One genuine limitation / scary thing about ML.

### Rules

- ❌ NO Google. NO ChatGPT / Claude / Gemini. NO copy-paste from textbooks.
- ⏱️ **60-minute hard stop.**
- ✅ Your raw understanding, in your own words.

### Grading rubric (mentor)

- Clarity (can a non-technical reader follow it?)
- Honesty (no hand-waving)
- Analogies (do they actually click?)
- Coverage (≥ 6 of 8 topics)
- Depth-without-jargon

---

## Deliverables for mentor (paste in chat when done)

1. GitHub link to `part1_eda.ipynb`
2. GitHub link to `baseline-feynman-what-is-ml.md` OR full essay text
3. How long each part actually took (be honest)
4. Self-rated confidence 1–10 BEFORE seeing my grade

---

## After grading: define

- Score on Part 1: \_\_ / 10
- Score on Part 2: \_\_ / 10
- Week 1 start point: full curriculum vs accelerated
- Top 3 gaps to address in Week 1

---

## Out of scope today

- MLflow hello-world (Sunday)
- Week 1 pre-reading (Sunday)
- Sunday retro (Sunday)
- Pre-commit hooks (after baseline tests, only if time allows)
- HF dummy push (after baseline tests, only if time allows)
