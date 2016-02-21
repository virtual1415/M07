# Patricio Vidal
# -*- coding: utf-8 -*-

from persona import Persona
from dbconnexio import DBConnexio
from PyQt4 import QtGui
import sqlite3


class PersonaModel:

    def __init__(self):
        self.db = DBConnexio()

    def create_table(self):
        connexio = self.db.getConnexio()
        cursor = connexio.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS contactes(nom TEXT NOT NULL, cognoms TEXT NOT NULL, correu TEXT NOT NULL UNIQUE)')
        connexio.commit()
        cursor.close()
        self.db.closeConnexio()

    def get_all_persons(self):
        connexio = self.db.getConnexio()
        cursor = connexio.cursor()
        cursor.execute('SELECT * FROM contactes ORDER BY nom')
        resultat = cursor.fetchall()
        persones = []
        if len(resultat) > 0:
            for item in resultat:
                persones.append(Persona(item[0], item[1], item[2]))
        cursor.close()
        self.db.closeConnexio()
        return persones

    def get_by_first_name(self, nom):
        connexio = self.db.getConnexio()
        cursor = connexio.cursor()
        sql = 'SELECT * FROM contactes WHERE nom LIKE "%s%%" ORDER BY nom' % nom
        cursor.execute(sql)
        resultat = cursor.fetchall()
        persones = []
        if len(resultat) > 0:
            for item in resultat:
                persones.append(Persona(item[0], item[1], item[2]))
        cursor.close()
        self.db.closeConnexio()
        return persones

    def get_by_last_name(self, cognoms):
        connexio = self.db.getConnexio()
        cursor = connexio.cursor()
        sql = 'SELECT * FROM contactes WHERE cognoms LIKE "%s%%" ORDER BY nom' % cognoms
        cursor.execute(sql)
        resultat = cursor.fetchall()
        persones = []
        if len(resultat) > 0:
            for item in resultat:
                persones.append(Persona(item[0], item[1], item[2]))
        cursor.close()
        self.db.closeConnexio()
        return persones

    def get_by_email(self,correu):
        connexio = self.db.getConnexio()
        cursor = connexio.cursor()
        sql = 'SELECT * FROM contactes WHERE cognoms LIKE "%s%%" ORDER BY nom' % correu
        cursor.execute(sql)
        resultat = cursor.fetchall()
        persones = []
        if len(resultat) > 0:
            for item in resultat:
                persones.append(Persona(item[0], item[1], item[2]))
        cursor.close()
        self.db.closeConnexio()
        return persones

    def insert_person(self, nom, cognoms, correu):
        insersio = True
        connexio = self.db.getConnexio()
        cursor = connexio.cursor()
        try:
            cursor.execute('INSERT INTO contactes (nom,cognoms,correu) VALUES (?,?,?)', (nom, cognoms, correu))
            connexio.commit()
        except sqlite3.IntegrityError:
            insersio = False
        else:
            cursor.close()
            self.db.closeConnexio()
        return insersio

    def update_person(self, nom, cognoms, correu, temp_correu):
        actualitzacio = True
        connexio = self.db.getConnexio()
        cursor = connexio.cursor()
        sql = 'UPDATE contactes SET nom = "%s", cognoms = "%s", correu = "%s" WHERE correu = "%s"' % (nom, cognoms, correu, temp_correu)
        try:
            cursor.execute(sql)
            connexio.commit()
        except sqlite3.IntegrityError:
            actualitzacio = False
        else:
            cursor.close()
            self.db.closeConnexio()
        return actualitzacio

    def delete_person(self, cognom):
        connexio = self.db.getConnexio()
        cursor = connexio.cursor()
        sql = 'DELETE FROM contactes WHERE correu = "%s"' % cognom
        cursor.execute(sql)
        connexio.commit()
        cursor.close()
        self.db.closeConnexio()
