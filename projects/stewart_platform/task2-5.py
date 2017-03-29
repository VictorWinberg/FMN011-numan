from scipy.optimize import fsolve
from _functions import *

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# Task 2
a, b, d = 10, 15, 1
L = [11.5 for i in range(0, 7)]

X, Y, P, h = geval(L, b, d)

# TODO: Task 3


# Task 4
data = h, X
X["T1"], X["T2"], X["T3"] = fsolve(starting_points, [-10 for i in range(0, 3)], data)
print(X["T1"], X["T2"], X["T3"])

X["T1"], X["T2"], X["T3"] = fsolve(starting_points, [10 for i in range(0, 3)], data)
print(X["T1"], X["T2"], X["T3"])
print()

data = a, h, X, Y
X["T1"], X["T2"], X["T3"] = fsolve(stf, (1, -5, 2), data)
print(X["T1"], X["T2"], X["T3"])

print(stf((X["T1"], X["T2"], X["T3"]), *data))

# Task 5
print(" ----- TASK 5 ----- ")
ax = make3dfig()

ax.plot_trisurf(*solve([8 for i in range(0, 7)]))
ax.plot_trisurf(*solve([15 for i in range(0, 7)]))
ax.plot_trisurf(*solve([-1, 15, 15, 8, 8, 8, 8]))
ax.plot_trisurf(*solve([-1, 8, 8, 8, 15, 15, 15], r=[2.5, 1.8, 0]))

# Animation
ax = make3dfig()

L = [-1, 0, 1.05, 2.09, 3.14, 4.19, 5.24]

for i in range(0, 100):
    surf = ax.plot_trisurf(*solve([1.5 * sin(i/10) + 2 * sin(i/10 + x) + 11.5 for x in L]), color='black')
    plt.pause(.001)
    ax.collections.remove(surf)

plt.show()
