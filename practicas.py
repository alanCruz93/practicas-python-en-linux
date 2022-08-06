"""
#--------Adivina el numero--------
import random
def adivina(n):
    print("=================")
    print("JUGUEMOS")
    print("=================")
    numero=""
    aleatorio = random.randint(0,n)
    intento = 0

    while numero != aleatorio and intento <= 11:
        numero = int(input("Dime un numero: "))
        if numero == aleatorio:
            print("Felicidades has encontrado el numero")

        elif numero < aleatorio:
            
            print("Tu numero es mas bajo")
            
        elif numero > aleatorio:
            print("Tu numero es mas alto")

        elif intento == 10:
            print("Lo siento tus intentos se han terminado")
            break
            
        else:
            print("Lo siento no lo has conseguido")

        intento += 1

adivina(100)

#Crea una funcion que te diga si es una año bisiesto 
def bisiesto(año):
    leap = False
    if (año%4)== 0:
        leap= True
        if(año%100)==0:
            leap=False
            if(año%400)==0:
                leap=True
        return leap
    else:
        print("fallo")

prueba=bisiesto(1996)
print(prueba)

#convertir una lista en string ordenado 

n = int(input("Dime un numero: "))
c=[]
while n > 0 and n <= n:
    c.append(n)
    c.sort()
    n-=1
    
print(c)
a= "".join(map(str,c))
print(a)

#comprension de listas 
import math
lista= [1,2,3,4,5,12,15,13,44]

prueba_1= [int(math.sqrt(x)) for x in lista]
print(prueba_1)

#ejemplo 2
prueba_2=[x if (x < 15) else "no" for x in lista]
print(prueba_2)

#ejemplo 3 tambien en cadena de caracteres
texto= "convierte a mayusculas"
c= [c.upper() for c in texto]
print(c)


#Mostrar por pantalla fecha y hora actuales
from cmath import sqrt
import datetime
fecha= datetime.datetime.now()
print(fecha) 
formato= fecha.strftime("Hora: %H:%M:%S Dia: %y-%m-%d")
print(formato)

#Solicitar al usuario el radio para calcular su area
import math
radio= float(input("Dime cual es el radio: "))
area= math.pi * radio ** 2
resultado= f"El area de tu radio es: {area} "
print(resultado)

#Pedir nombre al usuario y mostrarlo en orden inverso
nombre= input("Dime cual es tu nombre: ")
valor= nombre[::-1]
print(valor)

# Pedir base y altura para sacar area de un triangulo 
base= float(input("Cual es la base: "))
altura= float(input("Cual es la altura: "))
area_triangulo= (base * altura)/2
print(f"El area de tu triangulo es: {area_triangulo} ")


#devuelve las combinaciones de 3 listas pero solo las que su suma entre ellas no sea mayor a n
li1= 1
li2= 1
li3= 1
n=2

combinaciones= [[i,j,k] for i in range(0, li1+1) for j in range(0,li2+1) for k in range(0, li3+1) if(i+j+k) != n]
print(combinaciones)

#Devuelve el valor del numero submaximo de una lista
maximo= [1,2,3,9,11,4,11,11,5]
maximo.sort()
x = max(maximo)

while x == max(maximo):
    r=0
    maximo.pop()
    r= max(maximo)

print(r)

#Ejercicio hackerrank
materia=[]
for a in range(0,2):
        name = str(input("Dime cual es el nombre: "))
        score = float(input("Cual es su puntaje: "))
        alumno=[name,score]
        materia.append(alumno)

print(materia)

lista=[["alan",99.5],["maria",77.9],["adario", 89.5],["jesus", 89.5]]
segunda=[]
for c in lista:
    segunda.extend(c)
print(lista)
minimo= min(lista)
print(minimo)
"""