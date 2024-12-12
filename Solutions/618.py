f = [0,1]

k = 23
for i in range(k):
    f.append(f[-1] + f[-2])

from prime import primes, memoize

n = f[-1]
p = primes(n+1)
mod = 10**9

mem = [[-1 for x in range(len(p)+1)] for i in range(n+1)]

def s(x, i):
    if mem[x][i] != -1:
        return mem[x][i]
    if x == 0:
        return 1
    if i == len(p):
        return 0
    if p[i] > x:
        return 0
    ans = 0
    c = 1
    for j in range(0, x+1, p[i]):
        ans = (ans + c * s(x-j,i+1)) % mod
        c = (c * p[i]) % mod
    mem[x][i] = ans
    return ans

ans = 0
for i in f[2:]:
    ans = (ans + s(i, 0)) % mod
print(ans)