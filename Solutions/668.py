from prime import iter_number_of_primes, primes
from math import isqrt

n = 10**10
m = isqrt(n)
p = primes(m)

ans = n
for i in p:
    ans -= i

dp = iter_number_of_primes(n)

for j in range(1,m):
    ans -= (dp[-j] - dp[-j-1]) * j

print(ans)