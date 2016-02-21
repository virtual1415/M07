# Patricio Vidal
# -*- coding: utf-8 -*-

from PyQt4 import QtGui
from formulariController import Formulari

import sys


def main():
    app = QtGui.QApplication(sys.argv)
    form = Formulari()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
