from math import exp, pi, sqrt

s = 2
x = 1
m = 0
f1 = exp(-0.5 * ((x - m) / s) ** 2) / (sqrt(2 * pi) * s)
print("The function f(x) evaluated at x = 1 yields {}".format(round(f1, 3)))
