# -*- coding: utf-8 -*-
# Patricio Vidal

import sys
from PyQt4 import QtCore, QtGui, uic

# Carrega interficie
form_class = uic.loadUiType("colors.ui")[0]


class MyWindowClass(QtGui.QMainWindow, form_class):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)

        self.emplenarColor()
        self.redDisplay.setText(str(self.redSlider.value()))
        self.greenDisplay.setText(str(self.greenSlider.value()))
        self.blueDisplay.setText(str(self.blueSlider.value()))
        QtCore.QObject.connect(self.redSlider, QtCore.SIGNAL("valueChanged(int)"), self.emplenarColor)
        QtCore.QObject.connect(self.greenSlider, QtCore.SIGNAL("valueChanged(int)"), self.emplenarColor)
        QtCore.QObject.connect(self.blueSlider, QtCore.SIGNAL("valueChanged(int)"), self.emplenarColor)
        QtCore.QObject.connect(self.paletaButton, QtCore.SIGNAL("clicked()"), self.mostrarPaleta)



    def emplenarColor(self):
        ''' Es crea un objecte de la classe QColor al qual es passa els colors
        vermell, verd i blau obtinguts dels QSlider respectius '''
        col = QtGui.QColor(self.redSlider.value(), self.greenSlider.value(), self.blueSlider.value())
        self.colorPreview.setStyleSheet('background-color: %s; border-radius: 4px;' % col.name())
        self. colorHex.setText(str(col.name().toUpper()))

    def mostrarPaleta(self):
        col = QtGui.QColor(self.redSlider.value(), self.greenSlider.value(), self.blueSlider.value())
        col = QtGui.QColorDialog().getColor(col)
        if col.isValid():
            self.colorPreview.setStyleSheet('background-color: %s; border-radius: 4px;' % col.name())
            self.redSlider.setValue(col.red())
            self.greenSlider.setValue(col.green())
            self.blueSlider.setValue(col.blue())
            self. colorHex.setText(str(col.name().toUpper()))
            self.statusbar.showMessage('Color recuperat de la paleta de colors...', 3000)


app = QtGui.QApplication(sys.argv)
myWindow = MyWindowClass(None)
myWindow.show()
app.exec_()
