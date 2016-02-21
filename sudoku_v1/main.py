# Patricio Vidal
# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
import sys

import sudoku
import os
import time


class Joc(QtGui.QMainWindow, sudoku.Ui_MainWindow):

    # Es definexen els diferents estils que podran emprar tant els missatges com el tauler de joc
    CSS1 = 'color: green; background-color: rgb(236,236,236); border: 1px solid rgb(204,204,204); border-radius: 4px'
    CSS2 = 'color: red; background-color: rgb(236,236,236); border: 1px solid rgb(204,204,204); border-radius: 4px'
    CSS3 = 'background-color: rgb(236,236,236)'

    # Es defineixen constants per als missatges que mostrara l'aplicacio
    CORRECTE = "CORRECTE"
    MISSATGE_1 = "Valor repetit"
    MISSATGE_2 = "Nomes son valids els valors\nnumerics del 1 al 4"
    MISSATGE_3 = "Torna-ho a intentar"

    # Es defineixen el joc (JOC) i la seva solució (SUDOKU)
    SUDOKU = [[4, 2, 3, 1], [1, 3, 4, 2], [2, 4, 1, 3], [3, 1, 2, 4]]
    JOC = [[4, 0, 0, 1], [0, 0, 4, 0], [0, 4, 0, 0], [3, 0, 2, 0]]

    # Es defineix la mida del sudoku i els valors vàlids
    MIDA_SUDOKU = 4
    VALORS_VALIDS = (1, 2, 3, 4)

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.iniciar_joc()
        self.validateButton.clicked.connect(self.validar)
        self.resetButton.clicked.connect(self.iniciar_joc)

    def iniciar_joc(self):
        for i in range(self.MIDA_SUDOKU):
            for j in range(self.MIDA_SUDOKU):
                nom = 'cel_' + str(i) + '_' + str(j)
                obj_qlineedit = self.findChild(QtGui.QLineEdit, nom)
                obj_qlineedit.setValidator(QtGui.QIntValidator(1, self.MIDA_SUDOKU))
                if self.JOC[i][j] != 0:
                    obj_qlineedit.setText(str(self.JOC[i][j]))
                    obj_qlineedit.setStyleSheet(self.CSS3)
                    obj_qlineedit.setReadOnly(True)
                else:
                    obj_qlineedit.setText('')
                    obj_qlineedit.setStyleSheet('')
                    obj_qlineedit.setReadOnly(False)
                    self.messages.setText('')
                    self.messages.setStyleSheet('')

    def validar(self):
        proposta = []
        try:
            for i in range(self.MIDA_SUDOKU):
                proposta.append([])
                for j in range(self.MIDA_SUDOKU):
                    nom = 'cel_' + str(i) + '_' + str(j)
                    obj_qlineedit = self.findChild(QtGui.QLineEdit, nom)
                    proposta[i].append(int(obj_qlineedit.text()))
        except:
            self.messages.setStyleSheet(self.CSS2)
            self.messages.setText(self.MISSATGE_2)
        num_acerts = 0
        for i in range(self.MIDA_SUDOKU):
            if self.SUDOKU[i] == proposta[i]:
                num_acerts += 1
        if num_acerts == self.MIDA_SUDOKU:
            self.messages.setStyleSheet(self.CSS1)
            self.messages.setText(self.CORRECTE)
        else:
            for i in range(self.MIDA_SUDOKU):
                for j in range(self.MIDA_SUDOKU):
                    if proposta[i][j] not in self.VALORS_VALIDS:
                        nom = 'cel_' + str(i) + '_' + str(j)
                        obj_qlineedit = self.findChild(QtGui.QLineEdit, nom)
                        obj_qlineedit.setStyleSheet(self.CSS2)
                        self.messages.setStyleSheet(self.CSS2)
                        self.messages.setText(self.MISSATGE_2)
                        #time.sleep(3)
                        #obj_qlineedit.setStyleSheet('')
                        #self.messages.setStyleSheet('')
                        #self.messages.setText('')
            self.duplicats_fila()
            self.duplicats_columna()

    def duplicats_fila(self):
        for i in range(self.MIDA_SUDOKU):
            for j in range(self.MIDA_SUDOKU - 1):
                nom1 = 'cel_' + str(i) + '_' + str(j)
                obj_qlineedit1 = self.findChild(QtGui.QLineEdit, nom1)
                for k in range(j + 1, self.MIDA_SUDOKU):
                    nom2 = 'cel_' + str(i) + '_' + str(k)
                    obj_qlineedit2 = self.findChild(QtGui.QLineEdit, nom2)
                    if obj_qlineedit1.text() == obj_qlineedit2.text():
                        obj_qlineedit1.setStyleSheet(self.CSS2)
                        obj_qlineedit2.setStyleSheet(self.CSS2)
                        self.messages.setStyleSheet(self.CSS2)
                        self.messages.setText(self.MISSATGE_1)

    def duplicats_columna(self):
        for i in range(self.MIDA_SUDOKU):
            for j in range(self.MIDA_SUDOKU - 1):
                nom1 = 'cel_' + str(j) + '_' + str(i)
                obj_qlineedit1 = self.findChild(QtGui.QLineEdit, nom1)
                for k in range(j + 1, self.MIDA_SUDOKU):
                    nom2 = 'cel_' + str(k) + '_' + str(i)
                    obj_qlineedit2 = self.findChild(QtGui.QLineEdit, nom2)
                    if obj_qlineedit1.text() == obj_qlineedit2.text():
                        obj_qlineedit1.setStyleSheet(self.CSS2)
                        obj_qlineedit2.setStyleSheet(self.CSS2)
                        self.messages.setStyleSheet(self.CSS2)
                        self.messages.setText(self.MISSATGE_1)


def main():
    app = QtGui.QApplication(sys.argv)
    form = Joc()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
