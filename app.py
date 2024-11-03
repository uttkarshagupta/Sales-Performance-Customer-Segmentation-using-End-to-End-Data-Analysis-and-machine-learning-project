from flask import Flask, jsonify, render_template, request
import joblib
import numpy as np
import os

app = Flask(__name__)

# Define path for the model file
MODEL_PATH = os.path.join('model', 'Final_model.sav')

@app.route("/")
def index():
    return render_template("home.html")  # Make sure 'home.html' is in the 'templates' folder

@app.route('/predict', methods=['POST'])
def predict():
    # Collect input values from the form
    item_weight = float(request.form['item_weight'])
    item_fat_content = float(request.form['item_fat_content'])
    item_visibility = float(request.form['item_visibility'])
    item_type = float(request.form['item_type'])
    item_mrp = float(request.form['item_mrp'])
    outlet_establishment_year = float(request.form['outlet_establishment_year'])
    outlet_size = float(request.form['outlet_size'])
    outlet_location_type = float(request.form['outlet_location_type'])
    outlet_type = float(request.form['outlet_type'])

    # Prepare the input data as a numpy array for prediction
    X = np.array([[item_weight, item_fat_content, item_visibility, item_type, item_mrp,
                   outlet_establishment_year, outlet_size, outlet_location_type, outlet_type]])

    # Load the model and predict
    model = joblib.load(MODEL_PATH)
    Y_pred = model.predict(X)

    # Return the prediction as a JSON response
    return jsonify({'Prediction': float(Y_pred)})

if __name__ == "__main__":
    app.run(debug=True, port=9457)
