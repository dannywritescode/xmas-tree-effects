
# Author: Daniel Fernandes

# Each light smoothly glows on for a fraction of the time.
# You can control that fraction by adjusting n.
# They slowly change color while they are on,
# creating a calming yet chaotic effect!

from math import *
import colorsys

length = 72 * 8
n = 7 # the LEDs will be on for 1/n of the time

def effect(storage, positions, frame):
    rgb = []
    # calculate rgb for each light
    for i, led in enumerate(positions):
        x, y, z = led['x'], led['y'], led['z']
        v = norm(wave(n * tau * frame / length + i * i * x * y * z))
        hue = norm(sin(2 * tau * frame / length + (x + y + z)))
        rgb.append(list(colorsys.hsv_to_rgb(hue, 1, v)))

    return storage, rgb


def frame_max():
    # length of the animation
    return length


def frame_rate():
    # frame rate
    return 30

def norm(x): return x * 0.5 + 0.5

def wave(x):
    # negative cosine wave, 1/n of the time
    if ((x / tau) % n > 1): return -1
    else: return -cos(x)

