import math
from scipy.optimize import fsolve
from _functions import geval

print("Lengths = 3 gives: " + str(geval([3 for i in range(0, 8)], 15, 1)))
print("Lengths = 8 gives: " + str(geval([8 for i in range(0, 8)], 15, 1)))

def h(x, *data):
    b, d = data
    P = 1 / (2*b) * b**2
    return x**2-P**2;

data = 15, 1
print(fsolve(h, 0, args=data)[0])
