# Active Tasks — Week 7 Sprint (Jul 28 – Aug 2, 2026)

## Sprint goal

Build neural-network foundations from scratch (perceptron → MLP → backprop → PyTorch),
teach-back backprop, and scope P2 (nanoGPT). First full Phase 2 week.

## Theme: "Neural Foundations"

## Active rules

> Full standing rules live in `context/07-tracking-rules.md`. This block pins the
> highest-risk rules for THIS sprint only.

- **Break tripwire (TOP risk — post-milestone slump):** 2 missed days in a row →
  next day mandatory 15-min Anki-only re-entry. No new material.
- **Recognition≠Explanation:** every Anki card answered OUT LOUD before flipping.
- **Feynman check:** 3-sentence zero-jargon explanation before any concept = "learned".
- **20-min stuck rule:** switch resource; never close laptop without 1 alternative.
- **30-min carryover cap:** weekday spillover >30 min → Saturday, not next weekday.
- **Weekend minimum:** home → 15-min Anki floor; hostel → fixed clock slot.

## Time budget

Tue–Fri 1.5hr × 4 = 6hr | Sat–Sun 6hr × 2 = 12hr | **Target this week: 18hr**

## Carryover from Mon (if not done)

- Persist Week-6 rules into context (07 → 04 → 03 → 00) + write 3 fuzzy cards.
  (≤30 min → fold into Tue's first block; else push to Sat morning per carryover cap.)

---

### Tue Jul 28 (1.5hr, 9:00–10:30 PM) — Perceptron from scratch

- [ ] 15 min — Anki review (OUT LOUD, no silent passes)
- [ ] 60 min — `daily-notebooks/week-07/01-perceptron-from-scratch.ipynb`:
      single perceptron (AND/OR gate) in numpy, forward pass + manual gradient update,
      visualize decision boundary
- [ ] 15 min — Notes + Feynman 3-sentence check → Anki card
- [ ] 🚀 Commit: `week-07: perceptron from scratch`
      **Exit:** perceptron learns AND/OR, boundary plotted, 1 own-words Anki card added.

### Wed Jul 29 (1.5hr) — Backprop intuition

- [ ] 15 min — Anki (out loud)
- [ ] 60 min — 3B1B Ch 3–4 (backprop + chain rule + computational graph); notes with a
      hand-worked 2-node gradient example
- [ ] 15 min — Feynman check: explain backprop in 3 jargon-free sentences → if you can't, re-study
- [ ] 🚀 Commit: `week-07: backprop intuition + notes`
      **Exit:** can explain backprop out loud; hand-worked gradient in notes.

### Thu Jul 30 (1.5hr) — PyTorch basics

- [ ] 15 min — Anki (out loud)
- [ ] 60 min — `daily-notebooks/week-07/02-pytorch-basics.ipynb`:
      tensors, autograd (`.backward()`, `.grad`), `nn.Module`, optimizer step — tiny examples
- [ ] 15 min — Notes: map each PyTorch piece back to the from-scratch math
- [ ] 🚀 Commit: `week-07: PyTorch basics (tensors, autograd, nn.Module)`
      **Exit:** autograd reproduces your hand-worked Wed gradient.

### Fri Jul 31 (1.5hr) — MLP in PyTorch

- [ ] 15 min — Anki (out loud)
- [ ] 60 min — `daily-notebooks/week-07/03-mlp-pytorch.ipynb`:
      2-layer MLP on toy data (make_moons or MNIST subset), full train loop, plot loss + accuracy
- [ ] 15 min — 🚀 Commit: `week-07: MLP in PyTorch (train loop + eval)`
      **Exit:** MLP trains, loss decreases, >90% on toy set.

### Sat Aug 1 (6hr) — MLP from scratch + teach-back + Twitter

#### Morning (3hr)

- [ ] 15 min — Anki (out loud)
- [ ] 150 min — `04-mlp-from-scratch.ipynb`: 2-layer NN in pure numpy with manual backprop;
      match PyTorch result from Fri (sanity check both directions)
- [ ] 15 min — Buffer / fold in any Mon carryover

#### Afternoon (3hr)

- [ ] 90 min — Teach-back essay (backprop + MLP, ≥800 words, no AI) →
      `concepts/week-07-teachback-backprop.md` [NN3]
- [ ] 45 min — Twitter thread #6 (from-scratch NN journey) → POST LIVE, save URL [NN2]
- [ ] 30 min — Networking: 3 replies + 1 DM to a target engineer [Week 5+ track]
- [ ] 🚀 Commit: `week-07: MLP from scratch + teach-back + thread`
      **Exit:** scratch-MLP matches PyTorch; teach-back written; thread posted.

### Sun Aug 2 (6hr) — Retro + P2 scope + Anki authoring

#### Morning (3hr)

- [ ] 15 min — Anki (out loud)
- [ ] 90 min — Own-words Anki loop: author this week's concept cards in MY words,
      LLM rates, store polished versions (perceptron, activations, backprop, autograd)
- [ ] 75 min — P2 scope: break nanoGPT into Weeks 7–8 milestones (bigram → attention → block → training)

#### Afternoon (3hr)

- [ ] 90 min — Week 7 retro → `weekly-logs/retro-week-07.md`
      (shipped/slipped, velocity, ONE root cause, can-explain vs fuzzy table, top-3 gaps,
      ONE fix-rule, + did the tripwire/out-loud rules actually fire this week?) [NN5]
- [ ] 60 min — Update `01-current-state.md`, `03-active-tasks.md`, `06-current-task.md`
- [ ] 30 min — 🚀 Commit: `week-07: retro + P2 scope + Anki authoring`
      **Exit:** retro done, P2 milestones drafted, context updated, rules-fired check written.

---

## Non-negotiables (Week 7)

| #   | Rule           | Check                             |
| --- | -------------- | --------------------------------- |
| NN1 | GitHub commits | ≥4 (Tue–Fri)                      |
| NN2 | Twitter        | Thread #6 posted Sat              |
| NN3 | Teach-back     | backprop essay ≥800w Sat          |
| NN4 | Anki           | daily, OUT LOUD, no silent passes |
| NN5 | Retro          | `retro-week-07.md` Sun            |

## Risk & mitigation

| Risk                            | Mitigation                                                    |
| ------------------------------- | ------------------------------------------------------------- |
| Post-Phase-1 slump              | Tripwire armed; Tue restart is light + concrete (perceptron)  |
| Backprop rabbit hole            | Hard timebox; goal = intuition + 1 worked example, not proofs |
| Weekend fade (home/energy)      | Apply weekend-minimum rule: 15-min Anki floor non-negotiable  |
| Anki reverting to silent passes | "out loud" tagged on every day's block                        |
