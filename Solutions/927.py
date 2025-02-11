from prime import primes

g = lambda p, k: lambda x: (pow(x, k, p) + 1) % p
n = 10**7
p = primes(n)

def h(p, k):
    s = set()
    x = 1
    f = g(p, k)
    while x not in s:
        s.add(x)
        x = f(x)
    return 0 in s

px = []
for i in p:
    if i % 4 == 3:
        continue
    j = i-1
    t = True
    for k in p:
        if k > j:
            break
        if j % k == 0:
            t = t and h(i, k)
            while j % k == 0:
                j = j//k
    if t:
        px.append(i)

s = [1]
for i in px:
    ss = []
    for j in s:
        k = i * j
        if k <= n:
            ss.append(k)
    s.extend(ss)
print(sum(s))