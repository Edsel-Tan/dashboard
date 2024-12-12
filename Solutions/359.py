x = 71328803586048
from math import isqrt

def f(n,r):
    if n == 1:
        return (r*(r+1))//2
    c = n//2
    if (n+r)%2:
        return ((r+2*c-1)*(r+2*c))//2 - c
    else:
        return ((r+2*c-1)*(r+2*c))//2 + c

mod = 10**8
ans = 0
for j in range(1, isqrt(x)+1):
    if x % j == 0:
        ans = (ans + f(j, x//j) + f(x//j, j)) % mod

print(ans)