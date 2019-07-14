R = 0.01097
m = 1


def Lambda(n):
    return 1 / (R * (1 / (m ** 2) - 1 / (n ** 2)))


for n in [2, 3]:
    print("For n = {}, the emission line wavelength is {}nm".format(
        n, round(Lambda(n))
    ))