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

def hexadecimal(num):
    numHex = ""
    conv = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    if num > 15:
        while num >= 16:
            resDiv = num % 16
            num = num / 16
            if num < 16:
                numHex = conv[(num)]+conv[(resDiv)]+numHex
            else:
                numHex = conv[(resDiv)]+numHex
    else:
        numHex = conv[(num)]
    return numHex