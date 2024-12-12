from prime import primes
from math import gcd

MAX_INT = 10**17
n = 10**16

p = primes(60)

ans = {}

def f(idx: int, factor: int, remainder: int, total: int, totalf: int):
    if factor == 1:
        if totalf not in ans:
            ans[totalf] = MAX_INT
        ans[totalf] = min(total, ans[totalf])
    if total > n:
        return
    if idx == len(p):
        return
    for i in range(idx):
        if factor % p[i] == 0:
            return
    c = 1
    e = 1
    while c * total <= n:
        nf = factor * e
        nr = remainder * c
        nt = total * c
        ntf = totalf * e
        g = gcd(nf, nr)
        nf = nf//g
        nr = nr//g
        f(idx+1, nf, nr, nt, ntf)
        e += 1
        c *= p[idx]

f(0, 1, 1, 1, 1)
print(sum(ans.values()))