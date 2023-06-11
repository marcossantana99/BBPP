#assert
#assert 1==2, "información que le podemos añadir"
#Lanza un assertion Error donde comprueba y lanza el error
#Es tel if que utilizamos en el raise


#Ejemplo calculamos la media de una lista

def calcular_media(lista):
    return sum(lista)/len(lista)

assert(calcular_media([5,5,5])==5)
#Aqui estamos comprobando que una determinada entrada está dando una determinada salida

#Utilizamos los asserts dentro de funciones

def suma (a,b):
    assert(type(a)==int)
    assert(type(b)==int)
    return a+b

suma(2,3)

class Mi_1:
    pass
class Mi_2:
    pass

m1 = Mi_1()
m2 = Mi_2()

#comprobamos si pertenecen a la clase

assert(isinstance(m1,Mi_1))

#Ejecutando en la terminal el script con un -O se salta los asserts

#Crear nuestra propia excepcion

class miExcepcion(Exception):
    def __init__(self,param1,param2):
        self.mensaje=param1
        self.informacion=param2

try:
    raise miExcepcion("Este es mi mensaje","esta es la info")
except miExcepcion as ex:
    p1,p2 = ex.args
    print(p1,p2)


#Otro ejemplo de esto ultimo
class ValorMinimo(Exception):

    def __init__(self,mensaje):
        self.mensaje = mensaje

    def __str__(self):
        return "Error de valor minimo: {} ".format(self.mensaje)
    

minimo = 20

try: 
    numero = int(input("Introduce un numero"))
    if numero<minimo:
        raise ValorMinimo("Se ha introducido un valor menor a {}".format(minimo)) #El mensaje que recoge la clase y sera devuelta al usuario
        #mensaje dinamico
except ValueError:
    print("introduce un valor numerico")
except ValorMinimo as e:
    print("Error: ",e) #Aqui es mostrado


print("Fin")