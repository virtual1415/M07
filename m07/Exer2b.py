# Patricio Vidal
# -*- coding: utf-8 -*-
from convertidors import *

num = -1
esnum = False
while num < 0 or esnum != True:
    try:
        num = int(raw_input("Introdueix un numero positiu: "))
        if num < 0:
            print "El", num ,"es no es un numero positiu."
        esnum = True
    except:
        print "Has d'introduir un numero i ha de ser positiu"
        esnum = False
print "El valor de", num ,"en binari es " + binari(num)
print "El valor de", num ,"en Hexadecimal es " + hexadecimal(num)
print "El programa ha finalitzat correctament."