# Patricio Vidal
# -*- coding: utf-8 -*-

import random
import pprint

''' Funcio que genera una matriu de n files i n columnes.
La matriu es emplenada de forma aleatoria de ceros i uns. '''


def creacioMatriuAleatoria(n):
    matriu = []
    for i in range(n):
        matriu.append([])
        for j in range(n):
            matriu[i].append(random.randint(0, 1))
    return matriu


''' Funcio que genera una matriu de n files i n columnes.
La matriu es emplenada inicialment amb ceros.
S'afegeixen aleatoriament a la matriu un número nUns d'uns. '''


def creacioMatriuAleatoria(n, nUns):
    matriu = []
    for i in range(n):
        matriu.append([])
        for j in range(n):
            matriu[i].append(0)
    for i in range(nUns):
        matriu[random.randint(0, n - 1)][random.randint(0, n - 1)] = 1
    return matriu


''' Funcio que recull una matriu donada de NxN, el número d'oportunitats i
el número d'encerts necessaris per guanyar. '''


def resoldreJoc(matriu, oportunitats, encerts):
    enc = 0
    for i in range(oportunitats):
        ''' Aquestes variables booleanes es serviran per controlar que els valors
        introduïts estan dintre dels límits de la matriu '''
        correcteX = False
        correcteY = False
        while not correcteX or not correcteY:
            print '\nIntrodueix les coordenades on creus que hi ha un 1. Valors permesos: 0 -', len(matriu) - 1
            try:
                coordX = int(raw_input("Introdueix la coordenada fila: "))
                coordY = int(raw_input("Introdueix la coordenada columna: "))
                if coordX in range(0, len(matriu)):
                    correcteX = True
                else:
                    print 'La coordenada fila està fora de rang.'
                    correcteX = False
                if coordY in range(0, len(matriu)):
                    correcteY = True
                else:
                    print 'La coordenada columna està fora de rang.'
                    correcteY = False
            except:
                print "Has d'introduir un numero i ha d'estar dintre del rang demanat.\n"
        if matriu[coordX][coordY] == 1:
            print "Correcte.\n"
            matriu[coordX][coordY] = 'V'
            enc += 1
        else:
            print "Incorrecte.\n"
            matriu[coordX][coordY] = 'X'
    ''' Comprovem si s'han assolit el número d'encerts necessaris
    per guanyar el joc '''
    if enc >= encerts:
        print "Has guanyat!"
    else:
        print "Has perdut!"
    print "Aqui tens la matriu (V assenyala els encerts i X els errors):"
    pprint.pprint(matriu)
    print "\n"
