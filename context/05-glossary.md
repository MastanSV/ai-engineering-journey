# Glossary

> Append as you learn. Every term you Anki-card lives here too in fuller form.
> Format: term · 1-line definition · why-it-matters-to-you note (optional).

---

## Journey-specific

- **NN (Non-Negotiable)** — One of 5 weekly habits I cannot skip without triggering a red-flag retro.
- **Red-flag week** — Any week where I miss 2+ NNs. Triggers mandatory root-cause analysis.
- **Recruiter-stops-scrolling test** — 6-criterion bar every portfolio project must pass before I move on.
- **Capstone** — Project #6, Compliance Document QA, due Week 24, must combine RAG + agents + eval + deploy + monitor.
- **Teach-back** — Mentor-graded Feynman explanation of a concept, scored 0–10 weekly.

## Setup / tooling

- **CUDA driver vs runtime** — `nvidia-smi` shows max CUDA the _driver_ supports (e.g., 13.1). `torch.version.cuda` shows the _runtime_ bundled with the PyTorch wheel (12.4). Independent.
- **`--index-url`** — Overrides default PyPI; pip pulls only from the specified URL. Used for PyTorch CUDA channels, private mirrors.
- **uv** — Modern Rust-based Python package manager. Way faster than pip; handles venvs.
- **Ollama** — Local LLM runner. `ollama run llama3.2:3b "..."` to chat. Quantized models, runs on small GPUs.

## Hugging Face

- **HF Hub** — Git-LFS-backed model/dataset/space registry.
- **Model card** — README.md with YAML frontmatter (license, language, tags). Required metadata.
- **Spaces** — Free deployed demos (Gradio/Streamlit). Where my projects will live publicly.

## LLM tooling

- **Langfuse** — Observability for LLM apps: traces every prompt+response+latency+cost. Free tier 50k events/mo.
- **OpenRouter** — Unified gateway for 300+ LLMs (one API, one key, free models available). OpenAI-compatible endpoint.
- **Gateway pattern** — Abstract LLM provider behind one interface; enables fallback, A/B test, cost routing. Senior-level architectural move.

## ML basics (will fill as I learn)

- **Train/val/test split** — _to add Week 1_
- **Overfitting** — _to add Week 1_
- **Bias/variance** — _to add Week 1_
- **Cross-validation** — _to add Week 1_

## DL / Transformers (Week 5+)

- _(to fill)_

## RAG / Agents (Week 9+)

- _(to fill)_

## Fine-tuning / LLMOps (Week 17+)

- _(to fill)_

---

## Rules for this file

1. Add a term within 24 hours of meeting it.
2. Definition in YOUR words (Feynman). If you can't, you don't know it yet.
3. If a term has an Anki card, link the deck/subdeck.
4. Don't delete entries — strike them through if wrong, leave the lesson visible.
