import unittest
from unittest.mock import patch
from src.exceptions import (
    NumeroDebeSerPositivo,
)

class TestCalculoNumeros(unittest.TestCase):

    @patch( 'builtins.input', return_value='10')
    def test_ingreso_positivo(self, patch_input):
        with self.assertRaises(NumeroDebeSerPositivo):
            ingrese_numero()


    @patch( 'builtins.input', return_value='-10')
    def test_ingreso_negativo(self, patch_input):
        with self.assertRaises(Exception):
            ingrese_numero()

    @patch( 'builtins.input', return_value='AAA')
    def test_ingreso_letras(self, patch_input):
        with self.assertRaises(Exception):
            ingrese_numero()

if __name__ == '__main__':
    unittest.main() 
    