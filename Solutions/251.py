import math
from prime import segmented_sieve

n = 110000000
m = math.isqrt(n)
l = n//7
bound = math.sqrt((9*n**3)/(7**3))

ans = 0

for x in range(1, m+1):
    for y in range(1, m+1, 2):
        if math.gcd(x, y) != 1:
            continue

        if x*y > bound:
            break
        
        r1 = x-1
        r2 = (5*y**2-5)//8
        r = x*pow(x,-1,y**2)*r2 + (y**2)*pow(y**2,-1,x)*r1
        r = r%(x*y**2)

        v = (n-(3*r+2)-((r+1)*y)//x-((8*r+5)*x**2)//(y**2))//(3*x*y**2+y**3+8*x**3)+1
        if v > 0:
            ans += v

            for k in range(v):
                a = 3*k*x*y**2+3*r+2
                b = (k*x*y**2+r+1)//x * y
                c = (8*k*x*y**2+8*r+5)//(y**2) * x**2

print(ans)




        

        



