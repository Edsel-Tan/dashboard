n = 10**8
s = 10**6

from prime import memoize, primes

@memoize
def f(t, x):
    if x < 0:
        return 0
    if x == 0:
        return 1
    if len(t) <= 1:
        if sum(t) >= x:
            return 1
        else:
            return 0
    if sum(t) < x:
        return 0
    ans = 0
    for i in range(t[0]+1):
        ans += f(t[1:], x - i)
    return ans

p = primes(n+1)

ans = 0

for i in range(n//s):
    fs = [[] for i in range(s+1)]
    start = i*s + 1
    end = min((i+1)*s + 1, n+1)
    offset = i*s + 1

    for j in p:
        if j > end:
            break
        for k in range(start + (-start % j), end, j):
            fs[k-offset].append(1)
        k = j * j
        while k <= end:
            for l in range(start + (-start % k), end, k):
                fs[l-offset][-1] += 1
            k *= j
    
    for j in range(start, end):
        ans += f(tuple(sorted(fs[j-offset])), sum(fs[j-offset])//2)
    
print(ans)
        