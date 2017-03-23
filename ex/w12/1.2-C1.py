# -*- coding: utf-8 -

import numpy as np
import matplotlib.pyplot as plt
import math

x = np.linspace(-2, 3)
print(x)

def fixedPoint(f, x_i):
    dx = x[1]- x[0]
    df = np.diff(f(x)) / dx
    print(np.abs(df) < 1)
    for n in range(0, 1000):
        try:
            x_i = f(x_i)
        except:
            break
    print(x_i)

def f1(x):
    return (x**3 - 2) / 2

def f2(x):
    return 7 - np.exp(x)

def f3(x):
    return np.log(4 - np.sin(x))

plt.plot(x, x, label='x')
plt.plot(x, f1(x), label='f1')
plt.plot(x, f2(x), label='f2')
plt.plot(x, f3(x), label='f3')
plt.legend(loc='upper left')
plt.draw()

print(" --- f1 --- ")
fixedPoint(f1, 2.0)
print(" --- f2 --- ")
fixedPoint(f2, -2.0)
print(" --- f3 --- ")
fixedPoint(f3, 2.0)

plt.show()
