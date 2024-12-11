from prime import primes
import math

m = 1
n = 10**m
t = math.isqrt(n)+1
p = primes(2*t)

def factors(n):
    output = 1
    for pi in p:
        if pi > n:
            break
        count = 0
        while n % pi == 0:
            count += 1
            n = n // pi
        output *= (count+1)
    if n > 1:
        output *= 2
    return output

sols = 0
for m in range(1, 10):
    n = 10**m
    t = math.isqrt(n)+1
    p = primes(2*t)
    for a in range(1, m+1):
        for b in range(1,m+1):
            sols += factors((2**a + 5**b) * 2 ** (m-a) * 5 ** (m-b))
            # print((2**a + 5**b) * 2 ** (m-a) * 5 ** (m-b), a, b, factors((2**a + 5**b) * 2 ** (m-a) * 5 ** (m-b)))

    for a in range(0, m+1):
        for b in range(0, m+1):
            sols += factors((1 + 2**a * 5 ** b ) * 2 ** (m-a) * 5 ** (m-b))
    
print(sols)
        

