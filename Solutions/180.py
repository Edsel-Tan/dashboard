from fractions import Fraction # type: ignore
import itertools
import time
import math

n = 35
s = set()

start = time.time()
c = lambda x : x.denominator <= n and x.numerator <= n and x < 1
def check(x,y,z):
    output = False
    output = output or x+y-z == 0
    output = output or 1/x+1/y-1/z == 0
    output = output or x**2+y**2-z**2 == 0
    output = output or 1/(x**2)+1/(y**2)-1/(z**2) == 0
    return output

# def check2(x,y):
#     output = False
#     output = output or c(x+y)
#     output = output or c(1/(1/x+1/y))
#     output = output or c(1/x**2+1/z**2)
#     output = output or c()
#     return output

def isSquare(n):
    return math.isqrt(n) ** 2 == n


for i, j in itertools.combinations([t+1 for t in range(n)], 2):
    if math.gcd(i, j) != 1:
        continue
    for ii, jj in itertools.combinations([t+1 for t in range(n)], 2):
        if math.gcd(ii, jj) != 1:
            continue
        x = Fraction(i, j) 
        y = Fraction(ii, jj)
        z = [x+y, 1/(1/x+1/y)]
        zsq = (x**2+y**2, 1/(1/(x**2) + 1/(y**2)))
        for z_ in z:
            # print(z_)
            if c(z_):
                s.add(sum([x,y,z_]))
                # print(x,y,z_)
        for z_ in zsq:
            if isSquare(z_.numerator) and isSquare(z_.denominator):
                zz = Fraction(math.isqrt(z_.numerator), math.isqrt(z_.denominator))
                if c(zz):
                    s.add(sum([x,y,zz]))
                    # print(x,y,zz)


ans = sum(s)
print(ans.denominator+ans.numerator)