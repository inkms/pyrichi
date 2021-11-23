# Here go the imports


class Load():
    counter = 0

    def __init__(self, name, power=None):
        self.name = name
        self.power = power

    @property
    def name(self):
        return self.__name

    @property
    def power(self):
        return self.__power

    @name.setter
    def name(self, name: str):
        """Sets self.name to name
        """
        self.__name = name

    @power.setter
    def power(self, power: float):
        """Sets self.power to power if it is positive
        """
        if power is not None and power > 0:
            self.__power = power
        else:
            self.__power = None

    def defined(self):
        """Returns True if load has power defined
        """
        return bool(self.power is not None)
