from components.box import Box


class Normative:
    @classmethod
    def name(cls):
        return cls.__name__

    def calculate_box(self, box: Box):
        raise NotImplementedError("You need to select a normative implementation first!")
