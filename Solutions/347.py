from prime import primes

n = 10**7
p = primes(n+1)

ans = 0
for i in range(len(p)):
    for j in range(i+1, len(p)):
        if p[i] * p[j] > n:
            break

        z = p[i] * p[j]
        m = z
        while z <= n:
            x = z
            while x * p[i] <= n:
                x = x * p[i]
            m = max(m, x)
            z *= p[j]
        ans += m

print(ans)

