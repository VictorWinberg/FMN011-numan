# -*- coding: utf-8 -

from _functions import newton
from scipy.misc import derivative
import numpy as np
import matplotlib.pyplot as plt
import math

x = np.linspace(-6, 6, num=1000)
dx = x[1] - x[0]

def f1(x):
    return x**3 - 2*x - 2

def f2(x):
    return np.exp(x) + x - 7

def f3(x):
    return np.exp(x) + np.sin(x) - 4

def df(f):
    return np.gradient(f(x), dx)

def dfi(f, x_i):
    return derivative(f, x_i, dx=dx)

def pltSetup():
    plt.legend(loc='upper left')
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')

plt.subplot(2, 1, 1)
plt.plot(x, x, 'k--', label='x')
plt.plot(x, f1(x), label='f1')
plt.plot(x, f2(x), label='f2')
plt.plot(x, f3(x), label='f3')
pltSetup()

plt.subplot(2, 1, 2)
plt.plot(x, np.ones(x.size), 'k--', label='+-1')
plt.plot(x, -np.ones(x.size), 'k--')
plt.plot(x, df(f1), label='df1')
plt.plot(x, df(f2), label='df2')
plt.plot(x, df(f3), label='df3')
pltSetup()

plt.draw()

newton(f1, 1, dx, dfi)
newton(f2, 1, dx, dfi)
newton(f3, 1, dx, dfi)

plt.show()
