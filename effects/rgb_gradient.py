
# Author: Daniel Fernandes

# A simple RGB gradient created using three sine waves, one
# for each channel, that are equally offset form each other.

from math import *

length = 72 * 2

def effect(storage, positions, frame):
    rgb = []
    # calculate rgb for each light
    for i, led in enumerate(positions):
        x, y, z = led['x'], led['y'], led['z']
        r, g, b = 0, 0, 0
        r = sin(z + tau * frame / length) * 0.5 + 0.5
        g = sin(z + tau * frame / length + tau / 3) * 0.5 + 0.5
        b = sin(z + tau * frame / length + 2 * tau / 3) * 0.5 + 0.5
        rgb.append([r, g, b])

    return storage, rgb


def frame_max():
    # length of the animation
    return length


def frame_rate():
    # frame rate
    return 30

