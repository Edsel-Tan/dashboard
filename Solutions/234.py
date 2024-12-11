from prime import primes
import math

# n = 1000
n = 999966663333
m = math.isqrt(n)+1
p = primes(2*m)

def f(x, a):
    return (a * x * (x+1)) // 2

ans = 0

for i in range(len(p)-1):
    lower = p[i]**2
    upper = p[i+1]**2 - 1

    if upper > n:
        upper = n
    
    if lower >= n:
        break


    ans += f(upper//p[i], p[i]) - f(lower//p[i], p[i]) + f(upper//p[i+1], p[i+1]) - f(lower//p[i+1], p[i+1]) - 2 * (f(upper//(p[i+1] * p[i]), p[i+1]*p[i]) - f(lower//(p[i+1] * p[i]), p[i+1]*p[i]))


print(ans)

