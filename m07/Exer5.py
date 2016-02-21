# Patricio Vidal
# -*- coding: utf-8 -*-

from operacionsMatrius import *

'''
n = 0
esnum = False
while n < 2 or n > 8 or esnum != True:
    try:
        print ("Pots crear matrius de 2x2, 3x3, 4x4, 5x5, 6x6, 7x7 i 8x8")
        n = int(raw_input("Introdueix un número entre 2 i 8 (ambdos inclosos): "))
        if n < 2:
            print "El", n ,"no es troba dintre del rang permés."
        esnum = True
    except:
        print "No es poden introduir caràcters. Has d'introduir un numero."
        esnum = False
'''        

n = 4
matriu1 = creacioMatriuAleatoria(n)
matriu2 = creacioMatriuAleatoria(n)

#print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in matriu1]))
print "matriu 1:",matriu1
print "matriu 2:",matriu2
print "matriu 1 + matriu 2:",sumaMatrius(matriu1, matriu2, n)
print "matriu 1 * matriu 2:",multiplicaMatrius(matriu1, matriu2, n)
