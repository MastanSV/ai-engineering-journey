# 📅 Week 0 — Setup & Baseline · Apr 23–26, 2026

> **Mission:** Zero learning content. Pure infrastructure + calibration. You can't run a marathon without lacing your shoes. 🏃

---

## 🗓️ Thursday, April 23 · Budget: 1–2 hrs · 🔧 Environment + GPU

**🎯 Goal:** GPU + PyTorch verified. Nothing else matters until this works.

### ⏱️ Schedule (pick any ~90-min window)

| Time | Task | Time Budget |
|------|------|-------------|
| 0:00 | Install `uv` (or verify Python 3.11) | 10 min |
| 0:10 | Create folder + venv at `C:\Temp\Learnings\ai-engineer-journey` | 10 min |
| 0:20 | Run `nvidia-smi` → note CUDA version → install matching PyTorch build | 20 min |
| 0:40 | Install core libs (numpy, pandas, sklearn, matplotlib, jupyter, mlflow, pytest, black, ruff) | 10 min |
| 0:50 | Write + run `verify_gpu.py` | 10 min |
| 1:00 | Paste output in mentor chat → get green light | 5 min |
| 1:05 | `git init` + first commit: `feat: week 0 day 1 — env + GPU verified` | 15 min |
| 1:20 | Buffer for debugging if CUDA breaks | 20–40 min |

### ✅ Done When
- [ ] `python verify_gpu.py` prints `CUDA available: True` + your GPU name + VRAM + successful matmul
- [ ] First commit pushed to local Git (repo not on GitHub yet — Friday task)
- [ ] Output pasted in mentor chat

### 🚨 If CUDA fails
STOP. Don't try to push through. Paste `nvidia-smi` + the failing error in our chat. We debug together. Most common culprits: driver version mismatch, wrong PyTorch CUDA build (cu121 vs cu124), or Python version >3.12 (pick 3.11).

---

## 🗓️ Friday, April 24 · Budget: 1–2 hrs · 🌐 GitHub + Public Presence

**🎯 Goal:** Repo is PUBLIC. First Tweet is OUT. Ollama is running.

### ⏱️ Schedule

| Time | Task | Time Budget |
|------|------|-------------|
| 0:00 | Create public GitHub repo `ai-engineer-journey` | 5 min |
| 0:05 | Scaffold folders: `weekly-logs/`, `concepts/`, `mock-interviews/`, `projects/`, `twitter-posts/` (use `.gitkeep`) | 10 min |
| 0:15 | Paste README (from prior message) + replace placeholders | 15 min |
| 0:30 | Create ROADMAP.md (ask mentor: "dump long roadmap") + commit | 10 min |
| 0:40 | Add `.gitignore` (Python + venv + .env + .DS_Store) + push to GitHub | 10 min |
| 0:50 | **Pin repo** on GitHub profile | 2 min |
| 0:52 | Create accounts: Hugging Face, Kaggle, Colab (log in), Langfuse Cloud free, OpenRouter (grab free API key) | 20 min |
| 1:12 | Install Ollama → `ollama pull llama3.2:3b` → test prompt | 15 min |
| 1:27 | Install Obsidian → point vault at `concepts/` folder | 10 min |
| 1:37 | Install Anki desktop → create deck "AI Engineer Journey" | 5 min |
| 1:42 | **Post Tweet #1** (draft below) → tag @huggingface @LangChainAI | 15 min |

### ✅ Done When
- [ ] GitHub repo is public, pinned, README renders correctly
- [ ] All 5 accounts active (HF, Kaggle, Colab, Langfuse, OpenRouter)
- [ ] `ollama run llama3.2:3b "hello"` returns a response
- [ ] Obsidian vault + Anki deck exist
- [ ] **Tweet #1 link pasted in mentor chat** 🐦

### 🐦 Tweet #1 Draft (edit to your voice)
> 🚀 Starting a 32-week journey: Software Engineer → AI/LLM Engineer by Dec 2026.
> 
> 100% free tools: HF · Ollama · Colab · Kaggle · Chroma · Langfuse.
> 6 portfolio projects. Weekly threads every Friday. 
> 
> Public repo 👇 Follow if you're on the same path.
> 
> [github.com/YOUR_HANDLE/ai-engineer-journey]
> 
> #BuildInPublic #AIEngineer #MachineLearning

---

## 🗓️ Saturday, April 25 · Budget: 4–6 hrs · 🎯 Baseline + Deep Tooling

**🎯 Goal:** Prove you can USE the tools, not just install them. Baseline calibrated.

### ⏱️ Schedule

| Block | Duration | Task |
|-------|----------|------|
| 9:00 – 11:00 | 2h | **Baseline Test Part 1** — numpy/pandas exercise (mentor will design + send Sat morning). Load dataset, do EDA, answer 5 questions. |
| 11:00 – 11:30 | 30m | ☕ Break |
| 11:30 – 12:30 | 1h | **Baseline Test Part 2** — Feynman test: write 500 words explaining "what is machine learning" for a non-technical friend. **No Google.** Save to `concepts/what-is-ml.md`. |
| 12:30 – 13:30 | 1h | 🍽️ Lunch |
| 13:30 – 14:30 | 1h | **Git hygiene:** set up pre-commit hooks (`black`, `ruff`, `pytest`). Practice branch → commit → PR-to-self → tag `v0.1.0-setup`. |
| 14:30 – 15:30 | 1h | **Colab + Kaggle tour:** run a sample notebook on each. Document free quotas + secrets management in `concepts/free-tools-cheatsheet.md`. |
| 15:30 – 17:00 | 1.5h | **HF Hub deep dive:** explore models/datasets/spaces. Clone `sentence-transformers/all-MiniLM-L6-v2` locally. Push a **dummy model** with proper README + model card to your HF profile. |
| 17:00 – 17:30 | 30m | Commit everything. `git push`. Update README progress tracker. |

### ✅ Done When
- [ ] Baseline test both parts submitted in mentor chat 🎤 (mentor grades Sat evening)
- [ ] `concepts/what-is-ml.md`, `concepts/free-tools-cheatsheet.md` pushed
- [ ] Dummy model pushed to your HF Hub profile (paste link in chat)
- [ ] Pre-commit hooks running on every commit
- [ ] At least 3 commits today

---

## 🗓️ Sunday, April 26 · Budget: 4–6 hrs · 🧭 Week 1 Prep + FIRST RETRO

**🎯 Goal:** Locked and loaded for Week 1. First sacred retro done. 🫡

### ⏱️ Schedule

| Block | Duration | Task |
|-------|----------|------|
| 9:00 – 10:00 | 1h | **MLflow hello-world:** run a dummy experiment locally, understand UI, log metrics/params/artifacts. Save notebook to `concepts/mlflow-basics.ipynb`. |
| 10:00 – 12:00 | 2h | **Week 1 pre-reading (LIGHT — mental map only):**<br>• 3Blue1Brown "Essence of Linear Algebra" videos 1–3 (45 min)<br>• StatQuest: "ML Fundamentals — Bias/Variance" (11 min)<br>• StatQuest: "Linear Regression / Least Squares" (9 min)<br>• Take notes in Obsidian, create first 10 Anki cards from what stuck |
| 12:00 – 13:00 | 1h | 🍽️ Lunch |
| 13:00 – 14:00 | 1h | **Write `weekly-logs/week-00-setup.md`:** what you installed, what broke, what you learned, how you FEEL going into Week 1. Be honest — this will be gold later. Push to GitHub. |
| 14:00 – 14:30 | 30m | **Draft Twitter Thread #1** (short retro of Week 0) → schedule for Friday OR post now. |
| 14:30 – 15:30 | 1h | 🎤 **SUNDAY RETRO with Mentor** *(THE SACRED RITUAL)* — see template below |
| 15:30 – 16:00 | 30m | Apply mentor feedback, update README progress tracker, commit, celebrate Week 0 done 🎉 |

### 🎤 Sunday Retro Template (paste this in chat)

```
📊 WEEK 0 RETRO

NN Scorecard (1–10):
- NN1 GitHub commits this week: __ / 7 days
- NN2 Twitter thread posted: YES/NO (link)
- NN3 Feynman teach-back score: _ / 10 (baseline test)
- NN4 Anki reviews: __ / 5
- NN5 Weekly retro committed: YES/NO

✅ What went well:
- 
- 

❌ What didn't go well / blockers:
- 
- 

🧠 Biggest thing I learned:
- 

😰 What I'm nervous about going into Week 1:
- 

⏱️ Actual hours spent: __ hrs (target was 11–16 hrs)

🎯 Ready for Week 1? YES / NO / WITH-CONCERNS
```

### ✅ Done When
- [ ] `week-00-setup.md` pushed to GitHub
- [ ] MLflow hello-world notebook pushed
- [ ] Sunday retro posted in mentor chat
- [ ] Mentor has delivered Week 1 sprint plan in response
- [ ] Twitter thread drafted (in `twitter-posts/week-00.md`)

---

## 🏁 Week 0 Success Criteria (must ALL be ✅ by Sunday 11 PM)

- [ ] 🖥️  GPU + PyTorch + CUDA verified (`verify_gpu.py` passes)
- [ ] 🌐 Public GitHub repo scaffolded, pinned, README live, ROADMAP.md committed
- [ ] 👤 All 5 accounts active (HF, Kaggle, Colab, Langfuse, OpenRouter)
- [ ] 🦙 Ollama running with `llama3.2:3b`
- [ ] 🧠 Obsidian vault + Anki deck operational
- [ ] 🐦 Tweet #1 posted publicly
- [ ] 📝 Baseline test (both parts) submitted + graded by mentor
- [ ] 🤗 Dummy model pushed to HF Hub
- [ ] 📊 MLflow hello-world notebook committed
- [ ] 📔 `week-00-setup.md` retro pushed
- [ ] 🎤 Sunday retro completed with mentor

**If ANY slip to Monday, we DON'T rush Week 1. Foundation > pace.** 🫡

---

## ⏱️ Time Budget Summary

| Day | Target | Cumulative |
|-----|--------|------------|
| Thu | 1–2 hr | 1–2 hr |
| Fri | 1–2 hr | 2–4 hr |
| Sat | 4–6 hr | 6–10 hr |
| Sun | 4–6 hr | **10–16 hr total** |

Matches your committed budget exactly. No scope creep.

---

## 🧘 Mental Prep Notes

- ⚠️ **Expect something to break.** CUDA install, venv issues, HF auth — these are normal. Budget debugging time.
- 🎯 **Don't over-polish the README.** Ship ugly, iterate in public. Week 0 README will look cringe in Week 24 — that's good, it means you grew.
- 🚫 **Do NOT start Week 1 content early** even if you have free time. Week 0 is the warm-up. Pacing > heroics.
- 🏆 **Celebrate Sunday night.** Public announcement + first commit streak = real milestone. Take the win.