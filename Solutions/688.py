n = 10**16
k = 1
f = lambda x: (x*(x+1))//2
mod = 10**9+7
ans = 0

while f(k) <= n:
    x = n - f(k) + 1
    y = x%k
    ans = (ans + (k-y) * f((x//k)%mod) + y * f((x//k)%mod + 1))%mod
    k += 1

print(ans)