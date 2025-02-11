ans = 0
n = 1000
m = 10**10

for i in range(1, n+1):
    ans = (ans + pow(i, i, m)) % m

print(ans)