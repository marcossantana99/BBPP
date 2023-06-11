#Entrega Leccion 2 Marcos Santana Pastor 
#Archivo test unittest

import pytest
import funciones

#SUMA
def test_suma():
    assert funciones.add(10,20)==30 #test bueno
    assert funciones.add(10,10)==50 #test malo

#RESTA
def test_resta():
    assert funciones.substract(10,5)==5 #test bueno
    assert funciones.substract(90,5)==5 #test malo

#MULTIPLICACION
def test_multiplicar():
    assert funciones.multiply(10,5)==50 #test bueno
    assert funciones.multiply(90,5)==5 #test malo

#DIVISIÓN
def test_dividir():
    assert funciones.divide(10,5)==2 #test bueno
    assert funciones.divide(20,5)==2 #test malo
    #Con lo siguiente se comprueba que nuestro programa lanza una excepción
    with pytest.raises(Exception):
        funciones.divide(10,0)#Este test debería de pasarlo
        funciones.divide(10,2)#No genera una exception. No debería pasar el test

#LOGARITMO
def test_logaritmo():
    assert funciones.logarithm(1)==0 #test bueno
    assert funciones.logarithm(2)==1 #test malo
    #Con lo siguiente se comprueba que nuestro programa lanza una excepción
    with pytest.raises(Exception):
        funciones.logarithm(1)#Este test debería de pasarlo
        funciones.logarithm(1)#No genera una exception. No debería pasar el test
