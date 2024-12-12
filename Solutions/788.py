p = 10**9+7

n = 2022
f = [1]
fi = [1]
for i in range(n):
    f.append((f[-1] * (i+1))%p)
    fi.append(pow(f[-1], -1, p))

def c(n, r):
    return (f[n] * fi[r] * fi[n-r]) % p

ans = 0
for i in range(1, n+1):
    for j in range(i//2+1, i+1):
        ans += 10 * c(i, j) * pow(9, i-j, p)
        ans -= c(i-1, j-1) * pow(9, i-j, p)
        if i-j-1 >= 0:
            ans -= 9 * (c(i-1,j)) * pow(9, i-j-1, p)
        ans = ans % p

print(ans)
