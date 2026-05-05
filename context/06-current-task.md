### Wed May 6 — Notebook 05 Part A: Standardize + Ridge (1.5hr)

**Slot plan (90 min):**

- [ ] 💻 **75 min — `daily-notebooks/week-02/05-ridge-lasso-california.ipynb`** (create file + folder)
  - **Cell 1 — imports:**
    ```python
    import numpy as np, pandas as pd, matplotlib.pyplot as plt, mlflow
    from sklearn.datasets import fetch_california_housing
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    from sklearn.linear_model import LinearRegression, Ridge
    from sklearn.metrics import mean_squared_error, r2_score
    ```
  - **Cell 2 — load + split + standardize:**
    ```python
    data = fetch_california_housing(as_frame=True)
    X, y = data.data, data.target
    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)
    scaler = StandardScaler().fit(X_tr)
    X_tr_s = scaler.transform(X_tr); X_te_s = scaler.transform(X_te)
    ```
  - **Cell 3 — MLflow setup:**
    ```python
    mlflow.set_experiment("week-02-ridge-lasso")
    ```
  - **Cell 4 — baseline LinearRegression run** (log params: model_type, n_features; metrics: train_mse, test_mse, train_r2, test_r2; log model)
  - **Cell 5 — Ridge run** (try `alpha=1.0`); same logging pattern
  - **Cell 6 — markdown narration:** "Did Ridge improve test MSE? By how much? Did the coefficient magnitudes shrink? Show before/after."
  - **🚨 Sanity check:** baseline test R² should match Week 1 notebook 04 (~0.58). If not, you mis-split.
- [ ] 🚀 **15 min — commit + push:** `week-02 day-3: notebook 05 part A (standardize + ridge + mlflow)`

**End-of-day:** update state file; carryover audit.
