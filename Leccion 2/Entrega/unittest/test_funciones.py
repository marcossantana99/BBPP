#Entrega Leccion 2 Marcos Santana Pastor 
#Archivo test unittest

import unittest
import funciones

class TestFunciones(unittest.TestCase):

    def test_suma(self):

        self.assertEqual(funciones.add(10,20),30)#test bueno
        self.assertEqual(funciones.add(10,10),50)#test malo

    def test_subtract(self):
        self.assertEqual(funciones.substract(10,5),5)#test bueno
        self.assertEqual(funciones.substract(90,5),5)#test malo

    def test_multiply(self):
        self.assertEqual(funciones.multiply(10,5),50)#test bueno
        self.assertEqual(funciones.multiply(90,5),5)#test malo

    def test_divide(self):
        self.assertEqual(funciones.divide(10,5),2)#test bueno
        self.assertEqual(funciones.divide(20,5),2)#test malo
        #Con lo siguiente se comprueba que nuestro programa lanza una excepción
        with self.assertRaises(ValueError):
            funciones.divide(10,0)

    def test_logarithm(self):
        self.assertEqual(funciones.logarithm(1),0)#test bueno
        self.assertEqual(funciones.logarithm(2),1)#test malo
        #Con lo siguiente se comprueba que nuestro programa lanza una excepción
        with self.assertRaises(ValueError):
            funciones.logarithm(0)
