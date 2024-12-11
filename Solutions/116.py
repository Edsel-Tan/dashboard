n = 50

dp = [[1,1],[1,1,1],[1,1,1,1]]

for i in range(n):
    dp[0].append(dp[0][-2] + dp[0][-1])
    dp[1].append(dp[1][-3] + dp[1][-1])
    dp[2].append(dp[2][-4] + dp[2][-1])

print(dp[0][50] + dp[1][50] + dp[2][50] - 3)