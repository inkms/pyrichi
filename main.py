"""Pantalla principal de la aplicacion
"""
import sys
from PyQt5.QtWidgets import (QApplication, QHBoxLayout, QLayout, QMainWindow, QPushButton,
                             QWidget, QToolBar, QGridLayout, QAction)
from PyQt5.QtCore import QSize
from components.box import Box
from gui.box_gui import BoxGUI


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Pyrichi")

        self.entrance = Box()
        self.box_layout = QGridLayout()
        # self.main_layout.addS

        self.redraw_boxes()

        self.value = 2

        widget = QWidget()
        widget.setLayout(self.box_layout)
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

    def clickOnAddBox(self, selected: bool):
        print("click on add", selected)
        if selected:
            self.button_borrar.setChecked(False)
            self.mode = "Add"
        else:
            self.mode = "Default"

    def clickOnDeleteBox(self, selected: bool):
        print("click on delete", selected)
        if selected:
            self.button_anadir.setChecked(False)
            self.mode = "Delete"
        else:
            self.mode = "Default"

    def get_mode(self):
        return self.mode

    def redraw_boxes(self):
        while self.box_layout.count():  # Cleanup loop
            child = self.box_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        entranceGUI = BoxGUI(self.entrance)  # Renders boxes
        entranceGUI.render_with_children(self.box_layout, 0, 0)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
