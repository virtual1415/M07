# Patricio Vidal
# -*- coding: utf-8 -*-
def hexadecimal(num):
    numHex = ""
    conv = { 0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
    if num > 15:
        while num >= 16:
            resDiv = num % 16
            num = num / 16
            if num < 16:
                numHex = conv[num]+conv[resDiv]+numHex
            else:
                numHex = conv[resDiv]+numHex
    else:
        numHex = conv[num]
    return numHex

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
print "El valor de", num ,"en Hexadecimal es " + hexadecimal(num)
print "El programa ha finalitzat correctament."