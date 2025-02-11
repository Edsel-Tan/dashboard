n = 200
k = [1,2,5,10,20,50,100,200]

dp = [0 for i in range(n+1)]
dp[0] = 1

for i in k:
    for j in range(n-i+1):
        dp[j+i] += dp[j]
print(dp[n])