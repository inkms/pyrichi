from PyQt5.QtWidgets import (QPushButton, QWidget, QLabel, QVBoxLayout, QGridLayout)
# from PyQt5.QtCore import QSize
from components.box import Box
import utils.globalvars

# box_for_move_selected = False
selected_box = None


class BoxGUI(QPushButton):
    _selection_valid = False

    def __init__(self, box: Box):
        super().__init__()
        self.setAutoFillBackground(True)
        self.box = box
        box.gui = self
        self.setText(str(box.get_id()))
        self.clicked.connect(self.process_click)
        self.details = BoxDetails(self.box, self)

    def render_with_children(self, layout: QGridLayout,
                             row_initial: int,
                             column_initial: int):
        layout.addWidget(self, row_initial, column_initial)
        print("Adding box {} on row {} and column {}".format(
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
        if mode == "Add":
            self.process_click_add_mode()
            return
        if mode == "Delete":
            self.process_click_delete_mode()
            return
        if mode == "Move":
            self.process_click_move_mode()
            return
        self.process_click_default_mode()

    def process_click_add_mode(self):
        print("Add mode click")
        self.box.add_child(Box())
        self.window().redraw_boxes()

    def process_click_delete_mode(self):
        print("Delete mode click")
        self.box.parent.delete_child(self.box)
        del self.box
        self.window().redraw_boxes()

    def process_click_move_mode(self):
        # global box_for_move_selected
        global selected_box
        print("Move mode click")
        if not utils.globalvars.box_for_move_selected:
            utils.globalvars.box_for_move_selected = True
            selected_box = self.box
            self.disable_descendant_boxes()
            print("Selected box for moving {}".format(self.box.get_id()))
        else:
            self.box.add_child(selected_box)
            utils.globalvars.box_for_move_selected = False
            print("Moved box {} to hang from {}".format(
                selected_box.get_id(), self.box.get_id()))
            self.window().redraw_boxes()

    def process_click_default_mode(self):
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
