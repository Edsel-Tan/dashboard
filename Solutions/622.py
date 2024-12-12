from prime import primes, miller_rabin
import math

ans = 0
n = 60
x = 2**(n//2)-1
y = 2**(n//2)+1

for i in range(1,n//2):
    z = 2**i-1
    g = math.gcd(z, y)
    y = y//g
    x = x*g


p = primes(10**6)
def prime_factorise(x):
    ans = {}
    for i in p:
        if x%i == 0:
            ans[i] = 0
            while x%i == 0:
                x = x//i
                ans[i] += 1
    if x > 1:
        ans[x] = 1
    return ans

def factors(pf):
    ans = [1]
    for i in pf:
        nans = []
        for j in range(pf[i]+1):
            for k in ans:
                nans.append(k*i**j)
        ans = nans
    return ans

ans = 0
x = 2**n-1
xf = factors(prime_factorise(x))
nf = factors(prime_factorise(n))
nf.remove(n)
for i in xf:
    f = True
    for j in nf:
        if pow(2, j, i) == 1:
            f = False
            break
    if f:
        ans += i+1

print(ans-2)