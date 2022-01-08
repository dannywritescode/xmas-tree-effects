
# Author: Daniel Fernandes

# Similar to radar.py but the direction of rotation oscillates too
# Added a peaks variable to adjust the number of peaks in the wave

from math import *
import colorsys

peaks = 3
length = 72 * 8

def effect(storage, positions, frame):
    rgb = []
    # calculate rgb for each light
    for i, led in enumerate(positions):
        x, y, z = led['x'], led['y'], led['z']

        sine = sin(peaks * theta(x, y) + 2 * tau * sin(tau * frame / length))

        v = norm(sine)

        hue = norm(sin(tau * frame / length + pi / 2))

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
