## Heart Disease Dataset

### Problem statement:

<p>In this project, from the dataset we will be predicting whether the person has heart disease or not. Classifying the person has heart disease or not from the attributes given is very important because when we train the model properly with this dataset, from the future dataset, we can easily classify whether person has disease or not accurately. this model can be used anywhere in healthcare domain, like hospitals or general health surveys to understand whether the given person has heart disease or not.</p>

### Data set:

This data set dates from 1988 and consists of four databases: Cleveland, Hungary, Switzerland, and Long Beach V. It contains 76 attributes, including the predicted attribute, but all published experiments refer to using a subset of 14 of them. The "target" field refers to the presence of heart disease in the patient. It is integer valued 0 = no disease and 1 = disease.

The Heart Disease Dataset contains following attributes:

1. age
2. sex
3. chest pain type (4 values)
4. resting blood pressure
5. serum cholestoral in mg/dl
6. fasting blood sugar > 120 mg/dl
7. resting electrocardiographic results (values 0,1,2)
8. maximum heart rate achieved
9. exercise induced angina
10. oldpeak = ST depression induced by exercise relative to rest
11. the slope of the peak exercise ST segment
12. number of major vessels (0-3) colored by flourosopy
13. thal: 0 = normal; 1 = fixed defect; 2 = reversable defect
14. The names and social security numbers of the patients were recently removed from the database, replaced with dummy values.

### Feature list:

Input types, The dataset contains the following columns and iam listing the type of columns,

1. age (in years - int)
2. sex (1 = male; 0 = female)
3. chest pain type (4 values) (0, 1, 2, 3) int
4. resting blood pressure - int
5. serum cholestoral in mg/dl - int
6. fasting blood sugar > 120 mg/dl - iny
7. resting electrocardiographic results (values 0,1,2) - int
8. maximum heart rate achieved - int
9. exercise induced angina - int
10. oldpeak = ST depression induced by exercise relative to rest (Decimal)
11. the slope of the peak exercise ST segment - int
12. number of major vessels (0-3) colored by flourosopy - int
13. thal: 0 = normal; 1 = fixed defect; 2 = reversable defect - int

### Evaluation Plan:

<p>As the classification model, the metrics i will noting are, precision, recall, ROC-AUC score.
And also i will check whether the data balanced or imbalanced dataset, if it is a imbalanced dataset precision will give wrong picture. </p>

### Approach:

<p>I will try Ridge-Lasso regression model and Logistic regression model and will compare both of them.</p>
