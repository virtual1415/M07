# Patricio Vidal
# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
import re
import sys
import formulari
import sqlite3


class Persona(object):
    def __init__(self, nom, cognoms, correu):
        self.nom = nom
        self.cognoms = cognoms
        self.correu = correu


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
        QtCore.QObject.connect(self.tabWidget, QtCore.SIGNAL("currentChanged(int)"), self.emplenar)

    def inicialitzacio(self):
        connexio = sqlite3.connect('contactes.db')
        cursor = connexio.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS contactes(nom TEXT NOT NULL, cognoms TEXT NOT NULL, correu TEXT NOT NULL UNIQUE)')
        connexio.commit()
        cursor.close()
        connexio.close()

    def buidar(self):
        self.nom.setText('')
        self.cognoms.setText('')
        self.correu.setText('')
        self.tempItem = None
        self.insertar = True

    def inserir(self):
        nom = unicode(self.nom.text())
        cognoms = unicode(self.cognoms.text())
        correu = unicode(self.correu.text())
        if nom == '' or cognoms == '' or correu == '':
            QtGui.QMessageBox.warning(None, "Atencio", "Tots els camps son obligatoris")
        else:
            # patro = re.compile('\w+[.|\w]\w+@\w+[.]\w+[.|\w+]\w+')
            patro = re.compile('^[a-zA-Z0-9_\-\.~]{2,}@[a-zA-Z0-9_\-\.~]{2,}\.[a-zA-Z]{2,4}$')
            if not patro.match(correu):
                QtGui.QMessageBox.warning(None, "Atencio", "El format del correu electronic no es correcte")
            else:
                connexio = sqlite3.connect('contactes.db')
                cursor = connexio.cursor()
                try:
                    if self.insertar:
                        cursor.execute('INSERT INTO contactes (nom,cognoms,correu) VALUES (?,?,?)', (nom, cognoms, correu))
                        connexio.commit()
                        QtGui.QMessageBox.information(None, "Correcte", "El contacte s'ha afegit correctament a la base de dades")
                    else:
                        sql = 'UPDATE contactes SET nom = "%s", cognoms = "%s", correu = "%s" WHERE correu = "%s"' % (nom, cognoms, correu, self.tempItem)
                        cursor.execute(sql)
                        connexio.commit()
                        self.tempItem = None
                        self.insertar = True
                        QtGui.QMessageBox.information(None, "Correcte", "El contacte s'ha actualitzat correctament")
                        self.tabWidget.setCurrentIndex(1)
                        self.emplenar()
                except sqlite3.IntegrityError:
                    QtGui.QMessageBox.warning(None, "Atencio", "Ja existeix un contacte amb aquest correu")
                else:
                    self.nom.setText('')
                    self.cognoms.setText('')
                    self.correu.setText('')
                    cursor.close()
                    connexio.close()

    def emplenar(self):
        self.tableData = PersonTableModel()
        self.tableLectura.setModel(self.tableData)
        connexio = sqlite3.connect('contactes.db')
        cursor = connexio.cursor()
        cursor.execute('SELECT * FROM contactes ORDER BY nom')
        resultat = cursor.fetchall()
        if len(resultat) == 0 and self.tabWidget.currentIndex() == 1:
            QtGui.QMessageBox.information(None, "Informacio", "La base de dades esta buida")
        else:
            for item in resultat:
                self.tableData.addPersona(Persona(item[0], item[1], item[2]))
        cursor.close()
        connexio.close()

    def esborrar(self):
        indexes = self.tableLectura.selectionModel().selectedRows()
        if len(indexes) > 0:
            resposta = QtGui.QMessageBox.question(None, "Atencio", "Segur que vols continuar amb l'operacio d'esborrat?", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
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
            QtGui.QMessageBox.warning(None, "Atencio", "Has de selecionar una entrada")


class PersonTableModel(QAbstractTableModel):
    def __init__(self):
        super(PersonTableModel, self).__init__()
        self.headers = ['Nom', 'Cognoms', 'Correu electronic']
        self.persones = []

    def rowCount(self, index=QModelIndex()):
        return len(self.persones)

    def addPersona(self, persona):
        self.beginResetModel()
        self.persones.append(persona)
        self.endResetModel()

    def columnCount(self, index=QModelIndex()):
        return len(self.headers)

    def data(self, index, role=Qt.DisplayRole):
        col = index.column()
        persona = self.persones[index.row()]
        if role == Qt.DisplayRole:
            if col == 0:
                return QVariant(persona.nom)
            elif col == 1:
                return QVariant(persona.cognoms)
            elif col == 2:
                return QVariant(persona.correu)
            return QVariant()

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role != Qt.DisplayRole:
            return QVariant()
        if orientation == Qt.Horizontal:
            return QVariant(self.headers[section])
        return QVariant(int(section + 1))


def main():
    app = QtGui.QApplication(sys.argv)
    form = Formulari()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
