import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib

# Load train and test
X_train = pd.read_csv("X_train.csv")
X_test = pd.read_csv("X_test.csv")

# Initialize vectorizer
vectorizer = TfidfVectorizer(max_features=5000)

# Fit on training data
X_train_tfidf = vectorizer.fit_transform(X_train['comment_text'])
X_test_tfidf = vectorizer.transform(X_test['comment_text'])

# Save vectorizer and vectorized matrices
joblib.dump(vectorizer, "vectorizer.pkl")
joblib.dump(X_train_tfidf, "X_train_tfidf.pkl")
joblib.dump(X_test_tfidf, "X_test_tfidf.pkl")

print("Vectorization complete. TF-IDF matrices and vectorizer saved.")
