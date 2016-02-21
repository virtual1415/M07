# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'formulari.ui'
#
# Created: Fri Jan 22 13:36:42 2016
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(600, 365)
        MainWindow.setMinimumSize(QtCore.QSize(600, 365))
        MainWindow.setMaximumSize(QtCore.QSize(600, 365))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 580, 301))
        self.tabWidget.setMinimumSize(QtCore.QSize(580, 271))
        self.tabWidget.setMaximumSize(QtCore.QSize(580, 371))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tabInsertar = QtGui.QWidget()
        self.tabInsertar.setObjectName(_fromUtf8("tabInsertar"))
        self.gridLayoutWidget = QtGui.QWidget(self.tabInsertar)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 50, 551, 92))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.labelCognoms = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelCognoms.setFont(font)
        self.labelCognoms.setObjectName(_fromUtf8("labelCognoms"))
        self.gridLayout.addWidget(self.labelCognoms, 1, 0, 1, 1)
        self.labelNom = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelNom.setFont(font)
        self.labelNom.setObjectName(_fromUtf8("labelNom"))
        self.gridLayout.addWidget(self.labelNom, 0, 0, 1, 1)
        self.labelCorreu = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelCorreu.setFont(font)
        self.labelCorreu.setObjectName(_fromUtf8("labelCorreu"))
        self.gridLayout.addWidget(self.labelCorreu, 2, 0, 1, 1)
        self.nom = QtGui.QLineEdit(self.gridLayoutWidget)
        self.nom.setToolTip(_fromUtf8(""))
        self.nom.setMaxLength(15)
        self.nom.setObjectName(_fromUtf8("nom"))
        self.gridLayout.addWidget(self.nom, 0, 1, 1, 1)
        self.cognoms = QtGui.QLineEdit(self.gridLayoutWidget)
        self.cognoms.setToolTip(_fromUtf8(""))
        self.cognoms.setMaxLength(50)
        self.cognoms.setObjectName(_fromUtf8("cognoms"))
        self.gridLayout.addWidget(self.cognoms, 1, 1, 1, 1)
        self.correu = QtGui.QLineEdit(self.gridLayoutWidget)
        self.correu.setToolTip(_fromUtf8(""))
        self.correu.setInputMethodHints(QtCore.Qt.ImhEmailCharactersOnly)
        self.correu.setMaxLength(20)
        self.correu.setObjectName(_fromUtf8("correu"))
        self.gridLayout.addWidget(self.correu, 2, 1, 1, 1)
        self.buttonInsertar = QtGui.QPushButton(self.tabInsertar)
        self.buttonInsertar.setGeometry(QtCore.QRect(180, 180, 90, 27))
        self.buttonInsertar.setMinimumSize(QtCore.QSize(90, 27))
        self.buttonInsertar.setMaximumSize(QtCore.QSize(90, 27))
        self.buttonInsertar.setObjectName(_fromUtf8("buttonInsertar"))
        self.buttonReset = QtGui.QPushButton(self.tabInsertar)
        self.buttonReset.setGeometry(QtCore.QRect(300, 180, 90, 27))
        self.buttonReset.setMinimumSize(QtCore.QSize(90, 27))
        self.buttonReset.setMaximumSize(QtCore.QSize(90, 27))
        self.buttonReset.setObjectName(_fromUtf8("buttonReset"))
        self.tabWidget.addTab(self.tabInsertar, _fromUtf8(""))
        self.tabLlegir = QtGui.QWidget()
        self.tabLlegir.setObjectName(_fromUtf8("tabLlegir"))
        self.tableLectura = QtGui.QTableView(self.tabLlegir)
        self.tableLectura.setGeometry(QtCore.QRect(15, 11, 550, 211))
        self.tableLectura.setMinimumSize(QtCore.QSize(550, 171))
        self.tableLectura.setMaximumSize(QtCore.QSize(521, 550))
        self.tableLectura.setObjectName(_fromUtf8("tableLectura"))
        self.tableLectura.horizontalHeader().setDefaultSectionSize(169)
        self.tableLectura.horizontalHeader().setMinimumSectionSize(169)
        self.tableLectura.verticalHeader().setDefaultSectionSize(25)
        self.tableLectura.verticalHeader().setMinimumSectionSize(25)
        self.buttonEsborrar = QtGui.QPushButton(self.tabLlegir)
        self.buttonEsborrar.setGeometry(QtCore.QRect(180, 230, 90, 27))
        self.buttonEsborrar.setMinimumSize(QtCore.QSize(90, 27))
        self.buttonEsborrar.setMaximumSize(QtCore.QSize(90, 27))
        self.buttonEsborrar.setObjectName(_fromUtf8("buttonEsborrar"))
        self.buttonModificar = QtGui.QPushButton(self.tabLlegir)
        self.buttonModificar.setGeometry(QtCore.QRect(300, 230, 90, 27))
        self.buttonModificar.setMinimumSize(QtCore.QSize(90, 27))
        self.buttonModificar.setMaximumSize(QtCore.QSize(90, 27))
        self.buttonModificar.setObjectName(_fromUtf8("buttonModificar"))
        self.tabWidget.addTab(self.tabLlegir, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 24))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Formulari", None))
        self.labelCognoms.setText(_translate("MainWindow", "Cognoms", None))
        self.labelNom.setText(_translate("MainWindow", "Nom", None))
        self.labelCorreu.setText(_translate("MainWindow", "Correu electrònic", None))
        self.nom.setPlaceholderText(_translate("MainWindow", "Introdueix el nom (màx. 15 caràcters)", None))
        self.cognoms.setPlaceholderText(_translate("MainWindow", "Introdueix els cognoms (màx. 50 caràcters)", None))
        self.correu.setPlaceholderText(_translate("MainWindow", "Introdueix el correu electrònic (màx. 20 caràcters)", None))
        self.buttonInsertar.setText(_translate("MainWindow", "&Desar", None))
        self.buttonInsertar.setShortcut(_translate("MainWindow", "Ctrl+D", None))
        self.buttonReset.setText(_translate("MainWindow", "&Buidar", None))
        self.buttonReset.setShortcut(_translate("MainWindow", "Ctrl+B", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabInsertar), _translate("MainWindow", "Desar", None))
        self.buttonEsborrar.setText(_translate("MainWindow", "&Esborrar", None))
        self.buttonEsborrar.setShortcut(_translate("MainWindow", "Ctrl+E", None))
        self.buttonModificar.setText(_translate("MainWindow", "&Modificar", None))
        self.buttonModificar.setShortcut(_translate("MainWindow", "Ctrl+M", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabLlegir), _translate("MainWindow", "Visualitzar", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

