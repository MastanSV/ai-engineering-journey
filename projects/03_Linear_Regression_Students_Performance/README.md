# 01_Student_Exam_Score_Prediction

## Project Overview
This is my first Machine Learning project. I built a **Simple Linear Regression** model to predict a student's Exam Score based on the number of hours they studied.

## Objective
To understand the relationship between study hours and exam performance and build a model that can predict exam scores.

## Dataset
- **Number of samples**: 20
- **Feature (X)**: Study_Hours (in hours)
- **Target (y)**: Exam_Score (out of 100)

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn

## Results

| Metric              | Value          | Interpretation                        |
|---------------------|----------------|---------------------------------------|
| Slope (m)           | 5.4348         | +5.43 marks per additional hour      |
| Intercept (c)       | 39.3137        | Baseline score                       |
| R² Score            | 0.9806         | 98.06% variance explained            |
| RMSE                | 2.2389         | Average prediction error ~2.24 marks |
| MAE                 | 1.7562         | Typical error ~1.76 marks            |

## Key Insights
- There is a **very strong positive relationship** between study hours and exam score.
- For every extra hour of study, students score approximately **5.43 marks** higher on average.
- The model explains **98.06%** of the variation in exam scores.

## What I Learned
- Implementing Simple Linear Regression from data loading to interpretation
- Understanding and interpreting Slope, Intercept, and R² Score
- Difference between MSE, RMSE, and MAE
- Importance of data visualization (scatter plot + best fit line)
- How to draw real-world conclusions from a regression model

## How to Run
1. Open the Jupyter Notebook `student_exam_score_prediction.ipynb`
2. Run all cells

## Future Improvements
- Collect a larger and more diverse dataset
- Add more features (sleep hours, attendance, previous test scores, etc.)
- Perform residual analysis to check model assumptions

---

**Part of My Machine Learning Learning Journey**