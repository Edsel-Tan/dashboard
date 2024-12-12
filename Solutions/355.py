n = 200000
from prime import primes

p = primes(n)
pf = [[] for i in range(n+1)]
x = {}

for i in p:
    for j in range(i, n+1, i):
        pf[j].append(i)

for i in range(2, n+1):
    y = 1
    for j in pf[i]:
        y *= j
    x[y] = i

y = {}
for i in x:
    y[i] = x[i]

for i in x:
    for j in x:
        if i * j > n:
            break
        if i * j in y:
            y[i*j] = max(y[i*j], x[j] + x[i])

d = []
for i in y:
    if y[i] - x[i]:
        d.append(i)
for i in d:
    del y[i]


ans = 0
pos = []
for i in y:
    if len(pf[i]) == 1:
        pos.append((0, y[i]))
    else:
        c = 0
        for j in x:
            if j >= i:
                break
            if i % j == 0:
                c = max(c, x[j] + x[i//j])
        pos.append((y[i] - c, y[i]))

pos = sorted(pos, reverse=True)
s = set()
z = []
for j in range(len(pos)):
    a,b = pos[j]
    d = True
    for i in pf[b]:
        if i in s:
            d = False
            break
    if d:
        for i in pf[b]:
            s.add(i)
        ans += b
        z.append(j)

m = ans
print(m)