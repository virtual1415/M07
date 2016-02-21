# Patricio Vidal
# -*- coding: utf-8 -*-

from PyQt4 import QtGui
from palancaController import Palanca

import sys


def main():
    app = QtGui.QApplication(sys.argv)
    form = Palanca()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()