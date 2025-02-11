from field_extension import create
from math import floor, isqrt
from fractions import Fraction # type: ignore

def period(n):
    Q = create(n)
    cache = {}
    x = Q(Fraction(0,1), Fraction(1,1))
    while (x.a, x.b) not in cache:
        cache[(x.a, x.b)] = len(cache)
        x = Q(1, 0) / (x - Q(floor(x.value()), 0))
    return len(cache) - cache[(x.a, x.b)]

ans = 0
for i in range(1, 10001):
    if isqrt(i) ** 2 == i:
        continue
    if period(i) % 2 == 1:
        ans += 1
print(ans)