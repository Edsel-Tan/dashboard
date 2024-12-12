from prime import primes

n = 10**8 * 5
t = [i for i in range(n+1)]
p = primes(n+1)

for i in p:
    for j in range(i, n+1, i):
        t[j] = t[j]//i * (i-1)

ans = 0
for i in range(1, n+1, 2):
    ans += t[i]
print(ans)