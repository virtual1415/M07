# Patricio Vidal
# -*- coding: utf-8 -*-

from PyQt4 import QtGui
from reportlab.pdfgen import canvas
import fitxa


class Fitxa(QtGui.QDialog, fitxa.Ui_Fitxa):

    def __init__(self, nom, cognoms, correu, parent=None):
        super(self.__class__, self).__init__(parent)
        self.setupUi(self)
        self.nomField.setText(nom)
        self.cognomsField.setText(cognoms)
        self.correuField.setText(correu)
        self.pdfButton.clicked.connect(self.generarPDF)
        self.tancarButton.clicked.connect(self.tancar)

    def generarPDF(self):
        path = unicode(QtGui.QFileDialog.getSaveFileName(self, "Save file", ("%s.pdf" % self.nomField.text()), ".pdf"))
        if path != '':
            c = canvas.Canvas(path)
            c.drawString(100, 750, "Aquest arxiu fou generat per formulari pyqt")
            c.drawString(100, 700, ("Nom: %s" % unicode(self.nomField.text())))
            c.drawString(100, 680, ("Cognoms: %s" % unicode(self.cognomsField.text())))
            c.drawString(100, 660, ("Correu electrònic: %s" % str(self.correuField.text())))
            c.save()
            QtGui.QMessageBox.information(self, "Correcte", "S'ha generat un fitxer a:\n %s" % path)

    def tancar(self):
        self.close()
