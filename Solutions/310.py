n = 100000
s = [0]
import math
for i in range(1, n+1):
    m = set()
    for j in range(1, math.isqrt(i)+1):
        m.add(s[i-j**2])
    l = 0
    while l in m:
        l += 1
    s.append(l)

states = [0 for i in range(128)]
for i in s:
    states[i] += 1

nstates = [states[i] for i in range(128)]

for k in range(2):
    s = [0 for i in range(128)]
    for i in range(128):
        for j in range(128):
            s[i^j] += nstates[i] * states[j]
    nstates = s
print((nstates[0] - 3*(n+1)*states[0] + 2*states[0])//6 + states[0]*(n+1))


