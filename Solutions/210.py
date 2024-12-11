r = 1000000000
points = r**2 + (r+1)**2
points -= 3 * (r+1) - 2
points -= (r//2-1) * (r)
rs = 2*(r//8)**2
import math
d = math.isqrt(rs)
q = 0
for i in range(0, d+1):
    q += math.isqrt(rs - i**2-1)+1
q -= d+1
q = 4*q+1
points += q - (r//4-1)
print(points)