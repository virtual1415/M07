# Patricio Vidal
# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from fitxaController import Fitxa
from persona import Persona
from personTableModel import PersonTableModel
import re
import formulari
import sqlite3


class Formulari(QtGui.QMainWindow, formulari.Ui_MainWindow):

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.insertar = True
        self.inicialitzacio()
        self.tempItem = None
        self.buttonInsertar.clicked.connect(self.inserir)
        self.buttonReset.clicked.connect(self.buidar)
        self.buttonEsborrar.clicked.connect(self.esborrar)
        self.buttonModificar.clicked.connect(self.modificar)
        self.buttonFitxa.clicked.connect(self.mostrar)
        self.buttonNeteja1.clicked.connect(self.netejar)
        self.buttonNeteja2.clicked.connect(self.netejar)
        self.buttonNeteja3.clicked.connect(self.netejar)
        QtCore.QObject.connect(self.tabWidget, QtCore.SIGNAL("currentChanged(int)"), self.emplenar)
        QtCore.QObject.connect(self.filtre1, QtCore.SIGNAL("returnPressed()"), lambda: self.filtrar(1))
        QtCore.QObject.connect(self.filtre2, QtCore.SIGNAL("returnPressed()"), lambda: self.filtrar(2))
        QtCore.QObject.connect(self.filtre3, QtCore.SIGNAL("returnPressed()"), lambda: self.filtrar(3))

    def inicialitzacio(self):
        connexio = sqlite3.connect('contactes.db')
        cursor = connexio.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS contactes(nom TEXT NOT NULL, cognoms TEXT NOT NULL, correu TEXT NOT NULL UNIQUE)')
        connexio.commit()
        cursor.close()
        connexio.close()

    def buidar(self):
        self.nom.clear()
        self.cognoms.clear()
        self.correu.clear()
        self.tempItem = None
        self.insertar = True

    def netejar(self):
        self.filtre1.clear()
        self.filtre2.clear()
        self.filtre3.clear()
        self.emplenar()

    def inserir(self):
        nom = unicode(self.nom.text())
        cognoms = unicode(self.cognoms.text())
        correu = unicode(self.correu.text())
        if nom == '' or cognoms == '' or correu == '':
            QtGui.QMessageBox.warning(self, "Atencio", "Tots els camps amb asterisc son obligatoris")
        else:
            # patro = re.compile('\w+[.|\w]\w+@\w+[.]\w+[.|\w+]\w+')
            patro = re.compile('^[a-zA-Z0-9_\-\.~]{2,}@[a-zA-Z0-9_\-\.~]{2,}\.[a-zA-Z]{2,4}$')
            if not patro.match(correu):
                QtGui.QMessageBox.warning(self, "Atencio", "El format del correu electronic no es correcte")
            else:
                connexio = sqlite3.connect('contactes.db')
                cursor = connexio.cursor()
                try:
                    if self.insertar:
                        cursor.execute('INSERT INTO contactes (nom,cognoms,correu) VALUES (?,?,?)', (nom, cognoms, correu))
                        connexio.commit()
                        QtGui.QMessageBox.information(self, "Correcte", "El contacte s'ha afegit correctament a la base de dades")
                    else:
                        sql = 'UPDATE contactes SET nom = "%s", cognoms = "%s", correu = "%s" WHERE correu = "%s"' % (nom, cognoms, correu, self.tempItem)
                        cursor.execute(sql)
                        connexio.commit()
                        self.tempItem = None
                        self.insertar = True
                        QtGui.QMessageBox.information(self, "Correcte", "El contacte s'ha actualitzat correctament")
                        self.tabWidget.setCurrentIndex(1)
                        self.emplenar()
                except sqlite3.IntegrityError:
                    QtGui.QMessageBox.warning(self, "Atencio", "Ja existeix un contacte amb aquest correu")
                else:
                    self.nom.clear()
                    self.cognoms.clear()
                    self.correu.clear()
                    cursor.close()
                    connexio.close()

    def emplenar(self):
        self.filtre1.clear()
        self.filtre2.clear()
        self.filtre3.clear()
        self.tableData = PersonTableModel()
        self.tableLectura.setModel(self.tableData)
        self.tableLectura.setColumnWidth(0, 135)
        self.tableLectura.setColumnWidth(1, 205)
        self.tableLectura.setColumnWidth(2, 174)
        connexio = sqlite3.connect('contactes.db')
        cursor = connexio.cursor()
        cursor.execute('SELECT * FROM contactes ORDER BY nom')
        resultat = cursor.fetchall()
        if len(resultat) == 0 and self.tabWidget.currentIndex() == 1:
            QtGui.QMessageBox.information(self, "Informacio", "La base de dades esta buida")
        else:
            for item in resultat:
                self.tableData.addPersona(Persona(item[0], item[1], item[2]))
        cursor.close()
        connexio.close()

    def esborrar(self):
        indexes = self.tableLectura.selectionModel().selectedRows()
        if len(indexes) > 0:
            resposta = QtGui.QMessageBox.question(self, "Atencio", "Segur que vols continuar amb l'operacio d'esborrat?", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
            if resposta == QtGui.QMessageBox.Yes:
                connexio = sqlite3.connect('contactes.db')
                cursor = connexio.cursor()
                for index in sorted(indexes):
                    # print('Fila %d seleccionada' % index.row())
                    item = self.tableData.index(index.row(), 2)
                    # print(self.tableData.data(item).toString())
                    sql = 'DELETE FROM contactes WHERE correu = "%s"' % unicode(self.tableData.data(item).toString())
                    cursor.execute(sql)
                    connexio.commit()
                cursor.close()
                connexio.close()
                self.emplenar()

    def modificar(self):
        indexes = self.tableLectura.selectionModel().selectedRows()
        if len(indexes) == 1:
            self.nom.setText(self.tableData.data(self.tableData.index(indexes[0].row(), 0)).toString())
            self.cognoms.setText(self.tableData.data(self.tableData.index(indexes[0].row(), 1)).toString())
            self.correu.setText(self.tableData.data(self.tableData.index(indexes[0].row(), 2)).toString())
            self.tempItem = self.correu.text()
            self.tabWidget.setCurrentIndex(0)
            self.insertar = False
        else:
            QtGui.QMessageBox.warning(self, "Atencio", "Has de selecionar una entrada")

    def mostrar(self):
        indexes = self.tableLectura.selectionModel().selectedRows()
        if len(indexes) == 1:
            nom = self.tableData.data(self.tableData.index(indexes[0].row(), 0)).toString()
            cognoms = self.tableData.data(self.tableData.index(indexes[0].row(), 1)).toString()
            correu = self.tableData.data(self.tableData.index(indexes[0].row(), 2)).toString()
            fitxa = Fitxa(nom, cognoms, correu, self)
            fitxa.exec_()
        else:
            QtGui.QMessageBox.warning(self, "Atencio", "Has de selecionar una entrada")

    def filtrar(self, valor):
        if valor == 1:
            self.filtre2.clear()
            self.filtre3.clear()
            filtre1 = unicode(self.filtre1.text())
            sql = 'SELECT * FROM contactes WHERE nom LIKE "%s%%" ORDER BY nom' % filtre1
        elif valor == 2:
            self.filtre1.clear()
            self.filtre3.clear()
            filtre2 = unicode(self.filtre2.text())
            sql = 'SELECT * FROM contactes WHERE cognoms LIKE "%s%%" ORDER BY nom' % filtre2
        else:
            self.filtre1.clear()
            self.filtre2.clear()
            filtre3 = unicode(self.filtre3.text())
            sql = 'SELECT * FROM contactes WHERE cognoms LIKE "%s%%" ORDER BY nom' % filtre3
        self.tableData = PersonTableModel()
        self.tableLectura.setModel(self.tableData)
        connexio = sqlite3.connect('contactes.db')
        cursor = connexio.cursor()
        cursor.execute(sql)
        resultat = cursor.fetchall()
        if len(resultat) == 0:
            QtGui.QMessageBox.information(self, "Informacio", "No hi ha coincidencies amb el filtre")
        else:
            for item in resultat:
                self.tableData.addPersona(Persona(item[0], item[1], item[2]))
        cursor.close()
        connexio.close()
