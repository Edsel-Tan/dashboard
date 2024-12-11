v5 = [0]
v2 = [0]

n = 200000
for i in range(1, n+1):
    v5.append(v5[-1])
    while i % 5 == 0:
        v5[-1] += 1
        i = i // 5

for i in range(1, n+1):
    v2.append(v2[-1])
    while i % 2 == 0:
        v2[-1] += 1
        i = i // 2

ans = 0
for i in range(0, n//3 + 1):
    for j in range(i, (n-i)//2 + 1):
        k = n - i - j
        if v5[n] - v5[i] - v5[j] - v5[k] >= 12:
            if v2[n] - v2[i] - v2[j] - v2[k] >= 12:
                if i == k:
                    ans += 1
                elif i == j or j == k:
                    ans += 3
                else:
                    ans += 6
print(ans)
            


