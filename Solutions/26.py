n = 1000

ans = (0, 0)
for i in range(2, n):
    if i % 2 == 0 or i % 5 == 0:
        continue
    for j in range(1, i):
        if pow(10, j, i) == 1:
            break
    ans = max(ans, (j, i))

print(ans[1])
    