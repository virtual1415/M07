# -*- coding: utf-8 -*-
# author: Patricio Vidal

a = [1, 2, 3, 4]
print a[1:]
print a[:-1]
if a[1:] != a[:-1]:
    print 'No tots els elements de a son iguals'
else:
    print 'Tots els elements de a son iguals'

x = 55
print '10%'
print '%s%%' % x