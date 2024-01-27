'''script 
Cree una funcion que genere el lanzamiento de dos dados y que muestre en pantalla
un mensaje que diga "GANADOR" cuando genere par, de lo contrario
el mensaje dira "SIGA INTENTANDO"'''

#importo biblioteta para generar numeros aleatorios enteros
from random import randint 

#Lanzar y generar los valores de los dos lados
def dices():
    dice1 = randint(1,6)
    dice2 = randint(1,6)

    return dice1, dice2

d = dices()
print("Dado uno y dos respectivamente =",d)
print("Dado uno:",d[0],"Dado dos:",d[1])