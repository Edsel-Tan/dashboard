from itertools import combinations
from math import comb, factorial

def f(x):
    a = factorial(sum(x))
    for i in range(len(x)):
        a = a//factorial(x[i])
    return a

def g(x):
    if x[0] > 0:
        y = x.copy()
        y[0] -= 1
        return f(x) - f(y)
    else:
        return f(x)

m = 1
ans = 0
for n in range(1, m+1):
    for i in combinations(range(n+9), 9):
        state = []
        state.append(i[0])
        for j in range(1, len(i)):
            state.append(i[j]-i[j-1]-1)
        state.append(n+8 - i[-1])
        num = ""
        for i in range(10):
            num += str(i) * state[i]
        num = int(num)
        ans += g(state) * num

print(23892520736890167368025300356336085%(1123455689))


