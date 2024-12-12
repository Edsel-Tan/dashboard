from prime import primes
import math

n = 2*10**6
p = primes(2*n)
lp = [2 for i in range(n+1)]

def f(k):
    x = k
    output = 0
    for i in p:
        if i > math.sqrt(x):
            break
        while x % i == 0:
            x = x//i
            output = i
    return max(output, x)


tans = 0
for i in range(1, n+1):
    tans += max(f(i+1), f(i**2-i+1))-1
print(tans)