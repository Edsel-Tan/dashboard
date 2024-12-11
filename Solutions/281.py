from prime import primes

p = primes(100)
def prime_factorize(n): 
    factors = [1]
    for i in p:
        if n % i == 0:
            nf = []
            e = 0
            while n % i == 0:
                e += 1
                n = n // i
            for j in range(e+1):
                for k in factors:
                    nf.append(k * i**j)
            factors = nf
    return factors


def c(n, r):
    output = 1
    for i in range(r):
        output *= n - i
        output //= (i+1)
    return output

t = 1
while c(2*t, t) / (2*t) < 10**15:
    t += 1

import math
def g(m, n):
    return (math.factorial(m*n)) // (math.factorial(n)**m)

def f(m, n):
    fix = 0
    for i in range(1,n+1):
        d = math.gcd(i, n)
        fix += g(m, d)
    return fix // (m*n)


ans = 0
for n in range(1, t):
    m = 2
    v = f(m, n)
    while v <= 10**15:
        ans += v
        # print(v, n, m)
        m += 1
        v = f(m, n)

print(ans)
    