n = 10**18 * 2
from math import isqrt, gcd, sqrt, floor
from fractions import Fraction # type: ignore

ans = 0
ideal_range = floor(sqrt(n/(4+4*sqrt(2)))) + 10**7 * 9 - 10**6 * 5
search = 10**6 * 2
for x in range(ideal_range - search, ideal_range + search):
    y = isqrt(n-x**2)
    if y < x:
        break
    while (x % 2 == y % 2 or gcd(x, y) > 1) and y > 0:
        y -= 1
    if y == 0:
        continue
    ans = max(ans, Fraction(2*x*y*(y**2-x**2), 2*x*y + 2*y**2) )
    
print(ans)