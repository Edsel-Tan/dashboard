from prime import memoize
a = 21**7
b = 7**21
c = 12**7
m = 10**9


@memoize
def f(n):
    if n > b:
        return n-c
    else:
        return f(a + f(a + f(a + f(a+n))))

ans = 0
x = f(b)
d = b//a
ans = d*a*x+3*(a-c)*a*(d*(d-1))//2 - d*(a*(a-1))//2
ans %= m
e = b%a + 1
y = x + 3*d*(a-c)
ans += (e*(y+y-e+1))//2
ans %= m
print(ans)