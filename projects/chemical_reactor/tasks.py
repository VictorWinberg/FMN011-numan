from scipy.interpolate import CubicSpline
from scipy.optimize import fsolve
import matplotlib.pyplot as plt
import numpy as np

depth = [0, 0.5, 1, 1.5, 2, 2.5, 3]
temperature = [70, 70, 55, 22, 13, 10, 10]

cs = CubicSpline(depth, temperature, bc_type='clamped')

plt.figure()
plt.plot(depth, temperature, 'o', label='data')
plt.axhline(y = 0, color='k')

x = np.linspace(0, 3, num=100)

plt.plot(x, cs(x), label="S")
plt.plot(x, cs(x, 1), label="S'")
plt.plot(x, cs(x, 2), label="S''")

plt.legend(loc='best')

root = fsolve(cs, 1.2, args=2)
plt.axvline(x = root, color='k', linestyle='dashed')
print(root)

plt.show()
