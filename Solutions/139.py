n = 10**8
import math
t= math.isqrt(n)

ans = 0
sols = set()

for x in range(1,t+1):
    for y in range(1, x): 
        if math.gcd(x,y) != 1:
            continue
        a = 2*x*y
        b = x**2 - y**2
        c = x**2 + y**2 

        if math.gcd(a, b) != 1:
            continue

        if a + b + c < n and c % (abs(b-a)) == 0:
            sols.add(tuple(sorted((a,b,c))))
            ans += n // (a + b + c)

print(ans)

