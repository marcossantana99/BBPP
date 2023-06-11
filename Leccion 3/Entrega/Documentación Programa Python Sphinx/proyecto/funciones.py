#Entrega Leaccion2 Marcos Santana
#Archivo funciones
from math import log

"""Este es el archivo .py que vamos a utilizar para documentarlo"""

def add(x,y):

    """Add Function.
    
    Esta funcion suma los dos argumentos que se le dan.
    
    Parameters:
        x (float): un numero real
        y (float): un numero real

    Returns:
        float:Returning value"""
    
    return x + y


def substract(x,y):

    """Substract Function.
    
    Esta funcion resta los dos argumentos que se le dan.
    
    Parameters:
        x (float): un numero real
        y (float): un numero real

    Returns:
        float:Returning value"""
    
    return x - y

def multiply(x,y):

    """Substract Function
    
    Esta funcion multiplica los dos argumentos que se le dan.
    
    Parameters:
        x (float): un numero real
        y (float): un numero real

    Returns:
        float:Returning value"""
    
    return x * y

def divide(x,y):

    """Divide Function
    
    Esta funcion divide los dos argumentos que se le dan.

    Lanza un error si se intenta dividir por 0.
    
    Parameters:
        x (float): un numero real
        y (float): un numero real

    Returns:
        float:Returning value"""
    
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

def logarithm(x):
    """Logarithm Function
    
    Esta funcion calcula el logaritmo neperiano del argumento que le dan.

    Lanza un error en caso de que el valor de entrada no sea mayor que 0.
    
    Parameters:
        x (float): un numero real
        y (float): un numero real

    Returns:
        float:Returning value"""
    
    if x <= 0:
        raise ValueError("Cannot calculate the log by number <=0")
    return log(x)

