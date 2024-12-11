
from prime import memoize

@memoize
def S(n):
    if n == 0:
        return 0
    if n <= 4:
        return 1
    x = 1
    while 2*x < n:
        x *= 2
    

    return 2 * S(n-x) + S(x)

print(S(10**12))

