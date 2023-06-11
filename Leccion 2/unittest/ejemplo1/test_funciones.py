import unittest
import funciones

"""

assertEqual(a,b):Verifica la igualdad de ambos valores
asserTrue(x):Verifica que el valor es true
assertFalse(x):Verifica que el valor es false
asserIs(a,b):Verfica que ambas variable son la misma
assertIsNone(x):Verifica que el valor es None
assertIn(a,b): Verifica que a pertenece al iterable  b
assertRaises(x):Verifica que se lanza una excepcion

"""

#Siempre es necesario la clase

class TestFunciones(unittest.TestCase):

    #La idea de dar entradas dinamicas a los test 
    #setUp se ejecutara antes del test

    def setUp(self):
        print('setUp')
        #pedir mas self.value1, self.value2... ha dicho pero no ha escrito

    #tearDown se ejecutara despues

    def tearDown(self):
        print('tearDown\n')

    def test_suma(self):
        print("Comenzando suma: ")
        self.assertEqual(funciones.add(10,20),30)
        self.assertEqual(funciones.add(10,10),20)
        self.assertEqual(funciones.add(10,2),12)

    def test_subtract(self):
        self.assertEqual(funciones.subtract(10,5),5)
        #Asi copia y pega podrias comprobar todos

    def test_divide(self):
        self.assertEqual(funciones.divide(10,5),2)
        #Con lo siguiente se comprueba que nuestro programa lanza una excepción
        with self.assertRaises(ValueError):
            funciones.divide(10,0)

    