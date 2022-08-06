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
print(interseccion)

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
#otro ejemplo
nutricion = namedtuple("Alimento", "nombre proteina grasas hidratos")

jamon = nutricion("jamon", "20g", "15g", "1g")
print(jamon[1])#imprimir el contenido por indice
print(jamon._fields)#devuelve nombres de los campos
print(jamon._asdict())#si quieres que te devuelva la tuple como diccionario

jamon= jamon._replace(grasas="18g")# Si quieres modificar algun contenido
print(jamon)
pollo= nutricion._make(["pollo","25g", "5g", "0g"]) #esta es otra forma de crear la tupla
print(pollo)

#--------orderedDict---------
#orderedDict son como diccionarios pero recordando el orden en que se agregaron elementos
from collections import OrderedDict

libreria = {
    "primaria": "Atlas mexico",
    "secundaria" : "Baldor matematicas"
}
ordenada = OrderedDict(libreria)
print(ordenada)
#otro ejemplo
nombres= {"Alan":28, "Maria":22, "Jesus": 17, "Pedro":49}
orden = OrderedDict(nombres)
print(orden)


from click import prompt

# defaultDict devuelve por defecto un valor a algun elemento que no se encuentre definido
from collections import defaultdict
equipos= defaultdict(int)
equipos["chivas"]=12
equipos["Pumas"]=7
print(equipos["toluca"])

# coleccion deque funciona de una manera similar a una cola o fila
from collections import deque
año =[1993,2000,2018,2022]
mi_deque= deque(año)
print(mi_deque)
mi_deque.append(1945)#Si quiero agregar un valor al final
print(mi_deque)
mi_deque.appendleft(1929)#si quiero agregar al inicio
print(mi_deque)
restante= mi_deque.pop()#borra el valor al final y popleft al inicio
print(restante)#El elemento eliminado se puede asignar a otra variable

siglo_ant= [1840,1888,1867]
mi_deque.extend(siglo_ant)# puedes unir con extend tambien extendleft lo agrega del lado izquierdo
print(mi_deque)
mi_deque.rotate(2) #te permite rotar los elementos 
print(mi_deque)

#-----------------ITERTOOLS--------------
#nos permite realizar operaciones utiles con iteradores
#product regresa el producto cartesiano
from itertools import product
a= [1,2,3]
b= [3,4,5]
producto= list(product(a,b))
print(producto)
#para poder verlo necesitamos convertirlo a lista

#acumulate
from itertools import accumulate
num= [1,2,3,4,5,6,7]
acumulado= list(accumulate(num))# esto lo que hace es que va sumando desde cero y va sumando el valor al sig.
print(acumulado)


#permutations regresa permutaciones unicas ordenadas de longitud n

from itertools import permutations

permu= list(permutations([1,2,3,4], 2))
print(permu)
# resultado=[(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)]

from itertools import combinations

comb= list(combinations([1,2,3,4],2))#regresa las combinaciones no ordenadas y tampoco se combina entre el mismo elemento
print(comb)
#resultado= [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]

from itertools import combinations_with_replacement

comb_wr= list(combinations_with_replacement([1,2,3],2))# este si lo hace consigo mismo
print(comb_wr)
#resultado= [(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]

#groupby     ordena los elementos dentro de grupos
from itertools import groupby
num= [1,1,1,2,2,3,3,3,3,4,4,5,6,7,8,8,8]
grupo = groupby(num)

for k, g in grupo:
    print(f"llave: {k}")
    print(f"grupo: {list(g)}")
    print()

letras= "aaabbbbccdeeff" #tambien se puede hacer con strings
grupo_letras= groupby(letras)

for l,d in grupo_letras:
    print(f"llave: {l} ")
    print(f"grupo: {list(d)}")
    print()


#---------------Lambda functions--------------
#Son pequeñas funciones anonimas
x= lambda a,b: a * b
print(x(30,4))

#numeros complejos se componen de un numero real y una parte imaginaria
complejo1= 3 -2j    #Primera forma
print(type(complejo1))

complejo2= complex(3,-2) #Segunda forma
print(type(complejo2))

#operaciones artimeticas con numeros complejos

suma= complejo1 + complex(3, +3)
print(suma)
resta= complejo1 - complex(3, +3)
print(resta)

#-------------Funcion map-------------
def cuadrado(num):
    #return num * num
    return pow(num, 2)

lista= list(range(1,6))
print(lista)
elevar = list(map(cuadrado, lista))
print(elevar)


#------------listas anidadas------------
multidimension= [
    [1,2,3,4],
    [5,6],
    [11,13,[100,200]]
]
for fila in multidimension:
    for col in fila:
        print(col)

for tres in multidimension[2][2]:
    print(tres)


#Devuelve el alumno con el segundo puntaje mas bajo
n = int(input())
marksheet = [[input(), float(input())] for _ in range(n)]

second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))
"""

