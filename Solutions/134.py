from prime import primes
import math

n = 10**5 * 11
p = primes(n)
p.remove(2)
p.remove(3)

ans = 0
for i in range(len(p)-1):
    p1 = p[i]
    if p1 > 10**6:
        break
    p2 = p[i+1]

    x = math.ceil(math.log10(p1))
    y = pow(10, x, p2)
    z = -p1 * pow(y, -1, p2)
    counter = z % p2
    ans += counter * (10 ** x) + p1


print(ans)
#18612760000617135