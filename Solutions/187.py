from prime import primes, number_of_primes
import math
import sys
sys.setrecursionlimit(2500)

n = 10**8
t = math.isqrt(n) + 1
p = primes(t)
ans = 0

for i in range(len(p)):
    ans += number_of_primes(n//p[i]) - i

print(ans)