"""Unit tests para la clase caja
"""
import unittest

from components.caja import Caja
from components.carga import Carga

class TestCaja(unittest.TestCase):
    """Unit tests para la clase caja
    """

    def test_crear_caja_default_constructor(self):
        """
        Crear una caja sin mas sin darle parametros extra
        al constructor
        """
        caja1 = Caja()
        self.assertNotEqual(caja1.get_identidad(), None)


    def test_dos_cajas_tienen_ids_distintos(self):
        """
        Crear 2 cajas y comprobar que tienen ids distintos
        """
        caja1 = Caja()
        caja2 = Caja()
        self.assertNotEqual(caja1.get_identidad(), caja2.get_identidad())


    def test_enlazar_cajas(self):
        """
        Crear 2 cajas y enlazarlas como madre e hija
        """
        caja1 = Caja()
        caja2 = Caja()
        caja1.set_matriz(caja2)
        self.assertEqual(caja1.get_matriz(), caja2)
        self.assertEqual(caja2.get_hijas()[0], caja1)


    def test_enlazar_multiples_cajas(self):
        """
        Crear 3 cajas y enlazar 2 de ellas a una caja madre
        """
        cajam1 = Caja()
        cajah1 = Caja()
        cajah2 = Caja()
        cajah1.set_matriz(cajam1)
        cajah2.set_matriz(cajam1)
        self.assertEqual(cajam1.get_hijas()[0], cajah1)
        self.assertEqual(cajam1.get_hijas()[1], cajah2)


    def test_no_hay_bucles_matriz_hija(self):
        """
        Crear 2 cajas y enlazarlas como madre e hija. Luego cambiar
        """
        caja1 = Caja()
        caja2 = Caja()
        caja1.set_matriz(caja2)
        caja2.set_matriz(caja1)
        self.assertEqual(caja1.get_hijas()[0], caja2)
        self.assertEqual(caja2.get_matriz(), caja1)
        self.assertEqual(caja2.get_hijas(), [])
        self.assertNotEqual(caja1.get_matriz(), caja2)


    def test_no_hay_bucles_largos(self):
        """
        Crear 3 cajas e interntar crear un bucle de 3 cajas
        """
        caja1 = Caja()
        caja2 = Caja()
        caja3 = Caja()
        caja3.set_matriz(caja2)
        caja2.set_matriz(caja1)
        caja1.set_matriz(caja3)
        self.assertEqual(caja3.get_matriz(), None)
        self.assertEqual(caja2.get_hijas(), [])
        self.assertEqual(caja1.get_matriz(), caja3)


    def test_no_hay_bucle_caja_consigo_misma(self):
        """
        Asginar a una caja ella misma como matriz da una excepción y no hace nada
        """
        caja1 = Caja()
        with self.assertRaises( ValueError ):
            caja1.set_matriz(caja1)
        self.assertEqual(caja1.get_hijas(), [])
        self.assertEqual(caja1.get_matriz(), None)


    def test_hacer_una_hija_matriz_de_otra(self):
        """
        Crear 3 cajas, y asignar 2 hijas a una matriz. Despues cambiar una hija a ser matriz
        de la otra hija. Comprobar que la nieta ya no es hija
        """
        caja1 = Caja()
        caja2 = Caja()
        caja3 = Caja()
        caja3.set_matriz(caja1)
        caja2.set_matriz(caja1)
        # 1 tiene hijas [2,3]
        caja3.set_matriz(caja2)
        self.assertEqual(caja3.get_matriz(), caja2)
        self.assertEqual(len(caja1.get_hijas()), 1)
        self.assertEqual(caja1.get_hijas(), [caja2])
        self.assertEqual(caja2.get_hijas(), [caja3])


    def test_anadir_carga(self):
        """
        Crear una caja, añadir carga y comprobar que funciona
        """
        caja1 = Caja()
        carga1 = Carga("Uno")
        caja1.add_carga(carga1)
        self.assertEqual(caja1.get_cargas(), [carga1])


    def test_anadir_multiples_cargas(self):
        """
        Crear una caja, añadir 2 cargas y comprobar que funciona
        """
        caja1 = Caja()
        carga1 = Carga("Uno")
        carga2 = Carga("Dos")
        caja1.add_carga(carga1)
        caja1.add_carga(carga2)
        self.assertEqual(caja1.get_cargas(), [carga1,carga2])


    def test_borrar_carga(self):
        """
        Crear una caja, añadir carga, borrarla y comprobar que funciona
        """
        caja1 = Caja()
        carga1 = Carga("Uno")
        caja1.add_carga(carga1)
        caja1.delete_carga(carga1)
        self.assertEqual(caja1.get_cargas(), [])


    def test_borrar_solo_carga_elegida(self):
        """
        Crear una caja, añadir 2 cargas, borrar una y comprobar que funciona
        """
        caja1 = Caja()
        carga1 = Carga("Uno")
        carga2 = Carga("Dos")
        caja1.add_carga(carga1)
        caja1.add_carga(carga2)
        caja1.delete_carga(carga2)
        self.assertEqual(caja1.get_cargas(), [carga1])


    def test_caja_con_cargas_definidas(self):
        """
        Crear una caja, añadir 2 cargas definidas, comprobar que la caja esta definida
        """
        caja1 = Caja()
        carga1 = Carga("Uno",100)
        carga2 = Carga("Dos",200)
        caja1.add_carga(carga1)
        caja1.add_carga(carga2)
        self.assertEqual(caja1.completamente_definida(), True)


    def test_caja_con_cargas_indefinidas(self):
        """
        Crear una caja, añadir 2 cargas, una indefinida, comprobar que la caja esta indefinida
        """
        caja1 = Caja()
        carga1 = Carga("Uno",100)
        carga2 = Carga("Dos")
        caja1.add_carga(carga1)
        caja1.add_carga(carga2)
        self.assertEqual(caja1.completamente_definida(), False)


    def test_caja_con_cajas_definidas(self):
        """
        Crear una caja, añadir 2 cajas definidas, comprobar que la caja esta definida
        """
        caja0 = Caja()
        caja1 = Caja()
        caja2 = Caja()
        carga1 = Carga("Uno",100)
        carga2 = Carga("Dos",200)
        caja1.add_carga(carga1)
        caja2.add_carga(carga2)
        caja1.set_matriz(caja0)
        caja2.set_matriz(caja0)
        self.assertEqual(caja0.completamente_definida(), True)


    def test_caja_con_cajas_indefinidas(self):
        """
        Crear una caja, añadir 2 cajas, una indefinida, comprobar que la caja esta indefinida
        """
        caja0 = Caja()
        caja1 = Caja()
        caja2 = Caja()
        carga1 = Carga("Uno",100)
        carga2 = Carga("Dos")
        caja1.add_carga(carga1)
        caja2.add_carga(carga2)
        caja1.set_matriz(caja0)
        caja2.set_matriz(caja0)
        self.assertEqual(caja0.completamente_definida(), False)


if __name__ == '__main__':
    unittest.main()
