count = 25
n = 1
import math
from prime import miller_rabin

ans = 0
while count > 0:
    n += 1
    if math.gcd(n, 10) == 1:
        if pow(10, n-1, n*9) == 1:
            if not miller_rabin(n):
                ans += n
                n += 1
                count -= 1
                
print(ans)