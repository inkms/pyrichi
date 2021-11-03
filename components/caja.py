# This file uses NumPy style docstrings:
# https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt
"""Este modulo implementa una caja de registro.
"""
# Here go the imports

# Here goes the class
class Caja():
    """Este modulo implementa una caja de registro.
    """
    # Variables estaticas de la clase
    contador = 0  # Contador para que todas las cajas tengan ids diferentes
    def __init__(self, caja_matriz = None):
        self.cargas = []
        self.hijas = []
        self.matriz = None
        self.identidad = Caja.contador
        Caja.contador += 1
        if caja_matriz is not None:
            self.set_matriz(caja_matriz)


    def set_matriz(self, matriz):
        """
        Configura matriz como la caja aguas arriba, y se auto añade
        como hija de matriz
        """
        if matriz is self:
            raise ValueError("La caja no puede tenerse a si misma como matriz")
        if self.matriz is not None:
            self.matriz._delete_hija(self)
        self._detect_and_prevent_loop(matriz)
        if matriz is not None:
            matriz._add_hija(self)
        self.matriz = matriz


    def _add_hija(self, hija):
        """Método privado que añade hija a las cajas hijas de esta caja
        """
        self.hijas.append(hija)


    def _delete_hija(self, hija):
        """Método privado que borra hija a las cajas hijas de esta caja
        """
        self.hijas.remove(hija)


    def add_carga(self, carga):
        """Método que añade carga a las cargas de esta caja
        """
        self.cargas.append(carga)


    def delete_carga(self, carga):
        """Método que borra carga a las cargas de esta caja
        """
        self.cargas.remove(carga)


    def _detect_and_prevent_loop(self, caja_buscada):
        """Comprueba que no hay bucles, si los hay, los rompe
        """
        for hija in self.hijas:
            if hija is caja_buscada:
                hija.set_matriz(None)
                return
            hija._detect_and_prevent_loop(caja_buscada)


    def get_identidad(self):
        """Retorna la identificacion de la caja
        """
        return self.identidad


    def get_matriz(self):
        """Retorna una referencia a la caja matriz
        """
        return self.matriz


    def get_hijas(self):
        """Retorna un vector de referencias a las cajas hijas
        """
        return self.hijas


    def get_cargas(self):
        """Retorna un vector de referencias a las cargas
        """
        return self.cargas


    def completamente_definida(self):
        """Retorna True si todas sus cargas y cajas hijas estan definidas
        """
        for carga in self.cargas:
            if not carga.completamente_definida():
                return False
        for hija in self.hijas:
            if not hija.completamente_definida():
                return False
        return True
