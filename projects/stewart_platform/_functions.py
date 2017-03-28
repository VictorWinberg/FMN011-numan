import math

# Task 1
def ph(L, b, d):
    l = [1, 2, 3]
    P = {i: 1 / (2*b) * (b**2 + L[2*i-1]**2 - L[2*i]**2) for i in l}
    h_quad = {i: L[2*i-1]**2-P[i]**2 for i in l}
    for i in l:
        if h_quad[i] < 0:
            return P, "Negative height"
    h = {i: math.sqrt(L[2*i-1]**2-P[i]**2) for i in l}
    return P, h

def geval(L, b, d):
    P, h = ph(L, b, d)
    X = {
        "P1": math.sqrt(3) / 6 * (2*b + d - 3*P[1]),
        "P2": -math.sqrt(3) / 6 * (b + 2*d),
        "P3": -math.sqrt(3) / 6 * (b - d - 3*P[3])
    }
    Y = {
        "P1": 1 / 2 * (d + P[1]),
        "P2": -1 / 2 * (b - 2*P[2]),
        "P3": -1 / 2 * (b + d - P[3])
    }
    return X, Y, P, h
