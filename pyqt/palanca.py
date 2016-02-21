# -*- coding: utf-8 -*-
# author: Patricio Vidal

import sys
from PyQt4 import QtCore, QtGui, uic

# Carrega interficie
form_class = uic.loadUiType("palanca.ui")[0]


class MyWindowClass(QtGui.QMainWindow, form_class):

    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        palancaEq = QtGui.QPixmap('imatges_palanca/ley-palanca-equilibri.png')
        self.resultat.setPixmap(palancaEq)
        QtCore.QObject.connect(self.brmenys, QtCore.SIGNAL("clicked()"), self.decrementaR)
        QtCore.QObject.connect(self.brmes, QtCore.SIGNAL("clicked()"), self.incrementaR)
        QtCore.QObject.connect(self.bpmenys, QtCore.SIGNAL("clicked()"), self.decrementaP)
        QtCore.QObject.connect(self.bpmes, QtCore.SIGNAL("clicked()"), self.incrementaP)
        QtCore.QObject.connect(self.sliderBR, QtCore.SIGNAL("sliderReleased()"), self.calcular)
        QtCore.QObject.connect(self.sliderBP, QtCore.SIGNAL("sliderReleased()"), self.calcular)

    def decrementaR(self):
        R = int(self.R.text())
        if R > 0:
            R -= 1
            self.R.setText(str(R))
        self.calcular()

    def incrementaR(self):
        R = int(self.R.text())
        if R < 999:
            R += 1
            self.R.setText(str(R))
        self.calcular()

    def decrementaP(self):
        P = int(self.P.text())
        if P > 0:
            P -= 1
            self.P.setText(str(P))
        self.calcular()

    def incrementaP(self):
        P = int(self.P.text())
        if P < 999:
            P += 1
            self.P.setText(str(P))
        self.calcular()
    
    def calcular(self):
        BR = int(self.lcdBR.value())
        BP = int(self.lcdBP.value())
        R = int(self.R.text())
        P = int(self.P.text())
        resistencia = BR * R
        potencia = BP * P
        if resistencia == potencia:
            palancaEq = QtGui.QPixmap('imatges_palanca/ley-palanca-equilibri.png')
            self.resultat.setPixmap(palancaEq)
        elif resistencia > potencia:
            palancaNeg = QtGui.QPixmap('imatges_palanca/ley-palanca-negat.png')
            self.resultat.setPixmap(palancaNeg)
        else:
            palancaPos = QtGui.QPixmap('imatges_palanca/ley-palanca-pos.png')
            self.resultat.setPixmap(palancaPos)
    

app = QtGui.QApplication(sys.argv)
myWindow = MyWindowClass(None)
myWindow.show()
app.exec_()
