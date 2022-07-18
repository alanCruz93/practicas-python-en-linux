# sets son como listas o diccionarios, desordenado, mutable y no duplicados
"""
mi_set = {1,1,1,2,5,2,4}
#agrega 3 elementos y despues borra uno
mi_set.add(8)
mi_set.add(33)
mi_set.add(24)
mi_set.remove(33)# tambien se puede usar discard 
print(mi_set)

#itera el set
for num in mi_set:
    print(num)

set2 = {0,1,2,3,4,5}
set3 = {4,5,6,7,8}
#--------UNION-------
# une los sets
union = set2.union(set3)
print(union)
#otra forma de hacer uniones
union__dos ={"perro","gato","pato"} | {"caballo","gato"}
print(union__dos)

#------Intersecciones de sets-----------
#encuentra la interseccion entre 2 sets
interseccion = set2.intersection(set3)
print(interseccion)

#Otra forma de hacer una interseccion
conj__a = {3,6,8,3,5,6,7}
conj__b = {6,3,8,7,0,2,1}
interseecion= conj__a & conj__b
print(interseecion)

#-------Diferencia---------
#encuentra la diferencia entre los 2 sets
difer = set2.difference(set3)
print(difer)
#otra forma de hacer diferencia
diferencia = {3,6,7,0,11,42} - {3,6,7,11}
print(diferencia)

#--------Diferencia simetrica----- son elementos que estan en el primer conjunto y no en el segundo y alreves
simetrica1 = {11,65,22}
simetrica2={11,4,77}
simetricaRes= simetrica1.symmetric_difference(simetrica2)
print(simetricaRes)

#si se quisieran actualizar los sets usar update, difference_update, interseccion_update
#saber si son subconjuntos todos los elementos del primer set tienen que estar en el segundo para ser true
cuatro = {10,20,30,40}
quinto = {10,20}
print(cuatro.issubset(quinto))#false
print(quinto.issubset(cuatro))#true

#superset devuelve true si el primer set contiene todos los elementos del segundo cuando un conjunto contiene a otro
print(cuatro.issuperset(quinto))
#otro ejemplo
superSet= {1,2,3,4,5}.issuperset({1,2,3,4,5,6})
print(superSet)

#si no tiene elementos de interseccion
sexto = {50,60}
septimo = {70,80}
print(sexto.isdisjoint(septimo))
#otro ejemplo
sinInter= {1,2,3,4,5}.isdisjoint({6,7,8,9})
print(sinInter)#true

#tipo 2 de sets un frozenset es inmutable
frio = frozenset([1,2,3,4])
print(frio)

#-------------Metodos de string------
#Borra espacios del string
cadena = "          Esta cadena tenia espacios a la izquierda"
nueva= cadena.lstrip()#para borrar espacios a la derecha usar rstrip()
print(nueva)
#Borra espacios de ambos lados
ambos = "     Esta cadena tenia espacios a ambos lados      "
ambos_nue = ambos.strip()
print(ambos_nue)
otros = "........Esta cadena tiene otros simbolos $$?$$$"
quitar = otros.strip(". $ ?")
print(quitar)

#startswith y endswith
empezar = "Nintendo es una empresa famosa de videojuegos es japonesa"
print(empezar.startswith("Nintendo"))
print(empezar.endswith("ropa"))

#Find
print(empezar.find("es"))

#contar coincidencias count()
print(empezar.count(" es "))

#replace()
print(empezar.replace("japonesa", "China"))

#Split() convierte un string en lista
convertir = "Este string se convertira en lista"
lista = convertir.split()
print(lista)

#convertir lista en cadena
regresar = " ".join(lista)
print(regresar)

# %s es como concatenacion son formas antiguas de hacerlo
nombre = input("Dime cual es tu nombre: ")
ingresa = "El nombre de tu paciente es %s" %nombre
print(ingresa)

# %d
numero = 3453
print("Tu numero es: %d" %numero)#este es en caso de numero enteros
decimal = 234.24234
print("Tu decimal es: %.2f" %decimal)#Aqui especifique cuantos decimales queria

#los f-string son los mas recomendable ahora
suerte = int(input("Dime tu numero de la suerte: "))
deci = float(input("Dime un numero decimal: "))
oracion = f"Tu numero de la suerte es: {suerte} y tu numero decimal es: {deci}"
print(oracion)

#----------------Collections--------------
from collections import Counter
#Counter
letras = "aaaaaabbbbbbbbcccc"
contadas = Counter(letras)
print(contadas)
#mas comun  
print(contadas.most_common(2))

#convertir contador en lista   
contad_lista = list(contadas.elements()) #se tiene que convertir a una lista primero
print(contad_lista)

#namedtuple
from collections import namedtuple
punto = namedtuple('point', 'x,y')
pt = punto(24, -13)
print(pt)

#orderedDict son como diccionarios pero recordando el orden en que se agregaron elementos
from collections import OrderedDict

libreria = {
    "primaria": "Atlas mexico",
    "secundaria" : "Baldor matematicas"
}
ordenada = OrderedDict(libreria)
print(ordenada)


from click import prompt
"""
