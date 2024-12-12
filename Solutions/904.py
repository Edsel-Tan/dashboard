import math

L = 10**10
ll = math.isqrt(L) + 1

def angle(triangle):
    a,b,c = triangle
    return (math.atan(2*a/b) + math.atan(2*b/a))/math.pi * 180 - 90

def peri(triangle):
    return (L//triangle[2]) * sum(triangle)

n = 45000
angles = []
for i in range(1, n+1):
    angles.append(i**(1/3))
best_approx = [(math.inf,()) for i in range(n)]

for x in range(1, ll+1):
    for y in range(x+1, ll+1, 2):
        if math.gcd(x, y) > 1:
            continue
        if x**2 + y**2 > L:
            continue
        t = (y**2-x**2, 2*x*y, y**2+x**2)
        a = angle(t)

        l = 0
        r = n-1
        while (r-l):
            m = (l+r)//2
            if angles[m] > a:
                r = m
            else:
                l = m+1

        if l > 0:
            if best_approx[l-1][0] > abs(a - angles[l-1]):
                best_approx[l-1] = (abs(a - angles[l-1]), t)
        if best_approx[l][0] > abs(a - angles[l]):
            best_approx[l] = (abs(a - angles[l]), t)

ans = 0
for x,y in best_approx:
    ans += peri(y)
print(ans)
            
