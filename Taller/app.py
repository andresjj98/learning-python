# save this as app.py
from flask import Flask,request 
import base64
from PIL import Image
from io import BytesIO
from flask_cors import CORS
from keras.models import load_model
import numpy as np
from keras.models import model_from_json
import cv2



app = Flask(__name__)
CORS(app)

@app.route('/',methods=['POST'])
def hello():       
    data = request.json['imagen']    
    base64_data = data.split(',')[1]
    image_data = base64.b64decode(base64_data)
    img = Image.open(BytesIO(image_data))

    img = np.array(img)    
    

    print("imagen",img.shape)

    # Cargar la arquitectura desde el archivo JSON
    with open('helloworld.json', 'r', encoding='utf-8') as archivo:
        arquitectura = archivo.read()

    model = model_from_json(arquitectura)
    # Cargar los pesos desde el archivo HDF5
    model.load_weights('pesos_modelo.h5')

    img = cv2.resize(img, (28, 28),interpolation=cv2.INTER_AREA)
    img = img / np.max(img)
    img=img[:,:,1]
    x0=np.array([img])
    print("al modelo",x0.shape)
    return {'number':str(np.argmax(model.predict(x0)))}
