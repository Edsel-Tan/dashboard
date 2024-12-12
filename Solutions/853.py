from prime import primes

n = 120
m = 10**9
f = [0,1]
for i in range(2, n+1):
    f.append(f[-1] + f[-2])

import math
t = f[-1] - f[-2] + 1
t = math.gcd(f[-1], t)

factors = []
for i in range(2, m):
    if t % i == 0:
        factors.append(i)

ofactors = []
for i in range(1, n):
    if n % i == 0:
        ofactors.append(i)

# print(factors, ofactors)
# print(f)

s = []
for j in ofactors:
    t = f[j] - f[j-1] + 1
    t = math.gcd(t, f[j])
    s.append(t)


ans = 0
for i in factors:
    t = True
    for j in s:
        if j % i == 0:
            t = False
            break
    if t:
        # print(i)
        ans += i
print(ans)