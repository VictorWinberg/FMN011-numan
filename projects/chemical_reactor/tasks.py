from scipy.interpolate import CubicSpline
from scipy.integrate import simps
from scipy.optimize import fsolve
import matplotlib.pyplot as plt
import numpy as np

# Measured temperatures at different depths
depths = [0, 0.5, 1, 1.5, 2, 2.5, 3]
temperature = [70, 70, 55, 22, 13, 10, 10]

# Task 1 - clamped cubic spline
cs = CubicSpline(depths, temperature, bc_type='clamped')

# Task 2 - determine the thermocline depth
root = fsolve(cs, 1, args=2)[0]
print('thermocline depth: ' + str(root))
plt.text(0.05, 150, 'thermocline depth: ' + str(round(root, 2)) + 'm')

# Task 3 - compute the flux
# = -cs(x, 1)
def flux(x):
    return -cs(x, 1)

# Task 4 - plot data with curve with first and second derivate
x = np.linspace(-0.5, 4.5, num=100)

plt.plot(depths, temperature, 'o', label="data")

plt.axhline(y = 0, color='k')
plt.axvline(x = 0, color='k')

plt.plot(x, cs(x), label="S")
plt.plot(x, cs(x, 1), label="S'")
plt.plot(x, cs(x, 2), label="S''")

plt.plot(x, -cs(x,1), label='Heat flux')

plt.annotate('Thermical depth = ' + str(round(root, 3)) + 'm', xy = (root, cs(root, 2)), xytext = (1.8, -100), arrowprops = dict(facecolor='black', shrink = 0.05))

plt.axvline(x = root, color='k', linestyle='dashed', label='Thermical depth')

plt.legend(loc='upper right')

# Task 5
# temperature at a depth of 1.7 m
depth = 1.7
temp = cs(depth)

plt.plot(depth, temp, 'o')
print('temp at depth 1.7m: ' + str(temp))
plt.text(0.05, 130, 'temp at depth 1.7m: ' + str(np.round(temp, 2)) + u'\N{DEGREE SIGN}C')

# depth at which the temperature is 50 ◦C.
temp = 50
depth = fsolve(lambda x: cs(x) - temp, 1)[0]

plt.plot(depth, temp, 'o')
print('depth at 50 deg: ' + str(depth))
plt.text(0.05, 110, u'depth at temp 50\N{DEGREE SIGN}C: ' + str(round(depth, 2)) + 'm')

plt.show()
