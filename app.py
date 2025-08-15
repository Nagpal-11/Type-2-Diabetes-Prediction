from flask import Flask, request, render_template
import joblib
import numpy as np
import time

app = Flask(__name__)

# Load model 
model = joblib.load('diabetes_pipeline.pkl')


@app.route('/')
def home():
    return render_template("index.html" , time = time)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from form
        data = [float(x) for x in request.form.values()]
        data = np.array(data).reshape(1, -1)
        # Predict
        prediction = model.predict(data)[0]
        result = "Yes" if prediction == 1 else "No"
        
        return render_template("index.html", prediction_text=f"Diabetes: {result}")
    except Exception as e:
        return render_template("index.html", prediction_text=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
