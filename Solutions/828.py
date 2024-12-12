
with open("p828_number_challenges.txt", "r") as file:
    lines = file.readlines()

lines = [[int(i[:i.index(":")]), [int(j) for j in i[i.index(":")+1:].strip("\n").split(",")]] for i in lines]

import math
import itertools

def g(y, j, c):
    z = y.copy()
    z.append(j)
    return f(z, c)

def f(x, c):
    if c in x:
        return True
    for i in itertools.permutations(x, 2):
        y = x.copy()
        for j in i:
            y.remove(j)
        if g(y, i[0]+i[1], c):
            return True
        if i[0] - i[1] > 0:
            if g(y, i[0]-i[1], c):
                return True
        if i[0] % i[1] == 0:
            if g(y, i[0]//i[1], c):
                return True
        if g(y, i[0]*i[1], c):
            return True
    return False


s = []
for line in lines:
    c = math.inf
    for i in range(7):
        for j in itertools.combinations(line[1], i):
            if sum(j) > c:
                continue
            if f(list(j), line[0]):
                c = min(c, sum(j))
    if c == math.inf:
        c = 0
    s.append(c)

mod = 1005075251
ans = 0
for i in range(len(lines)):
    ans = (ans + pow(3, i+1, mod) * s[i]) % mod
print(ans)