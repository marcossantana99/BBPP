#Entrega Leaccion2 Marcos Santana
#Archivo funciones
from math import log

def add(x,y):
    """Add Function"""
    return x + y


def substract(x,y):
    """Substract Function"""
    return x - y

def multiply(x,y):
    """Substract Function"""
    return x * y

def divide(x,y):
    """Divide Function"""
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

def logarithm(x):
    """Logarithm Function"""
    if x <= 0:
        raise ValueError("Cannot calculate the log by number <=0")
    return log(x)

