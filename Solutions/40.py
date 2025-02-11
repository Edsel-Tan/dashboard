from math import isqrt

def f(n):
    a = 9
    b = 1
    while n >= a*b:
        n -= a*b
        a *= 10
        b += 1
    return str(10**(b-1) + n//b)[n%b]

ans = 1
for i in range(7):
    ans *= int(f(10**i-1))
print(ans)