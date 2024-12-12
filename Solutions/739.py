n = 10**8
mod = 10**9+7
f = [1]
fi = [1]

for i in range(1, 2*n+1):
    f.append((f[-1] * i) % mod)
    fi.append(pow(f[-1], -1, mod))

def young(n,k):
    return ((f[n+k] * (n - k + 1)) % mod * fi[k] * fi[n+1]) % mod

ans = 0

l = [0,1,3]
for i in range(n):
    l.append((l[-1] + l[-2]) % mod)


ans = 0
for i in range(2,n+1):
    ans = (ans + young(n-2, n-i) * l[i]) % mod

print(ans)