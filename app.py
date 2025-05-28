from fastapi import FastAPI
from pydantic import BaseModel
import joblib
from fastapi.responses import FileResponse
import pandas as pd

# Load the trained model
model = joblib.load("diabetes_model.joblib")

# Define input data model (for request validation)
class PatientData(BaseModel):
    Pregnancies: int
    Glucose: int
    BloodPressure: int
    SkinThickness: int
    Insulin: int
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int

# Initialize FastAPI app
app = FastAPI()

# Serve index.html at the root URL
@app.get("/", response_class=FileResponse)
def home():
    return FileResponse("index.html")

# Prediction endpoint
@app.post("/predict")
def predict_diabetes(data: PatientData):
    # Convert input data to DataFrame
    input_data = pd.DataFrame([data.dict()])
    
    # Make prediction
    prediction = model.predict(input_data)[0]
    
    # Return result
    if prediction == 1:
        return {"result": "You may have diabetes. Please consult a doctor."}
    else:
        return {"result": "You likely do not have diabetes."}