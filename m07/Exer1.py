# Patricio Vidal
# -*- coding: utf-8 -*-
def binari(num):
    numBin = ""
    while num >= 2:
        resDiv = num % 2
        num = num / 2
        if num < 2:
            numBin = str(num)+str(resDiv)+numBin
        else:
            numBin = str(resDiv)+numBin
    return numBin

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
print "El valor de", num, "en binari es " + binari(num)
print "El programa ha finalitzat correctament."