# Here go the imports


class Load():
    counter = 0

    def __init__(self, name, power=None):
        self.name = name
        self.power = power
        if power is not None and power <= 0:
            self.power = None

    def get_name(self):
        return self.name

    def get_power(self):
        return self.power

    def set_name(self, name):
        self.name = name

    def set_power(self, power):
        if power > 0:
            self.power = power

    def defined(self):
        return bool(self.power is not None)
