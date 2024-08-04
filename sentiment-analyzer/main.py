from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Sample data
texts = ["I love this!", "I hate this!", "It's okay.", "Absolutely wonderful!", "It's so bad", "It's not good"]
labels = [1, 0, 1, 1, 0, 0]  # 1: Positive, 0: Negative

# Split data
X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=0.2, random_state=42)

# Create a pipeline
pipeline = make_pipeline(CountVectorizer(), LogisticRegression())

# Train the model
pipeline.fit(X_train, y_train)

# Predict
predictions = pipeline.predict(X_test)
print(predictions)
# Evaluation
accuracy = accuracy_score(y_test, predictions)
precision = precision_score(y_test, predictions)
recall = recall_score(y_test, predictions)
f1 = f1_score(y_test, predictions)

print(f"Accuracy: {accuracy}")
print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"F1 Score: {f1}")