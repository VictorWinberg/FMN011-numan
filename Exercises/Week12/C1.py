# -*- coding: utf-8 -

import numpy as np

x = np.logspace(-1, -14, num=14)
print x

a = (1 - 1/np.cos(x)) / np.tan(x)**2
print "A: "
print a
print "1e-1, 1e-7  -> 8 sign. digits"
print "1e-8, 1e-14 -> 0 sign. digits"

a = np.cos(x)*(np.cos(x) - 1) / np.sin(x)**2
print a
print "same"

a = 1/np.tan(x)**2 - 1/(np.tan(x)*np.sin(x))
print a

b = (1 - (1-x)**3) / x
print "B: "
print b
print "1e-1          -> 3 sign. digits"
print "1e-2, 1e-7  -> 4-8 sign. digits"
print "1e-8, 1e-14 -> 9 sign. digits"

b = x**2 - 3*x + 3
print b
