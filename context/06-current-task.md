### Fri Jul 24 (1.5 hr, 9:00–10:30 PM) — HF Space deploy + interview-ready deep dive

**Meta-goal:** Don't just _deploy_. Understand _every layer_ so you can whiteboard "how do you serve an ML model?" in an interview. Each task below has a **DO** (the action) and a **KNOW** (the interview-level understanding to extract).

---

#### [x] 15 min — Anki review

- **DO:** Run your existing deck.
- **KNOW:** Note any card you hesitate on for >3 sec → that's an interview gap. Flag it.

---

#### [x] 60 min — HF Space deploy

**Sub-task A — Create Space `mastanai/p1-tabular-ml` (Gradio SDK)**

- **DO:** New Space → Gradio SDK → set hardware (CPU basic is free tier).
- **KNOW / interview questions to answer out loud:**
  - What _is_ a HF Space under the hood? (Hint: a git repo + a container that runs `app.py`.)
  - Why Gradio vs. FastAPI vs. Streamlit for a demo? What's the trade-off?
  - What does the "SDK" choice actually control at build time?

**Sub-task B — Push `app.py`, `model.pkl`, `requirements.txt`**

- **DO:** `git clone` the Space, add files, `git push`. (Or upload via UI, but do it via git — that's the interview-relevant workflow.)
- **KNOW:**
  - Why is `model.pkl` a _build artifact_, not source? Should large models live in git? (Look up: HF `git-lfs`.)
  - What is `joblib.load` doing vs. `pickle.load`? Why does sklearn recommend joblib?
  - **Security angle (common interview curveball):** why is loading a `.pkl` from an untrusted source dangerous? (Arbitrary code execution on unpickle.)

**Sub-task C — Verify live URL end-to-end**

- **DO:** Enter a test patient, confirm you get a diagnosis + probability back.
- **KNOW:**
  - Trace ONE prediction through the whole stack: browser input → Gradio event → `predict()` → DataFrame → `model.predict_proba` → response. Can you narrate it in 60 sec?
  - Why does the code build a `pd.DataFrame` with named columns instead of a raw list/array? (Column order & names must match training — classic serving bug.)
  - What does `predict_proba([0][1])` return, and why index `[1]`? (Prob of the positive class.)

---

#### [x] 15 min — Fix deployment issues (dependency pins, file paths)

⚠️ **This is the highest-value learning block. Your current `requirements.txt` has real bugs — find them yourself before reading my hints:**

- **DO:** Look at your `requirements.txt`. It lists `numpy, pandas, sklearn, matplotlib, seaborn, mlflow`.
  - Q1: `app.py` does `import gradio` and `import joblib`. Are those in the file? What happens on build if not?
  - Q2: Is `sklearn` the correct PyPI package name? (Try `pip install sklearn` and read the error/warning.)
  - Q3: `matplotlib/seaborn/mlflow` — does the _serving_ app need them, or are they training-only? What does shipping them cost? (Build time, image size, attack surface.)
- **KNOW — dependency pinning:**
  - Why pin versions (`scikit-learn==1.x.x`) for a deployed model? (Unpickling across sklearn versions can silently break or warn.)
  - How would you find the _exact_ version you trained with? (`pip freeze`, or `sklearn.__version__` in the training notebook.)
  - Interview phrase to own: **"reproducible environment"** — what makes an env reproducible?
- **KNOW — file paths:**
  - `joblib.load('model.pkl')` uses a _relative_ path. Relative to what? (The process CWD.) When does that break?

---

#### [x] 🚀 Commit: `week-06: P1 deployed on HF Space`

**Exit criteria (learning-augmented):**

1. ✅ Live HF URL returns a prediction for a test input.
2. ✅ You can whiteboard the request→prediction path from memory.
3. ✅ You can explain the 3 `requirements.txt` bugs and why each broke/risked the build.
4. ✅ You wrote 2–3 new Anki cards from gaps found today (pickle security, dep pinning, DataFrame column-matching).

---

**Stretch (if time remains):** Add a one-line `README.md` "Model card" — dataset, target, metric, known limitations. Interviewers love candidates who think about model _documentation_ and _limitations_.
