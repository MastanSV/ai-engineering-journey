# Active Tasks — Week 7 (Jul 28 – Aug 3, 2026)

## Sprint goal

Build concept-solid foundations for deep learning: neuron → activation → loss →
backprop → MLP from scratch. Concept-first, then derive, then code.

## Theme: **"Concept-first foundations"**

## Context

- Phase 1 CLOSED (P1 shipped, gate passed). Phase 2 begins.
- New guiding rule adopted this week: every topic runs CONCEPT → DERIVE → CODE.
  Do NOT open a derivation until the concept passes the Feynman check (said aloud).

## Active rules

- **30-min carryover cap:** weekday carryover >30 min → push to Saturday.
- **20-min stuck rule:** stuck >20 min → switch resource before quitting.
- **Feynman check:** 3-sentence zero-jargon explanation before any concept is "learned."
- **Recognition≠Explanation:** say every Anki answer OUT LOUD before flipping.
- **Anki own-words loop:** author cards in my words → LLM RATES → store polished version.
- **Break tripwire:** 2 missed days in a row → 15-min Anki-only re-entry next day.

## Time budget

- Mon–Fri 1.5hr × 5 = 7.5hr · Sat–Sun 6hr × 2 = 12hr · **Available: 19.5hr**

---

## Daily breakdown

### Mon Jul 28 (1.5hr) — CONCEPT: the neuron

- [ ] 15 min — Anki review (aloud)
- [ ] 60 min — Concept only: weighted sum + bias + activation (3B1B NN Ch.1). NO math.
- [ ] 15 min — Feynman note `concepts/week-07-neuron-concept.md` (3 sentences, zero jargon)
- [ ] 🚀 Commit: `week-07: neuron concept notes`
      **Exit:** can explain a neuron in 3 plain sentences aloud.

### Tue Jul 29 (1.5hr) — CONCEPT: activations + non-linearity

- [ ] 15 min — Anki
- [ ] 60 min — sigmoid / tanh / ReLU: what each does, why non-linearity matters
- [ ] 15 min — Feynman note: "without activation, a deep net collapses to **\_\_**"
- [ ] 🚀 Commit
      **Exit:** can state why a net needs non-linearity.

### Wed Jul 30 (1.5hr) — DERIVE: forward pass + loss

- [ ] 15 min — Anki
- [ ] 60 min — On paper: forward pass for 1 neuron → 2-layer net; MSE + cross-entropy forms
- [ ] 15 min — Photo of derivation → `concepts/images/`
- [ ] 🚀 Commit
      **Exit:** hand-written forward pass + both loss forms.

### Thu Jul 31 (1.5hr) — CONCEPT: backprop intuition

- [ ] 15 min — Anki
- [ ] 60 min — 3B1B Ch.3 (backprop) + Ch.4 (calculus). Story-level, no symbols.
- [ ] 15 min — Feynman note: explain backprop to a 12-year-old
- [ ] 🚀 Commit
      **Exit:** can tell the "send the error backward" story without notation.

### Fri Aug 01 (1.5hr) — DERIVE: backprop math

- [ ] 15 min — Anki
- [ ] 60 min — On paper: chain-rule gradients for 2-layer net (output → hidden layer)
- [ ] 15 min — Photo + note where you got stuck
- [ ] 🚀 Commit
      **Exit:** dL/dW derived by hand for both layers.

### Sat Aug 02 (6hr) — CODE: MLP from scratch (numpy)

- [ ] 15 min — Anki
- [ ] 120 min — `daily-notebooks/week-07/01-neuron-from-scratch.ipynb`: single neuron
      forward pass, plot activation, verify by hand
- [ ] 150 min — Extend to 2-layer MLP: forward + backward + gradient descent on XOR /
      make_moons; watch loss decrease
- [ ] 45 min — Feynman: "my gradients are correct because **\_\_**" (gradient-check idea)
- [ ] 🚀 Commit(s)
      **Exit:** MLP trains, loss goes down, gradients sanity-checked.

### Sun Aug 03 (6hr) — CONNECT + accountability

- [ ] 15 min — Anki
- [ ] 120 min — Author Anki cards (own words → LLM RATES): neuron, activation,
      non-linearity, forward pass, loss, chain rule, backprop → `anki-cards-week-07.tsv`
- [ ] 120 min — Teach-back `concepts/week-07-teachback-backprop.md` (≥800 words) [NN3]
- [ ] 60 min — Twitter thread `twitter-posts/week-07-thread-backprop.md`, POST LIVE [NN2]
- [ ] 45 min — Retro `weekly-logs/retro-week-07.md`
- [ ] 30 min — Update `01-current-state.md`, `03-active-tasks.md`, `06-current-task.md`
- [ ] 🚀 Commit
      **Exit:** teach-back written, Twitter posted, retro done, context updated.

---

## Non-negotiables this week

| #   | Rule           | Check                              |
| --- | -------------- | ---------------------------------- |
| NN1 | GitHub commits | ≥5 (daily)                         |
| NN2 | Twitter        | `week-07-thread-backprop.md` (Sun) |
| NN3 | Teach-back     | `week-07-teachback-backprop.md`    |
| NN4 | Anki           | Daily, said aloud                  |
| NN5 | Retro          | `retro-week-07.md` (Sun)           |

## Carried from Phase 1

- [ ] **[CONFIRM] Loom walkthrough** for P1 — do first thing if still open.
