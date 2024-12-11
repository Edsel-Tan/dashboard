from prime import primes
import math
import random # type: ignore

n = 50000000

p = primes(math.ceil(n * math.sqrt(2)))
# print(len(p))
p8 = []
for i in p:
    if i % 8 == 7 or i % 8 == 1:
        p8.append(i)

# print(len(p8))

def t(n):
    return 2*n**2 - 1

def rt(n, p):
    if p % 4 == 3:
        return pow(n, (p+1)//4, p)
    
    q = p - 1
    s = 0
    while q % 2 == 0:
        s += 1
        q = q//2

    z = random.randrange(1, p)
    while pow(z, (p-1)//2, p) == 1:
        z = random.randrange(1, p)

    m = s
    c = pow(z, q, p)
    r = pow(n, (q+1)//2, p)
    t = pow(n, q, p)


    while t != 1:
        s = 0
        t_ = t
        while t_ != 1:
            s += 1
            t_ = pow(t_, 2, p)

        b = pow(c, pow(2, m-s-1, p-1), p)
        m = s
        c = pow(b, 2, p)
        t = (t * c) % p
        r = (r * b) % p

    return r

sieve = [True for i in range(n+1)]

ans = 0

for p in p8:
    rsq = 1 * pow(2, -1, p)
    r = rt(rsq, p)
    if r > p - r:
        r = p - r
    
    if t(r) == p:
        # print(p)
        ans += 1

    # print(rsq, r, p)

    sieve[r:n+1:p] = [False for i in range(r, n+1, p)]
    sieve[p-r:n+1:p] = [False for i in range(p-r, n+1, p)]


for i in range(2, n+1):
    if sieve[i]:
        ans += 1

print(ans)