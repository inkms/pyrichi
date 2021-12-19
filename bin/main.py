import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QToolBar,
                             QGridLayout, QAction, QComboBox, QLabel)
from PyQt5.QtCore import QSize
from components.box import Box
from gui.box_gui import BoxGUI
import normatives
from components.mode import Mode
import utils.globalvars
import logging
import coloredlogs

logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG')


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        utils.globalvars.initialize()
        self.normative = normatives.Normative()

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

        toolbar.addSeparator()

        self.normative_selector = QComboBox()
        self.normative_selector.addItems(normatives.names)
        self.normative_selector.currentIndexChanged.connect(self.change_normative)
        toolbar.addWidget(QLabel("Normative:"))
        toolbar.addWidget(self.normative_selector)

        self.mode = Mode.DEFAULT
        self.redraw_boxes()

    def click_on_add_box(self, selected: bool):
        logger.debug("click on add {}".format(selected))
        if selected:
            self.change_mode(Mode.ADD)
        else:
            self.change_mode(Mode.DEFAULT)
        logger.info("State changed to {}".format(self.mode))

    def click_on_delete_box(self, selected: bool):
        logger.debug("click on delete {}".format(selected))
        if selected:
            self.change_mode(Mode.DELETE)
        else:
            self.change_mode(Mode.DEFAULT)
        logger.info("State changed to {}".format(self.mode))

    def click_on_move_box(self, selected: bool):
        logger.debug("click on move {}".format(selected))
        if selected:
            self.change_mode(Mode.MOVE)
        else:
            self.change_mode(Mode.DEFAULT)
        logger.info("State changed to {}".format(self.mode))

    def change_mode(self, candidate_state):
        self.button_add.setChecked(False)
        self.button_delete.setChecked(False)
        self.button_move.setChecked(False)
        self.mode = candidate_state
        if candidate_state == Mode.ADD:
            self.button_add.setChecked(True)
            utils.globalvars.box_for_move_selected = False
        elif candidate_state == Mode.DELETE:
            self.button_delete.setChecked(True)
            utils.globalvars.box_for_move_selected = False
        elif candidate_state == Mode.MOVE:
            self.button_move.setChecked(True)
        elif candidate_state == Mode.DEFAULT:
            utils.globalvars.box_for_move_selected = False
        self.redraw_boxes()

    def get_mode(self):
        return self.mode

    def change_normative(self, i):
        logger.debug(f"Normative selected is {normatives.names[i]}")
        self.normative = eval(f"normatives.{normatives.names[i]}")()
        logger.info(f"Normative changed to {self.normative.name()}")

    def redraw_boxes(self):
        self.clean()
        self.entranceGUI = BoxGUI(self.entrance)
        self.entranceGUI.render_with_children(self.box_layout, 0, 0)
        if self.mode == Mode.DELETE:
            self.entranceGUI.setEnabled(False)

    def clean(self):
        # for child in self.entrance.get_children():
        #     del child
        while self.box_layout.count():  # Cleanup loop
            child = self.box_layout.takeAt(0)
            if child.widget():
                # child.widget().setParent(None)
                child.widget().deleteLater()


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
