n = 1000
f = [0 for i in range(n+1)]

from math import isqrt, gcd

for a in range(2, isqrt(n)+1):
    for b in range((a+1)%2, a, 2):
        if gcd(a, b) != 1:
            continue
        x = 2*a*(a+b)
        if x > n:
            break
        for i in range(x, n+1, x):
            f[i] += 1

ans = (0, 0) 
for i in range(1, n+1):
    ans = max(ans, (f[i], i))
print(ans[1])