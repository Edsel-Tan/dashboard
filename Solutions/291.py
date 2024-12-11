from prime import miller_rabin
import math

n = 5*10**15
t = math.isqrt(n)
mb = lambda x:miller_rabin(x, 5)
sieve = [True for i in range(t+1)]
f = lambda x:2*x**2+2*x+1

p = [5,13,17,29,37,41,53,61,73,89,97]

for i in p:
    for j in range(1, i+1):
        if f(j) % i == 0:
            for k in range(j, t+1, i):
                sieve[k] = False

ans = 0
i = 1
v = f(i)
while v < n:
    if sieve[i]:
        if mb(v):
            ans += 1
    i += 1
    v = f(i)

print(ans)
    
