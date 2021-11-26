# Here go the imports
from components.load import Load


# Here goes the class
class Box():
    # Static variables
    counter = 0  # ID counter

    def __init__(self):
        self.loads = []
        self.children = []
        self.parent = None
        self.id = Box.counter
        self.gui = None
        Box.counter += 1

    def _set_parent(self, parent: "Box"):
        self.parent = parent

    def add_child(self, child: "Box"):
        """
        Adds child and sets itself as parent for the child
        """
        if child is self:
            raise ValueError("A box cannot be it's own parent")
        self.children.append(child)
        if child.get_parent() is not None:
            child.get_parent().delete_child(child)
        child._set_parent(self)
        self._detect_and_prevent_loop(self)

    def delete_child(self, child: "Box"):
        try:
            self.children.remove(child)
            child._set_parent(None)
        except Exception as e:
            print(f"{child.get_id()} is not a child of this box: {e}")

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

    def _detect_and_prevent_loop(self, box_buscada: "Box"):
        for child in self.get_children():
            if child is box_buscada:
                child.parent.delete_child(child)
                return
            child._detect_and_prevent_loop(box_buscada)

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
        return True

    def __del__(self):
        for child in self.get_children():
            self.delete_child(child)
            del child
