# -*- coding: utf-8 -*-
# author: Patricio Vidal

from PyQt4 import QtCore, QtGui
import palanca


class Palanca(QtGui.QMainWindow, palanca.Ui_MainWindow):

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        palancaEq = QtGui.QPixmap('imatges_palanca/ley-palanca-equilibri.png')
        self.resultat.setPixmap(palancaEq)
        QtCore.QObject.connect(self.brmenys, QtCore.SIGNAL("clicked()"), self.decrementa_r)
        QtCore.QObject.connect(self.brmes, QtCore.SIGNAL("clicked()"), self.incrementa_r)
        QtCore.QObject.connect(self.bpmenys, QtCore.SIGNAL("clicked()"), self.decrementa_p)
        QtCore.QObject.connect(self.bpmes, QtCore.SIGNAL("clicked()"), self.incrementa_p)
        QtCore.QObject.connect(self.sliderBR, QtCore.SIGNAL("valueChanged(int)"), self.calcular)
        QtCore.QObject.connect(self.sliderBP, QtCore.SIGNAL("valueChanged(int)"), self.calcular)

    def decrementa_r(self):
        R = int(self.R.text())
        if R > 0:
            R -= 1
            self.R.setText(str(R))
        self.calcular()

    def incrementa_r(self):
        R = int(self.R.text())
        if R < 999:
            R += 1
            self.R.setText(str(R))
        self.calcular()

    def decrementa_p(self):
        P = int(self.P.text())
        if P > 0:
            P -= 1
            self.P.setText(str(P))
        self.calcular()

    def incrementa_p(self):
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
