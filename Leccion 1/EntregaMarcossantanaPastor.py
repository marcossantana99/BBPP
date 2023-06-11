#Lección 1 
#Entrega realizada por Marcos Santana Pastor 
#Para la asignatura Buenas Practicas de programación en Python
class ErrorEdit(Exception):

    def __init__(self,mensaje):
        self.mensaje = mensaje

    def __str__(self):
        return "Error de valor minimo: {} ".format(self.mensaje)


def numero():
    max=10
    print("El numero debe ser entero y menor de 10.")
    print("Si esto no pasa entonces se activan las excepciones")
    n=(input("Dame un numero: "))
    try:
        n=int(n)
    except Exception:
        raise ErrorEdit("El valor introducido no es un número entero")
    
    if n>10:
        raise ErrorEdit("Se ha introducido un valor mayor a 10")
    
    print("Llegaste al final de la función")
    
numero()

#2 Parte 
#Entiendo que tengo que hacer una funcion que abra un txt.
#Para ello pedire la ruta donde esta y el nombre del archivo txt
def txt():
    #Supondre que el archivo de estar tiene que estar en la misma carpeta que el Script
    #pido el nombre del txt
    archivo=(input("Dame el nombre del txt: "))
    
    if archivo[-4:]!='.txt':
        raise ErrorEdit("No acaba en .txt el nombre que me has dado")
    else:
        try: 
            d = open(archivo,'r')
            try : 
                Filas=d.readlines()
                print(Filas[0])#Mostramos lo que ponga en el txt en la primera fila 
            except Exception as a:
                print("Error ",a)
            finally:
                d.close()
        except Exception as e:
            print("No esta el archivo que indicas con nombre: ",archivo)

 
txt()
