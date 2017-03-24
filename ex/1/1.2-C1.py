# -*- coding: utf-8 -

import numpy as np
import matplotlib.pyplot as plt
import math

x = np.linspace(-6, 6, num=1000)
dx = x[1] - x[0]

def fixedPoint(f, x_i):
    for n in range(0, 1000):
        try:
            x_i = f(x_i)
        except:
            print("None")
            return
    print(x_i)
    print(f(x_i))

def f1_1(x):
    return (x**3 - 2) / 2

def f1_2(x):
    return np.cbrt(2*x+2)

def f1_3(x):
    return 2 / (x**2-2)

def f2_1(x):
    return 7 - np.exp(x)

def f2_2(x):
    return np.log(7-x)

def f3(x):
    return np.log(4 - np.sin(x))

def df(f):
    return np.gradient(f(x), dx)

plt.subplot(2, 1, 1)
plt.plot(x, x, 'k--', label='x')
plt.plot(x, f1_1(x), label='f1_1')
plt.plot(x, f1_2(x), label='f1_2')
plt.plot(x, f1_3(x), label='f1_3')
plt.plot(x, f2_1(x), label='f2_1')
plt.plot(x, f2_2(x), label='f2_2')
plt.plot(x, f3(x), label='f3')
plt.legend(loc='upper left')
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.gca().set_ylim([-5,5])

plt.subplot(2, 1, 2)
plt.plot(x, np.ones(x.size), 'k--', label='+-1')
plt.plot(x, -np.ones(x.size), 'k--')
plt.plot(x, df(f1_1), label='df1_1')
plt.plot(x, df(f1_2), label='df1_2')
plt.plot(x, df(f1_3), label='df1_3')
plt.plot(x, df(f2_1), label='df2_1')
plt.plot(x, df(f2_2), label='df2_2')
plt.plot(x, df(f3), label='df3')
plt.legend(loc='upper left')
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.gca().set_ylim([-5,5])

plt.draw()

print(" --- f1 --- ")
fixedPoint(f1_1, 0)
fixedPoint(f1_2, 0)
fixedPoint(f1_3, 0)

print(" --- f2 --- ")
fixedPoint(f2_1, 0)
fixedPoint(f2_2, 0)

print(" --- f3 --- ")
fixedPoint(f3, 0)

plt.show()
