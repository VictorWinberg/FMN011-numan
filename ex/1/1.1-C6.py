# -*- coding: utf-8 -

from _functions import bisection
import numpy as np
import matplotlib.pyplot as plt
import math

x = np.linspace(-2, 2)

def f(x):
    return np.cos(x) - np.sin(x)

plt.plot(x, f(x), label='f')
plt.legend(loc='upper left')
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')

res = bisection(f, 0, 1, 1e-6)
print(res)

plt.axvline(x=res["c"], color='r', linestyle='dashed')
plt.show()
