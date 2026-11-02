# Active Tasks — Resume Week (Nov 2 – Nov 8, 2026)

## Sprint goal

Finish backprop to interview level. Build a 2-layer MLP from scratch in numpy.
Train it on XOR. Watch the loss go down. Prove the gradients are correct.

## Theme: **"Back on track — backprop to code"**

## Flow this week

```
Mon        Tue          Wed            Thu             Fri             Sat              Sun
FINISH  →  DERIVE    →  CODE        →  CODE         →  CODE         →  TRAIN         →  CONNECT
backprop   matrix form  1 neuron       forward pass    backward pass   XOR + moons      teach + post
(Tasks     (shapes)     numpy          2-layer         + grad check    + PyTorch check  + retro
 8–10)
```

## Active rules

- **Re-entry rule:** Start every session with 15 min Anki, said aloud. The break was long.
- **30-min carryover cap:** weekday carryover >30 min → push to Saturday.
- **20-min stuck rule:** stuck >20 min → switch resource before quitting.
- **Feynman check:** 3-sentence zero-jargon explanation before a concept is "learned."
- **CONCEPT → DERIVE → CODE:** do not write code for a step you cannot derive on paper.
- **Break tripwire:** 2 missed days in a row → 15-min Anki-only re-entry next day.

## Time budget

- Mon–Fri 1.5hr × 5 = 7.5hr · Sat–Sun 6hr × 2 = 12hr · **Available: 19.5hr**

---

## Daily breakdown

### Mon Nov 2 (1.5hr) — FINISH: backprop Tasks 8–10

- [ ] 15 min — Anki (aloud)
- [ ] 15 min — **Task 8:** record the 60-second pitch. Listen once. Record again.
- [ ] 20 min — **Task 9:** answer the 5 curveball questions aloud, without notes.
- [ ] 20 min — **Task 10:** whiteboard test. Draw `x → h → ŷ`, forward + backward, in < 5 min.
- [ ] 10 min — Tick the Commit Checklist in `06-current-task.md`
- [ ] 10 min — **[CONFIRM]** Loom walkthrough for P1: done or not? Write the answer in `01-current-state.md`.
- [ ] 🚀 Commit: `week-07: backprop tasks 8-10 done`
      **Exit:** all 5 items in the backprop Commit Checklist are ticked.

### Tue Nov 3 (1.5hr) — DERIVE: backprop in matrix form

- [ ] 15 min — Anki
- [ ] 60 min — On paper: the same 2-layer net, but with **vectors and matrices**.
  - Input `X` shape `(n, 2)`, hidden size 4, output size 1.
  - Write the shape of each item: `W₁`, `b₁`, `Z₁`, `H`, `W₂`, `b₂`, `ŷ`.
  - Write the 4 gradient formulas: `dW₂`, `db₂`, `dW₁`, `db₁`.
  - For each formula, check that the shapes match.
- [ ] 15 min — Photo → `concepts/images/`. Write where you got stuck.
- [ ] 🚀 Commit
      **Exit:** you can say why `dW₂ = Hᵀ · dŷ` and why the transpose is necessary.

### Wed Nov 4 (1.5hr) — CODE: one neuron in numpy

- [ ] 15 min — Anki
- [ ] 15 min — Open `week-08/neural-network.ipynb`. Write down what is already done.
- [ ] 45 min — New notebook `week-08/01-neuron-numpy.ipynb`:
  - Forward pass for one neuron with ReLU.
  - Backward pass with the Task 5 numbers (`x=2, w=3, b=1, y=10`).
  - Compare the code result with your hand result.
- [ ] 15 min — Feynman note: "My code matches my paper because \_\_\_"
- [ ] 🚀 Commit
      **Exit:** the code gives the same `dL/dw` as your Task 5 paper calculation.

### Thu Nov 5 (1.5hr) — CODE: 2-layer forward pass

- [ ] 15 min — Anki
- [ ] 60 min — New notebook `week-08/02-mlp-numpy.ipynb`:
  - Create the XOR data (4 points).
  - Initialize `W₁, b₁, W₂, b₂` with small random values.
  - Write `forward(X)` → returns `ŷ` and a cache of the intermediate values.
  - Use sigmoid at the output (XOR is yes / no) and binary cross-entropy loss.
  - Print the shape of every item. Compare with your Tuesday paper.
- [ ] 15 min — Note: "Why do I store a cache in the forward pass?"
- [ ] 🚀 Commit
      **Exit:** the forward pass runs, and all shapes match the paper.

### Fri Nov 6 (1.5hr) — CODE: backward pass + gradient check

- [ ] 15 min — Anki
- [ ] 45 min — Write `backward(cache, y)` → returns `dW₁, db₁, dW₂, db₂`.
- [ ] 30 min — **Gradient check:** change one weight by a tiny amount (`ε = 1e-5`).
      Measure the change in the loss. Compare it with your backprop value.
- [ ] 🚀 Commit
      **Exit:** the gradient check difference is less than `1e-6`.
      **Carryover rule:** if this is not done by 10:30 PM → move to Saturday.

### Sat Nov 7 (6hr) — TRAIN: make it learn

- [ ] 15 min — Anki
- [ ] 30 min — Finish Friday carryover (if any)
- [ ] 90 min — Training loop: forward → loss → backward → update. Train on XOR.
      Plot the loss curve. Print the 4 predictions.
- [ ] 60 min — Experiments. Write one sentence per result:
  - Hidden size 2 vs 4 vs 8
  - Learning rate 0.01 vs 0.1 vs 1.0
  - Remove the hidden ReLU. What happens? (Link to the "V-shape" lesson.)
- [ ] 60 min — Train on `make_moons`. Plot the decision boundary.
- [ ] 60 min — **PyTorch check:** build the same net in PyTorch. Use `loss.backward()`.
      Compare the PyTorch gradients with your numpy gradients for the same weights.
- [ ] 45 min — Feynman: "My gradients are correct because \_\_\_"
- [ ] 🚀 Commit(s)
      **Exit:** XOR accuracy is 100%, the loss goes down, and the numpy gradients match PyTorch.

### Sun Nov 8 (6hr) — CONNECT + accountability

- [ ] 15 min — Anki
- [ ] 90 min — Author Anki cards (own words → LLM RATES) → `anki-cards-week-07.tsv`:
      neuron, activation, non-linearity, output activation, forward pass, loss,
      chain rule, error signal, dead ReLU, gradient check
- [ ] 120 min — Teach-back `concepts/week-07-teachback-backprop.md` (≥800 words) [NN3]
- [ ] 45 min — Twitter thread `twitter-posts/week-07-thread-backprop.md`. POST LIVE. [NN2]
      Be honest about the break: "Back after 2 months. Here is what I built this week."
- [ ] 45 min — Retro `weekly-logs/retro-week-07.md`: - What caused the 2-month break? - What rule stops the next break? - Is the December 2026 target still real? If not, what is the new date?
- [ ] 30 min — Update `01-current-state.md`, `03-active-tasks.md`, `06-current-task.md`
- [ ] 15 min — Update the GitHub profile README
- [ ] 🚀 Commit
      **Exit:** teach-back written, thread posted, retro done, context updated, profile updated.

---

## Non-negotiables this week

| #   | Rule           | Check                                 |
| --- | -------------- | ------------------------------------- |
| NN1 | GitHub commits | ≥5 (one per day, Mon–Fri minimum)     |
| NN2 | Twitter        | `week-07-thread-backprop.md` (Sun)    |
| NN3 | Teach-back     | `week-07-teachback-backprop.md` (Sun) |
| NN4 | Anki           | Daily, said aloud                     |
| NN5 | Retro          | `retro-week-07.md` (Sun)              |

## Next week preview (Nov 9 – 15)

- PyTorch basics: tensors, autograd, `nn.Module`, optimizers
- MLP in PyTorch on a real dataset (MNIST)
- Start P2 scoping: nanoGPT milestones

## Carried from Phase 1

- [ ] **[CONFIRM] Loom walkthrough** for P1 (Mon Nov 2)
