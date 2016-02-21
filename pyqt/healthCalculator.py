# -*- coding: utf-8 -*-
# author: Patricio Vidal

import sys
from PyQt4 import QtCore, QtGui, uic

# Carrega interficie
form_class = uic.loadUiType("healthCalculator.ui")[0]


class MyWindowClass(QtGui.QMainWindow, form_class):

    css1 = 'background-color: rgb(236,236,236); border: 1px solid rgb(204,204,204); border-radius: 4px'
    css2 = 'color: red; background-color: rgb(236,236,236); border: 1px solid rgb(204,204,204); border-radius: 4px'

    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        imc = QtGui.QPixmap('imatges_healthCalculator/IMC.png')
        self.imgResult.setPixmap(imc)
        QtCore.QObject.connect(self.fumador, QtCore.SIGNAL("clicked()"), self.missatgeFumador)
        QtCore.QObject.connect(self.calcula, QtCore.SIGNAL("clicked()"), self.mostrarResultats)

    def mostrarResultats(self):
        self.imc.setStyleSheet(self.css1)
        alcada = float(self.alcada.value())
        pes = float(self.pes.value())
        edat = self.edat.value()
        if pes != 0:
            if alcada != 0:
                res = round(pes / ((alcada / 100) ** 2), 2)
                self.imgResultat(res)
                self.imc.setText(str(res))
            else:
                self.missatgeAlcada()
            if self.dona.isChecked():
                res = int((210 - (edat * 0.5)) - (pes * 0.1))
                self.fcmax.setText(str(res))
            if self.home.isChecked():
                res = int((210 - (edat * 0.5)) - (pes * 0.1) + 4)
                self.fcmax.setText(str(res))
        else:
            self.missatgePes()

    def imgResultat(self, res):
        if res < 18.5:
            imc = QtGui.QPixmap('imatges_healthCalculator/IMC_critico.png')
            self.imc.setStyleSheet(self.css2)
        elif res < 25:
            imc = QtGui.QPixmap('imatges_healthCalculator/IMC_1.png')
        elif res < 30:
            imc = QtGui.QPixmap('imatges_healthCalculator/IMC_2.png')
        elif res < 35:
            imc = QtGui.QPixmap('imatges_healthCalculator/IMC_3.png')
        elif res < 40:
            imc = QtGui.QPixmap('imatges_healthCalculator/IMC_4.png')
        elif res < 80:
            imc = QtGui.QPixmap('imatges_healthCalculator/IMC_5.png')
            self.imc.setStyleSheet(self.css2)
        else:
            imc = QtGui.QPixmap('imatges_healthCalculator/IMC_critico.png')
            self.imc.setStyleSheet(self.css2)
        self.imgResult.setPixmap(imc)

    def missatgeFumador(self):
        QtGui.QMessageBox.warning(None, "Atencio", "Fumar perjudica la seva salut")

    def missatgeAlcada(self):
        QtGui.QMessageBox.warning(None, "Atencio", "S'ha d'introduir l'alçada")

    def missatgePes(self):
        QtGui.QMessageBox.warning(None, "Atencio", "S'ha d'introduir el pes")


app = QtGui.QApplication(sys.argv)
myWindow = MyWindowClass(None)
myWindow.show()
app.exec_()
