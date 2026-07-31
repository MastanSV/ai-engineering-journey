### Tue Jul 29 (1.5 hr) — CONCEPT: Activation Functions & Non-Linearity

- [x] **15 min — Anki Review**
  - [x] Review previous Neural Network cards
  - [x] Review Logistic Regression vs Neural Networks
  - [x] Mark weak cards for revision

---

#### 1. Why do we need activation functions? (15 min)

- [x] Understand what happens if there is **no activation function**
- [x] Learn why stacking linear layers still produces a linear model
- [x] Understand why neural networks need **non-linearity**
- [x] Draw a simple diagram illustrating this

---

#### 2. Learn Sigmoid (15 min)

- [x] Understand the intuition behind Sigmoid
- [x] Learn the mathematical formula
- [x] Know the output range (0 to 1)
- [x] Understand where Sigmoid is used
- [x] Learn its drawbacks:
  - [x] Vanishing gradients
  - [x] Not zero-centered
  - [x] Saturation

---

#### 3. Learn Tanh (10 min)

- [ ] Understand how Tanh differs from Sigmoid
- [ ] Learn the output range (-1 to 1)
- [ ] Understand why zero-centered outputs help optimization
- [ ] Learn its drawbacks (vanishing gradients)

---

#### 4. Learn ReLU (15 min)

- [ ] Understand the intuition behind ReLU
- [ ] Learn the mathematical formula
- [ ] Understand why ReLU became the default activation
- [ ] Learn the "dying ReLU" problem
- [ ] Know common variants:
  - [ ] Leaky ReLU
  - [ ] ELU (high level)
  - [ ] GELU (high level)

---

#### 5. Compare Activation Functions (10 min)

- [ ] Create a comparison table:

| Property           | Sigmoid | Tanh | ReLU |
| ------------------ | ------- | ---- | ---- |
| Output Range       |         |      |      |
| Zero-Centered      |         |      |      |
| Vanishing Gradient |         |      |      |
| Computational Cost |         |      |      |
| Typical Usage      |         |      |      |

---

#### 6. Coding Exercise (10 min)

- [ ] Plot Sigmoid
- [ ] Plot Tanh
- [ ] Plot ReLU
- [ ] Observe their output ranges
- [ ] Observe how gradients behave visually

---

#### 7. Interview Practice (10 min)

- [ ] Explain:
  - [ ] Why do neural networks need activation functions?
  - [ ] Why can't we stack only linear layers?
  - [ ] Why is ReLU preferred over Sigmoid?
  - [ ] When would you use Sigmoid?
  - [ ] What is the dying ReLU problem?
  - [ ] What causes vanishing gradients?

---

#### 8. Feynman Notes (5 min)

- [ ] Complete the sentence:

> Without activation functions, a deep neural network collapses into a **single linear transformation**, regardless of the number of layers.

- [ ] Write a 5-line explanation in your own words.

---

#### 9. Revision (5 min)

- [ ] Create 5 Anki cards from today's learning
- [ ] Summarize the key takeaways in one page

---

- [ ] 🚀 Commit notes/code to GitHub

### Exit Criteria

- [ ] Explain non-linearity without notes.
- [ ] Explain Sigmoid, Tanh, and ReLU mathematically and intuitively.
- [ ] State the advantages and disadvantages of each activation function.
- [ ] Explain why ReLU is the default choice in modern neural networks.
- [ ] Answer common activation function interview questions confidently.
