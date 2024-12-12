from fractions import Fraction # type: ignore
import math

def transition(r):
    x = math.floor(r) + 1
    s = [i for i in range(1, x)]
    c = 0
    tolerance = 0

    ans = r+1
    while True:
        if s[c] * r < x:
            c += 1
        
        # if x / s[c-1] >= ans:
        #     tolerance += 1
        # else:
        #     tolerance = 0
        
        ans = min(ans, Fraction(x, s[c-1]))
        s.append(x)
        x = x + s[c]

        if x > r**3:
            break
        
    return ans

start = 1
x = []
for i in range(123455):
    x.append(start)
    start = transition(start)
print("{:.10f}".format(start.numerator / start.denominator))
