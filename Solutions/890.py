import sys
sys.setrecursionlimit(5000)

from prime import memoize
k = 1
mod = 10**9+7
n = 7 ** 777

fac = [1]
facinv = [1]
for i in range(1,10000):
    fac.append((fac[-1] * i) % mod)
    facinv.append(pow(fac[-1], -1, mod))

def c(n, r):
    return (fac[n] * facinv[n-r] * facinv[r]) % mod


@memoize
def f(n, k):
    # print(n,k)
    if n < 0:
        return 0
    if n == 0:
        return 1
    if n == 1:
        return k
    if n == 2:
        return (k*(k+1))//2 + 1
    if n % 2 == 1:
        ans = 0
        for j in range(1, k+1, 2):
            ans = (ans + f(n//2-j//2, k+1) * c(k, j))%mod
        return ans
    else:
        ans = 0
        for j in range(0, k+1, 2):
            ans = (ans + f(n//2-j//2, k+1) * c(k, j))%mod
        return ans

print(f(n,k))