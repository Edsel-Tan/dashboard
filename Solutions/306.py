n = 10 ** 6
ans = n - n//4 + 1 + ((n//4) - 8) // 17 * 7
m = (n//4 - 8)
k = [3,4,8,9,12,13]
for i in k:
    if m%17 >= i:
        ans += 1
print(ans)