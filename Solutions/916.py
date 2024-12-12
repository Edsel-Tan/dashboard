mod = 10**9 + 7

n = 10**8
m = [1]
for i in range(1,2*n+5):
    m.append((m[-1] * i) % mod)

def c(n, r):
    return (m[n] * pow(m[r], -1, mod) * pow(m[n-r], -1, mod)) % mod

def nara(n, r):
    if r == 1:
        return 1
    return (c(n, r-1) * c(n-1, r-1) * pow(r, -1, mod)) % mod

def cata(n):
    return (c(2*n, n) * pow(n+1,-1,mod)) % mod

print((cata(n) ** 2 + (cata(n+1) - cata(n))**2) % mod)