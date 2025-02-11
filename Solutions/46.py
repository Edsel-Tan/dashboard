from prime import primes
from math import isqrt
n = 10**6
p = set(primes(n))

for i in range(3, n+1, 2):
    if i in p:
        continue
    
    b = True
    for j in range(1, isqrt(i)):
        if i - 2*j*j in p:
            b = False
            break
    if b:
        print(i)
        break
