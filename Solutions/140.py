test = 10**6
import math
sols = []

def isSquare(n):
    return math.isqrt(n) ** 2 == n

for n in range(1, test+1):
    if isSquare(5*n**2 + 14*n + 1):
        sols.append(n)

g = [1,4]
for i in range(30):
    g.append(g[-1] + g[-2])


g = [1,1]
for i in range(30):
    g.append(g[-1] + g[-2])
    

def isAns(n):
    return isSquare(5*n**2 + 14*n + 1)

while len(sols) < 30:
    guess = math.ceil(sols[-2] / sols[-4] * sols[-2])
    while not isAns(guess):
        guess -= 1
    sols.append(guess)

print(sum(sols))
