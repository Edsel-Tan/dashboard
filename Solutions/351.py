from prime import primes, memoize
import math

n = 100000
p = primes(n)

@memoize
def f(n):
    if n <= 1:
        return 0
    ans = (n*(n-1))//2
    prev = 0
    for i in range(2, math.isqrt(n)+1):
        ans -= f(n//i)
        prev = n//i
    for i in range(math.isqrt(n), 0, -1):
        if i == prev:
            continue
        ans -= f(i) * (n//i - ((n)//(i+1)))
    return ans

def g(n):
    return (n*(n-1))//2 - f(n)

ans = g(n) * 6 + 6 * (n-1)
print(ans)