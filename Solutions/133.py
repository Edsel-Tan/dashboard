import math
from prime import primes

n = 100000
p = primes(n)
t = math.floor(math.log(n, 2))
sols = set()

for i in range(0, t+1):
    for j in p:
        if pow(10, 10**i, 9*j) == 1:
            sols.add(j)

print(sum(p) - sum(sols))
