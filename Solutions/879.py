from prime import memoize
import math

n = 4

@memoize
def line(point1, point2):
    g = math.gcd(point2[1] - point1[1], point2[0] - point1[0])
    y = (point2[1] - point1[1]) // g
    x = (point2[0] - point1[0]) // g
    output = []
    for i in range(1, g):
        output.append(((point1[0] + i*x), (point1[1] + i*y)))
    return output

states = [(i,j) for i in range(n) for j in range(n)]
@memoize
def expand(visited, curr):
    output = []
    for i in states:
        if i in visited or i == curr:
            continue
        pts = line(curr, i)
        v = True
        for j in pts:
            if j not in visited:
                v = False
                break
        if v:
            output.append(i)
    return output

astates = {}
ans = 0
for i in states:
    astates[((), i)] = 1
    # ans += 1

while len(astates) > 0:
    nstates = {}
    for x, y in astates:
        s = expand(x, y)
        z = list(x)
        z.append(y)
        z = tuple(sorted(z))
        for i in s:
            key = (z, i)
            if key in nstates:
                nstates[key] += astates[(x,y)]
            else:
                nstates[key] = astates[(x,y)]
    astates = nstates
    ans += sum(astates.values())
    # print(astates)

print(ans)