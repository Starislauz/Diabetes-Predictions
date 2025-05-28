# 🧪 Diabetes Prediction API

This is a simple and powerful API built using **FastAPI** that predicts the likelihood of diabetes based on patient health data. The model was trained using a machine learning algorithm and served using FastAPI.

---

## 🚀 Features

- ✅ Machine learning prediction using a pre-trained model  
- ✅ REST API endpoint for predictions (`/predict`)  
- ✅ Automatic input validation with Pydantic  
- ✅ Swagger UI documentation (`/docs`)  
- ✅ Simple and clean setup  

---

## 📦 Tech Stack

- Python 3.10+  
- FastAPI  
- Pydantic  
- pandas  
- scikit-learn (model training)  
- joblib (model loading)  

---

## 📂 Project Structure

├── diabetes_model.joblib # Trained machine learning model
├── main.py # FastAPI app
└── README.md # Project documentation


---

## ▶️ How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/diabetes-predictor-api.git
cd diabetes-predictor-api

Install Requirements
pip install fastapi uvicorn pandas scikit-learn joblib

 Run the App
uvicorn main:app --reload

The API will now be running at:
http://127.0.0.1:8000

This project is open-source and free to use for educational and non-commercial purposes.
git clone https://github.com/Starislauz/diabetes-predictor-api.git
