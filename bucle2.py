'''
Funcion para simular los intentos de ingreso de clave en cajero automatico
intentos maximos permitidos 3
'''
import os

os.system('clear')

def cajero():
    my_keybanc = '2024' #Clave registrada en el banco

    cont_attempts = 0 #Contador de intentos de ingresar la clave
    status = True

    while status:
        clave =input("Digite su clave: ")
        if my_keybanc == clave:
            print(f"bienvenido a tu cuenta, intento: {cont_attempts}")
            break #status = false
        else :
            if cont_attempts < 2 :
                print(f"Intento {cont_attempts}:Constraseña incorrecta, intenta nuevamente")
                cont_attempts += 1
            else:
                print(f"Intento {cont_attempts}: clave incorrecta")
                cont_attempts += 1

            if cont_attempts >= 3 :
                print("Se han agotado tus intentos, cuenta bloqueada")
                status = False
                  
    
#Clave digitada en el cajero

cajero()

