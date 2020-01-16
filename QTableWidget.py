#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem

datos = {"Col1":[1,2,3,4],
         "Col2":[1,3,5,7],
         "Col3":[1,2,4,6]}

class App(QTableWidget):
    def __init__(self, datos, *args):
        self.datos = datos
        self.asinarDatos()
        self.resizeColumnsToContents()
        self.resizeRowsToContents()

    def asinarDatos(self):
        cabeceirasHor = []
        for n, clave in enumerate(self.datos.keys()):
            cabeceirasHor.append(clave)
            for m, numero in enumerate(self.datos[clave]):
                novoElemento = QTableWidgetItem(numero)
                self.setItem(m, n, novoElemento)
        self.setHorizontalHeaderLabels(cabeceirasHor)

