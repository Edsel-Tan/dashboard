from fractions import Fraction
from prime import primes
import math

n = 80
p = 8
ans = set()

def find(v, curr, summ, r):
    if v == 0:
        ans.add(tuple(sorted(r)))
        return 1
    if len(curr) == 0 or summ < v:
        return 0
    
    rr = r.copy()
    rrr = r.copy()
    rr.append(math.isqrt(curr[0].denominator))
    return find(v-curr[0], curr[1:], summ-curr[0], rr) + find(v, curr[1:], summ-curr[0], rrr)

# def all(v, curr, result):
#     if len(curr) == 0:
#         if v.denominator % 32 != 0:
#             print(v, result)
#     else:
#         r = result.copy()
#         rr = result.copy()
#         r.append(curr[0])

#         all(v+curr[0], curr[1:], r)
#         all(v, curr[1:], rr)

# all(0, [Fraction(1, i**2) for i in range(p, n+1, p)], [])

p = primes(n+1)
pp = primes(10)
for i in pp:
    p.remove(i)
p.append(25)
p.append(16)

t = []
for i in range(2, n+1):
    a = True
    for j in p:
        if i % j == 0:
            a = False
    if a:
        t.append(i)

t = sorted(t)
t.remove(27)
t.remove(54)
t.remove(49)
s = [Fraction(1, i**2) for i in t]
find(Fraction(1,2), s, sum(s), [])
find(Fraction(1,2) - Fraction(1, 144), s, sum(s), [])
print(len(ans))