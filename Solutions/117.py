n = 50
dp = [1,1,2,4]

for i in range(n):
    dp.append(dp[-1] + dp[-2] + dp[-3] + dp[-4])

print(dp[50])

