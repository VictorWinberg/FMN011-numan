# -*- coding: utf-8 -

import math
from _functions import bisection

def function(x):
    return math.cos(x) - math.sin(x)

bisection(function, 0, 1, 1e-6)
