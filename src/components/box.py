# Here go the imports
import logging
import sys
from typing import Union
from components.load import Load

logger = logging.getLogger(__name__)


# Here goes the class
class Box:
    # Static variables
    counter = 0  # ID counter

    def __init__(self):
        self.loads = []
        self.children = []
        self.parent = None
        self.id = Box.counter
        self.gui = None
        Box.counter += 1
        self.waste = list(range(1, 10000000))  # TODO For test only, there is memory leak

    def _set_parent(self, parent: Union["Box", None]):
        self.parent = parent

    def add_child(self, candidate_child: "Box"):
        """
        Adds candidate_child as child and sets itself as parent for the child
        """
        if candidate_child is self:
            raise ValueError("A box cannot be it's own parent")
        if candidate_child._is_ascendant_of(self):
            raise ValueError("This child is an ascendant of this box. Adding this child would create a loop")
        self.children.append(candidate_child)
        if candidate_child.get_parent() is not None:
            candidate_child.get_parent().delete_child(candidate_child)
        candidate_child._set_parent(self)

    def delete_child(self, child: "Box"):
        """
        Deletes child from list of children
        """
        try:
            self.children.remove(child)
            child._set_parent(None)
            logger.debug(f"Child {child.get_id()} removed from parent {self.get_id()}")
        except Exception as e:
            logger.error(f"{child.get_id()} is not a child of this box: {e}")

    def _is_ascendant_of(self, wanted_box: "Box"):
        for child in self.get_children():
            if child is wanted_box:
                return True
            if child._is_ascendant_of(wanted_box):
                return True
        return False

    def add_load(self, load: Load):
        """Adds load to the list of loads connected directly to this box
        """
        self.loads.append(load)

    def delete_load(self, load: Load):
        """Deletes load from the list of loads connected directly to this box
        """
        try:
            self.loads.remove(load)
        except ValueError:
            pass

    def get_id(self):
        """Returns box id
        """
        return self.id

    def get_parent(self) -> "Box":
        """Returns reference to parent box
        """
        return self.parent

    def get_children(self) -> list["Box"]:
        """Returns a list of references to the children boxes
        """
        return self.children

    def get_loads(self) -> list[Load]:
        """Returns a list of references to the loads connected directly to this box
        """
        return self.loads

    def defined(self) -> bool:
        """Returns true if all its loads and children boxes are defined
        """
        for load in self.get_loads():
            if not load.defined():
                return False
        for child in self.get_children():
            if not child.defined():
                return False
        if len(self.get_loads()) + len(self.get_children()) == 0:  # TODO: Is a useless empty box undefined?
            return False
        return True

    @property
    def power(self) -> float:
        power = 0.0
        for load in self.get_loads():
            power += load.power
        for child in self.get_children():
            power += child.power
        return power

    def __del__(self):
        print(sys.getrefcount(self))
        print(self.get_id())
        del self.gui
        for child in self.get_children():
            print(child.get_id())
            self.delete_child(child)
            del child
        print(sys.getrefcount(self))
        del self
