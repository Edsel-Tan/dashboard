n = 30

dp = [[0 for i in range(7)] for j in range(n)]

dp[0] = [0,1,1,0,1,0,0]
for i in range(1, n):
    dp[i][0] = 3 * dp[i-1][0] + dp[i-1][3] + dp[i-1][4] + dp[i-1][5] + 2 * dp[i-1][6]
    dp[i][1] = dp[i-1][1] + dp[i-1][2] + dp[i-1][3]
    dp[i][2] = dp[i-1][1]
    dp[i][3] = dp[i-1][2]
    dp[i][4] = dp[i-1][1] + dp[i-1][2] + dp[i-1][3] + dp[i-1][4] + dp[i-1][5] + dp[i-1][6]
    dp[i][5] = dp[i-1][4]
    dp[i][6] = dp[i-1][5]

print(sum(dp[n-1]) - dp[n-1][0])
