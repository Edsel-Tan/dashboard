from prime import primes

p = set(primes(10**7))

ans = (0, 0)
for a in range(-999,1000):
    for b in range(-1000,1001):
        f = lambda x: x*x + a*x + b
        for i in range(1000):
            if f(i) not in p:
                break
        ans = max(ans, (i, a*b))
print(ans[1])
