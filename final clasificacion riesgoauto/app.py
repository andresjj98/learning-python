from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Cargar el modelo entrenado
model = joblib.load('random_forest_model.pkl')

# Ruta para renderizar el formulario
@app.route('/')
def form():
    return render_template('index.html')

# Ruta para recibir los datos del formulario y hacer la predicción
@app.route('/submit_dropdown', methods=['POST'])
def submit_dropdown():
    # Obtener los datos del formulario
    make = int(request.form['make'])
    fuelType = int(request.form['fuelType'])
    aspiration = int(request.form['aspiration'])
    numOfDoors = int(request.form['numOfDoors'])
    bodyStyle = int(request.form['bodyStyle'])
    driveWheels = int(request.form['driveWheels'])
    engineLocation = int(request.form['engineLocation'])
    engineType = int(request.form['engineType'])
    numOfCylinders = int(request.form['numOfCylinders'])
    normalizedLosses = float(request.form['normalizedLosses'])
    wheelBase = float(request.form['wheelBase'])
    length = float(request.form['length'])
    width = float(request.form['width'])
    height = float(request.form['height'])
    curbWeight = float(request.form['curbWeight'])
    engineSize = float(request.form['engineSize'])
    compressionRatio = float(request.form['compressionRatio'])
    horsepower = float(request.form['horsepower'])
    cityMpg = float(request.form['cityMpg'])
    highwayMpg = float(request.form['highwayMpg'])
    price = float(request.form['price'])

    # Formar un arreglo con los datos para hacer la predicción
    #data = np.array([[make, fuelType, aspiration, numOfDoors, bodyStyle, driveWheels, engineLocation, engineType,
    #                  numOfCylinders, normalizedLosses, wheelBase, length, width, height, curbWeight, engineSize,
    #                 compressionRatio, horsepower, cityMpg, highwayMpg, price]])


    data = np.array([[normalizedLosses, wheelBase, length, width, height, curbWeight, engineSize, compressionRatio, horsepower, cityMpg, highwayMpg, price, make, bodyStyle, driveWheels, engineType, numOfCylinders, fuelType, numOfDoors, aspiration, engineLocation]])
    
    # Realizar la predicción
    prediction = model.predict(data)

    # Pasar la predicción a la plantilla result.html
    return render_template('result.html', prediction=prediction[0])

if __name__ == '__main__':
    app.run(debug=True)
