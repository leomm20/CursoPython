import unittest
from src.cp09_extras.cp67_unittest_modulo import suma, resta


class PruebaSumaResta(unittest.TestCase):
    def test_suma(self): # tiene que ir sí o sí el "test_"
        n1, n2, n3, n4 = 1, 2, 3, 4
        resultado = suma(n1, n2, n3, n4)
        self.assertEqual(resultado, 10) # lo que devuelve la función vs lo que estoy esperando como resultado
        self.assertNotEqual(resultado, 10.01) # lo que devuelve la función vs lo que NO estoy esperando como resultado
        self.assertNotEqual(resultado, 9.99) # lo que devuelve la función vs lo que NO estoy esperando como resultado

    def test_resta(self): # tiene que ir sí o sí el "test_"
        n1, n2, n3, n4 = 10, 1, 2, 3
        resultado = resta(n1, n2, n3, n4)
        self.assertEqual(resultado, 4)  # lo que devuelve la función vs lo que estoy esperando como resultado
        self.assertNotEqual(resultado, 4.01)  # lo que devuelve la función vs lo que NO estoy esperando como resultado
        self.assertNotEqual(resultado, 3.99)  # lo que devuelve la función vs lo que NO estoy esperando como resultado

        # LÍNEA AGREGADA PARA DEMOSTRAR CÓMO SE MOSTRARÍA UN CASO FALLIDO
        self.assertEqual(resultado, 3.0)  # lo que devuelve la función vs lo que estoy esperando como resultado


# REQUIERE DEL INICIADOR MAIN
if __name__ == "__main__":
    unittest.main()


