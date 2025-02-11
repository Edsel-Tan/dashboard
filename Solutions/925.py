from math import isqrt

def d(x):
    y = x % 10
    while x > 0:
        if x % 10 < y:
            return True
        y = x % 10
        x = x//10
    return False

def g(x):
    z = x % 10
    d = []
    while True:
        d.append(x % 10)
        if x % 10 < z:
            break
        z = x % 10
        x = x // 10
    original = 0
    for i in reversed(d):
        original *= 10
        original += i
    y = d[-1]
    for i in d:
        if i > y:
            break
    d.remove(i)
    next = i
    for i in sorted(d):
        next *= 10
        next += i
    return next - original

n = 10 ** 16
mod = 10 ** 1
s = set()

ans = (n*(n-1)*(2*n-1))//6

for i in range(1, mod):
    s.add(i)

while mod < n:
    toremove = []
    tadd = []
    for i in s:
        if d((i * i) % mod):
            toremove.append(i)
    for i in toremove:
        s.remove(i)
        tmod = mod
        while i < n:
            ans += g((i * i)) * (max(n//tmod, 1))
            i = 10*i
            tmod = 10*tmod
    ns = set()
    for i in s:
        for j in range(10):
            ns.add(j * mod + i)
    mod = mod * 10
    s = ns


for i in s:
    if i == 0:
        continue
    while i < n:
        if d(i * i):
            ans += g(i*i)
        else:
            ans -= i * i
        i = 10*i

print(ans % (10 ** 9 + 7))