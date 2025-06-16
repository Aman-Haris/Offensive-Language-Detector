# 🧠 Offensive Language Detector (English + Kannada)

A machine learning-powered **NLP microservice API** that detects whether a given text input is offensive or not. Supports both **English** and **Kannada** languages. This project was developed as part of a coding assessment for the ML Engineer role at **Youth India E-school**.

---

## 🎯 Objective

This project was developed as a part of the coding assessment for the role of ML Engineer in Youth India E-school. The project requirements can be found in a separate file in this repo. This project aims to create a single API endpoint (`/detect-offensive`) that classifies user input as **offensive** or **not offensive** using a trained machine learning model. The model supports:
- 🚀 Fast predictions
- 🌍 Multi-language input (English + Kannada)
- 🛠️ Easy integration with external services

---

## 📁 Repository Structure

```

offensive-language-detector/
├── Data/
│   ├── english.csv              # English profanity dataset
│   ├── kannada.csv              # Combined Kannada data
│   ├── data.csv                 # Merged multilingual data
│   ├── Data Cleaning.py         # Cleans and merges Kannada CSVs
│   └── Data Processing.py       # Combines English + Kannada datasets
│
├── Model Training.py            # Trains the SVM model
├── Main Program.py              # Test script for local predictions
├── api.py                       # Flask-based API implementation
├── svm\_model.joblib             # Trained SVM model (serialized)
├── vectorizer.joblib            # Trained CountVectorizer
└── README.md                    # You are here

````

---

## 📊 Model Details

- **Algorithm**: Linear Support Vector Machine (SVM)
- **Features**: Bag-of-Words using `CountVectorizer`
- **Performance**:

| Metric        | Class 0 (Not Offensive) | Class 1 (Offensive) |
|---------------|--------------------------|----------------------|
| Precision     | 0.96                     | 0.93                 |
| Recall        | 0.98                     | 0.84                 |
| F1-Score      | 0.97                     | 0.88                 |
| Accuracy      | **95%** overall          |                      |

---

## 🚀 How to Use the API

### 1. Install Dependencies

```bash
pip install flask scikit-learn joblib
````

### 2. Run the API Server

```bash
python api.py
```

The server will be live at: `http://127.0.0.1:5000`

### 3. Test with Postman or CURL

**POST** request to:

```
http://127.0.0.1:5000/detect-offensive
```

**Body (JSON):**

```json
{
  "text": "your text here"
}
```

**Response:**

```json
{
  "is_offensive": true  // or false
}
```

---

## 📦 Model Training Pipeline

1. **Data Cleaning**: Preprocess Kannada CSVs (`k1.csv`, `k2.csv`, `k3.csv`)
2. **Data Merging**: Combine cleaned Kannada and English datasets
3. **Training**: Train a Linear SVM using BoW features
4. **Serialization**: Save model and vectorizer using `joblib`

---

## 📚 Dataset Sources

* **English Dataset**: [vzhou842/profanity-check](https://github.com/vzhou842/profanity-check)
* **Kannada Dataset**: [hate-alert/DravidianLangTech](https://github.com/hate-alert/Hate-Alert-DravidianLangTech)

---

## 📽️ Demo

> A video demonstration using Postman is included in the repository.

---

## 🙌 Author

* **Aman Haris**

---

## 📝 License

This project is for educational and assessment purposes. Attribution to the dataset sources is required if reused.
