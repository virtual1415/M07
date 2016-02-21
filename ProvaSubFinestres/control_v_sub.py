#-*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from vista_sub import Ui_Dialog
from objecte import Dades

class Control_V_S(QDialog, Ui_Dialog):

    def __init__(self, valor, parent = None):
        super(Control_V_S, self).__init__(parent)
        self.setupUi(self)
        self.lineEdit.setText(valor)

    def tancar(self):
        self.close()

    def getValors(self):
        valors = Dades()
        v1 = self.lineEdit.text()
        v2 = self.lineEdit_2.text()
        valors.addDades(v1, v2)
        return valors
