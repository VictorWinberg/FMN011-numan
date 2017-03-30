# -*- coding: utf-8 -

from _functions import fixedPoint
from plot import plot
import numpy as np
import matplotlib.pyplot as plt
import math

x = np.linspace(-6, 6, num=1000)

def f1_1(x) : return (x**3 - 2) / 2
def f1_2(x) : return np.cbrt(2*x+2)
def f1_3(x) : return 2 / (x**2-2)
def f2_1(x) : return 7 - np.exp(x)
def f2_2(x) : return np.log(7-x)
def f3(x) : return np.log(4 - np.sin(x))

f = [f1_1, f1_2, f1_3, f2_1, f2_2, f3]
roots = []
sigma = 1e-8

for i in range(0, len(f)):
    print(" --- " + f[i].__name__ + " --- ")
    r = fixedPoint(f[i], 0, sigma)
    print(r)
    if r['error'] < sigma:
        roots.append(r['res'])

plot(x, f, roots, ylim = [-5, 5], title = "Assignment 1.2 C1")
