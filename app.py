import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
with open('student_marks_predictor_model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

df = pd.DataFrame()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    global df

    # Get input features
    input_features = [int(x) for x in request.form.values()]
    feature_value = np.array(input_features)

    # Validate input study hours (between 1 and 23)
    if feature_value[0] < 1 or feature_value[0] > 23:
        return render_template('index.html', prediction_text='Please Enter a valid hour between 1 to 23')

    # Predict using the loaded model
    output = loaded_model.predict([feature_value])[0]  # Extracting scalar value from array
    output = float(output)  # Convert NumPy array to float
    output = round(output, 2)  # Round the output to 2 decimal places

    # Cap the predicted score between 0 and 100
    if output > 100:
        output = 100
    elif output < 0:
        output = 0

    # Store the input and predicted value in DataFrame and save to CSV
    df = pd.concat([df, pd.DataFrame({'Study Hours': input_features, 'Predicted Output': [output]})], ignore_index=True)
    df.to_csv('data_from_app.csv', index=False)

    # Render result in HTML template without brackets
    return render_template('index.html', prediction_text=f'The Predicted Score is {output}%, When You study for {int(feature_value[0])} hours per day.')

if __name__ == "__main__":
    app.run(host = '127.0.0.1', port = 5000)
