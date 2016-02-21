# Patricio Vidal
# -*- coding: utf-8 -*-

a = ((4, 3, 3, 1), (1, 3, 4, 2), (2, 4, 1, 3), (3, 2, 2, 4))
for i in range(4):
    print ('columna %s' % i)
    for j in range(3):
        x = a[j][i]
        print ('a[%s][%s] = %s' % (j, i, x))
        for k in range(j + 1, 4):
            y = a[k][i]
            print ('a[%s][%s] = %s' % (k, i, y))
            print ('comprovant si %s es igual %s' %(x, y))
            if x == y:
                print x, ' es igual a ', y
            else:
                print 'no son iguals'