from prime import memoize, primes
import math

n = 4*10**7
p = primes(n)

totient = [i for i in range(n+1)]
dp = [None for i in range(n+1)]
dp[1] = 1
for i in p:
    for j in range(i, n+1, i):
        totient[j] = totient[j]//i * (i-1)

ans = 0
for i in range(2, n+1):
    dp[i] = dp[totient[i]] + 1

for i in p:
    if dp[i] == 25:
        ans += i

print(ans)

    