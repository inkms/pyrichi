# This file uses NumPy style docstrings:
# https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt
"""Este modulo implementa una caja de registro.
"""
# Here go the imports

# Here goes the class
class Carga():
    """Este modulo implementa una carga
    """
    contador = 0
    def __init__(self, nombre, potencia = None):
        self.nombre = nombre
        self.potencia = potencia


    def get_nombre(self):
        """Retorna el nombre de la carga
        """
        return self.nombre


    def get_potencia(self):
        """Retorna la potencia de la carga
        """
        return self.potencia


    def set_nombre(self, nombre):
        """Asigna un nuevo nombre a la carga
        """
        self.nombre = nombre


    def set_potencia(self, potencia):
        """Asigna una (nueva) potencia a la carga
        """
        self.potencia = potencia


    def completamente_definido(self):
        """Retorna True si la carga tiene potencia asignada
        """
        return bool(self.potencia is not None)
