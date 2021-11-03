# This file uses NumPy style docstrings:
# https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt
"""Este modulo implementa una box de registro.
"""
# Here go the imports


class Load():
    counter = 0

    def __init__(self, name, power=None):
        self.name = name
        self.power = power
        if power is not None and power <= 0:
            self.power = None

    def get_name(self):
        """Retorna el name de la load
        """
        return self.name

    def get_power(self):
        """Retorna la power de la load
        """
        return self.power

    def set_name(self, name):
        """Asigna un nuevo name a la load
        """
        self.name = name

    def set_power(self, power):
        """Asigna una (nueva) power a la load
        """
        if power > 0:
            self.power = power

    def defined(self):
        """Retorna True si la load tiene power asignada
        """
        return bool(self.power is not None)
