from flask import Flask, render_template, request
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('random_forest_model.pkl')

# Load the dataset
dataset = pd.read_csv('df_encoded.csv')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the car number entered by the user
    car_number = int(request.form['car_number'])

    # Extract the features for the corresponding car number
    car_data = dataset.iloc[car_number][['normalized-losses','wheel-base','length','width','height','curb-weight',
                                         'engine-size','compression-ratio','horsepower','city-mpg','highway-mpg',
                                         'price','make_encoded','body-style_encoded','drive-wheels_encoded',
                                         'engine-type_encoded','num-of-cylinders_encoded','fuel-type_encoded',
                                         'num-of-doors_encoded','aspiration_encoded','engine-location_encoded']]
    
    # Make prediction using the model
    prediction = model.predict([car_data])[0]

    return f"El nivel de riego del vehiculo {car_number} es: {prediction}"

if __name__ == '__main__':
    app.run(debug=True)
