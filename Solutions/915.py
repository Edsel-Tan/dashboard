from math import gcd, isqrt

n = 10**8
m = 123456789

from prime import primes, memoize

@memoize
def f(n):
    if n == 1:
        return 1
    ans = (n * n) % m
    s = set()
    for i in range(1, isqrt(n) + 1):
        s.add(n//i)
        s.add(i)
    s = sorted(s)
    for i in range(len(s)-1):
        ans = (ans - (n//s[i] - n//s[i+1]) * f(s[i])) % m
    return ans

g = lambda x: ((x-1)**3 + 2) % m

s = [0,1]
seen = set(s)
x = g(s[-1])
while x not in seen:
    s.append(x)
    seen.add(x)
    x = g(x)

soffset = s.index(x)
scyc = len(s) - soffset

def smod(n):
    if n < soffset:
        return s[n]
    return s[(n-soffset)%scyc + soffset]

g = lambda x: ((x-1)**3 + 2) % scyc

ss = [0,1]
seen = set(ss)
x = g(ss[-1])

while x not in seen:
    ss.append(x)
    seen.add(x)
    x = g(x)


ssoffset = ss.index(x)
sscyc = len(ss) - ssoffset



def ssmod(n):
    if n <= 4:
        return smod(s[n])
    return smod(ss[(n-ssoffset)%sscyc + ssoffset] + scyc)


ans = 0
for i in range(1, n+1):
    ans = (ans + f(n//i) * ssmod(i)) % m
print(ans)