from math import sqrt
from scipy.optimize import fsolve
from _functions import geval

def equations(x, *data):
    a, b, d, L, h, X, Y = data
    X["T1"], X["T2"], X["T3"] = x
    return (
        a**2 + 2*X["T1"]*X["T2"] - 2*X["T1"]*(X["P1"] + sqrt(3)*(Y["P1"]-Y["P2"])) - 2*X["P2"]*X["T2"]-((sqrt(3)*X["P1"]-Y["P1"]+Y["P2"])**2+(h[1]**2+h[2]**2)-4*X["P1"]**2-X["P2"]**2)+2*sqrt((h[1]**2-4*(X["T1"]-X["P1"])**2)*(h[2]**2-(X["T2"]-X["P2"])**2)),
        a**2 - 4*X["T1"]*X["T3"] - 2*X["T1"]*(X["P1"] - 3*X["P3"] + sqrt(3)*(Y["P1"] - Y["P3"]))-2*X["T3"]*(-3*X["P1"] + X["P3"] + sqrt(3)*(Y["P1"] - Y["P3"]))-((sqrt(3)*(X["P1"] + X["P3"]) - Y["P1"] + Y["P3"])**2 + (h[1]**2+h[3]**2) - 4*X["P1"]**2 - 4*X["P3"]**2)
        +2*sqrt((h[1]**2 - 4*(X["T1"] - X["P1"])**2)*(h[3]**2 - 4*(X["T3"] - X["P3"])**2)),
        a**2 + 2*X["T2"]*X["T3"] - 2*X["T3"]*(X["P3"] + sqrt(3)*(Y["P2"] - Y["P3"])) - 2*X["P2"]*X["T2"]
        -((sqrt(3)*X["P3"] - Y["P2"] + Y["P3"])**2 + (h[2]**2+h[3]**2) - X["P2"]**2 - 4*X["P3"]**2)
        +2*sqrt((h[2]**2 - (X["T2"] - X["P2"])**2)*(h[3]**2 - 4*(X["T3"] - X["P3"])**2))
    )

a, b, d = 10, 15, 1
L = [11.5 for i in range(0, 8)]

X, Y, P, h = geval(L, b, d)

data = a, b, d, L, h, X, Y

def sqrtequations(x, *data):
    a, b, d, L, h, X, Y = data
    X["T1"], X["T2"], X["T3"] = x
    return (
        h[1]**2 - 4*(X["T1"] - X["P1"])**2,
        h[2]**2 - (X["T2"] - X["P2"])**2,
        h[3]**2 - 4*(X["T3"] - X["P3"])**2
    )

X["T1"], X["T2"], X["T3"] = fsolve(sqrtequations, [10 for i in range(0, 3)], data)
print(X["T1"], X["T2"], X["T3"])

X["T1"], X["T2"], X["T3"] = fsolve(sqrtequations, [-10 for i in range(0, 3)], data)
print(X["T1"], X["T2"], X["T3"])

X["T1"], X["T2"], X["T3"] = fsolve(equations, (1, -5, 2), data)

print(X["T1"], X["T2"], X["T3"])
