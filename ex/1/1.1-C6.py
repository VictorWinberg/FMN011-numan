# -*- coding: utf-8 -

from _functions import bisection
import math

def f(x):
    return math.cos(x) - math.sin(x)

bisection(f, 0, 1, 1e-6)
