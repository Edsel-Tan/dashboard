from prime import primes, memoize

n = 10**8
p = primes(n)
pset = set(p)
c = {}

def pi(x):
    l, r = 0, len(p)
    while r-l:
        m = (l+r)//2
        if p[m] > x:
            r = m
        else:
            l = m+1
    return l

for start in range(1, n+1):
    curr = 1 if start not in pset else 0
    start = pi(start)
    if start not in pset:
        curr += 1
    while start >= 1:
        if curr in c:
            c[curr] += 1
        else:
            c[curr] = 1
        start = pi(start)
        if start not in pset:
            curr += 1

mod = 10**9+7
ans = 1
for i in c:
    ans = (ans * c[i]) % mod
print(ans)