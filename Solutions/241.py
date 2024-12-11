from prime import primes, memoize
from fractions import Fraction # type: ignore
import math

n = 10**18
m = math.isqrt(n)
o = math.isqrt(m)
p = primes(o)

# @memoize
def pf(x):
    output = []
    for i in p:
        if x % i == 0:
            output.append(i)
        while x % i == 0:
            x = x//i
    if x > 1:
        output.append(x)
    return output

def exp(x, b):
    output = 0
    while x % b == 0:
        x = x // b
        output += 1
    return output

pos = []

for i in range(3, 17, 2):
    f = Fraction(i, 2)
    for j in range(1, 30):
        pos.append([pow(2, j), f * Fraction(pow(2, j), pow(2,j+1)-1), set([2])])


ans = set()
while len(pos) > 0:
    t = pos[-1]
    del pos[-1]

    if t[1].denominator == 1:
        if t[1].numerator == 1:
            if t[0] < n:
                ans.add(t[0])
            continue
        else:
            continue

    if t[0] * t[1].denominator > n:
        continue

    q = pf(t[1].denominator)
    b = max(q)
    e = exp(t[1].denominator, b)

    if b in t[2]:
        continue
    t[2].add(b)

    s = [t[0] * pow(b, e), t[1] * Fraction(pow(b, e), (pow(b, e+1) - 1) // (b - 1)), t[2].copy()]
    while s[0] < n:
        pos.append(s)
        e += 1
        s = [t[0] * pow(b, e), t[1] * Fraction(pow(b, e), (pow(b, e+1) - 1) // (b - 1)), t[2].copy()]

print(sum(ans))