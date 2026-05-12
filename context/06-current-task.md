### Wed May 13 — Notebook 06 Part A: sigmoid + log-loss (1.5hr, 9:00–10:30 PM)

**Slot plan (90 min):**

- [ ] 💻 **75 min — `daily-notebooks/week-02/06-logistic-from-scratch.ipynb`** (create file; no sklearn for the model)
  - **Cell 1 — imports:**
    ```python
    import numpy as np
    import matplotlib.pyplot as plt
    from sklearn.datasets import make_classification
    ```
  - **Cell 2 — fake binary data:**
    ```python
    X, y = make_classification(n_samples=200, n_features=2, n_redundant=0,
                               n_clusters_per_class=1, random_state=42)
    ```
    Scatter plot colored by class.
  - **Cell 3 — sigmoid function + sanity tests:**
    ```python
    def sigmoid(z): return 1 / (1 + np.exp(-z))
    # Test: sigmoid(0) ≈ 0.5, sigmoid(10) ≈ 1.0, sigmoid(-10) ≈ 0.0
    ```
  - **Cell 4 — log-loss function + sanity tests:**
    ```python
    def log_loss(y, p, eps=1e-15):
        p = np.clip(p, eps, 1 - eps)
        return -np.mean(y * np.log(p) + (1 - y) * np.log(1 - p))
    # Test: perfect → loss ≈ 0; random 0.5 → loss ≈ 0.693 (= ln 2)
    ```
  - **Cell 5 — gradient function + 3 sanity tests:**
    - At truth (should be near zero)
    - At zero weights (should be non-zero)
    - At flipped weights (should be large)
  - **Cell 6 — markdown:** "What does `eps` guard against? What would happen without it?"
- [ ] 🚀 **15 min — Commit:** `week-03 day-3: notebook 06 part A (sigmoid + log-loss + sanity tests)`
