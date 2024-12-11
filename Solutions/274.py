import math
from prime import primes

n = 10**7
p = primes(n)
p.remove(2)
p.remove(5)

ans = 0
for i in p:
    ans += pow(10, -1, i)
print(ans)
