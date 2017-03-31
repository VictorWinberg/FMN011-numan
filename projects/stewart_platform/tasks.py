from scipy.optimize import fsolve
from _functions import *

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# Task 1
print(" ----- TASK 1 ----- ")
print("Lengths = 3 gives: " + str(geval([3 for i in range(0, 8)], 15, 1)))
print("Lengths = 8 gives: " + str(geval([8 for i in range(0, 8)], 15, 1)))

data = 15, 1
print(fsolve(h, 0, args=data)[0])

# Task 2
print(" ----- TASK 2 ----- ")
a, b, d = 10, 15, 1
L = [11.5 for i in range(0, 7)]

X, Y, P, h = geval(L, b, d)

data = a, h, X, Y
print(stf((0, 0, 0), *data))
print(stf((2, -5, 2), *data))
print(stf((3, -6, 3), *data))

# TODO: Task 3
print(" ----- TASK 3 ----- ")
solve_print((1, -2, 1), data)
solve_print((2, -5, 2), data)
solve_print((3, -6, 3), data)

# Task 4
print(" ----- TASK 4 ----- ")
data = h, X
print(fsolve(starting_points, [-10 for i in range(0, 3)], data))
print(fsolve(starting_points, [10 for i in range(0, 3)], data))
print()

data = a, h, X, Y
x = fsolve(stf, (1, -5, 2), data)
print(x)
print(stf(x, *data))

# Task 5
print(" ----- TASK 5 ----- ")
ax = make3dfig()

lengths = [ [8 for i in range(0, 7)],
            [15 for i in range(0, 7)],
            [-1, 15, 15, 8, 8, 8, 8]]

for i in range(3):
    X, Y, Z = solve(lengths[i])
    ax.plot_trisurf(*vectTop(X, Y, Z))

X, Y, Z = solve([-1, 8, 8, 8, 15, 15, 15], r=[2.5, 1.8, 0])
ax.plot_trisurf(*vectTop(X, Y, Z))

X, Y = getVectBase(b, d, X, Y)
xb, yb, zb = vectBase(X, Y, 0)
ax.plot_trisurf(xb, yb, zb, color='red')

# Animation
if input("See plots with animation? y/N ") == "y":
    times = ""
    while(times.isdigit() is False):
        times = input("Iterations: ")

    ax = make3dfig()
    L = [-1, 0, 1.05, 2.09, 3.14, 4.19, 5.24]
    legs = []

    ax.plot_trisurf(xb, yb, zb, color='red')

    for i in range(0, int(times)):
        X, Y, Z = solve([1.5 * sin(i/10) + 2 * sin(i/10 + x) + 11.5 for x in L])
        surf = ax.plot_trisurf(*vectTop(X, Y, Z), color='blue')

        X, Y = getVectBase(b, d, X, Y)
        xb, yb, zb = vectBase(X, Y, 0)
        lx, ly, lz = getVectLegs(X, Y, Z)

        for j in range(6):
            legs.append(ax.plot_wireframe(lx[j], ly[j], lz[j], linewidths=7, colors='gray'))

        plt.pause(.001)
        ax.collections.remove(surf)
        for j in range(6):
            ax.collections.remove(legs.pop())

plt.show()
