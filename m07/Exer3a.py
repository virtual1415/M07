# Patricio Vidal
# -*- coding: utf-8 -*-
num = 0
esnum = False
while num < 1 or num > 100 or esnum != True:
    try:
        num = int(raw_input("Introdueix un numero entre 1 i 100: "))
        if num < 1 or num > 100:
            print "El", num ,"es troba fora del rang demanat."
        esnum = True
    except:
        print "Has d'introduir un numero"
        esnum = False
if num < 2:
    print "El", num ,"no es un numero primer."
else:
    primer = True
    i = 2
    while i < num and primer:
        if num % i == 0:
            primer = False
        i += 1
    if primer == False:
        print "El", num ,"no es un numero primer."
    else:
        print "El", num ,"es un numero primer."
print "El programa ha finalitzat correctament."
