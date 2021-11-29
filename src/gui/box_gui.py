from PyQt5.QtWidgets import (QLayout, QPushButton,
                             QWidget, QLabel, QVBoxLayout)
# from PyQt5.QtCore import QSize
from components.box import Box


class BoxGUI(QPushButton):

    def __init__(self, box: Box):
        super().__init__()
        self.setAutoFillBackground(True)
        self.box = box
        self.setText(str(box.get_id()))
        self.clicked.connect(self.processClick)
        self.details = BoxDetails(self.box, self)

    def render_with_children(self, layout: QLayout,
                             row_initial: int,
                             column_initial: int):
        """Adds itself and all of its children to a grid layout using
        the offset specified by row_initial and column_initial. This
        is done by creating a new BoxGUI for each child, the old ones,
        if present, are discarded.
        """
        layout.addWidget(self, row_initial, column_initial)
        print("Adding box {} on row {} and column {}".format(
            self.get_box().get_id(),
            row_initial, column_initial))
        column = column_initial + 1
        row = row_initial
        for child in self.get_box().get_children():
            nueva_box_gui = BoxGUI(child)
            row = nueva_box_gui.render_with_children(layout, row, column)
        return row + 1

    def processClick(self):
        """Directs the program to the right function to process the click based
        on the mode of the window
        """
        mode = self.window().get_mode()
        if mode == "Add":
            self.processClickAddMode()
            return
        if mode == "Delete":
            self.processClickDeleteMode()
            return
        self.processClickDefaultMode()

    def processClickAddMode(self):
        """Adds a new box to this box
        """
        print("Add mode click")
        Box(self.box)
        self.window().redraw_boxes()

    def processClickDeleteMode(self):
        """Deletes this box and all of its children
        """
        print("Delete mode click")
        self.box.set_parent(None)
        self.window().redraw_boxes()

    def processClickDefaultMode(self):
        """Displays box information and allows to change the box parameters
        """
        print("Default mode click")
        self.details.show()

    def get_box(self) -> Box:
        """Returns a reference to the underlying Box object
        """
        return self.box


class BoxDetails(QWidget):

    def __init__(self, box: Box, gui: BoxGUI):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Another Window")
        layout.addWidget(self.label)
        self.setLayout(layout)
        self.box = box
        self.gui = gui
