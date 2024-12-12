from prime import primes

def vp(n, p):
    ans = 0
    while n >= p:
        ans += 1
        n = n//p
    return ans

n = 10**8
p = primes(n+1)
mod = 10**9+7

ans = 1
for i in p:
    ans = (ans * pow(i, vp(n,i), mod))%mod
print((ans*2)%mod)