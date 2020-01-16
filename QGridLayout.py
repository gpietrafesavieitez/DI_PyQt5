#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import(QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout, QApplication)

class Aplicacion(QWidget):
    def __init__(self):
        super().__init__()
        lblTitulo = QLabel("Titulo")
        lblAutor = QLabel("Autor")
        lblResumo = QLabel("Resumo")
        editTitulo = QLineEdit()
        editAutor = QLineEdit()
        txtResumo = QTextEdit()
        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(lblTitulo, 1, 0)
        grid.addWidget(editTitulo, 1, 1)
        grid.addWidget(lblAutor, 2, 0)
        grid.addWidget(editAutor, 2, 1)
        grid.addWidget(lblResumo, 3, 0)
        grid.addWidget(txtResumo, 3, 1, 5, 1)
        self.setLayout(grid)
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle("Exemplo de QGridLayout")
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    exemplo = Aplicacion()
    sys.exit(app.exec())