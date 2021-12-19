from .empty_normative import Normative
from .netherlands import NetherlandsNormative
from .spain import SpainNormative
# from . import *

__all__ = ["Normative", "NetherlandsNormative", "SpainNormative", "names"]

names = [cls for cls in __all__ if cls != "names"]
