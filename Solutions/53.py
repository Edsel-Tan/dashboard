from math import comb
l = 10**6
n = 100
ans = 0
for i in range(1, n+1):
    for j in range(i+1):
        if comb(i, j) > l:
            ans += 1
print(ans)