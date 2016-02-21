# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'missatge.ui'
#
# Created: Mon Dec 21 18:06:57 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Missatge(object):
    def setupUi(self, Missatge):
        Missatge.setObjectName(_fromUtf8("Missatge"))
        Missatge.resize(208, 64)
        Missatge.setMinimumSize(QtCore.QSize(208, 64))
        Missatge.setMaximumSize(QtCore.QSize(208, 64))
        self.centralwidget = QtGui.QWidget(Missatge)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 182, 32))
        self.label.setMinimumSize(QtCore.QSize(182, 32))
        self.label.setMaximumSize(QtCore.QSize(182, 32))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        Missatge.setCentralWidget(self.centralwidget)

        self.retranslateUi(Missatge)
        QtCore.QMetaObject.connectSlotsByName(Missatge)

    def retranslateUi(self, Missatge):
        Missatge.setWindowTitle(_translate("Missatge", "Esperi...", None))
        self.label.setText(_translate("Missatge", "Generant sudoku!", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Missatge = QtGui.QMainWindow()
    ui = Ui_Missatge()
    ui.setupUi(Missatge)
    Missatge.show()
    sys.exit(app.exec_())

