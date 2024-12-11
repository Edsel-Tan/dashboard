"""
(900 - 3n)r^(n+1) + (3n - 897)r^n - 900r + 899 = -600 000 000 000 (r-1)^2
x≈1.002322108767227506139404881237042643482
"""


n = 5000

def g(x):
    return (900*(x**n - 1) - 3*n*(x**n)) / (x-1) + (3 * (x**n-1)) / ((x-1)**2) + 600000000000


lower = 1.001
upper = 1.005
tolerance = 10 ** (-15)

while (upper - lower) > tolerance:
    middle = (upper+lower)/2
    if g(middle) > 0:
        lower = middle
    else:
        upper = middle

print("{:.12f}".format(lower))