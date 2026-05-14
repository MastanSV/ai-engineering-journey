### Thu May 14 — Notebook 06 Part B: GD + decision boundary (1.5hr, 9:00–10:30 PM)

**Slot plan (90 min):**

- [ ] 💻 **75 min — Continue `06-logistic-from-scratch.ipynb`**
  - **Cell 7 — GD loop:** lr=0.1, epochs=1000; track loss every 50 epochs; print final weights + bias
  - **Cell 8 — loss curve plot** (epochs vs loss — should decrease smoothly)
  - **Cell 9 — decision boundary plot:** mesh grid over feature space, color regions by predicted class, scatter training points on top
  - **Cell 10 — accuracy:** compute train accuracy with threshold=0.5
  - **Cell 11 — markdown reflection:**
    1. What did you clip/guard against (the `eps`)?
    2. What if classes were perfectly separable — what happens to the weights?
    3. What's the analog of the "convex bowl" from linreg?
- [ ] 🚀 **15 min — Commit:** `week-03 day-4: notebook 06 part B (GD loop + decision boundary + reflection)`
