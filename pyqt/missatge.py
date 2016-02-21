# -*- coding: utf-8 -*-
# Patricio Vidal

import smtplib 
import sys
from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtCore import QObject
from PyQt4.QtGui import QAction

# Carrega interficie
form_class = uic.loadUiType("missatge.ui")[0]
 
class MyWindowClass(QtGui.QMainWindow, form_class):

    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.sortir_shortcut = QtGui.QShortcut(self)
        self.sortir_shortcut.setKey(QtCore.Qt.CTRL + QtCore.Qt.Key_S)
        self.sortir_shortcut.activated.connect(self.sortir)
        self.esborra_shortcut = QtGui.QShortcut(self)
        self.esborra_shortcut.setKey(QtCore.Qt.CTRL + QtCore.Qt.Key_E)
        self.esborra_shortcut.activated.connect(self.esborrar)
        self.envia_shortcut = QtGui.QShortcut(self)
        self.envia_shortcut.setKey(QtCore.Qt.CTRL + QtCore.Qt.Key_N)
        self.envia_shortcut.activated.connect(self.enviar)
        QtCore.QObject.connect(self.bEnviar, QtCore.SIGNAL("clicked()"), self.enviar)
        self.actionSortir.triggered.connect(self.sortir)
        self.actionEsborra.triggered.connect(self.esborrar)
        self.actionEnvia.triggered.connect(self.enviar)


    def sortir(self):
        app.quit()

    def esborrar(self):
        self.destinatari.clear()
        self.assumpte.clear()
        self.missatge.clear()

    def enviar(self):
        if self.destinatari.text() == "" or self.assumpte.text() == "" or self.missatge.toPlainText() == "":
            QtGui.QMessageBox.warning(None, "Atencio", "Has deixat algun camp del formulari buit.")
        else:
            self.correo
            self.statusbar.showMessage("Enviant...", 3000)
 
    def correo(self):
        remitent = "Exer8 <exer8@python.org>"
         
        email = """From: %s
        To: %s
        MIME-Version: 1.0
        Content-type: text/html
        Subject: %s
         
        %s
        """ % (remitent, self.destinatari, self.assumpte, self.missatge)
        try:
            smtp = smtplib.SMTP('localhost')
            smtp.sendmail(remitent, self.destinatari, email)
        except:
            self.statusbar.showMessage("El correu no s'ha pogut enviar", 4000)
 
app = QtGui.QApplication(sys.argv)
myWindow = MyWindowClass(None)
myWindow.show()
app.exec_()

