#Tipos de datos de python.
#Python es un lenguaje dinamicamente tipado 
#(Cuando declaro una variable no es obligatorio especificar el tipo de dato)

#1. Numéricos
##Enteros Z => int
num1= 42
print("Numero 1:", num1, type(num1))
##Flotantes o decinales (reales) => float
num2 = 50.5
print("Numero 2:", num2, type(num2))
##complejos => complex
num3= 2j
print("Numero 3:", num3, type(num3))

#2. Cadena => str (string)
name = "Andres"
lastname='Josa'
profile='''Hola soy 
andres
josa
musico
informatico
'''
a = "2"
b = '11'
print (name, lastname,profile)
print(name, type(name))
print(a+b)
#print(num1 + a) no se puede imprimir int con str

#3. Logicos (Valores o expresiones booleanas)
usuario_activo = True
print("usuario_activo", type(usuario_activo))
pago_realizado = False
print("pago_realizado", type(pago_realizado))

#4. Listas
frutas=['apple', 'banana']
print(frutas,type(frutas))
detodito=['nombres',100,4994,'juan','orange']
print(detodito)
print(detodito, type(detodito[2]))
#5. Tuplas
#6. Diccionarios
#7. Conjuntos