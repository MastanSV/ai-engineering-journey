# Current Task — Week 1 Day 1 (Monday April 27, 2026)

> **Replace this file at the start of every new chat session/topic.**

## This week's mission

**Master linear regression end-to-end.** From numpy scratch implementation to sklearn one-liner to real California housing dataset, all logged in MLflow. By Sunday I can teach linreg to a non-technical friend in 800 words.

## Today's block (Monday, 9:00–10:30 PM)

### 🌅 Warmup (15 min)

- Watch: 3Blue1Brown — Linear Algebra Essence **Episode 1: Vectors** (https://www.youtube.com/watch?v=fNk_zzaMoSs)
- Open `concepts/week-01-prereading.md`
- Add a section `## Ep 1: Vectors`
- Write **5 sentences in your own words** answering:
  1. What is a vector (in ML/data context)?
  2. What does it mean to "add" two vectors?
  3. What does scalar multiplication do geometrically?
  4. Where will I use this in AI engineering?
  5. One question I still have

### 💻 Numpy refresher (45 min)

Create: `daily-notebooks/week-01/01-numpy-refresher.ipynb`

Build these cells (no Googling syntax — use `np.array?` in Jupyter):

1. **Markdown:** title + "why numpy matters for ML" (2 sentences)
2. **Vectors:** create 1D arrays of length 5; check `.shape`, `.dtype`, `.ndim`
3. **Matrices:** create a 3×4 matrix; reshape it to 2×6; transpose it
4. **Element-wise vs matrix mult:** demonstrate `*` (Hadamard) vs `@` (matmul)
5. **Broadcasting:** add a (3,1) column vector to a (3,4) matrix — explain what happened
6. **Dot product:** two vectors `a, b` of length 4 → compute `a @ b`. What does the result mean geometrically?
7. **Random data:** generate 100 samples from a normal distribution (mean=0, std=1). Plot histogram.
8. **Markdown reflection:** 3 things you didn't know about numpy before today

### 📝 Anki (20 min)

- Review all due cards in `00-Setup` deck
- Create new deck: `01-Math-Foundations`
- Add 3 cards:
  - "Define a vector in ML context" / "ordered list of numbers; e.g. an embedding"
  - "Difference between `*` and `@` in numpy" / "`*` is element-wise; `@` is matrix multiplication"
  - "What is broadcasting?" / "numpy auto-expanding smaller arrays to match larger array shape during ops"

### 🚀 Commit (10 min)
