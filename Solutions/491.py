from math import comb
from itertools import combinations

f = [1]
for i in range(1,11):
    f.append(f[-1] * i)

s = set()

ans = 0
for i in combinations([i%10 for i in range(20)], 10):
    j = tuple(sorted(i))
    if sum(i) % 11 != 1 or j in s:
        continue
    s.add(j)
    cnt = [0 for i in range(10)]
    for x in j:
        cnt[x] += 1

    y = f[10]
    for i in cnt:
        y = y//f[i]
    if cnt[0]:
        x = f[9]//f[cnt[0]-1]
        for i in cnt[1:]:
            x = x//f[i]
        y -= x
    
    cnt2 = [2-cnt[i] for i in range(10)]
    a = f[10]
    for i in cnt2:
        a = a//f[i]
    ans += a * y

print(ans)
    
    
    