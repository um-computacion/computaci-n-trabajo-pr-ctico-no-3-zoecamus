import unittest
from unittest.mock import patch

class TestCalculoNumeros(unittest.TestCase):

    @patch( 'builtins.input', return_value='10')
    def test_ingreso_positivo(self, patch_input):
        numero = ingrese_numero()
        self.assertEqual(numero, 10)

if __name__ == '__main__':
    unittest.main() 