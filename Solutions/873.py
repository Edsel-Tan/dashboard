a = 10**6
b = 10**7
c = 10**8
# a, b, c = 2, 2, 4
# a, b, c = 4,4,44
m = 10**9+7

f = [1]
fi = [1]
for i in range(1, a+b+c+1):
    f.append((i * f[-1]) % m)
    fi.append((fi[-1] * pow(i, -1, m)) % m)


def choose(n,r):
    if n < 0:
        return 0
    if r > n or r < 0:
        return 0
    return (f[n] * fi[r] * fi[n-r]) % m


ans = 0

for chunks in range(2,2*(min(a,b))+2):
    c1 = chunks//2
    c2 = chunks - c1

    ans += choose(a - 1, c1 - 1) * choose(b - 1, c2 - 1) * choose(c + a + b - 2 * (chunks - 1), a + b)
    ans = ans % m

    c1 = c1 + c2
    c2 = c1 - c2
    c1 = c1 - c2

    ans += choose(a - 1, c1 - 1) * choose(b - 1, c2 - 1) * choose(c + a + b - 2 * (chunks - 1), a + b)
    ans = ans % m

print(ans)