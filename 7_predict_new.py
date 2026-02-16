import joblib

# Load model and vectorizer
model = joblib.load("sentiment_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Example new comment
new_comment = ["I hate modi"]

# Transform and predict
new_vector = vectorizer.transform(new_comment)
prediction = model.predict(new_vector)

print("Sentiment:", prediction[0])
