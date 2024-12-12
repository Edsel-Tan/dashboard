from math import exp, pi

idx = {}

n = 10000

f = lambda x: exp(x) - 1

for m in range(2, 2*n+1):
    if f(m/n) > pi:
        break


for a in range(0, m+1):
    for b in range(a, m+1):
        c = f(a/n) + f(b/n)
        if c > pi:
            break
        idx[c] = (a, b)

x = sorted(idx.keys())
mn = 1
ans = None

for i in x:
    l = 0
    r = len(x)-1
    v = pi - i

    while r-l:
        m = (l+r)//2
        if x[m] < v:
            l = m+1
        else:
            r = m
    
    if l > 0:
        if abs(pi - x[l-1] - i) < mn:
            mn = abs(pi - x[l-1] - i)
            ans = (idx[x[l-1]], idx[i])
        
    if abs(pi - x[l] - i) < mn:
        mn = abs(pi - x[l] - i)
        ans = (idx[x[l]], idx[i])

z = 0
for i in ans:
    a,b = i
    z += a*a + b*b
print(z)