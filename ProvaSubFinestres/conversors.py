#!usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'eloy'

def decToBin(valor):
    ' Torna un vector binari (MSB-LSB) '
    q = valor
    c = []
    # dividir per 2 fins que no es pugui
    while q >= 2:
        aux = q // 2
        r = q % 2
        q = aux
        c.append(r)
    c.append(q)
    c.reverse()
    return c

def decToBinStr(valor):
    ' Torna un binari en forma de cadena '
    q = valor
    c = ''
    # dividir per 2 fins que no es pugui
    while q >= 2:
        aux = q // 2
        r = q % 2
        q = aux
        c = c + str(r)
    c = c + str(q)
    # Invertim la cadena per mostrar el valor en binari correcte
    return c[::-1]

def decToHex(entrada):
    ' Torna una cadena en hexadecimal '
    vHex = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F')
    vResult = ''

    # dividir per 16 fins que no es pugui
    while entrada > 15:
        aux = entrada // 16
        aux2 = entrada % 16
        vResult = vHex[aux2] + vResult
        entrada = aux

    vResult = vHex[entrada] + vResult
    'Completa el resultat amb 0 si longitud senar'
    if len(vResult) % 2 != 0:
        vResult = '0' + vResult
    return vResult
