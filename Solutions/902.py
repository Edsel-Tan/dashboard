m = 100
n = m*(m+1)//2
p = 10**9+7

cycles = [None]

f = lambda x: (p*x)%n + 1
fi = lambda x: (x-1)*pow(p,-1,n)%n if x != 1 else n
from math import isqrt
def g(x):
    if isqrt(8*x+1)**2 == 8*x+1:
        k = (-1+isqrt(8*x+1))//2
        return k*(k-1)//2+1
    return x+1

h = lambda x:fi(g(f(x)))

for i in range(1,n+1):
    cycle = []
    s = set()
    curr = i
    while curr not in s:
        s.add(curr)
        cycle.append(curr)
        curr = h(curr)
    cycles.append(cycle)

fac = [1]
for i in range(1, n+1):
    fac.append((fac[-1] * i) % p)

ans = fac[m]
for x in range(1, n+1):
    c = (fac[m] * pow(len(cycles[x]), -1, p)) % p
    for y in cycles[x]:
        ans = (ans + (y-1) * (fac[n-x] * c)) % p

from math import gcd, lcm
for x in range(1, n+1):
    for y in range(1, x):
        a = gcd(len(cycles[x]), len(cycles[y]))
        b = lcm(len(cycles[x]), len(cycles[y]))
        c = (fac[m] * pow(b, -1, p)) % p
        for i in range(len(cycles[x])):
            for j in range(i%a, len(cycles[y]), a):
                if cycles[y][j] < cycles[x][i]:
                    ans = (ans - c * fac[n-x]) % p


print(ans)