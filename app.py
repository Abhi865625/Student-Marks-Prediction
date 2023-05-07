import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# Load the dataset into a Pandas DataFrame
data = pd.read_csv('student_data.csv', encoding='unicode_escape')

# Split the dataset into features (X) and target (y) variables
X = data[['internal marks', 'external marks']]
y = data['final marks']

# Create an instance of the LinearRegression class
model = LinearRegression()

# Train the model on the entire dataset
model.fit(X, y)

# Set up the Streamlit app
st.title("STUDENT MARKS PREDICTION")

# Add input fields for internal and external marks
internal_marks = st.number_input("Internal marks (out of 350):", min_value=105, max_value=350, step=1)
external_marks = st.number_input("External marks (out of 350):", min_value=105, max_value=350, step=1)

# Create a submit button
submit_button = st.button("Submit")

# Predict the final percentage upon submitting
if submit_button:
    prediction = model.predict([[internal_marks, external_marks]])
    predicted_final_percentage = prediction[0]

    # Check for failing grade
    if internal_marks < 105 and external_marks < 105:
        result = "Fail"
    else:
        result = "Pass"

    # Display the predicted final grade and result
    st.subheader("Predicted final percentage:")
    st.write(f"{predicted_final_percentage:.2f}%")
    st.subheader("Result:")
    st.write(result)
