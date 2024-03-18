'''
Bucle puede ser un loop, repetir una accion N veces, iteraciones.
Acomuladores (acumulacion de valores)
Contar valores es diferente de sumar valores
'''

#funcion Bucle para imprimir los numeros del 1 al 10 en pantalla.
import os

os.system('clear')

def list_numbers():
    i = 1
    while i <= 10:
        print("Numero",i)
        i+=1

    print("i:", i)

def list_numbers2():
    i = 1
    status = True
    while status: #while status ==true
        if  i == 11:
            break
        print(i)
        i+=1

def list_numbers3():
    i = 1
    status = True
    while status: #while status ==true
        
        print(i)
        i+=1
        if  i > 15:
            status = False

#list_numbers()
#list_numbers2()
list_numbers3()