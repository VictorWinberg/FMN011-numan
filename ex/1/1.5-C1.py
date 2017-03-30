# -*- coding: utf-8 -

from _functions import secant
from plot import plot
from scipy.misc import derivative
import numpy as np
import matplotlib.pyplot as plt
import math

x = np.linspace(-2, 2, num=1000)
dx = x[1] - x[0]

def f1(x) : return x**3 - 2*x - 2
def f2(x) : return np.exp(x) + x - 7
def f3(x) : return np.exp(x) + np.sin(x) - 4

f = [f1, f2, f3]
r = []
for i in range(0, len(f)):
    r.append(secant(f[i], 1, 2))

print(" --- roots --- ")
print(r)

plot(x, f, r, ylim = [-4, 4], title = "Assignment 1.5 C1")
