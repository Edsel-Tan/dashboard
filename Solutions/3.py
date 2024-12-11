from prime import primes
from math import isqrt
n = 600851475143
p = primes(isqrt(n)+1)

ans = 1
for i in p:
    while n % i == 0:
        ans = i
        n = n//i
print(ans)