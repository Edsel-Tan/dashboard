from prime import memoize
import math
m = 10**9
@memoize
def g(x):
    if x == 1:
        return 7
    if x == 0:
        return 0
    
    output = ((x+1)**3-1)
    for i in range(2,math.isqrt(x)+1):
        if i != x//i:
            output -= g(x//i)
            output = output

    for i in range(1, math.isqrt(x)+1):
        output -= (x//i - x//(i+1)) * g(i)
        output = output

    return output

x = str(g(10**10))
print(x[:10]+x[-10:])