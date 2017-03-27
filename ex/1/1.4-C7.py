# -*- coding: utf-8 -

from _functions import newton
from plot import plot
import numpy as np
import matplotlib.pyplot as plt
import math

x = np.linspace(-2, 2, num=1000)

def f(x):
    return np.exp(np.sin(x)**3) + x**6 - 2*x**4 - x**3 - 1

print(" --- roots of f --- ")
c = 10
r = []
for i in range(0, 3):
    c = newton(f, c - 1, 1e-8)
    r.append(c)
    print(c)

plot(x, [f], r, ylim = [-2, 2], title = "Assignment 1.4 C7")
