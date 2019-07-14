from math import sqrt


a = 9.81
u = 0
x = 100
t = (-u + sqrt(u ** 2 + 2 * a * x)) / a

print("It takes the ball {}s to drop {}m starting at {}ms^-1".format(
    round(t, 2), x, u))