import math
import itertools

def pandigital(n):
    return sorted(list(str(n))) == [str(i) for i in range(10)]

ans = 0

for i in itertools.permutations(range(8), 8):
    n = "98" + "".join([str(j) for j in i])
    for i in range(2,10):
        for j in itertools.combinations(range(1,10), i-1):
            j = list(j)
            j.insert(0,0)
            j.append(10)
            pieces = []
            for k in range(i):
                pieces.append(int(n[j[k]:j[k+1]]))
            g = math.gcd(*pieces)
            m = str(g) + "".join([str(i//g) for i in pieces])
            if pandigital(m):
                ans = max(ans, int(n))
print(ans)


