# -*- coding: utf-8 -

import math

def bisection(f, a, b, sigma):
    while (b - a) / 2.0 > sigma:
        c = (a + b) / 2.0 # midpoint
        if f(c)*f(a) > 0:
            a = c;
        elif f(c)*f(b) > 0:
            b = c;
        print c
    accurancy = (b - a) / 2.0
    print accurancy
    print c
    print f(c)
    return f(c)

def function(x):
    return math.cos(x) - math.sin(x)

bisection(function, 0, 1, 1e-6)
