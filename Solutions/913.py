

from math import lcm, gcd, isqrt
from prime import primes, miller_rabin

n = 10**5
p = primes(n)

pf = [{} for i in range(n+1)]
for x in p:
    for i in range(x, n+1, x):
        pf[i][x] = 1
    j = x*x
    while j < n+1:
        for k in range(j, n+1, j):
            pf[k][x] += 1
        j *= x

def getpf(n):
    return pf[n]

def factorize(m):
    if m <= n:
        return getpf(m)
    if miller_rabin(m):
        return {m:1}
    pf = {}
    for i in p:
        if i * i > m:
            if m > 1:
                pf[m] = 1
            break

        if m % i == 0:
            pf[i] = 0
            while m % i == 0:
                m = m//i
                pf[i] += 1
    return pf


def add(pf, x, y):
    if x not in pf:
        pf[x] = 0
    pf[x] += y

def upper(pf, x, y):
    if x not in pf:
        pf[x] = 0
    pf[x] = max(y, pf[x])

def factors(pf):
    output = [1]
    for p in pf:
        noutput = []
        for j in range(pf[p]+1):
            c = p ** j
            for i in output:
                noutput.append(c*i)
        output = noutput
    return output

def order(x, m, pf):
    for i in pf:
        if pow(x, i, m) == 1:
            return i
                
def orbits(x, m, pf):
    o = {}
    for p in pf:
        tpf = {p:pf[p]-1}
        tmp = factorize(p-1)
        for i in tmp:
            tpf[i] = tmp[i]
        tmp = factorize(order(x, p**pf[p], factors(tpf)))
        for i in tmp:
            upper(o, i, tmp[i])
    
    n = 1
    for i in o:
        n *= i ** o[i]
    f = factors(o)
    d = dict(zip(f, [0 for i in f]))
    ans = 0
    for i in f:
        t = pow(x, i, m)
        g = gcd(t-1, m)
        c = g - d[i]
        ans += c * n//i
        for j in f:
            if j % i == 0:
                d[j] += c
    return ans//n

def f(x, y):
    return orbits(x, x*y-1, factorize(x*y-1))

ans = 0
for x in range(2, 101):
    for y in range(x, 101):
        ans += x*y - f(x, y) - 1


z = 101
ans = 0
for x in range(2, z):
    for y in range(x, z):
        ans += ((x**4)*(y**4)) - 1 - f(x**4, y**4)



ans = 0
for x in range(2, z):
    for y in range(x, z):
        tpf = {}
        for t in [factorize(x*y-1), factorize(x*y+1), factorize(x*x*y*y+1)]:
            for i in t:
                add(tpf, i, t[i])
        test = 1
        for i in tpf:
            test *= i ** tpf[i]
        ans += x**4*y**4 - 1 - orbits(x**4, x**4*y**4-1, tpf)
        
print(ans)