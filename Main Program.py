import joblib
from sklearn.feature_extraction.text import CountVectorizer

# Loading the saved models
loaded_svm_model = joblib.load('svm_model.joblib')
loaded_vectorizer = joblib.load('vectorizer.joblib')

# Geting the user input
user_input = input("Enter a text: ")

# Preprocessing and vectorizing the user input
user_input = [user_input]  # Convert to a list for consistency with previous vectorization
X_user_input = loaded_vectorizer.transform(user_input)

# Making the predictions on the user input
prediction = loaded_svm_model.predict(X_user_input)

# Displaying the result
if prediction[0] == 1:
    print("The input is offensive.")
else:
    print("The input is not offensive.")
