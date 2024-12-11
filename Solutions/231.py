n = 20000000
r = 15000000

from prime import primes

p = primes(n)

def vp(n, i):
    output = n
    while n > 0:
        output -= n % i
        n = n//i
    return output // (i-1)

ans = 0
for i in p:
    ans += i * (vp(n, i) - vp(r, i) - vp(n-r, i))
print(ans)