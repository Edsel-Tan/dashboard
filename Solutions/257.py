import math

def irt(x):
    y = math.isqrt(x)
    if y**2 == x:
        return y
    return 0

def solve2(b, c):
    d = irt(b**2+c**2+6*b*c)
    if d:
        if (d-b-c) % 2 == 0 and (d-b-c) > 2*(c-b):
            return (d-b-c)//2
    return 0

def solve3(b, c):
    d = irt(b**2+c**2+10*b*c)
    if d:
        if (d-b-c) % 2 == 0 and (d-b-c) > 2*(c-b):
            return (d-b-c)//2
    return 0

ans = 0
l = 10**8
ans += l//3

s = set()
for n in range(1, math.isqrt(l)):
    for m in range(6*n+1, 8*n):
        if math.gcd(m, n) != 1:
            continue
        c = 2*m*n
        b = m**2 + 8*n**2 - 3*c
        a = m**2 - 8*n**2 - b - c
        a = a//2
        if a + b + c > 16*l:
            break
        if c >= 2*b:
            continue
        if c < b:
            break
        d = math.gcd(a,b,c)
        a = a//d
        b = b//d
        c = c//d
        if (a, b, c) not in s:
            if a+b+c <= l:
                s.add((a,b,c))
                ans += l//(a+b+c)

s = set()
for n in range(1,  math.isqrt(l)):
    for m in range(8*n+1, 10*n):
        if math.gcd(m, n) != 1:
            continue
        c = 2*m*n
        b = m**2 + 24*n**2 - 5*c
        a = m**2 - 24*n**2 - b - c
        a = a//2
        if a + b + c > 48*l:
            break
        if c >= 2*b:
            continue
        if c < b:
            break
        d = math.gcd(a,b,c)
        a = a//d
        b = b//d
        c = c//d
        if (a, b, c) not in s:
            if a+b+c <= l:
                s.add((a,b,c))
                ans += l//(a+b+c)

print(ans)