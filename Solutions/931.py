from prime import memoize, primes, count_primes
from math import isqrt

mod = 715827883

def csqrt(n):
    l = 1
    r = n
    while r-l:
        m = (l+r)//2
        if m * m < n:
            l = m+1
        else:
            r = m
    return l

n = 10**12
m = isqrt(n)
p = primes(m+1)

s = set()
for i in range(1, m+1):
    s.add(n//i)
    s.add(i)
s = sorted(s)

f = lambda x : x - 1 if x <= m else len(s) - (n // x) 

dp2 = [(i*(i+1))//2 for i in s]

for i in range(1, len(dp2)):
    c = isqrt(s[i])
    for j in range(2, s[i]//c+1):
        dp2[i] -= dp2[f(s[i]//j)]
    for j in range(1, c):
        dp2[i] -= dp2[f(j)] * (s[i]//j - s[i]//(j+1))

dp = count_primes(n)
dp3 = count_primes(n, lambda x: x, lambda x: (x*(x+1))//2)

dp = [i%mod for i in dp]
dp2 = [i%mod for i in dp2]
dp3 = [i%mod for i in dp3]

@memoize
def h(x):
    if x == 0:
        return 0
    
    output = 0
    y = isqrt(x)
    for i in p:
        if x//i < y:
            break
        c = x//i
        while c > 0:
            output += dp2[f(c)] * (i - 1)
            c = c//i
    
    for i in range(1, y):
        output += dp2[f(i)] * (dp3[f(x//i)] - dp3[(f(x//(i+1)))] - dp[f(x//i)] + dp[(f(x//(i+1)))])
    return output%mod


@memoize
def g(x):
    if x <= 1:
        return 0
    
    output = 0
    y = isqrt(x)
    for i in p:
        if x//i <= y:
            break
        output += x//i
    
    for i in range(1, y+1):
        output += i * (dp[f(x//i)] - dp[f(x//(i+1))])
    
    return output%mod

ans = n * h(1) - g(n) * (dp2[f(1)])
for i in range(1, len(s)):
    ans += n//s[i] * (h(s[i]) - h(s[i-1])) - g(n//s[i]) * (dp2[f(s[i])] - (dp2[f(s[i-1])]))
print(ans%mod)