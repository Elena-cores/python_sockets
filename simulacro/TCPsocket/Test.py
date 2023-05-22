import unittest
from Manager import *

class TestManejador(unittest.TestCase):
    def test_instancia(self):
        manager = Manager()
        self.assertIsInstance(manager, Manager)
    
    def test_palindromo1(self):
        palindromo = ['ana']
        manejador = Manager()
        respuesta = manejador.devolver_respuesta(palindromo)
        self.assertEqual([True], respuesta)
    
    def test_palindromo2(self):
        palindromo = ['hola']
        manager = Manager()
        respuesta = manager.devolver_respuesta(palindromo)
        self.assertEqual([False], respuesta)
    
    def test_palindromos1(self):
        palindromos = ['ana', 'sometemos']
        manejador = Manager()
        respuesta = manejador.devolver_respuesta(palindromos)
        self.assertEqual([True, True], respuesta)
    
    def test_palindromos2(self):
        palindromos = ['ana', 'holaaa']
        manager = Manager()
        respuesta = manager.devolver_respuesta(palindromos)
        self.assertEqual([True, False], respuesta)

if __name__ == "__main__":
    unittest.main()