# Decisions Log

> Append-only. Every entry: **Date · Decision · Why · Alternatives · Reversible?**
> Never delete; if a decision is reversed, add a new entry referencing the old one.

---

## 2026-04-23 · Capstone theme = Compliance Document QA System

- **Why:** Enterprise relevance, audit trail makes a great showcase for hallucination guardrails + citations + PII handling, combines RAG + agents + (optional) fine-tuning into one realistic product. High signal in interviews.
- **Alternatives considered:** AI code reviewer, personal learning coach, technical interview simulator.
- **Reversible?** Yes, until Week 18.

## 2026-04-23 · Learn-in-public platform = Twitter/X

- **Why:** AI community is densest there; #BuildInPublic is alive; HF/LangChain/Anthropic engineers engage with learners.
- **Alternatives considered:** LinkedIn, dev.to, personal blog.
- **Reversible?** Yes (add others later) but Twitter stays primary.

## 2026-04-23 · Mode = Brutal accountability

- **Why:** User explicitly rejected average outcomes; consistent reps + zero-excuse retros are the path from 30% → 65% offer probability.
- **Alternatives considered:** Soft-coaching mode.
- **Reversible?** No — explicit user contract.

## 2026-04-23 · LLM-first path (not classical ML depth)

- **Why:** Matches target role and 2026 market. Time-boxed at 32 weeks; depth in classical ML would push timeline to 12+ months.
- **Alternatives considered:** Classical-ML-first (Kaggle grandmaster route), then transition.
- **Reversible?** Partial — can add depth in Phase 7 if needed.

## 2026-04-24 · GPU strategy = local Quadro T1000 + free Colab/Kaggle for 7B

- **Why:** T1000 (4 GB) handles all of Phases 1–4 + small models in Phase 5. 7B QLoRA fine-tune (Project #5) routes to free Colab T4 (16 GB) or Kaggle P100/T4 (30 hrs/week).
- **Alternatives considered:** Cloud GPU rental (paid — violated free-tools constraint).
- **Reversible?** Yes — can shift more to cloud if local becomes bottleneck.

## 2026-04-24 · Pre-existing repo `MastanSV/ai-engineering-journey` retained

- **Why:** ~3 weeks of pre-journey commits + linear regression work add credibility ("warm-up lap"). Renaming would lose history.
- **Alternatives considered:** New repo with clean history.
- **Reversible?** Hard — would lose Git history.

## 2026-04-25 · Adopted External Persistent Context (`CONTEXT/`) pattern

- **Why:** Long chats with LLM mentors lose context; structured files survive sessions, are version-controlled, and mirror real production-LLM patterns (RAG, agent state, audit trails).
- **Alternatives considered:** Single rolling chat, Notion docs (off-repo, less recruiter-visible).
- **Reversible?** Yes, but unlikely to abandon — this is industry standard.

---

## Template for new entries

```
## YYYY-MM-DD · <Decision title>
- **Why:** ...
- **Alternatives considered:** ...
- **Reversible?** Yes/No/Partial — until when?
```
