from fractions import Fraction #type: ignore

s = [290797]
t = [s[0] % 2000 - 1000]

n = 100
for i in range(2*n):
    s.append((s[-1] ** 2) % 50515093)
    t.append(s[-1] % 2000 - 1000)

from math import gcd

lines = {}

for i in range(1,n+1):
    for j in range(i+1, n+1):
        a = t[2*i] - t[2*j]
        b = t[2*j-1] - t[2*i-1]
        c = t[2*i-1] * t[2*j] - t[2*j-1] * t[2*i]
        k = gcd(a,b,c)
        if a: 
            r = abs(a) // a
        else:
            r = abs(b) // b
        a = a // k * r
        b = b // k * r
        c = c // k * r

        v = (a, b, c)
        g = gcd(a, b)
        key = (a//g, b//g)

        if key not in lines:
            lines[key] = set()
        lines[key].add(v)

ans = 0
l = 0
for i in lines:
    l += len(lines[i])

for i in lines:
    ans += (l - len(lines[i])) * len(lines[i])
print(ans)