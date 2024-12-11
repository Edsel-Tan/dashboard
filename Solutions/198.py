from fractions import Fraction # type: ignore
import math

n = 10**8


def farey(a, b):
    if a*b*2 > n:
        return 0
    
    
    output = 1
    output += math.floor(n/(2*a**2) - b / a)
    output += math.floor(n/(2*b**2) - a / b)


    c = a + b
    d = c + a
    g = farey(d, c)
    while g != 0:
        output += g
        c = d
        d = d + a
        g = farey(d, c)
    
    c = a + b
    d = c + b
    g = farey(c, d)
    while g != 0:
        output += g
        c = d
        d = d + b
        g = farey(c, d)

    return output

ans = farey(1, 51)
for i in range(100, 51, -1):
    ans -= farey(i, i-1)
print(ans)
