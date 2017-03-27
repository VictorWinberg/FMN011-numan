import math
from scipy.misc import derivative

def df(f, x):
    dx = x[1] - x[0]
    return np.gradient(f(x), dx)

def dfi(f, x_i, sigma):
    return derivative(f, x_i, dx = sigma)

def bisection(f, a, b, sigma):
    while (b - a) / 2.0 > sigma:
        c = (a + b) / 2.0 # midpoint
        if f(c)*f(a) > 0:
            a = c;
        elif f(c)*f(b) > 0:
            b = c;
        print(c)
    accuracy = (b - a) / 2.0
    return {'f(c)': f(c), 'c': c, 'accuracy': accuracy}

def fixedPoint(f, x_i, sigma):
    for n in range(0, 1000):
        try:
            error = abs(f(x_i) - x_i)
            if(error < sigma):
                return {'res': f(x_i), 'error': error}
            x_i = f(x_i)
        except OverflowError:
            return {'error': math.inf}
    return {'res 1': x_i, 'res 2': f(x_i), 'error': abs(f(x_i) - x_i)}

def newton(f, x_i, sigma):
    for n in range(0, 1000):
        try:
            x_prev = x_i

            # TODO: CHANGE THIS
            if dfi(f, x_i, sigma) == 0:
                return x_i

            x_i -= f(x_i)/dfi(f, x_i, sigma)
            # x_i -= f(x_i)/(f(x_i + sigma) - f(x_i))/sigma
            if 2 * abs(x_i - x_prev) / abs(x_i + x_prev) < sigma * 2:
                return x_i
        except OverflowError:
            return x_prev
    return x_i

def secant(f, x_prev, x_i):
    for n in range(0, 1000):
        temp = x_i
        div = (f(x_i) - f(x_prev))
        if div == 0:
            return x_i
        x_i -= (f(x_i) * (x_i-x_prev)) / div
        x_prev = temp
    return x_i
