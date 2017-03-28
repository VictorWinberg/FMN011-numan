import math
from scipy.optimize import fsolve
from _functions import geval

def equations(x, *data):
    a, b, c = data
    X["T1"], X["T2"], X["T3"] = x
    return (X["T1"] + X["T2"] - a, X["T1"] - X["T2"] + X["T3"] - b, X["T3"]**2 - X["T1"] - c)

a, b, d = 10, 15, 1
L = [11.5 for i in range(0, 8)]

X, Y, P, h = geval(L, b, d)

data = 3, 2, 8

X["T1"], X["T2"], X["T3"] = fsolve(equations, (0, 0, 0), data)

print((X["T1"], X["T2"], X["T3"]))
print(equations((X["T1"], X["T2"], X["T3"]), *data))
