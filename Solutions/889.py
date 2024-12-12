k,t,r = 10**18+31, 10**14+31, 62
mod = 1000062031

from math import comb

x = pow(pow(2,t,mod)+1, r, mod)
y = pow(2,k,mod)+1
ans = x * pow(2, k, mod) * k%mod
ans %= mod

p = []
for i in range(r+1):
    c = comb(r, i)
    j = 0
    while c > 0:
        if c%2:
            p.append(i*t+j)
        j += 1
        c = c//2

# print(p, ans)

prev = 0
for i in range(len(p)-1, 0, -1):
    i = p[i]
    j = k-i
    te = j-prev-1
    x = x * pow(2, te, mod) % mod
    ans += (y - 2*x) * pow(2, i+1, mod)
    x = (x * 2 - y)% mod
    ans -= pow(2, i, mod) * i * y
    prev = j

print(ans%mod)