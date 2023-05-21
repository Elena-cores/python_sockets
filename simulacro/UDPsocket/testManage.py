import unittest
from Manage import *

class TestManejador(unittest.TestCase):
    def test_instancia(self):
        manejador = Manage()
        self.assertIsInstance(manejador, Manage)

if __name__ == "__main__":
    unittest.main()