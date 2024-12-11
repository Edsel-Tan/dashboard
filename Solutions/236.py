from fractions import Fraction # type: ignore
import math
import itertools

a = [5248,1312*6,5760]
b = [640,1888*6,3776]


# for i in range(5):
#     a[i] = a[i]//2
#     b[i] = b[i]//2

s = set()
d = {}

for i in range(3):
    t = set()
    for x in range(1,a[i]+1):
        for y in range(max(1, (b[i] * x * 108)//(59 * a[i])),min(b[i]+1, (b[i] * x * 3)//(a[i])+1)):
            k = Fraction(y*a[i], x*b[i])
            if k > 1 and k <= 3:
                t.add(k)
                if k in d:
                    if i in d[k]:
                        d[k][i].append((x,y))
                    else:
                        d[k][i] = [(x,y)]
                else:
                    d[k] = {}
                    d[k][i] = [(x,y)]
            

    if len(s) != 0:
        s = t.intersection(s)
    else:
        s = t
    e = []
    for j in d.keys():
        if j not in s:
            e.append(j)
    for j in e:
        del d[j]
        

s = sorted(s, reverse=True)
i = 1
del t

ans = 0

for m in range(len(s)):
    m = s[m]
    n = 1
    for j in d[m].keys():
        n *= len(d[m][j])
        continue
    for j in itertools.product(*d[m].values()):
        x = sum([k[0] for k in j])
        y = sum([k[1] for k in j])
        if Fraction(x*sum(b), y*sum(a)) == m:
            ans = max(ans, m)
            i += 1
            break
    del d[m]

print(ans)