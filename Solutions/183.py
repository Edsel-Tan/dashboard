import math

n = range(5, 10001)
ans = 0

def D(n):
    m = n/math.exp(1)
    low = math.floor(m)
    high = math.ceil(m)

    parts = high if high * math.log(n / high) > low * math.log(n / low) else low
    parts = parts / math.gcd(parts, n)
    
    while parts % 2 == 0:
        parts = parts//2
    while parts % 5 == 0:
        parts = parts//5

    return parts == 1

for i in n:
    ans += i if D(i) else -i

print(-ans)

