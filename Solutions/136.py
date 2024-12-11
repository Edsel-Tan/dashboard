#Equation reduces to (3k-z)(k+z) = n

import math

n = 50*10**6

sols = dict(zip([i+1 for i in range(n)], [0 for i in range(n)]))

for y in range(1, n+1):
    for x in range((-y)%4, 3*y, 4):
        if x == 0:
            continue
        m = x * y
        if m > n:
            break
        sols[m] += 1

ans = 0
for i in sols.keys():
    if sols[i] == 1:
        ans += 1

print(ans)
