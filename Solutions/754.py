n = 10**8

isPrime = [True for _ in range(n+1)]
mobius = [1 for _ in range(n+1)]
cnt = [n-i for i in range(n+1)]

for i in range(2,n+1):
    if isPrime[i]:
        for j in range(i,n+1,i):
            isPrime[j] = False
        for j in range(i**2,n+1,i**2):
            mobius[j] = 0
        for j in range(i,n+1,i):
            mobius[j] = -mobius[j]

for i in range(2,n+1):
    for j in range(i,n+1,i):
        cnt[j] += (n-j)//i * mobius[i]

ans = 1
mod = 10**9+7
for i in range(2,n+1):
    ans = (ans * pow(i, cnt[i], mod)) % mod

print(ans)
