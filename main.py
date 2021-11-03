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
        self.window().render_boxes()

    def processClickDeleteMode(self):
        print("Delete mode click")
        self.box.set_parent(None)
        self.window().render_boxes()

    def processClickDefaultMode(self):
        print("Default mode click")


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Pyrichi")

        entrance = Box()
        self.entrance = BoxGUI(entrance)
        self.layout = QGridLayout()

        self.render_boxes()

        self.value = 2

        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)

        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        self.boton_anadir = QAction("Add box", self)
        self.boton_anadir.setStatusTip("Add mode active")
        self.boton_anadir.triggered.connect(self.clickOnAddBox)
        self.boton_anadir.setCheckable(True)
        toolbar.addAction(self.boton_anadir)

        toolbar.addSeparator()

        self.boton_borrar = QAction("Delete box", self)
        self.boton_borrar.setStatusTip("mode borrar activado")
        self.boton_borrar.triggered.connect(self.clickOnDeleteBox)
        self.boton_borrar.setCheckable(True)
        toolbar.addAction(self.boton_borrar)

        self.mode = "Default"

    def clickOnAddBox(self, s):
        print("click on add", s)
        if s:
            self.boton_borrar.setChecked(False)
            self.mode = "Add"
        else:
            self.mode = "Default"

    def clickOnDeleteBox(self, s):
        global _mode
        print("click on delete", s)
        if s:
            self.boton_anadir.setChecked(False)
            self.mode = "Delete"
        else:
            self.mode = "Default"

    def render_boxes(self):
        # self.clearLayout()
        self.entrance.render_with_children(self.layout, 0, 0)

    def get_mode(self):
        return self.mode

    # def clearLayout(self):  # Magia potagia que limpia el layout
    #     while self.layout.count():
    #         child = self.layout.takeAt(0)
    #         if child.widget():
    #             child.widget().deleteLater()


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
