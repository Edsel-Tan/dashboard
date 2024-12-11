dp_inc = [[1 for i in range(9)] for j in range(100)]
dp_dec = [[1 for i in range(10)]for j in range(100)]
dp_dec[0][0] = 0

for i in range(1, 100):
    for j in range(0,10):
        dp_dec[i][j] = sum(dp_dec[i-1][j:])
    for j in range(0,9):
        dp_inc[i][j] = sum(dp_inc[i-1][:j+1])

ans = [9]
for i in range(1,100):
    ans.append(ans[-1] + sum(dp_inc[i]) + sum(dp_dec[i]) - 9)
print(ans[-1])