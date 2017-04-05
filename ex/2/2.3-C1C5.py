import math
import numpy as np
from numpy.linalg import solve, norm, inv

def sol(n):
    A = np.matrix([[5 / (i + 2*j - 1) for j in range(1, n+1)] for i in range(1, n+1)])
    x = np.matrix(np.ones(n)).T
    b = A*x

    x_c = solve(A, b)

    cond = norm(A, math.inf)*norm(inv(A), math.inf)
    print("cond(A) =", cond)

    rel_fwd_error = norm(x - x_c, math.inf) / norm(x, math.inf)
    print("FE =", rel_fwd_error)

    rel_back_error = norm(b - A*x_c, math.inf) / norm(b, math.inf)

    emf = rel_fwd_error / rel_back_error if rel_back_error else 0
    print("EMF =", emf)

for n in range(6, 15):
    print(" --- n = ", n, " ---")
    sol(n)
    print()
