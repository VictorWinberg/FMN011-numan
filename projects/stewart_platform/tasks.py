from scipy.optimize import fsolve
from _functions import *

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

from anim import make_gif, rotanimate
import numpy as np
import os

# Task 1
print(" ----- TASK 1 ----- ")
print("Lengths = 3 gives: " + str(geval([3 for i in range(8)], 15, 1)))
print("Lengths = 8 gives: " + str(geval([8 for i in range(8)], 15, 1)))

data = 15, 1
print(fsolve(h, 0, args=data)[0])

# Task 2
print(" ----- TASK 2 ----- ")
a, b, d = 10, 15, 1
L = [11.5 for i in range(7)]

X, Y, P, h = geval(L, b, d)

data = a, h, X, Y
print(stf((0, 0, 0), *data))
print(stf((2, -5, 2), *data))
print(stf((3, -6, 3), *data))

# Task 3
print(" ----- TASK 3 ----- ")
solve_print((1, -2, 1), data)
solve_print((2, -5, 2), data)
solve_print((3, -6, 3), data)

# Task 4
print(" ----- TASK 4 ----- ")
data = h, X
print(fsolve(starting_points, [-10 for i in range(3)], data))
print(fsolve(starting_points, [10 for i in range(3)], data))
print()

data = a, h, X, Y
x = fsolve(stf, (1, -5, 2), data)
print(x)
print(stf(x, *data))

# Task 5
print(" ----- TASK 5 ----- ")
lengths = [ [-1, 8, 8, 8, 8, 8, 8],
            [-1, 15, 15, 15, 15, 15, 15],
            [-1, 15, 15, 8, 8, 8, 8]]

for i in range(4):
    ax = make3dfig()

    if(i < 3):
        X, Y, Z = solve(lengths[i])
    else:
        L = [-1, 8, 15, 8, 15, 8, 15]
        X, Y, Z = getTwistTop(a, b, d, L, X, Y, Z)

    ax.plot_trisurf(*vectTop(X, Y, Z), color = 'blue')

    X, Y = getBase(b, d, X, Y)
    xb, yb, zb = vectBase(X, Y, 0)
    ax.plot_trisurf(xb, yb, zb, color = 'red')

    lx, ly, lz = getVectLegs(X, Y, Z)
    for j in range(6):
        ax.plot_wireframe(lx[j], ly[j], lz[j], linewidths = 5, colors='gray')

    # # (Optional assignment)
    # # Create an animated gif with a 360 degrees rotation
    # angles = [45 * sin(x / 20) for x in range(126)]
    #
    # rotanimate(ax, angles,'fig' + str(i+1) + '.gif', elev = 15, delay = 5)

# Animation (Optional assignment)
if input("See plots with animation? y/N ") == "y":
    times = ""
    while(times.isdigit() is False):
        times = input("Iterations: ")

    files = []
    ax = make3dfig()
    L = [-1, 0, 1.05, 2.09, 3.14, 4.19, 5.24]
    legs = []

    ax.plot_trisurf(xb, yb, zb, color='red')

    for i in range(int(times)):
        # angle = 45 * sin(i / 20)
        # ax.view_init(elev = 15, azim = angle)

        X, Y, Z = solve([2.5 * sin(i/10 + x) + 11.5 for x in L])
        surf = ax.plot_trisurf(*vectTop(X, Y, Z), color = 'blue')

        X, Y = getBase(b, d, X, Y)
        xb, yb, zb = vectBase(X, Y, 0)
        lx, ly, lz = getVectLegs(X, Y, Z)

        for j in range(6):
            legs.append(ax.plot_wireframe(lx[j], ly[j], lz[j], linewidths = 7, colors = 'gray'))

        # # Saves and adds a picture to a series of pictures
        # fname = '%s%03d.png'%('tmprot_', i)
        # ax.figure.savefig(fname)
        # files.append(fname)

        plt.pause(.001)
        ax.collections.remove(surf)
        for j in range(6):
            ax.collections.remove(legs.pop())

    # # Transforms the series of pictures into an animation
    # make_gif(files, "animation.gif", delay=5)
    #
    # for f in files:
    #     os.remove(f)

plt.show()
