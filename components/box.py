# Here go the imports

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

    def set_parent(self, parent):
        """
        Configura parent como la box aguas arriba, y se auto añade
        como child de parent
        """
        if parent is self:
            raise ValueError("La box no puede tenerse a si misma como parent")
        if self.parent is not None:
            self.parent._delete_child(self)
        self._detect_and_prevent_loop(parent)
        if parent is not None:
            parent._add_child(self)
        self.parent = parent

    def _add_child(self, child):
        """Método privado que añade child a las boxs children de esta box
        """
        self.children.append(child)

    def _delete_child(self, child):
        """Método privado que borra child a las boxs children de esta box
        """
        self.children.remove(child)

    def add_load(self, load):
        """Método que añade load a las loads de esta box
        """
        self.loads.append(load)

    def delete_load(self, load):
        """Método que borra load a las loads de esta box
        """
        self.loads.remove(load)

    def _detect_and_prevent_loop(self, box_buscada):
        """Comprueba que no hay bucles, si los hay, los rompe
        """
        for child in self.children:
            if child is box_buscada:
                child.set_parent(None)
                return
            child._detect_and_prevent_loop(box_buscada)

    def get_id(self):
        """Retorna la identificacion de la box
        """
        return self.id

    def get_parent(self):
        """Retorna una referencia a la box parent
        """
        return self.parent

    def get_children(self):
        """Retorna un vector de referencias a las boxs children
        """
        return self.children

    def get_loads(self):
        """Retorna un vector de referencias a las loads
        """
        return self.loads

    def defined(self):
        """Retorna True si todas sus loads y boxs children estan definidas
        """
        for load in self.loads:
            if not load.defined():
                return False
        for child in self.children:
            if not child.defined():
                return False
        return True
