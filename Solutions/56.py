def s(n):
    return sum([int(i) for i in str(n)])

ans = (0,0)
for a in range(1, 101):
    for b in range(1, 101):
        x = a**b
        ans = max(ans, (s(x), x))
print(ans[0])