"""
# #52   acceso a tuplas

datos= (10,20,30)
x= datos[0]
y= datos[1]
print(x)
print(y)
#otra forma es el desempaquetamiento    se van asignando los valores por orden 
abscisa, ordenada, tercera= datos
print(tercera)

#***********************Las tuplas son inmutables************************** son solo de lectura
# tambien son un elemento iterable
#ejemplo con while
iterame= (12,55,43,2,77,110,3,22,4,7,0,[1,2])

i=0
while i < len(iterame):
    print(f"El indice {i} tiene un valor de: {iterame[i]}")
    i+=1

#ejemplo con for
print("Iterado con for")
for i in range(len(iterame)):
    print(f"El indice {i} tiene un valor de: {iterame[i]}")

#otra forma es con la funcion enumerate este te devuelve dos valores la clave y el valor
print("Iterando con enumerate")
for i,v in enumerate(iterame):
    print(f"El indice {i} tiene un valor de: {v}")

#Todas las formas de crear tuplas
primera= (1,2,3) #con parentesis
segunda= 1,2,3,4 #sin parentesis si es de 1 solo valor poner una ,
tercera= tuple((1,2,3,4)) #con el constructor
print(tercera)
print(dir(tuple)) #Te muestra todos los metodos que puedes usar con tuplas, listas, set, etc

#Metodos de las tuplas

from itertools import count

numero= ("alan","kevin",3,5,3,"olivia")

print(numero.count(3))

print(numero.index("olivia"))


#Listas

lista= ["Chivas", "Pumas", "Monterrey", "Leon", "Tigres"]
cortados= lista[:5:2]  #slicing
print(cortados)
 #desempaquetamiento

primero, segundo, tercero= cortados
print(segundo)

numero= [55,6,776,97]
for i in range(len(numero)):
    print(f"indice {i} tiene un valor de: {numero[i]} ")

print("espacio")
#de derecha a izquierda
for a in range(len(numero)-1, -1, -1):
    print(f"indice {a} tiene un valor de: {numero[a]} ")

#El primer valor es len de numero menos 1 luego el rango de -1 para que tome al indice 0 y el tercero el decre

#Cuando no necesitas el indice hacerlo asi
for n in numero:
    print(f"valor: {n}")

#funcion enumerate permite iterar mas facil clave y valor
recorre= ["batman", "superman", "joker", "hulk","hulk"]
recorre.insert(2, "Ironman")
recorre.insert(-2, "spiderman")
recorre.remove("hulk")
for i,v in enumerate(recorre):
    print(f"indice {i} personaje: {v}")

"""
