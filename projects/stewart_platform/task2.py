from math import sqrt
from scipy.optimize import fsolve
from _functions import geval

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

# Task 2
def stf(x, *data):
    a, b, d, L, h, X, Y = data
    X["T1"], X["T2"], X["T3"] = x
    print(x)
    return (
        a**2 + 2*X["T1"]*X["T2"] - 2*X["T1"]*(X["P1"] + sqrt(3)*(Y["P1"]-Y["P2"])) - 2*X["P2"]*X["T2"]-((sqrt(3)*X["P1"]-Y["P1"]+Y["P2"])**2+(h[1]**2+h[2]**2)-4*X["P1"]**2-X["P2"]**2)+2*sqrt((h[1]**2-4*(X["T1"]-X["P1"])**2)*(h[2]**2-(X["T2"]-X["P2"])**2)),
        a**2 - 4*X["T1"]*X["T3"] - 2*X["T1"]*(X["P1"] - 3*X["P3"] + sqrt(3)*(Y["P1"] - Y["P3"]))-2*X["T3"]*(-3*X["P1"] + X["P3"] + sqrt(3)*(Y["P1"] - Y["P3"]))-((sqrt(3)*(X["P1"] + X["P3"]) - Y["P1"] + Y["P3"])**2 + (h[1]**2+h[3]**2) - 4*X["P1"]**2 - 4*X["P3"]**2)
        +2*sqrt((h[1]**2 - 4*(X["T1"] - X["P1"])**2)*(h[3]**2 - 4*(X["T3"] - X["P3"])**2)),
        a**2 + 2*X["T2"]*X["T3"] - 2*X["T3"]*(X["P3"] + sqrt(3)*(Y["P2"] - Y["P3"])) - 2*X["P2"]*X["T2"]
        -((sqrt(3)*X["P3"] - Y["P2"] + Y["P3"])**2 + (h[2]**2+h[3]**2) - X["P2"]**2 - 4*X["P3"]**2)
        +2*sqrt((h[2]**2 - (X["T2"] - X["P2"])**2)*(h[3]**2 - 4*(X["T3"] - X["P3"])**2))
    )

a, b, d = 10, 15, 1
L = [11.5 for i in range(0, 7)]

X, Y, P, h = geval(L, b, d)

data = a, b, d, L, h, X, Y

# TODO: Task 3


# Task 4
def starting_points(x, *data):
    a, b, d, L, h, X, Y = data
    X["T1"], X["T2"], X["T3"] = x
    return (
        h[1]**2 - 4*(X["T1"] - X["P1"])**2,
        h[2]**2 - (X["T2"] - X["P2"])**2,
        h[3]**2 - 4*(X["T3"] - X["P3"])**2
    )

X["T1"], X["T2"], X["T3"] = fsolve(starting_points, [-10 for i in range(0, 3)], data)
print(X["T1"], X["T2"], X["T3"])

X["T1"], X["T2"], X["T3"] = fsolve(starting_points, [10 for i in range(0, 3)], data)
print(X["T1"], X["T2"], X["T3"])

X["T1"], X["T2"], X["T3"] = fsolve(stf, (1, -5, 2), data)
print(X["T1"], X["T2"], X["T3"])

print(stf((X["T1"], X["T2"], X["T3"]), *data))

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

def solve(L):
    a, b, d = 10, 15, 1
    X, Y, P, h = geval(L, b, d)
    data = a, b, d, L, h, X, Y

    X["T1_0"], X["T2_0"], X["T3_0"] = fsolve(starting_points, [-10 for i in range(0, 3)], data)
    X["T1_1"], X["T2_1"], X["T3_1"] = fsolve(starting_points, [10 for i in range(0, 3)], data)

    print(X["T1_0"], X["T1_1"])
    print(X["T2_0"], X["T2_1"])
    print(X["T3_0"], X["T3_1"])

    r1 = (X["T1_0"] + X["T1_1"]) / 2
    r2 = (X["T2_0"] + X["T2_1"]) / 2
    r3 = (X["T3_0"] + X["T3_1"]) / 2

    X["T1"], X["T2"], X["T3"] = fsolve(stf, (r1, r2, r3), data)
    print(X["T1"], X["T2"], X["T3"])

    Y, Z = getyz(X, Y, h)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    xs = [X["T1"], X["T2"], X["T3"]]
    ys = [Y["T1"], Y["T2"], Y["T3"]]
    zs = [Z["T1"], Z["T2"], Z["T3"]]

    ax.scatter(xs, ys, zs)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

print(" ----- TASK 5 ----- ")
solve([8 for i in range(0, 7)])
solve([15 for i in range(0, 7)])
solve([-1, 15, 15, 8, 8, 8, 8])
# solve([-1, 8, 8, 8, 15, 15, 15])
plt.show()
