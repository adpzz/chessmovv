import unittest
from chessmovv import *

class QueenTest(unittest.TestCase):

    def test_movimiento_valido(self) -> bool:
        """
        Comprueba si el movimiento de la reina es válido.
        
        Retorna:
        bool: True si pasa el test, False si no pasa el test
        """

        reina = Queen(4, 4)

        # Pruebas para movimientos válidos
        self.assertTrue(reina.validar_movimiento(4, 8))   # 
        self.assertTrue(reina.validar_movimiento(1, 4))   # 
        self.assertTrue(reina.validar_movimiento(7, 7))   # 
        self.assertTrue(reina.validar_movimiento(2, 2))   # 

    def test_movimiento_invalido(self) -> bool:
        """
        Comprueba si el movimiento de la reina es inválido.
        
        Retorna:
        bool: True si pasa el test, False si no pasa el test
        """

        reina = Queen(4, 4)

        self.assertFalse(reina.validar_movimiento(5, 8))  # 
        self.assertFalse(reina.validar_movimiento(0, 4))  # 

    def test_movimiento_invalido_fuera_de_tablero(self) -> bool:
        """
        Comprueba si el movimiento de la reina se realiza fuera del tablero.
        
        Retorna:
        bool: True si pasa el test, False si no pasa el test
        """      
         
        reina = Queen(8, 8)
        
        self.assertFalse(reina.validar_movimiento(9, 9))


class KingTest(unittest.TestCase):

    def test_movimiento_valido(self) -> bool:
        """
        Comprueba si el movimiento del rey es válido.
        
        Retorna:
        bool: True si pasa el test, False si no pasa el test
        """

        rey = King(4, 4)

        self.assertTrue(rey.validar_movimiento(4, 5))   # 
        self.assertTrue(rey.validar_movimiento(3, 4))   # 

        rey = King(8, 8)

        self.assertTrue(rey.validar_movimiento(7, 8))   # 

    def test_movimiento_invalido(self) -> bool:
        """
        Comprueba si el movimiento del rey es inválido.
        
        Retorna:
        bool: True si pasa el test, False si no pasa el test
        """

        rey = King(4, 4)

        self.assertFalse(rey.validar_movimiento(2, 2))  # 
        self.assertFalse(rey.validar_movimiento(7, 4))  # 
    
    def test_movimiento_invalido_fuera_de_tablero(self) -> bool:
        """
        Comprueba si el movimiento del rey se realiza fuera del tablero.
        
        Retorna:
        bool: True si pasa el test, False si no pasa el test
        """
        
        rey = King(1, 1)
        
        self.assertFalse(rey.validar_movimiento(0, 0))

        rey = King(8, 8)

        self.assertFalse(rey.validar_movimiento(9, 8))
        
class TowerTest(unittest.TestCase):

    def test_movimiento_valido(self) -> bool:
        """
        Comprueba si el movimiento de la torre es válido.
        
        Retorna:
        bool: True si pasa el test, False si no pasa el test
        """
        
        torre = Tower(1, 1)

        self.assertTrue(torre.validar_movimiento(1, 8))   # 
        self.assertTrue(torre.validar_movimiento(8, 1))   # 

        torre = Tower(8, 8)

        self.assertTrue(torre.validar_movimiento(1, 8))   # 
        self.assertTrue(torre.validar_movimiento(8, 1))   # 

    def test_movimiento_invalido(self) -> bool:
        """
        Comprueba si el movimiento de la torre es inválido.
        
        Retorna:
        bool: True si pasa el test, False si no pasa el test
        """

        torre = Tower(1, 1)

        self.assertFalse(torre.validar_movimiento(2, 2))  # 
        self.assertFalse(torre.validar_movimiento(4, 2))  # 
        self.assertFalse(torre.validar_movimiento(3, 2))  # 

    def test_movimiento_invalido_fuera_de_tablero(self) -> bool:
        """
        Comprueba si el movimiento de la torre realiza fuera del tablero.
        
        Retorna:
        bool: True si pasa el test, False si no pasa el test
        """
        
        torre = Tower(1, 1)
        self.assertFalse(torre.validar_movimiento(9, 1))

        torre = Tower(8, 8)
        self.assertFalse(torre.validar_movimiento(8, 0))
        self.assertFalse(torre.validar_movimiento(1, 9))

if __name__ == '__main__':
    unittest.main()