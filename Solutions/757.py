ans = 0
n = 10**14
import math

x = 1
f = lambda x : x*(x+1)

ans = set()
while f(x)*f(x) < n:
    y = x
    while f(x)*f(y) < n:
        ans.add(f(x)*f(y))
        y += 1
    x += 1

print(len(ans))