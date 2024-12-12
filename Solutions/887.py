from prime import memoize
import math

cache = {}
def q(n, d):
    if d >= math.ceil(math.log2(n)):
        return math.ceil(math.log2(n))
    if d == 0:
        return n-1
    if (n, d) in cache:
        return cache[(n, d)]
    
    ans = math.inf
    for i in range(1, n):
        ans = min(ans, max(q(i, d-1), q(n-i, d+i-1))+1)
    cache[(n, d)] = ans
    return ans

p = -1
k = 1
for i in range(1, 200):
    if (q(i,k) != p):
        p = q(i,k)

n = 7**10
ans = 0
for d in range(1,8):
    left = 1
    right = 1
    c = 0
    x = 0
    while (left < n):
        ans += ((min(right+1, n+1)) - left) * c
        c += 1
        left = right+1
        right = right * 2
        if (right > (1 << (d+1))):
            x += 1
            right = right - x

ans += (n*(n-1))//2
print(ans)