n = 100000
import math

ans = 0
x = n//3
for a in range(1, x+1):
    for b in range(a, x-a+1):
        if math.gcd(a, b) != 1:
            continue
        for m in range(1, (n//(a+b) -1)//2 + 1):
            l = min((m*(a+b))//b, n//(a+b)-m)
            if l - m <= 0:
                continue
            ans += l-m

print(ans)