# -*- coding: utf-8 -

from _functions import fixedPoint
from plot import plot
import numpy as np
import matplotlib.pyplot as plt
import math

x = np.linspace(-4, 4, num=1000)

def f1(x) : return np.cos(x)
def f2(x) : return np.cos(x)**2

f = [f1, f2]
roots = []
for i in range(0, len(f)):
    print(" --- " + f[i].__name__ + " --- ")
    r = fixedPoint(f[i], 0, 1e-6)
    roots.append(r['res'])
    print(r)

plot(x, f, roots, title = "Assignment 1.2 C5")
