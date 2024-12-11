t = 47547

sols = set()
def reduce(n, result):
    if n == 0:
        sols.add(tuple(sorted(result)))
    for i in range(1,n+1):
        if n % (2*i+1) == i:
            r = result.copy()
            r.append(i)
            reduce(n//(2*i+1), r)

reduce(t, [])

import math
m = math.inf

sol = [9,6,5,3,2]
p = [2,3,5,7,11]
ans = 1
for i in range(len(sol)):
    ans *= p[i] ** sol[i]

print(ans*2)
