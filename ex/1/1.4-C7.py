# -*- coding: utf-8 -

from _functions import newton
from scipy.misc import derivative
import numpy as np
import matplotlib.pyplot as plt
import math

x = np.linspace(-2, 2, num=1000)
dx = x[1] - x[0]

def f(x):
    return np.exp(np.sin(x)**3) + x**6 - 2*x**4 - x**3 - 1

def df(f):
    return np.gradient(f(x), dx)

def dfi(f, x_i):
    return derivative(f, x_i, dx=dx)

def pltSetup():
    plt.legend(loc='upper left')
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.gca().set_ylim([-2,2])

plt.subplot(2, 1, 1)
plt.plot(x, f(x), label='f1')
pltSetup()

plt.subplot(2, 1, 2)
plt.plot(x, np.ones(x.size), 'k--', label='+-1')
plt.plot(x, -np.ones(x.size), 'k--')
plt.plot(x, df(f), label='df')
pltSetup()

print(" --- roots of f --- ")
r = 10
for i in range(0, 3):
    r = newton(f, r - 1, dx, dfi)
    print(r)
    plt.subplot(2, 1, 1)
    plt.axvline(x=r, color='r', linestyle='dashed')
    plt.subplot(2, 1, 2)
    plt.axvline(x=r, color='r', linestyle='dashed')
    print(r)

plt.show()
