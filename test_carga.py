"""Unit tests para la clase caja
"""
import unittest

from components.carga import Carga

class TestCarga(unittest.TestCase):
    """Unit tests para la clase carga
    """

    def test_crear_carga(self):
        """
        Crear una carga asigna el nombre y no tiene potencia
        """
        carga0 = Carga("Zero")
        self.assertEqual(carga0.get_nombre(), "Zero")
        self.assertEqual(carga0.get_potencia(), None)


    def test_crear_carga_con_potencia(self):
        """
        Crear una carga con potencia, asigna potencia
        """
        carga0 = Carga("Zero", 100)
        self.assertEqual(carga0.get_potencia(), 100)


    def test_asignar_potencia_despues(self):
        """
        Crear una carga sin potencia, asignar potencia despues
        """
        carga0 = Carga("Zero")
        carga0.set_potencia(100)
        self.assertEqual(carga0.get_potencia(), 100)


    def test_cambiar_nombre(self):
        """
        Crear una carga con un nombre, y cambiarlo
        """
        carga0 = Carga("Prince")
        carga0.set_nombre("The carga previously known as Prince")
        self.assertEqual(carga0.get_nombre(), "The carga previously known as Prince")


    def test_completamente_definido_funciona_si_esta_definido(self):
        """
        Crear una carga con un potencia y ver si esta definida
        """
        carga0 = Carga("Zero", 100)
        self.assertEqual(carga0.completamente_definido(), True)


    def test_completamente_definido_funciona_si_no_esta_definido(self):
        """
        Crear una carga con un potencia y ver si esta definida
        """
        carga0 = Carga("Zero")
        self.assertEqual(carga0.completamente_definido(), False)


    def test_completamente_definido_funciona_si_se_define_despues(self):
        """
        Crear una carga con un potencia y ver si esta definida
        """
        carga0 = Carga("Zero")
        carga0.set_potencia(2)
        self.assertEqual(carga0.completamente_definido(), True)


if __name__ == '__main__':
    unittest.main()
