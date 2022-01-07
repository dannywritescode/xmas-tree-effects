
# Author: Daniel Fernandes

# The colors rotate around the z-axis
# For best results, view from the top of the tree.

from math import *
import colorsys

length = 72 * 4

def effect(storage, positions, frame):
    rgb = []
    # calculate rgb for each light
    for i, led in enumerate(positions):
        x, y, z = led['x'], led['y'], led['z']

        v = norm(sin(2 * theta(x, y) + 4 * tau * frame / length))

        hue = norm(sin(0.5 * tau * frame / length))

        rgb.append(list(colorsys.hsv_to_rgb(hue, 1, v)))

    return storage, rgb


def frame_max():
    # length of the animation
    # var length is used in hue calculation, so the animation loops
    return length


def frame_rate():
    # frame rate
    return 30

def norm(x): return x * 0.5 + 0.5

def theta(x, y):
    if y == 0: y = nextafter(x, 1)
    theta = atan(x / y)
    if (y < 0): return theta + pi
    elif (x < 0): return theta + tau
    else: return theta
