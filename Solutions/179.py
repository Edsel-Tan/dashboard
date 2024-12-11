from prime import primes
import math

n = 10**7
p = primes(n)

def factors(n):
    """Returns number of factors of n"""

    output = 1
    counter = 0
    while n > 1:
        e = 1
        while n%p[counter] == 0:
            n = n//p[counter]
            e += 1
        output *= e
        counter += 1
        if counter >= len(p):
            break
        if p[counter] > math.isqrt(n):
            break
    if n != 1:
        output *= 2
    return output

prev = 1
curr = 1
ans = 0
for i in range(2, n):
    curr = factors(i)
    if curr == prev:
        ans += 1
    prev = curr

print(ans)

