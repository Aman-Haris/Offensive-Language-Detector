#Step 1: Importing packages
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Step 2: Loading and Preprocessing Data
data = pd.read_csv('Data\Data.csv', encoding='latin1')

# Handling the missing values by replacing NaN with an empty string
data['text'].fillna('', inplace=True)

# Step 3: Spliting Data for training and testing
train_data, test_data, train_labels, test_labels = train_test_split(
    data['text'], data['is_offensive'], test_size=0.2, random_state=42
)

# Step 4: Text Vectorization
vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(train_data)
X_test = vectorizer.transform(test_data)

# Step 5: Building and Training SVM Model
svm_model = LinearSVC(dual=False, max_iter=5000)
svm_model.fit(X_train, train_labels)

# Step 6: Evaluating the Model
predictions = svm_model.predict(X_test)

# Calculating the Metrics
accuracy = accuracy_score(test_labels, predictions)
classification_report_result = classification_report(test_labels, predictions)

print(f"Accuracy: {accuracy:.2f}")
print("\nClassification Report:")
print(classification_report_result)

# Step 7: Saving the trained model and vectorizer to use in the API
model_filename = 'svm_model.joblib'
vectorizer_filename = 'vectorizer.joblib'

joblib.dump(svm_model, model_filename)
joblib.dump(vectorizer, vectorizer_filename)

print(f"Trained model and vectorizer saved to {model_filename} and {vectorizer_filename}")
