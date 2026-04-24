# 🚀 AI Engineer Journey — 8-Month Sprint

> **Mission:** Transform from Software Engineer (SDE2) into an interview-ready **AI / LLM Engineer** in 32 weeks — using only free tools (Hugging Face, Ollama, Colab, Kaggle, Chroma, Langfuse free, OpenRouter free).

![Status](https://img.shields.io/badge/status-in_progress-yellow)
![Start](https://img.shields.io/badge/started-April_2026-blue)
![Target](https://img.shields.io/badge/target-December_2026-green)
![Tools](https://img.shields.io/badge/stack-100%25_free-brightgreen)
![Made with](https://img.shields.io/badge/made_with-PyTorch_%7C_Transformers_%7C_Ollama-orange)

---

## 🎯 The Goal

Land an **AI / LLM Engineer** role by **December 2026** by shipping **6 production-grade portfolio projects**, learning in public on [Twitter/X](https://twitter.com/mastan_ai), and mastering the full stack from **transformers-from-scratch → RAG → agents → fine-tuning → LLMOps**.

**Capstone theme:** Compliance Document QA System (enterprise-grade RAG with audit trails, citations, PII handling, hallucination guardrails).

> 📝 _Pre-journey work (the ~3 weeks before April 23, 2026): linear regression explorations, first Python notebooks, tool discovery. Visible in `daily-notebooks/` and `promptsNresponses/linearregression/`. Consider it my warm-up lap. The official 32-week sprint starts April 23, 2026._ 🏃

---

## 📊 Progress Tracker

### 🏆 6 Portfolio Projects

| #   | Week | Project                                         | Status         | Demo | Repo |
| --- | ---- | ----------------------------------------------- | -------------- | ---- | ---- |
| 1   | 4    | Tabular ML w/ Engineering Rigor                 | ⬜ Not started | —    | —    |
| 2   | 8    | nanoGPT from Scratch                            | ⬜ Not started | —    | —    |
| 3   | 12   | Production RAG v1 (hybrid + reranker + RAGAS)   | ⬜ Not started | —    | —    |
| 4   | 16   | Autonomous Research Agent (pure Py → LangGraph) | ⬜ Not started | —    | —    |
| 5   | 20   | QLoRA Fine-Tune + Full LLMOps Loop              | ⬜ Not started | —    | —    |
| 6   | 24   | **Capstone: Compliance Document QA System**     | ⬜ Not started | —    | —    |

_Legend: ⬜ Not started · 🟡 In progress · ✅ Shipped · 🌟 Polished + deployed_

### 📈 Weekly Progress

| Week | Dates                 | Focus               | Retro          |
| ---- | --------------------- | ------------------- | -------------- |
| 0    | Apr 23 – Apr 26, 2026 | Setup & baseline    | _(coming Sun)_ |
| 1    | Apr 27 – May 3        | ML foundations 1    | —              |
| 2    | May 4 – May 10        | ML foundations 2    | —              |
| 3    | May 11 – May 17       | ML foundations 3    | —              |
| 4    | May 18 – May 24       | **Project #1 ship** | —              |
| 5    | May 25 – May 31       | Deep learning 1     | —              |
| …    | …                     | …                   | —              |

_(Updated every Sunday — commit streak is visible on my profile 🔥)_

---

## 🗺️ The 32-Week Roadmap

### 🔰 Phase 0 — Setup & Baseline · Week 0

Dev environment, GPU verification, public accounts (HF / Kaggle / Colab / Langfuse / OpenRouter / Ollama), repo scaffold, baseline calibration test, first public Tweet.

### 1️⃣ Phase 1 — ML Foundations & Math-as-Needed · Weeks 1–4

- **Math lean-in:** 3Blue1Brown linear algebra + essence of calculus. StatQuest for stats.
- **ML core:** supervised learning, train/val/test, regularization, bias/variance, metrics, sklearn pipelines, feature engineering.
- **From scratch in numpy:** linear regression (GD), logistic regression, k-NN, decision tree splits.
- **Stack:** numpy · pandas · scikit-learn · matplotlib · MLflow · pytest · Docker · FastAPI.
- 🚀 **Project #1: Tabular ML with Engineering Rigor** — Kaggle dataset → EDA → sklearn pipeline → MLflow tracking → tests → Dockerfile → FastAPI on Hugging Face Space → README with model card, limitations, cost notes.

### 2️⃣ Phase 2 — Deep Learning & Transformers From the Inside · Weeks 5–8

- **PyTorch deep dive:** tensors, autograd, `nn.Module`, `DataLoader`, mixed precision, GPU usage.
- **DL fundamentals:** MLP → backprop by hand → CNN → RNN/LSTM → **Transformer from scratch** (Karpathy "Let's build GPT" — solo reimplementation).
- **Attention internals:** scaled dot-product, multi-head, positional encodings (abs, RoPE), KV cache.
- **Tokenization:** BPE, SentencePiece, `tokenizers` library.
- 🚀 **Project #2: nanoGPT from Scratch** — ~10M-param GPT trained on local GPU on a custom dataset. Blog/Twitter thread explaining attention math. Model pushed to Hugging Face Hub.

### 3️⃣ Phase 3 — LLM Engineering Fundamentals · Weeks 9–12

- **Prompt engineering (real):** zero/few-shot, CoT, self-consistency, structured outputs (JSON mode, Pydantic), prompt injection defenses.
- **HF ecosystem:** `transformers`, `datasets`, `accelerate`, pipelines, model cards, Ollama, llama.cpp.
- **First RAG:** sentence-transformers embeddings, chunking strategies, Chroma, retrieval → answer pipeline.
- **Eval basics:** perplexity, BLEU/ROUGE and their limits, LLM-as-judge introduction.
- **Parallel track starts:** 1 LeetCode problem/day (ML-interview patterns).
- 🚀 **Project #3: Production RAG v1** — corpus = compliance docs (seeds the capstone). Hybrid search (BM25 + dense) + reranker (`bge-reranker`) + query rewriting + structured citations + RAGAS evaluation + Langfuse tracing + Gradio UI on HF Space.
- 📞 **Mock Interview #1 (Week 10)** — easy ML concepts, baseline calibration.

### 4️⃣ Phase 4 — Advanced RAG, Agents & Orchestration · Weeks 13–16

- **Advanced RAG:** multi-query, HyDE, parent-document retrieval, contextual compression, query routing, multi-modal. And — just as important — **knowing when NOT to use RAG.**
- **Agents deeply:** ReAct, tool-calling, function-calling specs, planning vs reactive, multi-agent (supervisor/worker), memory (short/long), self-critique. **Built from scratch in pure Python first, then refactored to LangGraph.**
- **Guardrails:** input/output validation, PII redaction, jailbreak detection, rate limiting, cost caps.
- **System-design micro-lessons:** 1 case study per weekend.
- 🚀 **Project #4: Autonomous Research Agent** — takes a research question → plans → searches (DuckDuckGo / arXiv) → reads → synthesizes → cites → self-critiques. Evals: task success rate, hallucination rate, tool-call accuracy. Deployed on HF Space.
- 📞 **Mock Interview #2 (Week 14)** — LLM concepts + Project #3 deep dive.

### 5️⃣ Phase 5 — Fine-Tuning, Evaluation & LLMOps · Weeks 17–20

- **Fine-tuning on local GPU:** full fine-tune (small model), LoRA, QLoRA with `peft` + `bitsandbytes`, instruction/chat formatting, DPO introduction.
- **Evaluation rigor:** building eval sets, LLM-as-judge done right, RAGAS, `lm-eval-harness`, bias/safety checks, A/B testing.
- **LLMOps:** inference optimization (vLLM intro, quantization GGUF/AWQ), serving (FastAPI + streaming), monitoring (Langfuse, OpenTelemetry), cost accounting, semantic caching, prompt versioning.
- 🚀 **Project #5: QLoRA Fine-Tune + Full LLMOps Loop** — fine-tune a 7B-class model (Llama / Qwen / Mistral) on a specific task. Full loop: data pipeline → LoRA training (Colab/Kaggle for 7B) → eval vs. base → GGUF quantization → Ollama deployment → Gradio demo on HF → monitoring dashboard → cost/latency report. **💎 Crown jewel.**
- 📞 **Mock Interview #3 (Week 18)** — fine-tuning + LLMOps deep dive.
- 📤 **Applications start Week 20** with 4 projects live.

### 6️⃣ Phase 6 — Capstone + System Design + Interview Blitz · Weeks 21–24

- 🚀 **Capstone Project #6: Compliance Document QA System** — enterprise-grade RAG with audit trails, citations, PII handling, access control, hallucination guardrails. Combines RAG + agents + fine-tuning + eval + deployment + monitoring.
- **System design for AI:** design LLM-backed systems (chatbot at scale, RAG for enterprise, embedding-based recommendations, real-time moderation). Study 10+ public post-mortems (Shopify, Notion, Anthropic blogs).
- **DSA refresher:** 2 LeetCode/day (Blind 75 → NeetCode 150 subset for ML interviews).
- **Interview content:** Anki deck of 30+ Qs with brutally honest answers + STAR behavioral stories.
- 📞 **Mock Interviews #4, #5, #6** — full-loop simulations (coding + ML + system design + behavioral).

### 7️⃣ Phase 7 — Apply, Polish, Iterate · Weeks 25–32

Resume + LinkedIn overhaul · weekly mocks · 2 LeetCode/day · apply to 5–10 target roles/week · 1 Twitter thread/week · 1 blog/month · 1 PR to an open-source AI project (HF / LangChain / LlamaIndex).

**Keep shipping — fresh GitHub activity matters until the offer is signed.** ✍️

---

## 🧭 Core Learning Laws

1. **80/20 rule** — 80% building, 20% absorbing. A concept without a mini-project in 24h is not learned.
2. **Feynman + Teach-back** — every concept gets explained back out loud. Shallow understanding gets ripped apart.
3. **Learn in public** — every Friday, a Twitter thread. No exceptions.
4. **Spaced repetition** — Anki deck built weekly for concepts + interview Qs.
5. **Production mindset from day 1** — every project ships with tests, README, eval, deployment, cost notes, failure modes.
6. **Mock interviews** — bi-weekly from Week 10, weekly from Week 20.

---

## 🚨 Weekly Non-Negotiables

| NN  | What                                     | Miss-count this week |
| --- | ---------------------------------------- | -------------------- |
| NN1 | Ship to GitHub (daily commit streak)     | 0                    |
| NN2 | 1 Twitter thread / week                  | 0                    |
| NN3 | 1 Feynman teach-back (scored)            | 0                    |
| NN4 | ≥ 5 Anki reviews                         | 0                    |
| NN5 | Weekly retro committed to `weekly-logs/` | 0                    |

_Missing 2+ NNs in a week triggers a root-cause retro. No drift allowed._

---

## 🎯 Quality Bar — "Recruiter Stops Scrolling" Test

Every portfolio project must pass **all 6** before moving on:

- ✅ Live demo (HF Space — not "run locally")
- ✅ 3-min Loom walkthrough embedded in README
- ✅ Architecture diagram (Excalidraw or hand-drawn)
- ✅ Real evaluation numbers (not "works great")
- ✅ Twitter thread explaining it publicly
- ✅ Solves a real problem someone would pay to fix

**5 great projects > 6 mediocre ones.**

---

## 🛠️ The Stack (100% Free)

**Compute:** Local NVIDIA GPU (Quadro T1000, 4 GB) · Google Colab · Kaggle Notebooks  
**Models:** Hugging Face Hub · Ollama (local) · OpenRouter free tier  
**Vector stores:** Chroma (local) · FAISS  
**Frameworks:** PyTorch · Transformers · LangGraph · Gradio · FastAPI  
**Observability:** Langfuse free tier · MLflow (local) · OpenTelemetry  
**Eval:** RAGAS · `lm-eval-harness` · custom LLM-as-judge harness  
**MLOps:** Docker · pytest · pre-commit (`black`, `ruff`) · GitHub Actions  
**Knowledge:** Obsidian + Anki for notes & spaced repetition

---

## 📂 Repo Structure

```
ai-engineering-journey/
├── README.md                ← this file (progress tracker)
├── ROADMAP.md               ← full detailed 32-week roadmap
├── weekly-logs/             ← Sunday retros (week-00, week-01, …)
├── concepts/                ← Feynman-style notes + Anki card exports
├── daily-notebooks/         ← Jupyter experiments, sandbox work
├── interviews/              ← mock interview scores, feedback, transcripts
├── projects/                ← portfolio projects (6 big + small experiments)
├── promptsNresponses/       ← prompt engineering logs + LLM responses archive
├── templates/               ← note + code templates for consistency
└── twitter-posts/           ← drafts before going public
```

---

## 🔗 Follow Along

- 🐦 **Twitter/X:** [@mastan_ai](https://twitter.com/mastan_ai) — weekly threads every Friday
- ✍️ **Blog:** _coming soon_
- 💼 **LinkedIn:** [linkedin.com/in/mastan-vali-02a102197](https://linkedin.com/in/mastan-vali-02a102197)
- ⭐ **Star this repo** to follow the journey

---

## 💬 Why I'm Doing This Publicly

Accountability. Proof of work. Paying it forward for the next engineer making this transition.

If you're on the same path, **open an issue or DM me on Twitter** — I'll be doing weekly retros and sharing every failure and every win.

_Let's make this the most ruthlessly productive 8 months of our lives._ 🔥
