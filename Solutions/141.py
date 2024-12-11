import math


sols = set()
def isSquare(n):
    return math.isqrt(n) ** 2 == n

a = 10**12
b = math.ceil(a**(1/3)) + 1
c = math.ceil(a**(1/2)) + 1

for y in range(1, b):
    for z in range(y+1, b):
        for x in range(1, math.ceil(c/math.sqrt(y*z**3))):
            n = (x**2)*y*(z**3) + x*(y**2)
            # print(n)
            if isSquare(n) and n < a:
                sols.add(n)
print(sum(sols))