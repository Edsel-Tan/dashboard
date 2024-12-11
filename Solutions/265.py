import math
n = 5
import itertools

def check(lis):
    s = set()
    for i in range(len(lis)-n-1):
        j = tuple(lis[i:i+n])
        if j not in s:
            s.add(j)
        else:
            return False
    return True

ans = 0
for i in itertools.combinations([j for j in range(n+1, 2**n)], 2**(n-1)-1):
    lis = ["1" if k in i else "0" for k in range(2**n+n-1)]
    lis[n] = "1"
    if check(lis):
        ans += int("".join(lis[:2**n]), 2)
print(ans)

