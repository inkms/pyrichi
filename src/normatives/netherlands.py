from components.box import Box
from normatives.empty_normative import Normative


class NetherlandsNormative(Normative):
    @classmethod
    def name(cls):
        return cls.__name__

    @classmethod
    def calculate_box(cls, box: Box):
        """
        This function calculates takes a box and returns normative values for it, such as cable thickness
        :param box: Box object for which the values are calculated
        :return: Dictionary including main parameters calculated through the normative
        """
        return {"a": 0}
