from prime import memoize
n = 10000
s = [0,0,1]
for i in range(2,n+1):
    s.append((1+s[-1]) ^ (1+s[-2]))
m = 10**18
u = 8192

dp = [[0 for i in range(u)] for j in range(n+1)]
dp[2][0] = 1
for i in range(3):
    dp[3][i] = 1

for i in range(4, n+1):
    for j in range(u):
        l = (j^(1+s[i-2]))-1
        r = (j^(1+s[i-1]))-1
        if l == -1:
            dp[i][j] += 1
        else:
            dp[i][j] += dp[i-1][l]
        if r == -1:
            dp[i][j] += 1
        else:
            dp[i][j] += dp[i-2][r]
        dp[i][j] %= m

print(dp[n][0])