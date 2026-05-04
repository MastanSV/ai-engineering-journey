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

## 2026-05-02 · Week 1 scope cut: merge sklearn + California housing into one Sunday notebook; drop Ridge/Lasso

- **Why:** 3 weekday slips (Tue 🔄, Wed 🔄, Thu ⏭️, Fri 🔄) triggered the Saturday re-plan rule. Original Week 1 plan had 6 separate notebooks (01–06) plus Ridge/Lasso comparison plus diagnostics; with only Sun May 3 left, full scope is impossible without fake-finishing. Merging sklearn (was notebook 04) + California housing (was notebook 05) + 1 residual plot (was diagnostics notebook 06) into one notebook saves ~90 min of ceremony without losing the "scratch → sklearn → real data" learning arc.
- **What stays:** notebook 03 (scratch GD ✅ shipped Sat); merged Sun notebook covering sklearn-on-fake-data + California housing + MLflow + 1 residual plot; teach-back essay (≥800 words, no AI); Sun retro; Twitter thread #3.
- \*\*What drops/moves:
  - Ridge/Lasso comparison → **Week 2 buffer** (regularization is genuinely Week 2 territory)
  - Full diagnostics notebook 06 → **Week 2 buffer** (1 residual plot in merged notebook is enough for Week 1 DoD)
  - Curiosity bucket review (was Sat 30 min) → next week
  - Optional Kaggle submission → next week if relevant
  - Bias-variance video → Sun warmup (was Thu)
- \*\*Alternatives considered:
  - (a) Push California housing to Mon and teach-back to Tue — rejected, breaks 7-day week boundary and pushes Week 2 plan
  - (b) Drop teach-back essay — rejected, NN3 violation
  - (c) Drop Sun retro — rejected, NN5 violation and we lose the slip-pattern analysis
- **Reversible?** Yes — Ridge/Lasso and full diagnostics return in Week 2 buffer slot or Week 3 regularization deep-dive.
- **Calibration takeaway:** For Week 2 plan, budget 2 days per "from-scratch" notebook (not 1). First-time ML topics consistently took ~2× my estimate.

## 2026-05-03 · Week 2 calibration rule: 30-min carryover cap

- **Why:** Week 1 retro surfaced a 3-day cascade (Wed low energy → Thu avoidance → Fri's own slot eaten by cleanup). Single-cause: carryover from any one day was unbounded, so a 1-hour deficit on Wed compounded into ~5 hours of lost weekday execution by Friday. The Saturday/Sunday weekend covered the gap (15hr / 24hr total) but that's not sustainable across 25 more weeks.
- **Rule:** At end of each weekday, write the day's carryover task. If estimated remainder is >30 min, it does NOT go to the next weekday — it goes straight to Saturday in `03-active-tasks.md`. Weekdays absorb only ≤30-min spillover.
- **Alternatives considered:**
  - (a) "Try harder on weekdays" — rejected, not enforceable.
  - (b) Cap weekly hours at 19 to force ruthless cuts — rejected for Week 2; want one more datapoint.
  - (c) Move all carryover to Saturday regardless of size — rejected, eliminates flexibility for genuine ≤30-min spillovers.
- **Reversible?** Yes — re-evaluate at end of Week 2 retro. If cascade recurs despite rule, escalate to (b).
- **Source:** `weekly-logs/retro-week-01-linreg.md` §5.

---

## Template for new entries

```
## YYYY-MM-DD · <Decision title>
- **Why:** ...
- **Alternatives considered:** ...
- **Reversible?** Yes/No/Partial — until when?
```
