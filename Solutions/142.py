import itertools
import math

t = 1000
def factors(n):
    output = []
    for i in range(1, math.isqrt(n) + 1):
        if n%i == 0:
            output.append(i)
    return output

def sqDiff(n):
    output = []
    for i in factors(n):
        j = n//i
        if (i-j)%2 == 0 and (i+j)%2 == 0:
            output.append(((i+j)//2, abs(i-j)//2))
    return output

def isSquare(n):
    return math.isqrt(n) ** 2 == n

def check(n):
    if len(set(n)) < 3:
        return False
    for x,y in itertools.combinations(n, 2):
        if not isSquare(abs(x-y)) or not isSquare(x+y):
            return False
    return True

sols = []
for i in range(1, t+1):
    # print(sqDiff(i**2))
    for j, k in itertools.combinations(sqDiff(i**2), 2):
        c, a = j
        e, d = k
        if isSquare(a**2 + e**2):
            b = check(((abs(d**2-a**2))//2, (d**2+a**2)//2, (c**2+e**2)//2))
            if b:
                # print((abs(d**2-a**2))//2, (d**2+a**2)//2, (c**2+e**2)//2)
                # print(sum(((abs(d**2-a**2))//2, (d**2+a**2)//2, (c**2+e**2)//2)))
                sols.append((sum(((abs(d**2-a**2))//2, (d**2+a**2)//2, (c**2+e**2)//2)),(abs(d**2-a**2))//2, (d**2+a**2)//2, (c**2+e**2)//2))

print(sorted(sols)[0][0])