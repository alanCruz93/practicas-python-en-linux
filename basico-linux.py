# Comentarios

'''
name = "Alan" #string
año = 2022 # Entero
año_Nacim = 1993
print("Hola mundo")#print mostrar en consola
edad = año - año_Nacim
print(edad)

#Tipos de datos
#Enteros no llevan decimales sean + o - 
numero = 362
print(type(numero)) #regresa int

#Flotantes 
flotante = 39.12
print(type(flotante))# regresa float

#Boolean
acceso = True
print(type(acceso))#regresa bool

#String secuencia de caracteres
cadena = "Esta es una secuencia de caracteres"
print(type(cadena))#regresa str

#funcion len() nos ayuda a saber cuantos caracteres hay
print(len(cadena))

#Indexacion permite acceder a caracteres indiv
print(cadena[1])

#Rebanado o slicing sirve para obtener una porcion de un string
print(cadena[0 : 4])

#variaciones
print(cadena[5 : ])#solo lleva el inicio y se agregara todo lo demas

print(cadena[ : 11])# lo contrario al anterior

print(cadena[ : ])#Se obtendra una copia del string

# PASO hay una manera de saltar un caracter al sig
joker="principal enemigo de batman!!"
print(joker[10 : 17 : 2])#se salta un caracter intermedio entre indices

#------METODOS de strings
print(joker.capitalize())#Vuelve mayuscula la primer letra
#Find() busca el caracter buscado el primer
print(joker.find("i"))
#upper() devuelve copia en mayusculas
print(joker.upper())
#lower devuelve copia en minusculas
mayus= "ESTE TEXTO SE VOLVERA EN MINUSCULAS"
minus= mayus.lower()
print(minus)
pruebaindex = "Encuentra la letra"
print(pruebaindex.index("e"))
#Si quiero saber si es minuscula todo el string 
print(pruebaindex.islower())
print(pruebaindex.lower().islower())#ahora es true

#---------------NUMBERS----------
uno = 324
dos = 87
print(uno % dos)
#max me devuelve el numero mayor
print(max(3534, 5675, 234))
#min lo contrario
print(min(34, 4564, 323))
#Redondea un numero 
print(round(39.5))
#convierte un numero a binario
print(bin(3))

#Importar funciones math
from math import * # de math importa todo
print(sqrt(200))#raiz cuadrada


#--------INPUTS-----------
#Escribe un programa que pida al usuario nombre, edad, estado civil, estudios y devuelva su informacion completa
nombre = input("Escribe tu nombre completo ")
edad = (input("¿Que edad tienes? "))
civil = input("¿Cual es tu estado civil? ")
estudios = input("¿Cual es tu grado de estudios? ")
resumen = print("Tu nombre es "+ nombre + " con una edad de ",edad + " ,estudios concluidos hasta " + estudios + " y  su estado civil es " + civil )

#Ejercicio remplaza la palabra que quieras de tu texto
texto= input("Cuentame algo nuevo")
cambio=input("Que palabra quieres cambiar?")
nueva= input("Cual es la nueva palabra?")
original = print(texto)
remplazo = texto.replace(cambio, nueva)
print(remplazo)


#-------Listas o arrays
paises = ["Mexico","UK","Alemania", "Francia"]
print(paises[0])
#Aqui tambien funciona el slicing
print(paises[2: 4])
#Cambia UK por canada
paises[1] = "Canada"
print(paises)
#si coloco un -1 me devuelve el ultimo valor
print(paises[-1])
#Obten la longitud de toda la lista
print(len(paises))
#Esta es otra forma de crear una lista
raza= list(("Chihuahua","baset hound","bulldog"))
'''
#----------Metodos de listas
heroes =["Batman", "Superman", "Ironman"]
villanos=["Joker", "Lex Luthor", "Dormamu"]
villanos.append("Darkseid")   #Agrega un villano mas
#Une las listas
heroes.extend(villanos)
heroes.append("Capitan America")
print(heroes)