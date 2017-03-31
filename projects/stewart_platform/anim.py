from mpl_toolkits.mplot3d import axes3d
import os

# Creates a series of pictures
def make_views(ax, angles, elev = None, width=4, height = 3, prefix='tmprot_'):
    files = []
    ax.figure.set_size_inches(width, height)

    for i, angle in enumerate(angles):
        ax.view_init(elev = elev, azim = angle)
        fname = '%s%03d.png'%(prefix, i)
        ax.figure.savefig(fname)
        files.append(fname)

    return files

# Transforms a series of pictures into an gif-animation
def make_gif(files, output, delay=20, repeat=True):
    loop = -1 if repeat else 0
    os.system('convert -delay %d -loop %d %s %s'
              %(delay,loop," ".join(files),output))


# Creates a rotating animation
def rotanimate(ax, angles, output, elev = None, delay = 20):
    files = make_views(ax, angles, elev = elev)

    make_gif(files, output, delay = delay)

    for f in files:
        os.remove(f)
