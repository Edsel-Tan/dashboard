n = 1000

ans = 0
for a in range(1, n):
    for b in range(a, n-a):
        c = n - a - b
        if a*a + b*b == c*c:
            ans = a*b*c
print(ans)