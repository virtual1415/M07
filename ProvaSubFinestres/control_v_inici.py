#-*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtCore, QtGui
from vista_inici import Ui_Dialog
from control_v_sub import Control_V_S
from objecte import Dades

class Control_V_I(QDialog, Ui_Dialog):
    def __init__(self, parent = None):
        super(Control_V_I, self).__init__(parent)
        self.setupUi(self)

    def tancar(self):
        self.close()

    def mostraSub(self):
        result = Dades()

        # Crea finestra de forma modal (self)
        cs = Control_V_S('T')
        cs.exec_()
        # imprimeix variable de la subfinestra
        result = cs.getValors()
        result.mostraDades()
