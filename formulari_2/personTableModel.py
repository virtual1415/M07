# Patricio Vidal
# -*- coding: utf-8 -*-

from PyQt4.QtCore import *


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
