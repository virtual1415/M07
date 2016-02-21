# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fitxa.ui'
#
# Created: Sat Jan 30 19:06:20 2016
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

class Ui_Fitxa(object):
    def setupUi(self, Fitxa):
        Fitxa.setObjectName(_fromUtf8("Fitxa"))
        Fitxa.resize(412, 177)
        Fitxa.setMinimumSize(QtCore.QSize(412, 177))
        Fitxa.setMaximumSize(QtCore.QSize(412, 177))
        self.gridLayoutWidget = QtGui.QWidget(Fitxa)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 391, 101))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.nomTitle = QtGui.QLabel(self.gridLayoutWidget)
        self.nomTitle.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nomTitle.setFont(font)
        self.nomTitle.setObjectName(_fromUtf8("nomTitle"))
        self.gridLayout.addWidget(self.nomTitle, 0, 0, 1, 1)
        self.cognomsTitle = QtGui.QLabel(self.gridLayoutWidget)
        self.cognomsTitle.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cognomsTitle.setFont(font)
        self.cognomsTitle.setObjectName(_fromUtf8("cognomsTitle"))
        self.gridLayout.addWidget(self.cognomsTitle, 1, 0, 1, 1)
        self.cognomsField = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cognomsField.setFont(font)
        self.cognomsField.setStyleSheet(_fromUtf8("color: rgb(0, 85, 255);"))
        self.cognomsField.setText(_fromUtf8(""))
        self.cognomsField.setObjectName(_fromUtf8("cognomsField"))
        self.gridLayout.addWidget(self.cognomsField, 1, 1, 1, 1)
        self.nomField = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nomField.setFont(font)
        self.nomField.setStyleSheet(_fromUtf8("color: rgb(0, 85, 255);"))
        self.nomField.setText(_fromUtf8(""))
        self.nomField.setObjectName(_fromUtf8("nomField"))
        self.gridLayout.addWidget(self.nomField, 0, 1, 1, 1)
        self.correuLabel = QtGui.QLabel(self.gridLayoutWidget)
        self.correuLabel.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.correuLabel.setFont(font)
        self.correuLabel.setObjectName(_fromUtf8("correuLabel"))
        self.gridLayout.addWidget(self.correuLabel, 2, 0, 1, 1)
        self.correuField = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.correuField.setFont(font)
        self.correuField.setStyleSheet(_fromUtf8("color: rgb(0, 85, 255);"))
        self.correuField.setText(_fromUtf8(""))
        self.correuField.setObjectName(_fromUtf8("correuField"))
        self.gridLayout.addWidget(self.correuField, 2, 1, 1, 1)
        self.tancarButton = QtGui.QPushButton(Fitxa)
        self.tancarButton.setGeometry(QtCore.QRect(310, 130, 90, 27))
        self.tancarButton.setMinimumSize(QtCore.QSize(90, 27))
        self.tancarButton.setMaximumSize(QtCore.QSize(90, 27))
        self.tancarButton.setObjectName(_fromUtf8("tancarButton"))
        self.pdfButton = QtGui.QPushButton(Fitxa)
        self.pdfButton.setGeometry(QtCore.QRect(10, 130, 90, 27))
        self.pdfButton.setMinimumSize(QtCore.QSize(90, 27))
        self.pdfButton.setMaximumSize(QtCore.QSize(90, 27))
        self.pdfButton.setObjectName(_fromUtf8("pdfButton"))

        self.retranslateUi(Fitxa)
        QtCore.QMetaObject.connectSlotsByName(Fitxa)

    def retranslateUi(self, Fitxa):
        Fitxa.setWindowTitle(_translate("Fitxa", "Fitxa de contacte", None))
        self.nomTitle.setText(_translate("Fitxa", "Nom", None))
        self.cognomsTitle.setText(_translate("Fitxa", "Cognoms", None))
        self.correuLabel.setText(_translate("Fitxa", "Correu electrònic", None))
        self.tancarButton.setText(_translate("Fitxa", "&Tancar", None))
        self.tancarButton.setShortcut(_translate("Fitxa", "Ctrl+T", None))
        self.pdfButton.setText(_translate("Fitxa", "&PDF", None))
        self.pdfButton.setShortcut(_translate("Fitxa", "Ctrl+P", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Fitxa = QtGui.QDialog()
    ui = Ui_Fitxa()
    ui.setupUi(Fitxa)
    Fitxa.show()
    sys.exit(app.exec_())

