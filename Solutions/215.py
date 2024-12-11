from prime import memoize

dp = [1,0,1]
for i in range(2, 33):
    dp.append(dp[-2] + dp[-3])


n = 32
m = 10

@memoize
def w(n):
    if n == 0:
        return [[0]]
    
    if n < 0:
        return []
    
    output = []
    for i in w(n-2):
        j = i.copy()
        j.append(j[-1]+2)
        output.append(j)

    for i in w(n-3):
        j = i.copy()
        j.append(j[-1]+3)
        output.append(j)

    return output

walls = w(n)
ws = [set(i) for i in walls]
intersections = dict(zip([i for i in range(len(walls))], [[] for i in range(len(walls))]))

for i in ws:
    i.remove(0)
    i.remove(n)

for i in range(len(ws)):
    for j in range(i):
        if len(ws[i].intersection(ws[j])) == 0:
            intersections[i].append(j)
            intersections[j].append(i)

ans = dict(zip([i for i in range(len(walls))], [1 for i in range(len(walls))]))


for i in range(m-1):
    newans = dict(zip([i for i in range(len(walls))], [0 for i in range(len(walls))]))
    for j in range(len(ws)):
        for k in intersections[j]:
            newans[j] += ans[k]
    ans = newans

print(sum(ans.values()))