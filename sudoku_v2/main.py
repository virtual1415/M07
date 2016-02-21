# Patricio Vidal
# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from numpy import *
import numpy as np
import threading
import sys
import sudoku
import missatge
import sudokuMaker
import time
import os


# class Missatge(threading.Thread, QtGui.QMainWindow, missatge.Ui_Missatge):
#     def __init__(self):
#         super(self.__class__, self).__init__()
#         self.setupUi(self)
#         threading.Thread.__init__(self)
#
#     def run(self):
#         app = QtGui.QApplication(sys.argv)
#         form = Missatge()
#         form.show()
#         app.exec_()


class Joc(QtGui.QMainWindow, sudoku.Ui_MainWindow):

    # Es definexen els diferents estils que podran emprar tant els missatges com el tauler de joc
    CSS1 = 'color: green; background-color: rgb(236,236,236); border: 1px solid rgb(204,204,204); border-radius: 4px'
    CSS2 = 'color: red; background-color: rgb(236,236,236); border: 1px solid rgb(204,204,204); border-radius: 4px'
    CSS3 = 'background-color: rgb(236,236,236)'

    # Es defineixen constants per als missatges que mostrara l'aplicacio
    CORRECTE = "CORRECTE"
    GENERANT = "S'esta generant un sudoku"
    MISSATGE_1 = "Valor repetit"
    MISSATGE_2 = "Nomes son valids els valors\nnumerics del 1 al 9"
    MISSATGE_3 = "Hi ha caselles sense emplenar"

    # Es defineix la mida del sudoku i els valors valids
    MIDA_SUDOKU = 9
    VALORS_VALIDS = (1, 2, 3, 4, 5, 6, 7, 8, 9)

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.generar_joc()
        self.validateButton.clicked.connect(self.validar)
        self.resetButton.clicked.connect(self.iniciar_joc)
        self.newButton.clicked.connect(self.generar_joc)

    # Funcio que genera un sudoku, a partir del qual es generara la graella del joc
    # S'utilitzen funcions del fitxer sudokuMaker.py
    def generar_joc(self):
        # fil = Missatge()
        # fil.start()
        self.sudoku = sudokuMaker.generate_grid()  # Funcio que genera el sudoku
        print self.sudoku
        self.joc = sudokuMaker.generate_game(self.sudoku)  # Funcio que genera la graella del joc,
                                                           # posa 0 en els números que no es mostraran
        self.iniciar_joc()

    # Funcio que a partir de la graella de joc generada en la funció anterior emplena la interficie gràfica
    def iniciar_joc(self):
        for i in range(self.MIDA_SUDOKU):
            for j in range(self.MIDA_SUDOKU):
                nom = 'cel_' + str(i) + '_' + str(j)
                obj_qlineedit = self.findChild(QtGui.QLineEdit, nom)
                obj_qlineedit.setValidator(QtGui.QIntValidator(1, self.MIDA_SUDOKU, self))
                # obj_qlineedit.setInputMask("D")
                if self.joc[i][j] != 0:
                    obj_qlineedit.setText(str(self.joc[i][j]))
                    obj_qlineedit.setStyleSheet(self.CSS3)
                    obj_qlineedit.setReadOnly(True)
                    obj_qlineedit.setDisabled(True)
                else:
                    obj_qlineedit.setText('')
                    obj_qlineedit.setStyleSheet('')
                    obj_qlineedit.setReadOnly(False)
                    obj_qlineedit.setDisabled(False)
                    self.messages.setText('')
                    self.messages.setStyleSheet('')

    # Funcio que recull els valors emplenats pel jugador i comprova si es correcte o no
    def validar(self):
        # La solucio proposada per l'usuari es guarda en una llista de numeros enters
        proposta = []
        # Variable boleana que servira per saber si un usuari ha deixat caselles sense emplenar
        espais_buits = False
        try:
            # Es recorre la matriu grafica de QLineEdits i es recull el seu contingut
            for i in range(self.MIDA_SUDOKU):
                proposta.append([])
                for j in range(self.MIDA_SUDOKU):
                    nom = 'cel_' + str(i) + '_' + str(j)
                    obj_qlineedit = self.findChild(QtGui.QLineEdit, nom)
                    if not obj_qlineedit.isReadOnly():
                        obj_qlineedit.setStyleSheet('')
                    else:
                        obj_qlineedit.setStyleSheet(self.CSS3)
                    # Si l'usuari no ha emplenat una casella de la matriu, si afegeix un 0
                    # i la variable boleana espais_buits canvia de valor
                    if obj_qlineedit.text() == '':
                        proposta[i].append(0)
                        espais_buits = True
                    else:
                        proposta[i].append(int(obj_qlineedit.text()))
        except:
            self.messages.setStyleSheet(self.CSS2)
            self.messages.setText(self.MISSATGE_2)

        # Transformem la llista en un array numpy
        propostaObject = np.array(proposta)
        if np.array_equal(self.sudoku, propostaObject):
            self.messages.setStyleSheet(self.CSS1)
            self.messages.setText(self.CORRECTE)
        else:
            if espais_buits is True:
                self.messages.setStyleSheet(self.CSS2)
                self.messages.setText(self.MISSATGE_3)
            else:
                for i in range(self.MIDA_SUDOKU):
                    for j in range(self.MIDA_SUDOKU):
                        if proposta[i][j] not in self.VALORS_VALIDS:
                            nom = 'cel_' + str(i) + '_' + str(j)
                            obj_qlineedit = self.findChild(QtGui.QLineEdit, nom)
                            obj_qlineedit.setStyleSheet(self.CSS2)
                            self.messages.setStyleSheet(self.CSS2)
                            self.messages.setText(self.MISSATGE_2)
                self.duplicats_fila()
                self.duplicats_columna()

    # Funcio que recorre les files de la solució proposada pel jugador
    # i comprova si hi ha duplicats.
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

    # Funcio que recorre les columnes de la solució proposada pel jugador
    # i comprova si hi ha duplicats.
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

    # Funcio que recorre els blocs de 3x3 de la matriu proposada pel jugador
    # i comprova si hi ha duplicats (FUNCIO INACABADA)
    def duplicats_blocs(self, matriu):
        subMatriu = []
        iniciFila = 0
        iniciColumna = 0
        fiFila = (len(matriu) / 3) - 1
        fiColumna = (len(matriu) / 3) - 1
        for i in range(iniciFila, fiFila):
            subMatriu.append([])
            for j in range(iniciColumna, fiColumna):
                subMatriu.append([matriu[i][j]])
        vector = np.hstack(self.sudoku)
        print vector


def main():
    app = QtGui.QApplication(sys.argv)
    form = Joc()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
