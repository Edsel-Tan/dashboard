def f(a, b):
    if a == 0:
        return [[]]
    if b == 0:
        return []
    output = []
    for i in range(1, a+1):
        for j in f(a-i, b-1):
            j.append(i)
            output.append(j)
    return output

import math
def g(x):
    output = math.factorial(sum(x))
    for i in x:
        output //= math.factorial(i)
    return output

s = f(20, 12)
ans = 0
import itertools
for i in s:
    h = g(i)
    for j in itertools.combinations([k+1 for k in range(12)], len(i)):
        t = 0
        c = 10
        index = len(i) - 1
        while c > 0:
            if c > i[index]:
                t += j[index] * i[index]
                c -= i[index]
                index -= 1
            else:
                t += j[index] * c
                c = 0
        if t == 70:
            ans += h

print(ans)