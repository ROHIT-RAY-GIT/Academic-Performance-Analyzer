# Academic Performance Analyzer 📚✨

## Overview
The **Academic Performance Analyzer** is a machine learning project that predicts student marks based on their study hours. Utilizing linear regression, this tool helps students understand how their study time correlates with academic performance. 

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Usage](#usage)
- [Model Performance Metrics](#model-performance-metrics)
- [Results and Analysis](#results-and-analysis)
- [Summary of Performance Metrics](#summary-of-performance-metrics)
- [Conclusion](#conclusion)

## Features
- 📈 Predicts student marks based on input study hours.
- 📊 Displays model performance metrics such as Mean Squared Error (MSE) and R-squared (R²).
- 💾 Saves input study hours and predicted marks to a CSV file for record-keeping.
- 🌐 User-friendly interface built with Streamlit.

## Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Streamlit
- Pickle

## 📊 Model Performance Metrics:

- **Mean Squared Error (MSE): 1.1080**
- **R-squared (R²): 0.9514 (95.14%)**
- **Mean Absolute Error (MAE): 0.8781**

## 📈 Results and Analysis:

- **Test Accuracy:**
Value: **0.9514** (or 95.14%)
**Interpretation**: This indicates that the model correctly predicts student marks approximately 95.14% of the time on the test dataset. High test accuracy suggests that the model generalizes well to new, unseen data and effectively captures the relationship between study hours and student performance.

- **Train Accuracy:**
Value: 0.9589 (or 95.89%)
**Interpretation**: The model achieves an accuracy of 95.89% on the training dataset. This score is slightly higher than the test accuracy, indicating that the model has learned well from the training data. However, it's essential to ensure that the model is not overfitting.

- **Mean Squared Error (MSE):**
Value: **1.1080**
**Interpretation**: MSE measures the average squared difference between the predicted marks and the actual marks. A lower MSE value indicates a better fit of the model to the data. In this case, an MSE of 1.1080 suggests that, on average, the squared errors of predictions are small.

- **R-squared (R²):**
Value: **0.9514** (or 95.14%)
**Interpretation**: R² indicates the proportion of variance in the dependent variable (student marks) that can be explained by the independent variable (study hours). An R² value of 0.9514 implies that approximately 95.14% of the variability in student marks can be explained by their study hours.

- **Mean Absolute Error (MAE):**
Value: **0.8781**
**Interpretation**: MAE measures the average magnitude of the errors in a set of predictions. An MAE of 0.8781 means that, on average, the model's predictions deviate from the actual marks by about 0.8781 marks.

## 🚀 Summary of Performance Metrics:
**Test Accuracy: 95.14%** – High predictive accuracy on unseen data.
**Train Accuracy: 95.89% **– Slightly higher accuracy on the training data, indicating good learning but warranting an assessment for overfitting.
**Mean Squared Error (MSE): 1.1080** – Low average squared error suggests a good fit to the data.
**R-squared (R²): 95.14%** – A high percentage of variance explained by study hours.
**Mean Absolute Error (MAE): 0.8781** – Indicates average absolute prediction error is small.

## Conclusion:
The results show that the Student Mark Predictor model is highly effective in predicting student performance based on study hours. The high accuracies and low error metrics reflect a robust model capable of generalizing well to unseen data.
