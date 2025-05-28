import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

# Load dataset (make sure your CSV file is in the same folder)
df = pd.read_csv("diabetes.csv")

# Features and target
X = df.drop("Outcome", axis=1)  # Input features
y = df["Outcome"]               # Target variable

# Split into training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Evaluate
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print(f"Model Accuracy: {accuracy:.2f}")

# Save the trained model
joblib.dump(model, "diabetes_model.joblib")
print("Model saved as diabetes_model.joblib")
