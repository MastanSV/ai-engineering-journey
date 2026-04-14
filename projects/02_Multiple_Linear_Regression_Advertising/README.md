# Advertising Budget vs Sales Prediction

## 📋 Project Overview
This is my second Machine Learning project. I built a **Multiple Linear Regression** model to predict product sales based on advertising budget spent on TV, Radio, and Newspaper.

## 🎯 Objective
Understand how different advertising channels (TV, Radio, Newspaper) impact sales and identify the most effective channel.

## 📊 Dataset
- **Source**: Classic Advertising Dataset
- **Number of samples**: 10 (small version for learning)
- **Features (X)**: TV, Radio, Newspaper (advertising spend in thousands)
- **Target (y)**: Sales (in thousands of units)

## 🛠️ Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib & Seaborn
- Scikit-learn

## 📈 Key Results

| Metric                    | Value          | Interpretation                          |
|--------------------------|----------------|-----------------------------------------|
| R² Score                 | 0.9094         | 90.94% of sales variation explained     |
| RMSE                     | 1.4537         | Average prediction error ≈ 1,454 units  |
| MAE                      | 1.1232         | Typical error ≈ 1,123 units             |

### Model Coefficients

| Feature      | Coefficient | Interpretation (per ₹1,000 spend)          |
|-------------|-------------|--------------------------------------------|
| TV          | 0.0633      | +63.3 units in sales                       |
| Radio       | 0.2374      | +237.4 units in sales (Most Effective)     |
| Newspaper   | -0.0671     | -67.1 units in sales (Negative impact)     |
| Intercept   | 1.8555      | Base sales when advertising = 0            |

## 📊 Key Insights
- **Radio** is the most effective advertising channel.
- **TV** also shows positive impact.
- **Newspaper** advertising shows a negative relationship with sales.
- The model explains **90.94%** of the variation in sales.

## 🔍 What I Learned
- How to implement Multiple Linear Regression
- Interpreting multiple coefficients
- Importance of Exploratory Data Analysis (EDA)
- Understanding correlation between features and target
- Difference between Simple and Multiple Linear Regression
- Converting mathematical coefficients into business insights

## 🚀 How to Run
1. Open `advertising_sales_prediction.ipynb`
2. Run all cells

## 📌 Future Improvements
- Use the full Advertising dataset (200 rows)
- Handle outliers and multicollinearity
- Apply regularization (Ridge/Lasso)
- Add more features (season, discount, competition, etc.)

---

**Made with ❤️ as part of My Machine Learning Journey**