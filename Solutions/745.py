import math

n = 10**14
m = math.isqrt(n)
p = 10**9+7

cnt = [(i**2)%p for i in range(m+1)]

ans = 0
for i in range(1, m+1):
    ans += cnt[i] * (n//(i**2)) % p
    ans = ans % p
    for j in range(2*i, m+1, i):
        cnt[j] -= cnt[i]
print(ans)