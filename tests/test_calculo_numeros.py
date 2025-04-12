import unittest
from unittest.mock import patch
from src.exceptions import ( ingrese_numero,
    NumeroDebeSerPositivo,
)

class TestCalculoNumeros(unittest.TestCase):

    @patch( 'builtins.input', return_value='10')
    def test_ingreso_positivo(self, mock_input):
        resultado=ingrese_numero()
        self.assertEqual(resultado, 10)


    @patch( 'builtins.input', return_value='-10')
    def test_ingreso_negativo(self, mock_input):
        with self.assertRaises(NumeroDebeSerPositivo):
            ingrese_numero()

    @patch( 'builtins.input', return_value='AAA')
    def test_ingreso_letras(self, mock_input):
        with self.assertRaises(ValueError):
            ingrese_numero()

if __name__ == '__main__':
    unittest.main() 
    