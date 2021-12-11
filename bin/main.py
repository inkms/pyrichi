import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QToolBar,
                             QGridLayout, QAction)
from PyQt5.QtCore import QSize
from components.box import Box
from gui.box_gui import BoxGUI
import utils.globalvars
import logging, coloredlogs

logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG')


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        utils.globalvars.initialize()
        logger.critical("panic in the disco")
        self.setWindowTitle("Pyrichi")

        self.entranceGUI = None
        self.entrance = Box()
        self.box_layout = QGridLayout()

        self.value = 2

        widget = QWidget()
        widget.setLayout(self.box_layout)
        self.setCentralWidget(widget)

        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        self.button_add = QAction("Add box", self)
        self.button_add.setStatusTip("Add mode active")
        # noinspection PyUnresolvedReferences
        self.button_add.triggered.connect(self.click_on_add_box)
        self.button_add.setCheckable(True)
        toolbar.addAction(self.button_add)

        toolbar.addSeparator()

        self.button_delete = QAction("Delete box", self)
        self.button_delete.setStatusTip("Delete mode active")
        # noinspection PyUnresolvedReferences
        self.button_delete.triggered.connect(self.click_on_delete_box)
        self.button_delete.setCheckable(True)
        toolbar.addAction(self.button_delete)

        toolbar.addSeparator()

        self.button_move = QAction("Move box", self)
        self.button_move.setStatusTip("Move mode active")
        # noinspection PyUnresolvedReferences
        self.button_move.triggered.connect(self.click_on_move_box)
        self.button_move.setCheckable(True)
        toolbar.addAction(self.button_move)

        self.mode = "Default"
        self.redraw_boxes()

    def click_on_add_box(self, selected: bool):
        logger.debug("click on add {}".format(selected))
        if selected:
            self.change_state("Add")
        else:
            self.change_state("Default")
        logger.info("State changed to {}".format(self.mode))

    def click_on_delete_box(self, selected: bool):
        logger.debug("click on delete {}".format(selected))
        if selected:
            self.change_state("Delete")
        else:
            self.change_state("Default")
        logger.info("State changed to {}".format(self.mode))

    def click_on_move_box(self, selected: bool):
        logger.debug("click on move {}".format(selected))
        if selected:
            self.change_state("Move")
        else:
            self.change_state("Default")
        logger.info("State changed to {}".format(self.mode))

    def change_state(self, candidate_state):
        self.button_add.setChecked(False)
        self.button_delete.setChecked(False)
        self.button_move.setChecked(False)
        self.mode = candidate_state
        if candidate_state == "Add":
            self.button_add.setChecked(True)
            utils.globalvars.box_for_move_selected = False
        elif candidate_state == "Delete":
            self.button_delete.setChecked(True)
            utils.globalvars.box_for_move_selected = False
        elif candidate_state == "Move":
            self.button_move.setChecked(True)
        elif candidate_state == "Default":
            utils.globalvars.box_for_move_selected = False
        self.redraw_boxes()

    def get_mode(self):
        return self.mode

    def redraw_boxes(self):
        while self.box_layout.count():  # Cleanup loop
            child = self.box_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        self.entranceGUI = BoxGUI(self.entrance)
        self.entranceGUI.render_with_children(self.box_layout, 0, 0)
        if self.mode == "Delete":
            self.entranceGUI.setEnabled(False)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
