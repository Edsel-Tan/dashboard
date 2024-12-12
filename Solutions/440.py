
from prime import miller_rabin
from matrix import Matrix
mod = 987898789
M = Matrix([[10,1],[1,0]])
v = Matrix([[1],[0]])

def gcd(a,b,x,y):
    if a == 0:
        if x == -1:
            return b,y
        return -1, -1
    
    return gcd(b%a, a, pow(-x, b//a) * y, x)
    

def f(x):
    return (M.fastexp(x, mod) * v).entries[1][0]

def g(x, y):
    m = M.fastexp(1, mod)
    for i in range(y):
        m = m.fastexp(x, mod)
    return (m * v).entries[0][0]

p = 987898789
n = 2000
cnt = [1 for i in range(n+1)]
two = 0
for a in range(1, n+1):
    for b in range(a+1, n+1):
        x,y = gcd(a,b,1,1)
        if x == -1:
            two += 2
        else:
            cnt[x] += 2

ans = 0
for c in range(1, n+1):
    m = M.fastexp(c, mod)
    for i in range(1, n+1):
        ans = (ans + cnt[i] * (m*v).entries[0][0]) % mod
        m = m.fastexp(c, mod)
    

ans += (n//2 + n%2) * two * 10
ans += (n//2) * two


print(ans % mod)