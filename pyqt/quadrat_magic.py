# -*- coding: utf-8 -*-
# author: Patricio Vidal

import sys
from PyQt4 import QtCore, QtGui, uic

# Carrega interficie
form_class = uic.loadUiType("quadrat_magic.ui")[0]


class MyWindowClass(QtGui.QMainWindow, form_class):

    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)

        ''' Es defineixen constants per als missatges que mostrara l'aplicacio '''

        self.INCORRECTE = "INCORRECTE."
        self.MISSATGE_1 = " Valor repetit."
        self.MISSATGE_2 = " Nomes son valids els valors numerics del 1 al 9."
        self.MISSATGE_3 = " Torna-ho a intentar."

        ''' Es crea una llista amb els valor valids que es podran introduir en el
        quadrat magic '''

        self.valors_valids = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

        ''' Es crea un diccionari anomenat self.funcions que conte en cada key una llista
        amb la crida per cada objecte a les funcions de lectura i esborrat del seu contingut '''

        self.funcions = {0: [self.A1.text, self.A1.clear], 1: [self.A2.text,
                        self.A2.clear], 2: [self.A3.text, self.A3.clear], 3: [self.B1.text,
                        self.B1.clear], 4: [self.B2.text, self.B2.clear], 5: [self.B3.text,
                        self.B3.clear], 6: [self.C1.text, self.C1.clear], 7: [self.C2.text,
                        self.C2.clear], 8: [self.C3.text, self.C3.clear]}
        self.resultats = {0: [self.R1.text, self.R1.clear], 1: [self.R2.text,
                        self.R2.clear], 2: [self.R3.text, self.R3.clear], 3: [self.R4.text,
                        self.R4.clear], 4: [self.R5.text, self.R5.clear], 5: [self.R6.text,
                        self.R6.clear], 6: [self.R7.text, self.R7.clear], 7: [self.R8.text,
                        self.R8.clear]}
        self.quadrat_magic = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        ''' Com no es poden passar funcions amb parametres, utilitzo una funcio anonima lambda, la
        qual executa una funcio que rep com a parametre les key del diccionari self.funcions '''

        QtCore.QObject.connect(self.A1, QtCore.SIGNAL("editingFinished()"), lambda: self.addMatriu(0))
        QtCore.QObject.connect(self.A2, QtCore.SIGNAL("editingFinished()"), lambda: self.addMatriu(1))
        QtCore.QObject.connect(self.A3, QtCore.SIGNAL("editingFinished()"), lambda: self.addMatriu(2))
        QtCore.QObject.connect(self.B1, QtCore.SIGNAL("editingFinished()"), lambda: self.addMatriu(3))
        QtCore.QObject.connect(self.B2, QtCore.SIGNAL("editingFinished()"), lambda: self.addMatriu(4))
        QtCore.QObject.connect(self.B3, QtCore.SIGNAL("editingFinished()"), lambda: self.addMatriu(5))
        QtCore.QObject.connect(self.C1, QtCore.SIGNAL("editingFinished()"), lambda: self.addMatriu(6))
        QtCore.QObject.connect(self.C2, QtCore.SIGNAL("editingFinished()"), lambda: self.addMatriu(7))
        QtCore.QObject.connect(self.C3, QtCore.SIGNAL("editingFinished()"), lambda: self.addMatriu(8))
        QtCore.QObject.connect(self.calcula, QtCore.SIGNAL("clicked()"), self.calcular)
        QtCore.QObject.connect(self.reset, QtCore.SIGNAL("clicked()"), self.esborrar)

    def esborrar(self):
        self.quadrat_magic = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for i in range(9):
            self.funcions[i][1]()
        for i in range(8):
            self.resultats[i][1]()
        self.missatges.clear()
        self.resolt.clear()

    def comprovar(self, valor):
        for i in range(3):
            if int(valor) in self.quadrat_magic[i]:
                return True
        return False

    ''' Aquesta funcio rep per parametre la key per llegir al diccionari self.funcions, que li permetra
    accedir a la llista de funcions de l'objecte invocat '''

    def addMatriu(self, valor):
        num = self.funcions[valor][0]()
        if num in self.valors_valids:
            if self.comprovar(num):
                self.missatges.setText(self.INCORRECTE + self.MISSATGE_1)
                self.funcions[valor][1]()
            else:
                if valor == 0:
                    self.quadrat_magic[0][0] = int(num)
                elif valor == 1:
                    self.quadrat_magic[0][1] = int(num)
                elif valor == 2:
                    self.quadrat_magic[0][2] = int(num)
                elif valor == 3:
                    self.quadrat_magic[1][0] = int(num)
                elif valor == 4:
                    self.quadrat_magic[1][1] = int(num)
                elif valor == 5:
                    self.quadrat_magic[1][2] = int(num)
                elif valor == 6:
                    self.quadrat_magic[2][0] = int(num)
                elif valor == 7:
                    self.quadrat_magic[2][1] = int(num)
                elif valor == 8:
                    self.quadrat_magic[2][2] = int(num)
                self.missatges.clear()
        elif len(num) > 0:
            self.missatges.setText(self.INCORRECTE + self.MISSATGE_2)
            self.funcions[valor][1]()

    def calcular(self):
        res1 = res2 = res3 = res4 = res5 = res6 = res7 = res8 = 0
        for i in range(3):
            for j in range(3):
                if i == 0:
                    res1 += self.quadrat_magic[i][j]
                elif i == 1:
                    res2 += self.quadrat_magic[i][j]
                elif i == 2:
                    res3 += self.quadrat_magic[i][j]
        for i in range(3):
            for j in range(3):
                if j == 0:
                    res7 += self.quadrat_magic[i][j]
                elif j == 1:
                    res6 += self.quadrat_magic[i][j]
                elif j == 2:
                    res5 += self.quadrat_magic[i][j]
        res4 = self.quadrat_magic[0][0] + self.quadrat_magic[1][1] + self.quadrat_magic[2][2]
        res8 = self.quadrat_magic[0][2] + self.quadrat_magic[1][1] + self.quadrat_magic[2][0]
        self.R1.setText(str(res1))
        self.R2.setText(str(res2))
        self.R3.setText(str(res3))
        self.R4.setText(str(res4))
        self.R5.setText(str(res5))
        self.R6.setText(str(res6))
        self.R7.setText(str(res7))
        self.R8.setText(str(res8))
        if res1 == res2 == res3 == res4 == res5 == res6 == res7 == res8 == 15:
            self.resolt.setText("Enhorabona!")
        else:
            self.missatges.setText(self.INCORRECTE + self.MISSATGE_3)


app = QtGui.QApplication(sys.argv)
myWindow = MyWindowClass(None)
myWindow.show()
app.exec_()
