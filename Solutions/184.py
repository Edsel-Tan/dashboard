import math
import itertools

def C(n, r):
    if r > n:
        return 0
    if r > n/2:
        r = n - r
    output = 1
    for i in range(r):
        output *= n-i
        output = output // (i+1)
    return output

def dist(x,y):
    return x**2 + y**2

r = 105
points = {}
for i in range(1, r):
    for j in range(r):
        if dist(i, j) >= r**2:
            break
        k = (i // math.gcd(i, j), j // math.gcd(i, j))
        if k in points.keys():
            points[k] += 1
        else:
            points[k] = 1

a = []
for i in list(points.keys()):
    k = (-i[1], i[0])
    points[k] = points[i]

# print(len(points.keys()))
pp = {}
for i in points.keys():
    if points[i] in pp.keys():
        pp[points[i]] += 1
    else:
        pp[points[i]] = 1

# print(len(pp.keys()))
# print(pp)

ans = 0
for i in itertools.combinations(pp.keys(), 3):
    x,y,z = i
    ans += 2 * x * y * z * pp[x] * pp[y] * pp[z]
    # print(ans)
for i in itertools.combinations(pp.keys(), 2):
    x,y = i
    ans += 2 * x * y * y * pp[x] * C(pp[y], 2)
    ans += 2 * x * x * y * C(pp[x], 2) * pp[y]
    # print(ans)
for i in itertools.combinations(pp.keys(), 1):
    x = i[0]
    ans += 2 * x ** 3 * C(pp[x], 3)
    # print(ans, x, pp[x], C(4,3))
print(ans)

# ans = 0
# for i in itertools.combinations(points.keys(), 3):
#     ans += 2 * points[i[0]] * points[i[1]] * points[i[2]]
# print(ans)