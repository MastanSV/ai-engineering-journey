## Planning rule (added 2026-11-02)

- 90-min slot = **60 min planned work + 30 min buffer**.
- **One main outcome per weekday.** If the main outcome is done → day = ✅.
- Saturday = max 4.5hr planned of 6hr. Sunday = max 4.5hr planned of 6hr.

---

## Flow this week (realistic)

```
Mon         Tue          Wed            Thu             Fri              Sat              Sun
PITCH   →   WHITEBOARD → DERIVE      →  CODE         →  CODE          →  CODE + TRAIN  →  CONNECT
Task 8+9    Task 10      matrix shapes  1 neuron        2-layer forward  backward + XOR   teach + retro
```

---

## Daily breakdown

### Mon Nov 2 (60 min planned) — Main outcome: 60-second pitch

- [x] 15 min — Anki (aloud)
- [x] 25 min — **Task 8:** skeleton (5 min) → record (2 min) → score (5 min) → fix → record again (5 min) → save
- [x] 15 min — **Task 9:** curveball questions, cold, aloud. Mark ✅ / 🟡 / ❌ only. No second round today.
- [x] 5 min — Commit: `week-07: backprop pitch + curveballs`
      **Main outcome:** pitch recorded in under 60 sec.

### Tue Nov 3 (60 min planned) — Main outcome: whiteboard test passed

- [x] 15 min — Anki
- [x] 5 min — Task 9 second round: only the 🟡 / ❌ questions from Monday
- [ ] 30 min — **Task 10:** timed run (5 min) → score → fix → timed run again → photo
- [ ] 5 min — Tick the Commit Checklist + Progress Tracker in `06-current-task.md`
- [ ] 5 min — Loom check: found / not found → one line in `01-current-state.md`
      **Main outcome:** whiteboard forward + backward in < 5 min. Backprop is closed.

### Wed Nov 4 (60 min planned) — Main outcome: matrix shapes on paper

- [ ] 15 min — Anki
- [ ] 45 min — On paper: 2-layer net with `X (4, 2)`, hidden size 4, output size 1.
  - Shape of `W₁`, `b₁`, `Z₁`, `H`, `W₂`, `b₂`, `ŷ` (forward only)
  - Then `dW₂` and `db₂` only. Stop there.
    **Main outcome:** all forward shapes correct + `dW₂` shape matches `W₂`.
    _`dW₁`, `db₁` → Saturday morning (with code next to it)._

### Thu Nov 5 (60 min planned) — Main outcome: one neuron in numpy

- [ ] 15 min — Anki
- [ ] 10 min — Open `week-08/neural-network.ipynb`. List what is already done.
- [ ] 35 min — `week-08/01-neuron-numpy.ipynb`: forward + backward with Task 5 numbers.
      **Main outcome:** code `dL/dw` = your paper `dL/dw`.

### Fri Nov 6 (60 min planned) — Main outcome: 2-layer forward pass runs

- [ ] 15 min — Anki
- [ ] 45 min — `week-08/02-mlp-numpy.ipynb`: XOR data, init weights, `forward(X)` with cache. Print every shape.
      **Main outcome:** forward runs; shapes match Wednesday's paper.

### Sat Nov 7 (4.5hr planned) — Main outcome: MLP learns XOR

- [ ] 15 min — Anki
- [ ] 45 min — Paper: `dW₁`, `db₁` (finish Wednesday's derivation)
- [ ] 75 min — Code `backward()`
- [ ] — 15 min break —
- [ ] 45 min — Gradient check on 1–2 weights
- [ ] 60 min — Training loop on XOR + loss plot + 4 predictions
- [ ] 15 min — Commit
      **Main outcome:** loss goes down, XOR predictions correct.
      **If time remains:** 1 experiment only — remove hidden ReLU. What happens?

### Sun Nov 8 (4.5hr planned) — Main outcome: retro + honest public update

- [ ] 15 min — Anki
- [ ] 60 min — Anki cards (own words → LLM rates) → `anki-cards-week-07.tsv`
- [ ] 90 min — Teach-back `concepts/week-07-teachback-backprop.md` (≥800 words) [NN3]
- [ ] 45 min — Retro `weekly-logs/retro-week-07.md` (break cause, prevention rule, new target date)
- [ ] 30 min — Twitter post (short thread, 4–5 tweets) [NN2]
- [ ] 30 min — Update context files (01, 02, 03, 04, 06) + GitHub profile
      **Main outcome:** retro written, new target date decided, public update posted.

---

## Moved to next week (Nov 9–15)

- `make_moons` + decision boundary plot
- Experiments: hidden size, learning rate
- PyTorch check: compare autograd gradients with numpy gradients (fits PyTorch-basics week)
