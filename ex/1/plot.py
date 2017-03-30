# -*- coding: utf-8 -

import numpy as np
import matplotlib.pyplot as plt

def plot(x, f, roots, ylim = None, title = "Title"):
    dx = x[1] - x[0]
    
    def df(f) : return np.gradient(f(x), dx)

    for k in range(1, 3):
        plt.subplot(2, 1, k)
        if k == 1:
            if(title):
                plt.title(title)
            for i in range(0, len(f)):
                plt.plot(x, f[i](x), label=f[i].__name__)
            plt.plot(x, x, 'k--', label='x')
        elif k == 2:
            for i in range(0, len(f)):
                plt.plot(x, df(f[i]), label='d' + f[i].__name__)
            plt.plot(x, np.ones(x.size), 'k--', label='+-1')
            plt.plot(x, -np.ones(x.size), 'k--')

        for i in range(0, len(roots)):
            plt.axvline(x=roots[i], color='r', linestyle='dashed')

        plt.legend(loc='upper left')
        plt.axhline(y=0, color='k')
        plt.axvline(x=0, color='k')
        if(ylim):
            plt.gca().set_ylim([ylim[0], ylim[1]])
    plt.show()
