#Script description: get all data about comets.

import requests
import os

os.system('clear')

def get_comets():
    print(":::Comets inforamtion:::")
    url = "https://api.le-systeme-solaire.net/rest/bodies/?filter%5B%5D=isComet"
   
    try:
        #request to api
        response = requests.get(url)
        response.raise_for_status()

        #print all comets names
        data = response.json()
        #print(data["bodies"]) codigo comentariado
        count = 0

        total = int(input("Cantidad de datos a mostrar "))
        planeta= input("Introdusca el planeta")
        print(" ")
        
        for comet in data ["bodies"]:

            if comet ["englishName"] == planeta:
                print("English name: ", comet["englishName"])
                #print("moons: ", comet["moons"])
                print("gravity: ", comet["gravity"])
                print("Is planet?: ", comet["isPlanet"])
                print(" ")

            count = count + 1
            
            if count == total:
                break
            print(count)
    except requests.exceptions.RequestException as e:
        print(f" API error:{e}")

#Call function
get_comets()
