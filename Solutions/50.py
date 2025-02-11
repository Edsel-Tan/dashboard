from prime import primes

n = 10**6
p = primes(n)
s = set(p)

ans = (0, 0)
for i in range(len(p)):
    c = 0
    for j in range(i, len(p)):
        c += p[j]
        if c in s:
            ans = max((j-i+1, c), ans)
        if c > n:
            break
print(ans[1])