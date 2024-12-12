n = 10**5
mod = 10**9+7

s = {}
from itertools import product

for i,j,k,l in product(range(3), repeat=4):
    s[(i,j,k,l)] = 0

for i in range(3):
    k = [0 for _ in range(4)]
    k[0] = 1
    k[i] += 1
    k[3] = i
    s[tuple(k)] = 3

for _ in range(n-1):
    ns = {}
    for i in s:
        ns[i] = 0
    
    for i in s:
        k = list(i)
        k[k[3]] = (k[k[3]]+1)%3
        k = tuple(k)
        ns[k] = (ns[k] + 4 * s[i]) % mod
        for j in range(1,3):
            k = list(i)
            k[3] = (k[3] + j) % 3
            k[k[3]] = (k[k[3]]+1)%3
            k = tuple(k)
            ns[k] = (ns[k] + 3 * s[i]) % mod
    s = ns

ans = 0
for i in s:
    c = 0
    for j in i[:3]:
        c += 1 if j == 2 else 0
    if c%3 == 0:
        ans = (ans + s[i]) % mod

print(ans)