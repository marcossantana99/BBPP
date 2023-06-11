#Uso del try y el except

a = 5
b = 0

try: 
    a/b
    d = 2 + "hola"
except ZeroDivisionError as e:#Le damos un alias
    print("Hemos entrado en el except por error de dividir por 0")
    print("Error",e)
except TypeError:#otro tipo de error
    print("Error en el tipo de dato")
except Exception as a:#si no es ninguna de las anteriores entra en esta, es el más util si no controlas el error
    print("Error",a)
else:
    print("Entra en este bloque si no ocurrio ninguna excepción")
finally:
    print("Este bloque se ejuta siempre")
#La cosa es que si no estuviera el try no podriamos llegar al final
print("Fina")