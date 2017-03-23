# -*- coding: utf-8 -

import numpy as np
import math
import matplotlib.pyplot as plt

def fixedPoint(f, x):
    while 1:
        x = f(x)
        print(x)

def f1(x):
    return x**3-2*x-2

def f2(x):
    return np.exp(x)+x-7

def f3(x):
    return np.exp(x)+np.sin(x)-4

x = np.linspace(-5, 5)
plt.plot(x, f1(x))
plt.plot(x, f2(x))
plt.plot(x, f3(x))
plt.show()
