from prime import primes
import math

p = primes(190)


o = 1
for i in p:
    o *= i
g = math.isqrt(o)
ans = 0

x = len(p)//2
f = [1]
for i in p[:x+1]:
    df = []
    for j in f:
        df.append(j)
        if j*i < g:
            df.append(j*i)
    f = df

f = sorted(f)

s = [1]
for i in p[x+1:]:
    ds = []
    for j in s:
        ds.append(j)
        if j*i < g:
            ds.append(j*i)
    s = ds

s = sorted(s)

def binary_search(t, l, r, v):
    if (l == r):
        return t[l]
    if (r - l <= 1):
        if t[r] <= v:
            return t[r]
        return t[l]

    
    m = (l+r)//2

    if t[m] <= v:
        return binary_search(t, m, r, v)
    else:
        return binary_search(t, l, m, v)

    
ans = 0
for i in f:
    ans = max(ans, binary_search(s, 0, len(s)-1, g//i) * i)
print(ans%(10**16))