import pytest

def capital(x):
    return x.capitalize()#Pone la primera letra en mayuscula

def test_capital1():
    assert capital("hola") =="Hola"

def test_capital2():
    assert capital("hola") == "hoola"