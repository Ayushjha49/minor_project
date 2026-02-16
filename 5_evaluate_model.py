import joblib
import pandas as pd
from sklearn.metrics import accuracy_score, classification_report

# Load model, test data, labels
model = joblib.load("sentiment_model.pkl")
X_test_tfidf = joblib.load("X_test_tfidf.pkl")
y_test = pd.read_csv("y_test.csv")

# Predict
y_pred = model.predict(X_test_tfidf)

# Evaluate
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
