import joblib
import pandas as pd

# Load the saved model
model = joblib.load('diabetes_model.joblib')

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a number.")

print("Enter the patient's data for prediction:")

# Gather inputs interactively
data = {
    "Pregnancies": int(get_float_input("Number of pregnancies: ")),
    "Glucose": get_float_input("Glucose level: "),
    "BloodPressure": get_float_input("Blood pressure: "),
    "SkinThickness": get_float_input("Skin thickness: "),
    "Insulin": get_float_input("Insulin level: "),
    "BMI": get_float_input("BMI: "),
    "DiabetesPedigreeFunction": get_float_input("Diabetes pedigree function: "),
    "Age": int(get_float_input("Age: "))
}

# Create DataFrame with one row
input_df = pd.DataFrame([data])

# Make prediction
prediction = model.predict(input_df)[0]

# Output result with friendly message
if prediction == 1:
    print("\nPrediction: You may have diabetes. Please consult a healthcare professional for further tests and advice.")
else:
    print("\nPrediction: Your test results look good, no indication of diabetes based on this model.")
