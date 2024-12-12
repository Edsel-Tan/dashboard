n = 5**10

from math import isqrt
from prime import primes

p = set(primes(2*n))
cp = {}

for a in range(isqrt(2*n)+1):
    for b in range(a, isqrt(2*n) + 1):
        if a**2 + b**2 in p:
            cp[a**2+b**2] = complex(a,b)

pf = [[] for _ in range(2*n+1)]
for i in p:
    for j in range(i, 2*n+1, i):
        pf[j].append(i)
        pf[j].append(1)
    j = i*i
    while j < 2*n+1:
        for k in range(j, 2*n+1, j):
            pf[k][-1] += 1
        j *= i

sols = set()
sols.add((0,0,n))


for x in range(0, n):
    m = {}
    for i in range(len(pf[n-x])//2):
        m[pf[n-x][2*i]] = pf[n-x][2*i+1]
    
    for i in range(len(pf[n+x])//2):
        if pf[n+x][2*i] not in m:
            m[pf[n+x][2*i]] = 0
        m[pf[n+x][2*i]] += pf[n+x][2*i+1]
    
    possible = True

    for i in m:
        if m[i] % 2 and i % 4 == 3:
            possible = False

    if not possible:
        continue

    output = [complex(1,0)]
    m = list(zip(m.keys(), m.values()))
    for y,z in m:
        new_output = []
        if y % 4 == 3:
            c = y ** (z//2)
            for i in output:
                new_output.append(i * c)
        elif y % 4 == 2:
            c = cp[y] ** (z)
            for i in output:
                new_output.append(i * c)
        else:
            for i in output:
                for j in range(z+1):
                    new_output.append(cp[y] ** j * cp[y].conjugate() ** (z - j) * i)
        output = new_output

    for sol in output:
        y = int(abs(sol.real))
        z = int(abs(sol.imag))
        sols.add(tuple(sorted([x,y,z])))



ans = 0
for a,b,c in sols:
    mul = 8 * 2**10
    if a == 0:
        mul = mul//2
    if b == 0:
        mul = mul//2
    if a == b:
        ans += 3 * mul * (a+b+c)
    elif b == c:
        ans += 3 * mul * (a+b+c)
    else:
        ans += 6 * mul * (a+b+c)
print(ans)