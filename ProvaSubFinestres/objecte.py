#-*- coding: utf-8 -*-

class Dades:

    def __init__(self):
        __dato1 = ''
        __dato2 = ''
    def addDades(self, d1, d2):
        self.__dato1 = d1
        self.__dato2 = d2

    def mostraDades(self):
        print self.__dato1
        print self.__dato2
