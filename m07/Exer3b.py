# Patricio Vidal
# -*- coding: utf-8 -*-
def es_primer(num):
    if num < 2:
        return False
    for i in range (2,num):
        if num % i == 0:
            return False
    return True

for i in range (1,101):
    if es_primer(i):
        print "El numero", i ,"es primer."
    else:
        print "El numero", i ,"no es primer."
