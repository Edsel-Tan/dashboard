from prime import iter_number_of_primes, primes
import math

n = 10**12
m = math.isqrt(n)
p = primes(m+1)

mod = 10**9 + 7

ans = 0

for i in p:
    j = i
    while j < n:
        c = n//j
        ans = (ans + 2*c*(n-c)) % mod
        j *= i

p = primes(m+1)

s = set()
for i in range(1, m+1):
    s.add(n//i)
    s.add(i)
s = sorted(s)

f = lambda x : x - 1 if x <= m else len(s) - (n // x) 

dp = [i for i in s]

for i in range(len(p)):
    for j in range(len(s)-1, -1, -1):

        if s[j] < p[i] * p[i]:
            break
        
        dp[j] -= dp[f(s[j]//p[i])] - (i+1)

for i in range(len(dp)):
    dp[i] = (dp[i] - 1) % mod

for i in range(1, m):
    ans = (ans + 2*(n%mod)*i*(dp[len(s)-i] - dp[len(s)-i-1])) % mod
    ans = (ans - 2*i*i*(dp[len(s)-i] - dp[len(s)-i-1])) % mod

print(ans)