def C(n,r):
    if r > n // 2:
        r = n - r

    output = 1
    for i in range(r):
        output *= n-i
        output = output // (i+1)
    return output


n = 50
ans = 0
for i in range((n+1)//4 + 1):
    m = i * 4 - 1
    ans += C(n-m + 2*i, 2*i)
print(ans)