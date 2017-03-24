# -*- coding: utf-8 -

import numpy as np
import matplotlib.pyplot as plt
import math

x = np.linspace(-2, 2)
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

def f1(x):
    return (x**3 - 2) / 2

def f2(x):
    return 7 - np.exp(x)

def f3(x):
    return np.log(4 - np.sin(x))

def df(f):
    return np.gradient(f(x), dx)

plt.plot(x, x, label='x')
plt.plot(x, f1(x), label='f1')
plt.plot(x, f2(x), label='f2')
plt.plot(x, f3(x), label='f3')
plt.legend(loc='upper left')

plt.figure()

plt.plot(x, np.ones(x.size), 'k--', label='+-1')
plt.plot(x, -np.ones(x.size), 'k--')
plt.plot(x, df(f1), label='df1')
plt.plot(x, df(f2), label='df2')
plt.plot(x, df(f3), label='df3')
plt.legend(loc='upper left')

plt.draw()

print(" --- f1 --- ")
fixedPoint(f1, 0)
print(" --- f2 --- ")
fixedPoint(f2, 0)
print(" --- f3 --- ")
fixedPoint(f3, 0)

plt.show()
