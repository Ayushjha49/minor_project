import pandas as pd
from sklearn.model_selection import train_test_split

# Load cleaned data
df = pd.read_csv("labeled_comments.csv")

# Features and labels as DataFrames
X = df[['comment_text']]
y = df[['sentiment']]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Reset index for neatness
X_train, X_test = X_train.reset_index(drop=True), X_test.reset_index(drop=True)
y_train, y_test = y_train.reset_index(drop=True), y_test.reset_index(drop=True)

# Save splits
X_train.to_csv("X_train.csv", index=False)
X_test.to_csv("X_test.csv", index=False)
y_train.to_csv("y_train.csv", index=False)
y_test.to_csv("y_test.csv", index=False)

print("Train-test split complete and saved as CSV files.")

