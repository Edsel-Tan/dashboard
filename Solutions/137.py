def next(x, y):
    return 9*x+20*y, 4*x+9*y

import math
def isSquare(n):
    return math.isqrt(n) ** 2 == n

z, y = 3, 1
seeds = [(3,1), (7,3), (18,8)]
sols = []

for z,y in seeds:
    for i in range(14):
        x = (y + z) // 2 if (y+z)%2 == 0 else 0
        sols.append(x*y)
        z, y = next(z, y)

sols = sorted(sols)
print(sols[14])