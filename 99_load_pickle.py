import joblib

file_path = "X_train_tfidf.pkl"
data = joblib.load(file_path)
print(data)
