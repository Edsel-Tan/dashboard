from prime import primes
import math

n = 10**6
sn = math.isqrt(n)
p = primes(n)

ans = 0
for i in range(1, sn):
    j = (i+1) ** 3 - i ** 3
    if j in p:
        ans += 1

print(ans)