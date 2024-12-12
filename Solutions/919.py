from math import gcd, isqrt

n = 10**7
m = 100*n

sols = set()
sols.add((1,2,2))

for p in range(1,isqrt(m//5)+1):
    l = isqrt((m-5*p*p)//3)
    for q in range(1, l+1):

        if gcd(p,q) == 1:
            continue

        a = 3*q*q+5*p*p
        b = 8*p*q
        c = abs(5*p*p - 2*p*q - 3*q*q)

        g = gcd(a,b,c)
        a,b,c = a//g, b//g, c//g

        sols.add(tuple(sorted([a,b,c])))

    # for q in range(-l, 0):

    #     a = 3*q*q+5*p*p
    #     b = -8*p*q
    #     c = -5*p*p + 2*p*q + 3*q*q

    #     if c <= 0:
    #         continue

    #     g = gcd(a,b,c)
    #     a,b,c = a//g, b//g, c//g

    #     sols.add(tuple(sorted([a,b,c])))

sols.remove((0,1,1))
ans = 0
for i in sols:
    s = sum(i)
    j = n//s
    ans += (j * (j+1))//2 * s

print(ans)