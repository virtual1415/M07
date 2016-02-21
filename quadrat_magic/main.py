# -*- coding: utf-8 -*-
# author: Patricio Vidal

import sys
import quadrat_magic
from PyQt4 import QtGui


class Joc(QtGui.QMainWindow, quadrat_magic.Ui_MainWindow):

    # Es definexen els diferents estils que podran emprar tant els missatges com el tauler de joc
    CSS1 = 'color: green'
    CSS2 = 'color: red'

    # Es defineixen constants per als missatges que mostrara l'aplicacio
    CORRECTE = "ENHORABONA!"
    INCORRECTE = "INCORRECTE."
    MISSATGE_1 = " Hi ha valors repetits."
    MISSATGE_2 = " Nomes son valids els valors numerics del 1 al 9."
    MISSATGE_3 = " Torna-ho a intentar."
    MISSATGE_4 = " Hi ha caselles en blanc."

    # Es defineix la mida del quadrat magic, el resultat i els valors valids
    MIDA_QUADRAT = 3
    # SUMA_RESULTAT = 15
    VALORS_VALIDS = (1, 2, 3, 4, 5, 6, 7, 8, 9)

    def __init__(self, parent=None):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.quadrat_magic = []
        self.limitar()
        self.calcula.clicked.connect(self.validar)
        self.reset.clicked.connect(self.esborrar)

    def limitar(self):
        for i in range(self.MIDA_QUADRAT):
            for j in range(self.MIDA_QUADRAT):
                nom = 'cel_' + str(i) + '_' + str(j)
                obj_qlineedit = self.findChild(QtGui.QLineEdit, nom)
                obj_qlineedit.setValidator(QtGui.QIntValidator(min(self.VALORS_VALIDS), max(self.VALORS_VALIDS), self))

    def esborrar(self):
        self.quadrat_magic = []
        self.missatges.setStyleSheet('')
        self.missatges.setText('')
        for i in range(self.MIDA_QUADRAT):
            for j in range(self.MIDA_QUADRAT):
                nom = 'cel_' + str(i) + '_' + str(j)
                obj_qlineedit = self.findChild(QtGui.QLineEdit, nom)
                obj_qlineedit.setText('')
                obj_qlineedit.setStyleSheet('')
            nom = 'cel_' + str(i) + '_' + str(j + 1)
            obj_qlabel = self.findChild(QtGui.QLabel, nom)
            obj_qlabel.setText('')
            nom = 'cel_' + str(j + 1) + '_' + str(i)
            obj_qlabel = self.findChild(QtGui.QLabel, nom)
            obj_qlabel.setText('')
            self.D1.setText('')
            self.D2.setText('')

    def recollir_proposta(self):
        self.quadrat_magic = []
        self.missatges.setStyleSheet('')
        self.missatges.setText('')
        for i in range(self.MIDA_QUADRAT):
            self.quadrat_magic.append([])
            for j in range(self.MIDA_QUADRAT):
                nom = 'cel_' + str(i) + '_' + str(j)
                obj_qlineedit = self.findChild(QtGui.QLineEdit, nom)
                obj_qlineedit.setStyleSheet('')
                if obj_qlineedit.text() == '':
                    self.missatges.setStyleSheet(self.CSS2)
                    self.missatges.setText(self.INCORRECTE + self.MISSATGE_4)
                    return False
                elif int(obj_qlineedit.text()) not in self.VALORS_VALIDS:
                    obj_qlineedit.setStyleSheet(self.CSS2)
                    self.missatges.setStyleSheet(self.CSS2)
                    self.missatges.setText(self.INCORRECTE + self.MISSATGE_2)
                    return False
                else:
                    self.quadrat_magic[i].append(int(obj_qlineedit.text()))
        return True

    def validar(self):
        if self.recollir_proposta():
            correcte = True
            suma_diagonal_1 = 0
            suma_diagonal_2 = 0
            resultats = []
            for i in range(self.MIDA_QUADRAT):
                suma_fila = 0
                suma_columna = 0
                suma_diagonal_1 += self.quadrat_magic[i][i]
                suma_diagonal_2 += self.quadrat_magic[i][(self.MIDA_QUADRAT - 1) - i]
                for j in range(self.MIDA_QUADRAT):
                    suma_fila += self.quadrat_magic[i][j]
                    suma_columna += self.quadrat_magic[j][i]
                nom = 'cel_' + str(i) + '_' + str(j + 1)
                obj_qlabel = self.findChild(QtGui.QLabel, nom)
                obj_qlabel.setText(str(suma_fila))
                nom = 'cel_' + str(j + 1) + '_' + str(i)
                obj_qlabel = self.findChild(QtGui.QLabel, nom)
                obj_qlabel.setText(str(suma_columna))
                resultats.append(suma_fila)
                resultats.append(suma_columna)
                # if suma_fila != self.SUMA_RESULTAT or suma_columna != self.SUMA_RESULTAT:
                # if (suma_fila or suma_columna) != self.SUMA_RESULTAT:
                #     correcte = False
            self.D1.setText(str(suma_diagonal_1))
            resultats.append(suma_diagonal_1)
            self.D2.setText(str(suma_diagonal_2))
            resultats.append(suma_diagonal_2)
            if resultats[1:] != resultats[:-1]:
                correcte = False
            if correcte:
                self.missatges.setStyleSheet(self.CSS1)
                self.missatges.setText(self.CORRECTE)
            else:
                self.duplicats_fila()
                self.duplicats_columna()
                self.duplicats_diagonal_principal()
                self.duplicats_diagonal_secundaria()

    # Funcio que recorre les files de la solució proposada pel jugador
    # i comprova si hi ha duplicats.
    def duplicats_fila(self):
        for i in range(self.MIDA_QUADRAT):
            for j in range(self.MIDA_QUADRAT - 1):
                nom1 = 'cel_' + str(i) + '_' + str(j)
                obj_qlineedit1 = self.findChild(QtGui.QLineEdit, nom1)
                for k in range(j + 1, self.MIDA_QUADRAT):
                    nom2 = 'cel_' + str(i) + '_' + str(k)
                    obj_qlineedit2 = self.findChild(QtGui.QLineEdit, nom2)
                    if obj_qlineedit1.text() == obj_qlineedit2.text():
                        obj_qlineedit1.setStyleSheet(self.CSS2)
                        obj_qlineedit2.setStyleSheet(self.CSS2)
                        self.missatges.setStyleSheet(self.CSS2)
                        self.missatges.setText(self.INCORRECTE + self.MISSATGE_1 + '\n' + self.MISSATGE_3)

    # Funcio que recorre les columnes de la solució proposada pel jugador
    # i comprova si hi ha duplicats.
    def duplicats_columna(self):
        for i in range(self.MIDA_QUADRAT):
            for j in range(self.MIDA_QUADRAT - 1):
                nom1 = 'cel_' + str(j) + '_' + str(i)
                obj_qlineedit1 = self.findChild(QtGui.QLineEdit, nom1)
                for k in range(j + 1, self.MIDA_QUADRAT):
                    nom2 = 'cel_' + str(k) + '_' + str(i)
                    obj_qlineedit2 = self.findChild(QtGui.QLineEdit, nom2)
                    if obj_qlineedit1.text() == obj_qlineedit2.text():
                        obj_qlineedit1.setStyleSheet(self.CSS2)
                        obj_qlineedit2.setStyleSheet(self.CSS2)
                        self.missatges.setStyleSheet(self.CSS2)
                        self.missatges.setText(self.INCORRECTE + self.MISSATGE_1 + '\n' + self.MISSATGE_3)

    def duplicats_diagonal_principal(self):
        for i in range(self.MIDA_QUADRAT - 1):
            for j in range(i + 1, self.MIDA_QUADRAT):
                nom1 = 'cel_' + str(i) + '_' + str(i)
                obj_qlineedit1 = self.findChild(QtGui.QLineEdit, nom1)
                nom2 = 'cel_' + str(j) + '_' + str(j)
                obj_qlineedit2 = self.findChild(QtGui.QLineEdit, nom2)
                if obj_qlineedit1.text() == obj_qlineedit2.text():
                    obj_qlineedit1.setStyleSheet(self.CSS2)
                    obj_qlineedit2.setStyleSheet(self.CSS2)
                    self.missatges.setStyleSheet(self.CSS2)
                    self.missatges.setText(self.INCORRECTE + self.MISSATGE_1 + '\n' + self.MISSATGE_3)

    def duplicats_diagonal_secundaria(self):
        for i in range(self.MIDA_QUADRAT - 1):
            for j in range(i + 1, self.MIDA_QUADRAT):
                nom1 = 'cel_' + str(i) + '_' + str((self.MIDA_QUADRAT - 1) - i)
                obj_qlineedit1 = self.findChild(QtGui.QLineEdit, nom1)
                nom2 = 'cel_' + str(j) + '_' + str((self.MIDA_QUADRAT - 1) - j)
                obj_qlineedit2 = self.findChild(QtGui.QLineEdit, nom2)
                if obj_qlineedit1.text() == obj_qlineedit2.text():
                    obj_qlineedit1.setStyleSheet(self.CSS2)
                    obj_qlineedit2.setStyleSheet(self.CSS2)
                    self.missatges.setStyleSheet(self.CSS2)
                    self.missatges.setText(self.INCORRECTE + self.MISSATGE_1 + '\n' + self.MISSATGE_3)


def main():
    app = QtGui.QApplication(sys.argv)
    form = Joc()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
