# House Price Prediction using Linear Regression

## 📋 Project Overview
This is my first Machine Learning project. I built a simple Linear Regression model to predict house prices based on house size (in square feet).

## 🎯 Objective
Predict house price (in lakhs) using house size as the only feature.

## 📊 Dataset
- **Number of samples**: 8
- **Feature (X)**: House Size (sq ft)
- **Target (y)**: House Price (in lakhs)

## 🛠️ Technologies Used
- Python
- NumPy
- Matplotlib
- Scikit-learn

## 📈 Results

| Metric                    | Value                  | Interpretation                     |
|--------------------------|------------------------|------------------------------------|
| Slope (m)                | 0.0299                 | ₹2,990 per additional sq ft       |
| Intercept (c)            | 0.265 lakhs            | Baseline value                     |
| R² Score                 | 0.9992                 | 99.92% variance explained          |
| RMSE                     | 0.597 lakhs            | Average prediction error           |
| MAE                      | 0.420 lakhs            | Average absolute error             |

## 📊 Key Visualizations
- Scatter plot showing relationship between house size and price
- Best Fit Line overlaid on actual data

## 🔍 Key Learnings
- Understood how Linear Regression finds the best straight line
- Learned to interpret **slope** and **intercept** in real-world terms
- Understood difference between MSE, RMSE, and MAE
- Practiced model training, evaluation, and visualization using scikit-learn
- Importance of saying "on average" while interpreting coefficients

## 🚀 How to Run
1. Open the Jupyter Notebook
2. Run all cells

## 📌 Future Improvement Ideas
- Add more features (location, number of bedrooms, age of house)
- Try Multiple Linear Regression
- Use real-world larger dataset

---

**Made with ❤️ as part of My ML Learning Journey**