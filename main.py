"""Pantalla principal de la aplicacion
"""
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout
from PyQt5.QtGui import QPalette, QColor
from components.caja import Caja

class CajaGUI(QPushButton):

    def __init__(self, caja):
        super().__init__()
        self.setAutoFillBackground(True)
        self.caja = caja
        caja._set_gui(self)
        self.setText(str(caja.get_identidad()))


    def render_con_hijas(self, layout, fila_inicial, columna_inicial):
        layout.addWidget(self, fila_inicial, columna_inicial)
        print("Adding caja {} en la fila {} y columna {}", self.caja.get_identidad(), fila_inicial, columna_inicial)
        columna = columna_inicial + 1
        fila = fila_inicial
        for hija in self.caja.get_hijas():
            nueva_caja_gui = CajaGUI(hija)
            fila = nueva_caja_gui.render_con_hijas(layout,fila,columna)
        return fila + 1


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Pyrichi")

        acometida = Caja()
        self.acometida = CajaGUI(acometida)
        caja1 = Caja(self.acometida.caja)
        caja2 = Caja(self.acometida.caja)
        caja1a = Caja(caja1)
        caja1b = Caja(caja1)
        caja2a = Caja(caja2) 
        self.layout = QGridLayout()

        self.render_cajas()

        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)


    def render_cajas(self):
        """Distribuye las cajas partiendo de la caja de acometida
        """
        columna = 0
        fila = 0
        self.acometida.render_con_hijas(self.layout,0,0)
        # self.layout.addWidget(CajaGUI(self.acometida), fila, columna)
        # print("Adding caja {} en la fila {} y columna {}", self.acometida.get_identidad(), fila, columna)
        # columna += 1
        # for hija in self.acometida.get_hijas():
        #     nueva_caja_gui = CajaGUI(hija)
        #     fila = nueva_caja_gui.render_con_hijas(self.layout,fila,columna)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
