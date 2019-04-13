#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from numba import njit


@njit(parallel=True, fastmath=True, nogil=True)
def jit_julia_fractal(z_re, z_im, j, n=2, nmax=100, c=0.279):
    for m in range(len(z_re)):
        for n in range(len(z_im)):
            z = z_re[m] + 1j * z_im[n]
            for t in range(nmax):
                z = z**2 + c
                if np.abs(z) > 2.0:
                    j[m, n] = t
                    break


def update(c0, *args):
    global j
    jit_julia_fractal(z_real, z_imag, j, c=c0)
    im.set_data(j)


if __name__ == '__main__':
    N = 1024
    j = np.zeros((N, N), np.int64)
    z_real = np.linspace(-1.5, 1.5, N)
    z_imag = np.linspace(-1.5, 1.5, N)

    nframes = 500
    r = 0.7885
    a = np.linspace(0, np.pi * 2, nframes)
    c = r * np.cos(a) + 1.0j * np.sin(a)
    jit_julia_fractal(z_real, z_imag, j, c=c[0])

    size = np.array(j.shape)
    dpi = 80.0
    figsize = size[1] / float(dpi), size[0] / float(dpi)

    fig = plt.figure(figsize=figsize, dpi=dpi)
    fig.add_axes([0.0, 0.0, 1.0, 1.0], frameon=False)
    im = plt.imshow(j, cmap=plt.cm.jet, extent=[-1.5, 1.5, -1.5, 1.5])
    plt.axis('off')

    animation = FuncAnimation(fig, update, interval=10, frames=c)
    # animation.save('julia_set.mp4', fps = 10, dpi=dpi, bitrate=-1, codec="libx264",
    #                 extra_args=['-pix_fmt', 'yuv420p'],
    #                 metadata={'artist':'hlyang'})
    animation.save('julia_set.gif', fps=10, dpi=dpi, writer='imagemagick',
                   metadata={'artist': 'hlyang'})
    # plt.show()