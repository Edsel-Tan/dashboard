from prime import primes, miller_rabin  

p = primes(5000)
m = 10**16

n = sum(p)
dp = [0 for i in range(n+1)]
dp[0] = 1
cs = 0
for i in p:
    cs += i
    for j in range(cs, i-1, -1):
        dp[j] += dp[j-i]
        dp[j] = dp[j] % m
ans = 0
for i in range(2, n+1):
    if miller_rabin(i):
        ans += dp[i]
        ans = ans % m
print(ans)
