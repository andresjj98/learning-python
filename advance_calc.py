'''Crear una calculadora que reciba dos valores por consola y realice las
operaciones aritméticas basicas'''

import os #para utilizar comandos del sistema

os.system('clear')#Para limpiar la pantalla en git bash

#inputs
print("Ingrese primer valor: ")
n1= int(input())

n2 = int(input("Ingrese segundo valor:"))

suma= n1 + n2

print("suma:", suma)

