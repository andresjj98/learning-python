'''
Bucle que genere una n cantidad de numeros enteros solicitada por el usuario
El usuario debe digitar la cantidad de numeros enteros positivos o negativos a generar.
Al finalizar debe presentar por pantalla el siguiente reporte

- Total de numeros ingresados
- Cuantos numeros son pares
- Cuantos numeros son impares
- Cuantos numeros son positivos
- Cuantos numeros son negativos
- La suma de los numeros pares
'''


import os
import random

os.system('clear')

def number_generator(cant):
    i = 1
    pares = 0
    impares = 0
    positivos = 0
    negativos = 0
    sum_pos = 0
    sum_neg = 0
    while i <= cant:
        num = random.randint(-100,100)
        print(num)
        
        if num % 2 == 0:
            pares = pares + 1
        else:
            impares += 1
        #validad y contar los positivos y negativos
        if num > 0:
            positivos += 1
            sum_pos = sum_pos + num
        else:
            negativos += 1
            sum_neg += num

    

        i += 1

    print(f"Total de numeros generados: {cant}")
    print(f"Total de numeros pares generados: {pares}")
    print(f"Total de numeros impares generados: {impares}")
    print(f"Total de numeros positivos generados: {positivos}")
    print(f"Total de numeros negativos generados: {negativos}")
    print(f"Suma de numeros positivos generados: {sum_pos}")
    print(f"Suma de numeros positivos generados: {sum_neg}")

cant_num = int(input("¿Qué cantidad de numeros deseas generar?: "))
number_generator(cant_num)


