# Week 7 · Wed — DERIVE: Forward Pass + Loss (mini-tasks)

**Rule for every step:** end with a "prove it" checkpoint. Don't move on until you
can say/write the answer without peeking.

## 15 min — Anki (aloud)

- Say the answer OUT LOUD _before_ flipping. If you only _recognize_ it, mark it wrong.
- Checkpoint: any card you hesitated on → note it, fold it into today's derivation.

## 60 min — On paper (core). 4 mini-tasks:

### M1 (10 min) — One neuron, symbols only

- Draw a single neuron with 3 inputs. Label everything: inputs, weights, bias,
  the weighted sum, the activation.
- **Prove it:** write the neuron's output as one equation. Name what each symbol
  _is_ (not just its letter).
- **Question (aloud):** why is the bias separate from the weights? What breaks if
  you drop it?

### M2 (15 min) — Vectorize it

- Rewrite that same neuron using a dot product instead of a sum of products.
- **Prove it:** show the sum form and the vector form side by side; convince
  yourself they're identical.
- **Question:** if you have 4 neurons in a layer, what shape does the weight object
  become? (Write the dimensions.)

### M3 (20 min) — 2-layer net forward pass

- Chain it: input → hidden layer (with activation) → output layer.
- Order: (1) hidden pre-activation, (2) hidden activation, (3) output
  pre-activation, (4) final output.
- **Prove it:** pick tiny numbers (2 inputs, 2 hidden units) and push one example
  all the way through by hand. Get an actual number out.
- **Question:** what happens to the output if you remove the activation between the
  layers? (Tie to Tue's non-linearity note.)

### M4 (15 min) — Both loss forms

- Write MSE and cross-entropy as formulas, then annotate each.
- **Prove it (each loss, one line):** what task is it for (regression vs
  classification)? What does the prediction look like right before the loss (raw
  number? probability?)
- **Sanity check:** plug your M3 output + a fake target into MSE → single loss number.

## 15 min — Photo → `concepts/images/`

- Before you snap it, add two margin notes in your own words:
  - (a) "forward pass = \_\_\_" in one sentence
  - (b) "the difference between MSE and cross-entropy is \_\_\_"
- The annotation is what makes the photo a _learning artifact_, not just a picture.

## 🚀 Commit

- Suggested message: `week-07: forward pass derivation + MSE/CE loss forms`

---

## Feynman exit check (aloud, before "done")

Explain in 3 plain sentences, zero jargon, how one example travels from input to a
loss number. If you reach for a symbol you can't name in words → that's your weak
spot → revisit that mini-task.
