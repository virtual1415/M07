# Patricio Vidal
# -*- coding: utf-8 -*-

from AuxExer6 import *

opcio = 0
sortir = False
while opcio < 1 or opcio > 3 or not sortir:
    try:
        print "#######  Menú  #######"
        print "1. Matriu de 3x3"
        print "2. Matriu de 4x4"
        print "3. Sortir"
        opcio = int(raw_input("Escull una opcio: "))
        if opcio == 1:
            # Es crea una matriu de zeros de 3x3 on s'afegeixen de forma aleatoria 3 uns
            matriu = creacioMatriuAleatoria(3, 3)
            ''' El numero d'oportunitats de que disposa el jugador es 5 i el numero
            d'encerts necessaris per guanyar son 3 '''
            resoldreJoc(matriu, 5, 3)
        elif opcio == 2:
            # Es crea una matriu de zeros de 4x4 on s'afegeixen de forma aleatoria 5 uns
            matriu = creacioMatriuAleatoria(4, 5)
            ''' El numero d'oportunitats de que disposa el jugador es 9 i el numero
            d'encerts necessaris per guanyar son 5 '''
            resoldreJoc(matriu, 9, 5)
        elif opcio == 3:
            sortir = True
            print "S'ha sortit del programa."
        else:
            print "Opció incorrecta.\n"
    except:
        print "Has d'introduir un valor numèric.\n"
