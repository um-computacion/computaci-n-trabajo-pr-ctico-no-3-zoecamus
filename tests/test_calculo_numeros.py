import unittest
from unittest.mock import patch

class TestCalculoNumeros(unittest.TestCase):

    @patch( 'builtins.input', return_value='10')
    def test_ingreso_positivo(self, patch_input):
        numero = ingrese_numero()
        self.assertEqual(numero, 10)


    @patch( 'builtins.input', return_value='-10')
    def test_ingreso_negativo(self, patch_input):
        numero = ingrese_numero()
        self.assertEqual(numero, -10)

    @patch( 'builtins.input', return_value='AAA')
    def test_ingreso_letras(self, patch_input):
        with self.assertRaises(ValueError):
            ingrese_numero()

if __name__ == '__main__':
    unittest.main() 
    454555