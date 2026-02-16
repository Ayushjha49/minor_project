import joblib
from sklearn.linear_model import LogisticRegression

import pandas as pd

# Load vectorized data and labels
X_train_tfidf = joblib.load("X_train_tfidf.pkl")
y_train = pd.read_csv("y_train.csv")

# Initialize model
model = LogisticRegression(max_iter=1000)

# Train model
model.fit(X_train_tfidf, y_train['sentiment'])

# Save trained model
joblib.dump(model, "sentiment_model.pkl")
print("Model training complete and model saved as sentiment_model.pkl")
