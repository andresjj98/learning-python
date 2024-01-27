#API: application programming interface
#Nasa API: https://api.nasa.gov/
#Developer: Andres Josa
#Date: 26012024
#Get data  from NASA about comets
#API_KEY_NASA: Nb6SJKGykZgc7aLyKCI4IptBrgxo53SzVXpbUYYr

import requests
import os

os.system('clear')

def get_comet_data(api_key):
    print(":::::COMET INFORMATION::::")
    url = f"https://api.nasa.gov/neo/rest/v1/neo/3726712?api_key={api_key}"

    try:
        #realizar la solicitud a la api
        response = requests.get(url)
        response.raise_for_status()#valida si se presenta algun error
        #convertir la respuesta a formato json
        datos = response.json()

        print(f"comet name: {datos['name']}")

    except requests.exceptions.RequestException as e:
        print(f"Error en la peticion a la api de nasa: {e}")


api_key_nasa = 'Nb6SJKGykZgc7aLyKCI4IptBrgxo53SzVXpbUYYr'
get_comet_data(api_key_nasa)