#Compresion de listas 
cuadrados =[]

for i in range(10):
    cuadrados.append(i**2)


#nueva_lista = [expresion for elemento in iterable]
'''
nueva_lista: es la lista resultante que se creará a partir de la compresión.
expresón : es la operación o calculo que se realizará en cada elemento del iterable.
elemento: es la variable que representa cada elemento del iterable en cada iteración.
iterable: es una secuencia, como una lista, una cadena de texto, una tupla o incluso otro objeto iterable.
'''

cuadrados_opt = [i**2 for i in range(10)]

#Si tenemos una lista y queremos solo recorrer los que son pares
numeros = [1,2,3,4,5]

pares = []
for x in numeros:
    if x %2 ==0:
        pares.append(x)

pares_opt = [x for x in numeros if x % 2 == 0]

palabras = ["hola", "python", "compresion", "listas"]
longitudes = [len(palabra) for palabra in palabras]
print(longitudes)

#funcion map->aplica un funcion a cada elemento de una lista
#map(funcion, iterable)
'''
funcion: es la funcion que deseas aplicar a cada elemento del iterable.
iterable: es una secuencia, como una lista, una tupla o icluso otro objeto iterable.
'''
numeros = [1,2,3,4,5]
cuadrados = list(map(lambda x: x**2, numeros))
#lo convertimos a lista porque si no es un objeto map que no hay quien entienda
print(cuadrados)
#La función lambda es una funcion de una linea de codigo que se puede guardar en una variable invluso
#cuadrados = lambda x: x**2
#Luego lo usariamos de la forma cuadrados(2)

numeros1 = [1,2,3,4,5]
numeros2 = [10,20,30,40,50]
suma = list(map(lambda x,y: x+y,numeros1, numeros2))
print(suma)

#filter
#filter(funcion,iterable)
'''
funcion: es una funcion que toma un elemento del iterable como argumento y devuelve un valor booleano se incluira si es verdadero en el resultado y si es falso no
iterable: es una secuencia, como una lista, una tupla, o incluso otro objeto iterable
'''
def par(x):
    return x%2 == 0

numeros=[1,2,3,4,5]
pares = list(filter(lambda x: x%2 == 0, numeros))
print(pares)

def es_mayor_de_edad(persona):
    return persona["edad"]>= 18

personas = [
    {"nombre":"Juan", "edad": 25},
    {"nombre":"Maria", "edad": 16},
    {"nombre":"Pedro", "edad": 19},
    {"nombre":"Laura", "edad": 17}
]

mayores_de_edad = list(filter(es_mayor_de_edad,personas))
print(mayores_de_edad)

#reduce
#reduce(funcion,secuencia)
'''
funcion: es una funcion que tiene dos argumentos y realiza una operacion de reduccion entre ellos.
seccuencia es una secuencia como una lista, una tupla o incluso otro objeto iterativo.
'''

from functools import reduce
numeros = [1,2,3,4,5]
suma = reduce(lambda x,y:x+y, numeros)
print(suma)
sum(numeros)
print(suma)