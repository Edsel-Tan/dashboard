from prime import primes
from fractions import Fraction #type: ignore
import math

def totient(n):
    count = 0
    for i in range(1,n+1):
        if math.gcd(i,n) == 1:
            count += 1
    return count

def prime_factorise(n):
    p = primes(n+1)

    output = []
    for i in p:
        if n % i == 0:
            power = 1
            while n % (i ** power) == 0:
                power += 1
            power -= 1
            output.append((i, power))
    return output

def factors(n):
    pf = prime_factorise(n)

    output = [1]
    for i,j in pf:
        to_append = []
        for k in range(1,j+1):
            for l in output:
                to_append.append(l * (i ** k))
        for t in to_append:
            output.append(t)
    return output

def order(d):
    posRd = sorted(factors(totient(d)))
    if d == 1:
        return 1
    for i in posRd:
        if pow(10, i, d) == 1:
            return i


total = 0

for d in range(1,10):
    for d1 in range(1,10):
        s = Fraction(d*d1, 10*d-1)
        t = order(s.denominator)
        for r in range(t, 101, t):
            if r != 1:
                s1 = pow(10*d-1, -1, 100000) * d1 * (pow(10, r, 100000) - 1)
                s1 = s1%100000
                if d1 / (10*d-1) >= 0.1:
                    total = (total + s1)%100000

print(total)
            
