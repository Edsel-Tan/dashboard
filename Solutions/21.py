n = 10000
f = [0 for i in range(n+1)]

for i in range(1, n+1):
    for j in range(i*2, n+1, i):
        f[j] += i

ans = 0
for i in range(1, n+1):
    if f[i] <= n and f[f[i]] == i and f[i] != i:
        ans += i
print(ans)