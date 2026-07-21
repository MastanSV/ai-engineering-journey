> **As of 2026-07-21 — Week 6 · Tuesday (planning day).**
> Previous session: Finished teach-back blocks 4–6 + Anki cards (Fri Jul 17).
> Next session (Wed Jul 23): Build Gradio app for P1.

# Current Task — Build Gradio App (Wed Jul 23, 1.5hr)

## Pre-check (first 15 min)

Before writing `app.py`, verify the model artifact exists:

1. Open `projects/05_P1_Tabular_ML/Heart_Disease_Dataset.ipynb`
2. Check if the best model was saved to disk (look for `joblib.dump` or `pickle.dump` or MLflow `log_model`)
3. If no saved model file exists → add a cell at the end of the notebook:
   ```python
   import joblib
   joblib.dump(best_pipeline, 'best_model.pkl')
   ```
4. Run that cell, confirm `best_model.pkl` appears in the project folder

## Build `app.py` (60 min)

### Structure

```
projects/05_P1_Tabular_ML/
├── Heart_Disease_Dataset.ipynb   (existing)
├── heart.csv                     (existing)
├── README.md                     (existing — polish on Sat)
├── app.py                        ← BUILD THIS
├── best_model.pkl                ← from pre-check
└── requirements.txt              ← create Thu
```

### What the app needs

1. **Load model:** `joblib.load('best_model.pkl')`
2. **Input components:** one Gradio input per feature (14 total). Use sliders for continuous, dropdowns for categorical. Get ranges from `heart.csv` min/max.
3. **Predict function:** takes 14 inputs → create DataFrame row → `model.predict_proba()` → return prediction label + probability
4. **Output:** prediction ("High Risk" / "Low Risk") + probability percentage
5. **Examples:** 2–3 pre-filled example rows from the dataset (one healthy, one sick)

### Don't overthink

- No fancy CSS. Default Gradio theme is fine.
- No model retraining. Just load and predict.
- Title + one-line description is enough for now.

## Verify (15 min)

- [ ] `python app.py` launches without error
- [ ] Submitting example input returns a prediction
- [ ] Probability displays correctly (0–100%)

## 🚀 Commit when done

`week-06: P1 Gradio app initial build`

## What comes after

- **Thu Jul 24:** Local end-to-end testing + deploy prep
- **Fri Jul 25:** Push to HF Space
- **Sat Jul 26:** README + Loom + Twitter + gate + retro
- **Sun Jul 27:** Phase 2 kickoff
