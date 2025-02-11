k = sorted('123456789')
ans = 0
for i in range(9000, 10000):
    if sorted(str(i) + str(i*2)) == k:
        ans = max(ans, int(str(i) + str(i*2)))

print(ans)