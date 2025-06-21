# 🛡️ Offensive Language Detector (Multilingual)

A Flask-based NLP service for detecting offensive language in **English** and **Kannada** text inputs. Built using **SVM (Support Vector Machine)** and trained on publicly available datasets, this tool classifies text as either **offensive** or **not offensive** via a simple API endpoint.

---

## 📌 Problem Statement

Detecting offensive and harmful content online is crucial for promoting safer digital environments. This project was developed as part of the **ML Engineer Assessment** for Youth India E-School and includes:

- Multilingual support (English & Kannada)
- One API endpoint (`/detect-offensive`)
- Trained using labeled datasets from open-source repositories
- High performance with real-world test cases

---

## 🧠 Features

- 🧾 Input: A sentence or word in English/Kannada
- 🚦 Output: Boolean (`true` for offensive, `false` otherwise)
- 🔗 One-click REST API integration using Flask
- 💬 Clean prediction logic using trained SVM classifier
- 📁 Trained on combined datasets with preprocessing included

---

## 🚀 How to Run

1. Clone the repository
```
git clone https://github.com/yourusername/offensive-language-detector.git
cd offensive-language-detector
```

2. Install requirements
```
pip install -r requirements.txt
```

3. Run the API server
```
python api.py
```

4. Make a sample API call
Use Postman or curl:

```
curl -X POST http://127.0.0.1:5000/detect-offensive \
     -H "Content-Type: application/json" \
     -d '{"text": "your input text here"}'
```

---

## 🗂️ Project Structure

```
Offensive-Language-Detector/
│
├── api.py                 # Flask API for predictions
├── Main Program.py        # CLI version for local testing
├── Model Training.py      # Training script for SVM model
├── svm_model.joblib       # Trained classifier (binary)
├── vectorizer.joblib      # CountVectorizer (for encoding text)
├── /Data/                 # Dataset folder (CSV files)
├── ReadMe.txt             # Original brief
└── README.md              # You're here
```

---

## 📈 Model Performance

The model was trained on 39,221 samples across both languages. Below are the evaluation metrics:

|              | precision | recall | f1-score | support |
| ------------ | --------- | ------ | -------- | ------- |
|           0  |     0.96  |   0.98 |     0.97 |  31237  |
|           1  |     0.93  |   0.84 |     0.88 |    7984 |
|              |           |        |          |         |
|    accuracy  |           |        |     0.95 |   39221 |
|   macro avg  |     0.95  |   0.91 |     0.93 |   39221 |
| weighted avg |      0.95 |   0.95 |     0.95 |   39221 |	

---

## 🌐 Dataset Sources

* English Dataset:
profanity-check by vzhou842

* Kannada Dataset:
Hate-Alert-DravidianLangTech

---

## 🧪 Example Inputs & Output

|       Input        |  Output  |
| ------------------ | -------- |
| "You are a fool"   |   true   |
| "Have a nice day"  |   false  |
| "ನೀನು ಮೂರ್ಖ"    |   true    |
| "ನೀವು ಚೆನ್ನಾಗಿದ್ದೀರಿ" |   false   |

---

## 🧰 Dependencies

* Python 3.x
* Flask
* scikit-learn
* pandas
* joblib

---

## 🧑‍💻 Author

Aman Haris
- Submitted for: Youth India E-School – ML Engineer Assessment

---

## 📜 License

This project is distributed for academic and demonstration purposes. Please credit the author if reused or extended.
