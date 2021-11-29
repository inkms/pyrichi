# Here go the imports
from components.load import Load


# Here goes the class
class Box():
    # Static variables
    counter = 0  # ID counter

    def __init__(self, box_parent=None):
        self.loads = []
        self.children = []
        self.parent = None
        self.id = Box.counter
        Box.counter += 1
        if box_parent is not None:
            self.set_parent(box_parent)

    def set_parent(self, parent: "Box"):
        """
        Configure parent as preceding box, and adds itself as child
        """
        if parent is self:
            raise ValueError("A box cannot be it's own parent")
        if self.parent is not None:
            self.parent._delete_child(self)
        self._detect_and_prevent_loop(parent)
        if parent is not None:
            parent._add_child(self)
        self.parent = parent

    def _add_child(self, child: "Box"):
        self.children.append(child)

    def _delete_child(self, child: "Box"):
        try:
            self.children.remove(child)
        except Exception as e:
            print(f"{child.get_id()} is not a child of this box: {e}")

    def add_load(self, load: Load):
        """Adds load to the list of loads connected directly to this box
        """
        self.loads.append(load)

    def delete_load(self, load: Load):
        """Deletes load from the list of loads connected directly to this box
        """
        # Try-except
        self.loads.remove(load)

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
