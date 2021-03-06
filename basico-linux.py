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

#----------Metodos de listas
heroes =["Batman", "Superman", "Ironman"]
villanos=["Joker", "Lex Luthor", "Dormamu"]
villanos.append("Darkseid")   #Agrega un villano mas
#Une las listas
heroes.extend(villanos)
heroes.append("Capitan America")

#Agregar un valor nuevo en otra parte de la lista
heroes.insert(2, "Spiderman")
print(heroes)
#Elimina un valor de la lista
heroes.remove("Dormamu")
print(heroes)

#Elimina una lista completa
vacia= [1,2,3,4,5]
vacia.clear()
print(vacia)
#Encuentra el indice de un valor de la lista
nombres= ["Alan", "Maria", "Jesus", "Alberto", "Allison", "Alan"]
print(nombres.index("Jesus"))
#Cuantas veces aparece Alan en la lista
print(nombres.count("Alan"))

#Ordena una lista en orden ascendente 
ascendente= [233, 34, 78, 984]
ascendente.sort()
print(ascendente)
#Ahora ordenalos alreves
ascendente.reverse()
print(ascendente)
#haz una copia de una lista
copia= ["a" , "b", "c", "d"]
copia2= copia.copy()
print(copia2)
#Borra el ultimo elemento de la lista
copia2.pop()
print(copia2)
#Agrega z y borra c
copia2.append("z")
copia2.pop(2)#Con pop tambien se puede borrar mediante indices como remove
print(copia2)

#Tuples son como las listas pero inmutables osea que no se pueden modificar
ejemplo= (1,2,True ,3,4, "prueba",5)
print(ejemplo)
#Obten el tipo de dato en el indice 2
print(type(ejemplo[2]))
#Crea un tuple con el constructor
ejemplo2= tuple((5,9, False))
print(ejemplo2)

#---------------Functions-----------
#Crea una calculadora con las operaciones basicas
def calculadora():
    num1 =int(input("Dime el primer numero: "))
    num2=int(input("Dime el segundo numero: "))
    print("La suma es: "+str(num1+num2))
calculadora()

#Cuando no sabes cuantos parametros tendras usar *
def saludo(*nombres):
    print("Bienvenido: "+nombres[1])
saludo("Juan", "Jose", "Alan")

#Calculadora dinamica usa return para devolver el valor
def calcu(num1, num2):
    res= print("La suma es: "+ str(num1+num2) + " la resta es: "+ str(num1-num2)+ " la multiplicacion es: "+ str(num1*num2)+ " la division es: "+ str(num1/num2))
    return res
num1 = int(input("Dime el primer numero: "))
num2 = int(input("Dime el segundo numero: "))
calcu(num1, num2)

#-------------Condicionales------------
#Crea una app que permita la entrada solo a mayores de 18 años en un horario de 5 de la noche a 12 de la mañana y las mujeres pagan la mitad a partir de las 9
edad = int(input("¿Cual es tu edad?: "))
hora = int(input("Horario de entrada?: "))
genero = input("¿Cual es tu sexo?: ")
def acceso():
    if edad >= 18 and hora >= 17 and  hora < 24:
        return print("Acceso permitido disfruta")
    if edad >= 18 and hora >= 21 and hora < 24 and genero == "female":
        return print("Acceso permitido y por ser chica pagas la mitad disfruta")
    else:
        return print("No tienes la edad necesaria para ingresar o el local esta cerrado sorry")
acceso()

#----------------Diccionarios--------
lista_compras = {"pan":38, "leche": 26, "jabon": 10}
print(type(lista_compras))
#obten el precio de pan y cambialo despues
print(lista_compras["pan"])
lista_compras["pan"]= 42
print(lista_compras)
#agrega un nuevo producto
lista_compras["pollo"] = 140
print(lista_compras)
#agrega otro elemento y despues borralo
lista_compras["camara"] = 483
print(lista_compras)
del lista_compras["camara"]
print(lista_compras)

print(abs(5.7))

#-------------Bucles for-------
#se usan cuando sabemos cuantas vueltas o ciclos se haran
#crea una funcion que devuelva una lista de 0-100 y que solo sean numeros pares

def lista():
    for i in range(0, 102, 2):
        print(i)
lista()

#---------ciclos sobre elementos iterables------
carreras = ["Enfermeria", "Nutricion", "Sistemas", "Medicina"]
for c in carreras:
    print(c)

#itera sobre un diccionario primero su clave y luego el valor
peliculas = {"Terror": "IT", "Accion": "Top Gun", "Drama": "Joker"}
for clave in peliculas:
    print(clave)

for valor in peliculas.values():
    print(valor)

#itera la clave y valor al mismo tiempo 
for clave, valor in peliculas.items():
    print(clave, valor)
    

#-----------while-------
#crea una funcion que devuelva los numeros introducidos por 2 usuarios diferentes e iteralos de 3 en 3 

def ciclo():
    uno = int(input("Dame un numero: "))
    dos = int(input("Dame otro numero: "))
    while uno < dos:
        print(uno)
        uno += 3
        if uno == 25:
            continue

ciclo()
# crtl + c sirve para cortar un buble infinito

#Crea una funcion con variables locales
def registro(nombre, apellido, edad):
    nombre = input("Dime tu nombre: ")
    apellido = input("Dime tu apellido: ")
    edad = int(input("¿Cual es tu edad?: "))
    return "El cliente "+ nombre + " " +apellido+ " a sido aceptado a la edad de "+ str(edad) +" años."
alan = registro("nombre", "apellido", "edad")
print(alan)

#Serie fibonacci
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(7))

#--------------Archivos----------
with open("texto-prueba.txt", "r") as archivo:
    for linea in archivo:
        print("-----Linea-----")
        print(linea)

#para remplazar el texto completo de un archo usar w y despues el metodo .write
remplazo = {
    "alan": 100,
    "veronica": 44,
    "sofia" : 89
}
with open("archivo.txt", "w") as file:
    for nombre,calif in remplazo.items():
        file.write(nombre + " : "+ str(calif) + " \n")
#Agrega al archivo 3 claves y valor nuevas con a y luego write

agregar = {
    "eddy" : 35,
    "carolina" : 60,
    "Karla" : 95
}
with open("archivo.txt", "a") as file:
    for clave, valor in agregar.items():
        file.write(clave + " : "+ str(valor) + " \n")

#----------------importaciones--------
#importa la funcion raiz cuadrada desde el archivo modulo1
import modulo1
print(modulo1.exportar)

print(modulo1.raiz(50))
aqui = modulo1.raiz(80)
print(aqui)

#---------Errores y try except

primero = int(input("Dame un numero: "))
segundo = int(input("Dame otro numero: "))
try:
    print(primero/segundo)
except ZeroDivisionError:
    print("Tienes que ingresar solo numeros del 1-100")
#puede llevar else y al final una finally
finally:
    print("Esta clausula se ejecuta si o si ")
'''

#--------------POO-----------------
class MiCuenta:
    def __init__(self, nombre, num_cuenta, balance):
        self.nombre = nombre
        self.num_cuenta = num_cuenta
        self.balance = balance
    
    def mi_balance(self):
        print("Querido socio su balance es de: "+ str(self.balance))
    
    def datos_completos(self):
        print("Querido socio: "+ self.nombre+ " con numero de cuenta: "+ self.num_cuenta+ " tiene un balance de: " + str(self.balance))

    def deposito(self, monto):
        if self.balance > 0:
            self.balance -= monto
            print("Haz realizado un deposito de: "+ str(monto)+ " tu balance ahora es de: "+ str(self.balance))
        else:
            print("No cuentas con el saldo suficiente")

    def retiro(self, monto):
        self.balance -= monto
        print("Haz retirado de tu cuenta: "+ str(monto)+ " tu saldo actual es de: "+ str(self.balance))


cuenta_alan = MiCuenta("Alan Hernandez","4360-2257-3175", 8000)
cuenta_alan.mi_balance()
cuenta_alan.datos_completos()
cuenta_vero = MiCuenta("Veronica Rodriguez", "4475-1209-6300", 15000)
cuenta_vero.deposito(4000)
cuenta_vero.retiro(2750)

class tarjeta:
    def __init__(self, saldo, comprar, recargar):
        self.saldo= saldo
        self.comprar= comprar
        self.recargar= recargar

    def consulta(self, saldo):
        tarjeta = input("Ha introducido su tarjeta responda y/n: ")
        if tarjeta == "y":
            print("--------CARGANDO-------")
            if saldo > 0 and saldo <= 10000:
                print(f"Tienes un saldo de: {saldo} puedes tener el credito basico.")
            elif saldo >10000 and saldo <= 20000:
                print(f"Tienes un saldo de: {saldo} puedes tener el credito golden.")
            elif saldo > 20000 and saldo <= 80000:
                print(f"Tienes un saldo de: {saldo} puedes tener el credito luxury.")
            else:
                print(f"Tienes un saldo de: {saldo} no contamos con creditos para tu saldo actual.")
            print("Retire su tarjeta.")
            print("Vuelva pronto.")
        
        elif tarjeta == "n":
            print("Puede comprar una tarjeta nueva aqui")
            print("Vuelva pronto") 
    
    def recarga(self, saldo):
        print("------CARGANDO-----")
        print(f"Querido usuario usted tiene en saldo de: {saldo}")
        recargar= int(input("Introduzca la cantidad que quiere recargar: "))
        print("------PROCESANDO------")
        saldo += recargar
        print(f"Usted a recargado la cantidad de: {recargar} su saldo al momento es de: {saldo}")
        print("Gracias por confiar en nosotros vuelva pronto")
        print("Retire su tarjeta")
        
        
mia = tarjeta(8585, "no", 2000)
mia.recarga(15000)
print(mia)