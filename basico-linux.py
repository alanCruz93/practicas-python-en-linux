# Comentarios


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

