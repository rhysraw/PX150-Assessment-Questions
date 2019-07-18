from math import pi


G = 6.67 * 10 ** -11
M = 5.97 * 10 ** 24
R = 6371 * 10 ** 3


def satellite(T):
    h = ((G * M * T ** 2)/(4 * pi ** 2)) ** (1/3) - R
    # this conditional excludes non-sensical orbits of zero or negative altitudes and oribital periods
    if h > 0 and T > 0:
        return h
