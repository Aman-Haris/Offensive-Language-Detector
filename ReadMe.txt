This project was developed as a part of the coding assessment for the role of ML Engineer in Youth India E-school. The project requirements can be found in a separate file in this repo. The aim of this project is to create a single API endpoint NLP service which can detect whether the user input is offensive or not. This service can detect inputs of both English and Kannada languages.

Folders and Files in this Repo:

Data Folder: This folder contains the data files used to train our model. english.csv contains the data for English language and kannada.csv contains the data for Kannada language. Data.csv contains the combined data of both the languages. Data Cleaning.py was used to pre process the kannada language csv named k1,k2 and k3 and combine them into a single csv, and Data Processing.py program was used to combine english and kannada csv files.

Data for English language has been taken from the following repo: https://github.com/vzhou842/profanity-check/tree/master
Data for Kannada language has been taken from the following repo: https://github.com/hate-alert/Hate-Alert-DravidianLangTech/tree/master

Model Training.py: This program is used to train our data. I used Linear Support Vector Machine(SVM) to train the data, as this model is the best text classifier model. Below shows the performance metrics of our model. Class 0 represents not-offensive and Class 1 represents offensive.

Performance Metrics:
              precision    recall  f1-score   support

           0       0.96      0.98      0.97     31237
           1       0.93      0.84      0.88      7984

    accuracy                           0.95     39221
   macro avg       0.95      0.91      0.93     39221
weighted avg       0.95      0.95      0.95     39221

Main Program.py: This is a basic python program used to test the trained models before building an API for the models.

api.py: This script defines a Flask web application with a single endpoint /detect-offensive that accepts POST requests containing JSON data with a key 'text'. I have used PostMan service to deploy and test the application. The output video can be found in this repo.