import streamlit as st
import numpy as np
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import os

# Loading the trained model
with open('student_marks_predictor_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Function to predict marks
def predict_marks(study_hours):
    return model.predict([[study_hours]])[0][0]

# Function to save input and prediction to a CSV file
def save_to_csv(study_hours, predicted_marks):
    # Check if the CSV file exists, if not create it with headers
    file_path = 'predictions.csv'
    if not os.path.isfile(file_path):
        df = pd.DataFrame(columns=["Study Hours", "Predicted Marks"])
        df.to_csv(file_path, index=False)

    # Append the new data to the CSV file
    new_data = pd.DataFrame({"Study Hours": [study_hours], "Predicted Marks": [predicted_marks]})
    new_data.to_csv(file_path, mode='a', header=False, index=False)

# Dashboard title
st.title("Student Mark Predictor 📚")

st.markdown("<hr>", unsafe_allow_html=True)  # Horizontal line
st.markdown("<br>", unsafe_allow_html=True)

# Sidebar for user input
st.sidebar.header("Input Parameters")
study_hours = st.sidebar.number_input("Enter Study Hours:", min_value=0.0, max_value=24.0, value=0.0)

# Button to trigger prediction
if st.sidebar.button("Predict"):
    predicted_marks = predict_marks(study_hours)
    # Display predicted marks in a larger, bold font
    st.markdown(f"<h3 style='font-weight: bold;'>Predicted Marks for {study_hours} hours of study: <span style='color: blue;'>{predicted_marks:.2f} %</span></h2>", unsafe_allow_html=True)
    
    # Add a gap and a horizontal line
    st.markdown("<hr>", unsafe_allow_html=True)  # Horizontal line
    st.markdown("<br>", unsafe_allow_html=True)  # Gap

    # Save input and prediction to CSV
    save_to_csv(study_hours, predicted_marks)
    # st.success("Input hours and predicted marks saved to predictions.csv!")

    # Display model performance metrics
    # Replace these with your actual metrics from the previous code
    mse = 1.108  # Example value, replace with actual MSE
    r2 = 0.951  # Example value, replace with actual R²
    mae = 0.8780690208883186  # Replace with actual MAE computation

    # Show performance metrics
    st.subheader("Model Performance Metrics:")
    st.write(f"Mean Squared Error (MSE): **{mse:.3f}**")
    st.write(f"R-squared (R²): **{r2:.3f}**")
    st.write(f"Mean Absolute Error (MAE): **{mae:.3f}**")

    # Create a plot for visualization
    # st.subheader("Predicted vs Actual Marks")
    # plt.figure(figsize=(10, 6))
    # plt.scatter([study_hours], [predicted_marks], color='blue', label='Predicted Marks')
    # plt.plot([0, 24], [0, 100], color='red', linestyle='--', label='Perfect Prediction Line')
    # plt.title("Actual vs Predicted Marks")
    # plt.xlabel("Study Hours")
    # plt.ylabel("Marks")
    # plt.legend()
    # st.pyplot(plt)

# Footer
st.markdown("---")
st.markdown("### About this Project")
st.write("This dashboard predicts student marks based on study hours using a linear regression model. "
         "The model's performance is evaluated using various metrics.")
