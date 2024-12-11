import math

l = 10**8
rl = math.isqrt(l*12)

ans = l//3

for n in range(1, rl+1):
    for m in range(n+1, l+1, 2):
        if math.gcd(m, n) != 1:
            continue
        a = m**2-n**2
        b = 2*m*n
        c = m**2+n**2
        # ans += l//(a+b+c)
        # g = math.gcd(a, b)
        # ps = (min(a, b)//g, max(a, b)//g)
        # if ps not in s:
        #     s.add(ps)
        ans += l//(a+b+c)
        # print(a, b, c)
        if a + b + c > l:
            break

s = set()
# mg = 0
for n in range(1, rl+1):
    for m in range(3*n+1, l+1):
        if math.gcd(m, n) != 1:
            continue
        a = m**2+2*m*n-3*n**2
        b = 4*m*n
        c = m**2+3*n**2
        # print(a, b, c)
        g = math.gcd(a, b)
        # mg = max(mg, g)
        # print(mg)
        ps = (min(a, b)//g, max(a, b)//g)
        if ps not in s:
            s.add(ps)
            ans += l//((a+b+c)//g)
        # print(a, b, c)
        if a + b + c > 12 * l:
            break


for n in range(1, rl+1):
    for m in range(3*n+1, l+1):
        if math.gcd(m, n) != 1:
            continue
        a = abs(2*m*n - (m**2-3*n**2))
        b = 4*m*n
        c = m**2+3*n**2
        # print(a, b, c)
        g = math.gcd(a, b)
        # mg = max(mg, g)
        # print(mg)
        ps = (min(a, b)//g, max(a, b)//g)
        if ps not in s:
            # print("Found!")
            s.add(ps)
            ans += l//((a+b+c)//g)
        # print(a, b, c)
        if a + b + c > 12 * l:
            break
print(ans)

