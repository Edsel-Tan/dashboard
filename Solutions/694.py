from prime import primes
import math

n = 10**18
m = math.ceil(n**(1/3))
p = primes(m)

sieve = [True for i in range(m+1)]
for i in p:
    for j in range(i**2, m+1, i**2):
        sieve[j] = False

sieve2 = [i for i in range(m+1)]
for i in p:
    for j in range(i**2, m+1, i**2):
        sieve2[j] = sieve2[j]//i
    for j in range(i**3, m+1, i**3):
        sieve2[j] = 0

factors = [set() for i in range(m+1)]
for i in range(2, m+1):
    if sieve2[i] == 0:
        continue
    for j in range(sieve2[i], m+1, sieve2[i]):
        factors[j].add(i)
        factors[j].add((sieve2[i]**3)//i)
 
ans = n
for i in range(2, m+1):
    ans += n//(i**3)
    for j in factors[i]:
        ans += n//(i**3 * j)
print(ans)