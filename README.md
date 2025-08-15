A Flask-based machine learning web application that predicts the likelihood of diabetes based on medical input parameters. Built with Python, Flask, HTML/CSS/JS, and a trained ML model stored in .pkl format.

Features : Machine Learning Model trained and serialized with .pkl format Flask Backend for handling predictions HTML, CSS, and JavaScript frontend for a user-friendly interface Joblib/Pickle for model loading and execution Supports real-time predictions through a web form

Technical Stuff: Backend: Python, Flask Frontend: HTML, CSS, JavaScript ML Libraries: Scikit-learn, Pandas, NumPy Model Storage: Pickle (.pkl)

Dataset: The model is trained on the PIMA Indians Diabetes Dataset containing diagnostic measurements to determine the likelihood of diabetes occurrence.

Installation & Usage:


1.git clone https://github.com/Nagpal-11/diabetes-prediction-webapp.gitcd diabetes-prediction-webapp

2.pip install -r requirements.txt 3.python app.py 4.Open http://127.0.0.1:5000 in your browser.

Example Input for Testing: Pregnancies: 2 Glucose: 120 BloodPressure: 70 SkinThickness: 25 Insulin: 80 BMI: 28.0 DiabetesPedigreeFunction: 0.4 Age: 35


