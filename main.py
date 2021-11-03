"""Pantalla principal de la aplicacion
"""
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QWidget,
                             QToolBar, QVBoxLayout, QHBoxLayout, QGridLayout,
                             QAction)
from PyQt5.QtCore import QSize
from components.box import Box


class BoxGUI(QPushButton):

    def __init__(self, box):
        super().__init__()
        self.setAutoFillBackground(True)
        self.box = box
        self.setText(str(box.get_id()))
        self.clicked.connect(self.processClick)

    def render_with_children(self, layout, row_initial, column_initial):
        layout.addWidget(self, row_initial, column_initial)
        print("Adding box {} on row {} and column {}".format(
            self.box.get_id(),
            row_initial, column_initial))
        column = column_initial + 1
        row = row_initial
        for child in self.box.get_children():
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


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Pyrichi")

        self.entrance = Box()
        self.layout = QGridLayout()

        self.redraw_boxes()

        self.value = 2

        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)

        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        self.button_anadir = QAction("Add box", self)
        self.button_anadir.setStatusTip("Add mode active")
        self.button_anadir.triggered.connect(self.clickOnAddBox)
        self.button_anadir.setCheckable(True)
        toolbar.addAction(self.button_anadir)

        toolbar.addSeparator()

        self.button_borrar = QAction("Delete box", self)
        self.button_borrar.setStatusTip("Delete mode active")
        self.button_borrar.triggered.connect(self.clickOnDeleteBox)
        self.button_borrar.setCheckable(True)
        toolbar.addAction(self.button_borrar)

        self.button_redraw = QAction("Force redraw", self)
        self.button_redraw.setStatusTip("Redrawing everything")
        self.button_redraw.triggered.connect(self.redraw_boxes)
        self.button_redraw.setCheckable(False)
        toolbar.addAction(self.button_redraw)

        self.mode = "Default"

    def clickOnAddBox(self, s):
        print("click on add", s)
        if s:
            self.button_borrar.setChecked(False)
            self.mode = "Add"
        else:
            self.mode = "Default"

    def clickOnDeleteBox(self, s):
        print("click on delete", s)
        if s:
            self.button_anadir.setChecked(False)
            self.mode = "Delete"
        else:
            self.mode = "Default"

    def get_mode(self):
        return self.mode

    def redraw_boxes(self):
        while self.layout.count():  # Cleanup loop
            child = self.layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        entranceGUI = BoxGUI(self.entrance)  # Renders boxes
        entranceGUI.render_with_children(self.layout, 0, 0)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
