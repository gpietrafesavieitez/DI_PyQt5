#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import(QWidget, QPushButton, QGridLayout, QApplication, QSizePolicy)

class Aplicacion(QWidget):
    def __init__(self):
        super().__init__()
        btn1 = QPushButton("Boton1")
        btn2 = QPushButton("Boton2")
        btn3 = QPushButton("Boton3")
        btn3.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        btn4 = QPushButton("Boton4")
        btn5 = QPushButton("Boton5")
        btn6 = QPushButton("Boton6")
        grid = QGridLayout()
        grid.addWidget(btn1, 0, 0, 1, 1)
        grid.addWidget(btn2, 0, 1, 1, 2)
        grid.addWidget(btn3, 1, 0, 2, 1)
        grid.addWidget(btn4, 1, 1, 1, 2)
        grid.addWidget(btn5, 2, 1, 1, 1)
        grid.addWidget(btn6, 2, 2, 1, 1)
        self.setLayout(grid)
        self.setWindowTitle("Ejercicio botones")
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    exemplo = Aplicacion()
    sys.exit(app.exec())