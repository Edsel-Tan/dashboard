from prime import primes
import math
import random # type: ignore

n = 13082761331670030

p = primes(10**6)
pf = []

for i in p:
    if i > math.isqrt(n):
        pf.append(n)
        break
    while n%i == 0:
        pf.append(i)
        n = n//i

def ppf(n):
    output = []
    for i in p:
        if i > math.sqrt(n):
            output.append(n)
            break
        if n%i == 0:
            output.append(i)
        while n%i == 0:
            n = n // i
    return output


def check(g, i):
    for j in ppf(i-1):
        if pow(g, i//j, i) == 1:
            return False
    return True
    

m = [[1]]

for i in pf[1:]:
    if i % 3 != 1:
        m.append([1])
        continue
    g = random.randint(1, i-1)
    while not check(g, i):
        g = random.randint(1, i-1)

    a = []
    for j in range(3):
        a.append(pow(g, j * (i//3), i))
    m.append(a)

def crt(a, x, b, y):
    return (x*(pow(x,-1,y)*b) + y*(pow(y,-1,x)*a)) % (x*y)

n = 13082761331670030

import itertools
ans = 0
for i in itertools.product(*tuple(m)):
    a = 0
    x = 1
    for j in range(len(i)):
        a = crt(a, x, i[j], pf[j])
        x = x * pf[j]
    ans += a

print(ans-1)
