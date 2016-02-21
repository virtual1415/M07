#-*- coding: utf-8 -*-

import sys, os
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from control_v_inici import Control_V_I

class MainC (object):
    def __init__(self):
        # Crea objecte finestra principal
        cp = Control_V_I()
        cp.exec_()
        # En tancar la finestra principal surt de l'aplicació
        sys.exit(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mc = MainC()
    sys.exit(app.exec_())
