ans = 0
c = 10**8
import math

for x in range(1, 10**4):
    for y in range(x+1, 10**4, 2):
        if math.gcd(x, y) != 1:
            continue
        if x**2 + y**2 > c:
            break
        m = y**2 - x**2
        n = 2*x*y
        # print(m**2 - n**2, 2*m*n, m**2 + n**2, x, y)
        a = (m**2 - n**2) * m * n
        if a % 84 != 0:
            ans += 1
    

print(ans)
        

        