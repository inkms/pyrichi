from components.box import Box
from normatives.empty_normative import Normative
import logging
from components.load import Load  # For testing only

logger = logging.getLogger(__name__)

__all__ = ["SpainNormative"]


class SpainNormative(Normative):
    @classmethod
    def power_to_thickness(cls, power: float):  # TODO calculate properly
        """
        This function calculates the thickness of the phase and neutral cables of the box
        :param power: Total maximum power draw of loads connected to the box
        :return: thickness: Minimum diameter for copper cables in millimeters
        """
        return power / 100

    @classmethod
    def calculate_box(cls, box: Box):
        """
        This function calculates takes a box and returns normative values for it, such as cable thickness
        :param box: Box object for which the values are calculated
        :return: Dictionary including main parameters calculated through the normative
        """
        if box.defined():
            logger.debug("The box is fully defined")
            return {"cable_thickness": cls.power_to_thickness(box.power)}
        else:
            # For testing only!!
            box.add_load(Load("a", 345))
            logger.debug("The box is not fully defined, we add a dummy load")
            if box.defined():
                logger.debug("Now it is actually defined")
                return {"cable_thickness": cls.power_to_thickness(box.power)}
            else:
                logger.error("The box is not fully defined")
