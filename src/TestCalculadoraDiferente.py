import unittest
from src.CalculadoraDiferente import CalculadoraDiferente
from random import randint


class TestCalculadoraDiferente(unittest.TestCase):

    
    def setUp(self):
        self.calc = CalculadoraDiferente()


    #CASO 1 (INVERTER NUMEROS)
    def test_inverte_numero_1(self):
        self.assertEqual(self.calc.inverte_numero(123), 321)

    def test_inverte_numero_2(self):
        self.assertEqual(self.calc.inverte_numero(1111), 1111)

    def test_inverte_numero_3(self):
        self.assertEqual(self.calc.inverte_numero(120), 21)

    # CASO 2 (FATORIAL)
    def test_fatorial_1(self):
        self.assertEqual(self.calc.fatorial(5), 120)

    def test_fatorial_2(self):
        self.assertEqual(self.calc.fatorial(0), 1)

    def test_fatorial_3(self):
        self.assertEqual(self.calc.fatorial(1), 1)
    
    # CASO 3 (SOMA O DOBRO DO SEGUNDO NÚMERO)
    def test_soma_dobro_1(self):
        self.assertEqual(self.calc.soma_dobro(2, 3), 8)

    def test_soma_dobro_2(self):
        self.assertEqual(self.calc.soma_dobro(4, 0), 4)

    def test_soma_dobro_3(self):
        self.assertEqual(self.calc.soma_dobro(-1, -1), -3)

def start_test():
    if __name__ == 'main':
        unittest.main()

