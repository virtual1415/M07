# Patricio Vidal
# -*- coding: utf-8 -*-
 
import sys
from PyQt4 import QtCore, QtGui, uic

# Carrega interficie
form_class = uic.loadUiType("conversor.ui")[0]
 
class MyWindowClass(QtGui.QMainWindow, form_class):

    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.inicial.setPlaceholderText('Introdueix una quantitat')
        QtCore.QObject.connect(self.convertir, QtCore.SIGNAL("clicked()"), self.mostrarResultat)


    def mostrarResultat(self):
        try:
            num = float(self.inicial.text())
        except:
            self.inicial.setText('')
        else:
            if self.eurosPessetes.isChecked():
                res = num * 166.386
            elif self.pessetesEuros.isChecked():
                res = num / 166.386
            self.final.setText(str("%.2f" % res))


app = QtGui.QApplication(sys.argv)
myWindow = MyWindowClass(None)
myWindow.show()
app.exec_()

