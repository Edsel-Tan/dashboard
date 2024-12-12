from prime import miller_rabin

n = 10**12
h = [1]
p = [2,3,5]

for i in p:
    l = len(h)
    x = i
    while x <= n:
        for j in range(l):
            if h[j] * x > n:
                continue
            h.append(h[j] * x)
        x *= i

h = sorted(h)
mod = 2**32
t = []

for i in h:
    if i+1 > 5 and miller_rabin(i+1):
        t.append(i+1)

f = [1]
for i in t:
    l = len(f)
    for j in range(l):
        if f[j] * i > n:
            continue
        f.append(f[j] * i)

f = sorted(f)

ans = 0
for i in f:
    for j in h:
        if i * j > n:
            break
        ans = (ans + i*j) % mod
print(ans)
