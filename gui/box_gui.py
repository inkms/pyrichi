from PyQt5.QtWidgets import (QApplication, QLayout, QMainWindow, QPushButton,
                             QWidget, QLabel, QVBoxLayout, QAction)
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
        mode = self.window().get_mode()
        if mode == "Add":
            self.processClickAddMode()
            return
        if mode == "Delete":
            self.processClickDeleteMode()
            return
        self.processClickDefaultMode()

    def processClickAddMode(self):
        print("Add mode click")
        Box(self.box)
        self.window().redraw_boxes()

    def processClickDeleteMode(self):
        print("Delete mode click")
        self.box.set_parent(None)
        self.window().redraw_boxes()

    def processClickDefaultMode(self):
        print("Default mode click")
        self.details.show()

    def get_box(self) -> Box:
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
