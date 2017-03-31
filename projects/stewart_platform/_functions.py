from math import sqrt, sin
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

# Task 1
def h(x, *data):
    b, d = data
    P = 1 / (2*b) * b**2
    return x**2-P**2;

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

# Task 3
def solve_print(r, data):
    a, h, X, Y = data
    X["T1"], X["T2"], X["T3"] = fsolve(stf, r, data)
    print(X["T1"], X["T2"], X["T3"])
    print(stf((X["T1"], X["T2"], X["T3"]), *data))

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
def getCordsTop(X, Y, h):
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
    Y, Z = getCordsTop(X, Y, h)

    return X, Y, Z

def vectTop(X, Y, Z):
    xt = [X["T1"], X["T2"], X["T3"]]
    yt = [Y["T1"], Y["T2"], Y["T3"]]
    zt = [Z["T1"], Z["T2"], Z["T3"]]
    return xt, yt, zt

def vectBase(X, Y, z):
    xb = [X["B1"], X["B2"], X["B3"], X["B4"], X["B5"], X["B6"]]
    yb = [Y["B1"], Y["B2"], Y["B3"], Y["B4"], Y["B5"], Y["B6"]]
    zb = [z for i in range(6)]
    return xb, yb, zb

def getBase(b, d, X, Y):
    X["B1"] = sqrt(3) / 6 * (2*b + d)
    X["B2"] = -sqrt(3) / 6 * (b - d)
    X["B3"] = -sqrt(3) / 6 * (b + 2*d)
    X["B4"] = -sqrt(3) / 6 * (b + 2*d)
    X["B5"] = -sqrt(3) / 6 * (b - d)
    X["B6"] = sqrt(3) / 6 * (2*b + d)

    Y["B1"] = d / 2
    Y["B2"] = (b + d) / 2
    Y["B3"] = b / 2
    Y["B4"] = -b / 2
    Y["B5"] = -(b+d) / 2
    Y["B6"] = -d / 2
    return X, Y

def getVectLegs(X, Y, Z):
    lx = [[X["B1"], X["T1"]],
            [X["B2"], X["T1"]],
            [X["B3"], X["T2"]],
            [X["B4"], X["T2"]],
            [X["B5"], X["T3"]],
            [X["B6"], X["T3"]]]
    ly = [[Y["B1"], Y["T1"]],
            [Y["B2"], Y["T1"]],
            [Y["B3"], Y["T2"]],
            [Y["B4"], Y["T2"]],
            [Y["B5"], Y["T3"]],
            [Y["B6"], Y["T3"]]]
    lz = [[0, Z["T1"]],
            [0, Z["T1"]],
            [0, Z["T2"]],
            [0, Z["T2"]],
            [0, Z["T3"]],
            [0, Z["T3"]]]
    return lx, ly, lz

def getTwistTop(a, b, d, L, X, Y, Z):
    X["T1"] = sqrt(3) / (4*b) * (L[1]**2 - L[2]**2) + 1/2 * sqrt(1/3 * a**2 - 1 / (4*b**2) * (L[2]**2 - L[1]**2)**2)
    Y["T1"] = 1 / (4*b) * (L[2]**2 - L[1]**2) + sqrt(3) / 2 * sqrt(1/3 * a**2 - 1 / (4*b**2) * (L[2]**2 - L[1]**2)**2)
    Z["T1"] = sqrt(1/2 * (L[2]**2 + L[1]**2) - 1/3 * (a**2 + b**2 + b*d + d**2) + (b + 2*d) / sqrt(3) * sqrt(1/3 * a**2 - 1 / (4*b**2) * (L[2]**2 - L[1]**2)**2))
    X["T2"] = -sqrt(1/3 * a**2 - 1/(4*b**2) * (L[2]**2 - L[1]**2)**2)
    Y["T2"] = -1 / (2*b) * (L[2]**2 - L[1]**2)
    Z["T2"] = sqrt(1/2 * (L[2]**2 + L[1]**2) - 1/3 * (a**2 + b**2 + b*d + d**2) + (b + 2*d) / sqrt(3) * sqrt(1/3 * a**2 - 1/(4*b**2) * (L[2]**2 - L[1]**2)**2))
    X["T3"] = sqrt(3) / (4*b) * (L[2]**2 - L[1]**2) + 1/2 * sqrt(1/3 * a**2 - 1 / (4*b**2) * (L[2]**2 - L[1]**2)**2)
    Y["T3"] = 1 / (4*b) * (L[2]**2 - L[1]**2) - sqrt(3)/2 * sqrt(1/3 * a**2 - 1 / (4*b**2) * (L[2]**2 - L[1]**2)**2)
    Z["T3"] = sqrt(1/2 * (L[2]**2 + L[1]**2) - 1/3 * (a**2 + b**2 + b*d + d**2) + (b + 2*d) / sqrt(3) * sqrt(1/3 * a**2 - 1/(4*b**2) * (L[2]**2 - L[1]**2)**2))
    return X, Y, Z

def make3dfig():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')
    ax.set_xlim3d(-10, 10)
    ax.set_ylim3d(-10, 10)
    ax.set_zlim3d(0, 20)
    ax.set_title("Victor Winberg & Anton Göransson")
    return ax
