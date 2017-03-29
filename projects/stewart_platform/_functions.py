from math import sqrt, sin
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

# Task 1
def ph(L, b, d):
    l = [1, 2, 3]
    P = {i: 1 / (2*b) * (b**2 + L[2*i-1]**2 - L[2*i]**2) for i in l}
    h_quad = {i: L[2*i-1]**2-P[i]**2 for i in l}
    for i in l:
        if h_quad[i] < 0:
            return P, "Negative height"
    h = {i: sqrt(L[2*i-1]**2-P[i]**2) for i in l}
    return P, h

def geval(L, b, d):
    P, h = ph(L, b, d)
    X = {
        "P1": sqrt(3) / 6 * (2*b + d - 3*P[1]),
        "P2": -sqrt(3) / 6 * (b + 2*d),
        "P3": -sqrt(3) / 6 * (b - d - 3*P[3])
    }
    Y = {
        "P1": 1 / 2 * (d + P[1]),
        "P2": -1 / 2 * (b - 2*P[2]),
        "P3": -1 / 2 * (b + d - P[3])
    }
    return X, Y, P, h

# Task 2
def stf(x, *data):
    a, h, X, Y = data
    X["T1"], X["T2"], X["T3"] = x
    return (
        a**2 + 2*X["T1"]*X["T2"] - 2*X["T1"]*(X["P1"] + sqrt(3)*(Y["P1"]-Y["P2"])) - 2*X["P2"]*X["T2"]-((sqrt(3)*X["P1"]-Y["P1"]+Y["P2"])**2+(h[1]**2+h[2]**2)-4*X["P1"]**2-X["P2"]**2)+2*sqrt((h[1]**2-4*(X["T1"]-X["P1"])**2)*(h[2]**2-(X["T2"]-X["P2"])**2)),
        a**2 - 4*X["T1"]*X["T3"] - 2*X["T1"]*(X["P1"] - 3*X["P3"] + sqrt(3)*(Y["P1"] - Y["P3"]))-2*X["T3"]*(-3*X["P1"] + X["P3"] + sqrt(3)*(Y["P1"] - Y["P3"]))-((sqrt(3)*(X["P1"] + X["P3"]) - Y["P1"] + Y["P3"])**2 + (h[1]**2+h[3]**2) - 4*X["P1"]**2 - 4*X["P3"]**2)
        +2*sqrt((h[1]**2 - 4*(X["T1"] - X["P1"])**2)*(h[3]**2 - 4*(X["T3"] - X["P3"])**2)),
        a**2 + 2*X["T2"]*X["T3"] - 2*X["T3"]*(X["P3"] + sqrt(3)*(Y["P2"] - Y["P3"])) - 2*X["P2"]*X["T2"]
        -((sqrt(3)*X["P3"] - Y["P2"] + Y["P3"])**2 + (h[2]**2+h[3]**2) - X["P2"]**2 - 4*X["P3"]**2)
        +2*sqrt((h[2]**2 - (X["T2"] - X["P2"])**2)*(h[3]**2 - 4*(X["T3"] - X["P3"])**2))
    )

# Task 4
def starting_points(x, *data):
    h, X = data
    X["T1"], X["T2"], X["T3"] = x
    return (
        h[1]**2 - 4*(X["T1"] - X["P1"])**2,
        h[2]**2 - (X["T2"] - X["P2"])**2,
        h[3]**2 - 4*(X["T3"] - X["P3"])**2
    )

# Task 5
def getyz(X, Y, h):
    Y = {
        "T1":  sqrt(3)*X["T1"] - (sqrt(3)*X["P1"]-Y["P1"]),
        "T2": Y["P2"],
        "T3": -sqrt(3)*X["T3"] + (sqrt(3)*X["P3"]+Y["P3"])
    }
    Z = {
        "T1": sqrt(h[1]**2 - 4*(X["T1"]-X["P1"])**2),
        "T2": sqrt(h[2]**2 - (X["T2"]-X["P2"])**2),
        "T3": sqrt(h[3]**2 - 4*(X["T3"]-X["P3"])**2)
    }
    return Y, Z

def solve(L, r = None):
    a, b, d = 10, 15, 1
    X, Y, P, h = geval(L, b, d)

    data = h, X
    X["T1_0"], X["T2_0"], X["T3_0"] = fsolve(starting_points, [-10 for i in range(0, 3)], data)
    X["T1_1"], X["T2_1"], X["T3_1"] = fsolve(starting_points, [10 for i in range(0, 3)], data)

    if r is None:
        r = (X["T1_0"] + X["T1_1"]) / 2, (X["T2_0"] + X["T2_1"]) / 2, (X["T3_0"] + X["T3_1"]) / 2

    data = a, h, X, Y
    X["T1"], X["T2"], X["T3"] = fsolve(stf, r, data)

    Y, Z = getyz(X, Y, h)

    xs = [X["T1"], X["T2"], X["T3"]]
    ys = [Y["T1"], Y["T2"], Y["T3"]]
    zs = [Z["T1"], Z["T2"], Z["T3"]]

    return xs, ys, zs

def make3dfig():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')
    ax.set_xlim3d(-10, 10)
    ax.set_ylim3d(-10, 10)
    ax.set_zlim3d(-10, 10)
    return ax
