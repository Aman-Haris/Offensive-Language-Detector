from flask import Flask, request, jsonify
import joblib
from sklearn.feature_extraction.text import CountVectorizer

app = Flask(__name__)

#Loading the saved models
loaded_svm_model = joblib.load('svm_model.joblib')
loaded_vectorizer = joblib.load('vectorizer.joblib')

@app.route('/detect-offensive', methods=['POST'])
def detect_offensive():
    try:
        # Geting text input from the user
        input_text = request.json['text']

        # Preprocessing and vectorizing the user input
        input_text = [input_text]  # Convert to a list for consistency with previous vectorization
        X_input = loaded_vectorizer.transform(input_text)

        # Making predictions on the user input
        prediction = loaded_svm_model.predict(X_input)

        # Converting the prediction to boolean (True for offensive, False for not offensive)
        is_offensive = bool(prediction[0])

        return jsonify({'is_offensive': is_offensive})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
