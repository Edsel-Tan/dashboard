n = 10**6

p = []
isPrime = [True for i in range(n+1)]
factors = [[] for i in range(n+1)]

for i in range(2, n+1):
    if isPrime[i]:
        p.append(i)
        for j in range(i, n+1, i):
            isPrime[j] = False
            factors[j].append(i)
        isPrime[i] = True

s = set()
z = []
for i in range(3, n+1, 10):
    for j in factors[i]:
        if j in s:
            break
    else:
        if isPrime[i]:
            s.add(i)
        else:
            z.append((i, factors[i]))


while len(z) > 0:
    cnt = {}
    for i in z:
        for j in i[1]:
            if j in cnt:
                cnt[j] += 1
            else:
                cnt[j] = 1

    m = max(cnt.values())
    for i in sorted(cnt.keys()):
        if cnt[i] == m:
            a = i
            s.add(i)
            break
    
    nz = []
    for i in z:
        if a not in i[1]:
            nz.append(i)
    z = nz

ans = 0
from math import log
for i in s:
    ans += log(i)

print("{:.6f}".format(ans))