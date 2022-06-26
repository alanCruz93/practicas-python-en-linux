# sets son como listas o diccionarios, desordenado, mutable y no duplicados

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
# une los sets
union = set2.union(set3)
print(union)
#encuentra la interseccion entre 2 sets
interseccion = set2.intersection(set3)
print(interseccion)
#encuentra la diferencia entre los 2 sets
difer = set2.difference(set3)
print(difer)

#si se quisieran actualizar los sets usar update, difference_update, interseccion_update
#saber si son subconjuntos todos los elementos del primer set tienen que estar en el segundo para ser true
cuatro = {10,20,30,40}
quinto = {10,20}
print(cuatro.issubset(quinto))#false
print(quinto.issubset(cuatro))#true

#superset devuelve true si el primer set contiene todos los elementos del segundo
print(cuatro.issuperset(quinto))
#si no tiene elementos de interseccion
sexto = {50,60}
septimo = {70,80}
print(sexto.isdisjoint(septimo))

#un frozenset es inmutable
frio = frozenset([1,2,3,4])
print(frio)