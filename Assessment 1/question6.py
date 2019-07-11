from math import log, pi


M = 67
rho = 1.038
c = 3.7
K = 0.0054
Tw = 100
Ty = 70
const_term = (M ** (2/3) * c * rho ** (1/3)) / (K * pi ** 2 * (4 * pi / 3) ** (2/3))


def time(T0):
    log_term = log(0.76 * (T0 - Tw) / (Ty - Tw))
    return const_term * log_term


for T0 in [4, 20]:
    t = time(T0)
    print("It takes {}s for an egg yolk to reach {}°C starting from {}°C".format(
        round(t), Ty, T0
    ))