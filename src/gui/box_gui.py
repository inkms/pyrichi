from PyQt5.QtWidgets import (QPushButton, QWidget, QLabel, QVBoxLayout, QGridLayout)
from components.box import Box
from components.mode import Mode
import utils.globalvars
import logging

logger = logging.getLogger(__name__)

# box_for_move_selected = False
selected_box = None


class BoxGUI(QPushButton):
    _selection_valid = False

    def __init__(self, box: Box):
        super().__init__()
        self.setAutoFillBackground(True)
        self.box = box
        if box.gui is not None:
            del box.gui
        box.gui = self
        self.setText(str(box.get_id()))
        self.clicked.connect(self.process_click)
        # self.details = BoxDetails(self.box)

    def render_with_children(self, layout: QGridLayout,
                             row_initial: int,
                             column_initial: int):
        layout.addWidget(self, row_initial, column_initial)
        logger.debug("Adding box {} on row {} and column {}".format(
            self.get_box().get_id(),
            row_initial, column_initial))
        column = column_initial + 1
        row = row_initial
        for child in self.get_box().get_children():
            new_box_gui = BoxGUI(child)
            row = new_box_gui.render_with_children(layout, row, column)
        return row + 1

    def disable_descendant_boxes(self):
        self.setEnabled(False)
        for child in self.box.get_children():
            child.gui.disable_descendant_boxes()

    def process_click(self):
        mode = self.window().get_mode()
        if mode == Mode.ADD:
            self.process_click_add_mode()
            return
        if mode == Mode.DELETE:
            self.process_click_delete_mode()
            return
        if mode == Mode.MOVE:
            self.process_click_move_mode()
            return
        if mode == Mode.DEFAULT:
            self.process_click_default_mode()
            return
        logger.error("Unknown execution mode")

    def process_click_add_mode(self):
        logger.info(f"Add mode click on box {self.box.get_id()}")
        self.box.add_child(Box())
        self.window().redraw_boxes()

    def process_click_delete_mode(self):
        logger.info(f"Delete mode click on box {self.box.get_id()}")
        self.box.parent.delete_child(self.box)
        self.box.erase()
        self.window().redraw_boxes()

    def process_click_move_mode(self):
        global selected_box
        logger.info(f"Move mode click on box {self.box.get_id()}")
        if not utils.globalvars.box_for_move_selected:
            utils.globalvars.box_for_move_selected = True
            selected_box = self.box
            self.disable_descendant_boxes()
            logger.debug("Selected box for moving {}".format(self.box.get_id()))
        else:
            self.box.add_child(selected_box)
            utils.globalvars.box_for_move_selected = False
            logger.debug("Moved box {} to hang from {}".format(
                selected_box.get_id(), self.box.get_id()))
            self.window().redraw_boxes()

    def process_click_default_mode(self):
        logger.info(f"Default mode click on box {self.box.get_id()}")
        logger.debug(self.window().normative.calculate_box(self.box))
        # self.details.show()

    def get_box(self) -> Box:
        return self.box


class BoxDetails(QWidget):

    def __init__(self, box: Box):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Another Window")
        layout.addWidget(self.label)
        self.setLayout(layout)
        self.box = box
