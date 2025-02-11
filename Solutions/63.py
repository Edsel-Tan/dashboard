ans = 0

for i in range(1, 10):
    c = 1
    x = i**c
    while len(str(x)) == c:
        ans += 1
        c += 1
        x = i**c
print(ans)