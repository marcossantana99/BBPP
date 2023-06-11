#raise
#raise ZeroDivisionError("Info de la excepcion")#Lanzamos una excepcion 
#Rompe el codigo y no va a ejecutar todo lo que haya debajo del raise
#print("Hola")

edad = 17
try:
    if edad < 18:
        raise Exception("Menor de edad")
    else:
        print("OK")
except Exception:
    print("NO ES MAYOR DE EDAD")
print("Fin")