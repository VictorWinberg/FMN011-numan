import math

def bisection(f, a, b, sigma):
    while (b - a) / 2.0 > sigma:
        c = (a + b) / 2.0 # midpoint
        if f(c)*f(a) > 0:
            a = c;
        elif f(c)*f(b) > 0:
            b = c;
        print(c)
    accurancy = (b - a) / 2.0
    print(accurancy)
    print(c)
    print(f(c))
    return f(c)

def fixedPoint(f, x_i):
    for n in range(0, 1000):
        try:
            x_i = f(x_i)
        except:
            print("None")
            return
    print(x_i)
    print(f(x_i))

def newton(f, x_i, dx, dfi):
    for n in range(0, 1000):
        try:
            x_i -= f(x_i)/dfi(f, x_i)
        except:
            print("None")
            return
    return x_i

def secant(f, x_prev, x_i, dx, dfi):
    for n in range(0, 1000):
        temp = x_i
        div = (f(x_i) - f(x_prev))
        if div == 0:
            return x_i
        x_i -= (f(x_i) * (x_i-x_prev)) / div
        x_prev = temp
    return x_i
