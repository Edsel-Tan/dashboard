n = 10**16

f = lambda y: lambda x: x*x + x*y + 41*y*y

l = 0
r = n

ans = 0

while r-l:
    m = (l+r+1)//2
    if f(m)(-m/2) > n:
        r = m-1
    else:
        l = m

from math import isqrt
ans += isqrt(n) * 2 

for i in range(1, l+1):
    g = f(-i)
    x = (i+1)//2
    y = n+x
    while y-x:
        m = (y+x+1)//2
        if g(m) > n:
            y = m-1
        else:
            x = m
    ans += (2*x - i + 1)*2

print(ans)