# Patricio Vidal
# -*- coding: utf-8 -*-

import sqlite3


class DBConnexio:

    def __init__(self):
        self.__connexio = sqlite3.connect('contactes.db')

    def getConnexio(self):
        return self.__connexio

    def closeConnexio(self):
        self.__connexio.close()
