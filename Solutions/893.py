m = [6,2,5,5,4,5,6,3,7,6]

def cost(x):
    ans = 0
    while x > 0:
        ans += m[x%10]
        x = x//10
    return ans

k = 6
n = 10**k

dp1 = [0 for i in range(n+1)]
dp2 = [0 for i in range(n+1)]

import math
for i in range(1, n+1):
    dp1[i] = cost(i)
    for j in range(1, math.isqrt(n)+1):
        if i%j == 0:
            dp1[i] = min(dp1[i], dp1[i//j] + 2 + dp1[j])

c = [[] for i in range(7*k+1)]

for i in range(1, n+1):
    dp2[i] = min(cost(i), dp1[i])
    for j in c[:dp2[i]//2+1]:
        for k in j:
            dp2[i] = min(dp2[k] + 2 + dp2[i-k], dp2[i])
    c[dp2[i]].append(i)

print(sum(dp2[1:]))