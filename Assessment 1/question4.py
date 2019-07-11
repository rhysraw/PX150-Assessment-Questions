A = 1000
p = 5
n = 3
B = A * ((1 + p / 100) ** n)
print("A £{} after {} years with an interest rate of {}% will yield £{}".format(
    A, n, p, round(B, 2)
))