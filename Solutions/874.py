from prime import primes

p = primes(100000)

ans = 0

dp = [[0 for i in range(7000)] for j in range(6999)]
for i in range(7000):
    dp[0][i] = p[i]
for j in range(1,6999):
    for i in range(7000):
        if j < 100:
            for k in range(0,7000):
                dp[j][i] = max(dp[j-1][(i-k)%7000] + p[k], dp[j][i])
        else:
            for k in range(6900,7000):
                dp[j][i] = max(dp[j-1][(i-k)%7000] + p[k], dp[j][i])

for i in range(0, 6999):
    j = (p[7000]-i-1)%7000
    ans = max(ans, (p[7000]-i-1)*p[6999] + dp[i][j])
print(ans)
