n = 50000

s = [0]
for k in range(1, 56):
    s.append((100003 - 200003 * k + 300007 * k**3) % 1000000)

for k in range(56, 6*n+1):
    s.append((s[k-24]+s[k-55]) % 1000000)

def intersection(c1, c2):
    x1 = intersect(c1[0], c1[0] + c1[3], c2[0], c2[0] + c2[3])
    x2 = intersect(c1[1], c1[1] + c1[4], c2[1], c2[1] + c2[4])
    x3 = intersect(c1[2], c1[2] + c1[5], c2[2], c2[2] + c2[5])
    return x1[0], x2[0], x3[0], x1[1], x2[1], x3[1]

def intersect(a, b, x, y):
    return max(a, x), min(y, b) - max(a, x)

cuboids = []
for i in range(n):
    cuboids.append((s[6*i+1] % 10000, 
                    s[6*i+2] % 10000, 
                    s[6*i+3] % 10000, 
                    1 + s[6*i+4] % 399, 
                    1 + s[6*i+5] % 399, 
                    1 + s[6*i+6] % 399))

stack = [(cuboids, 1)]
# tans = 0
# for i in cuboids:
#     print(i)
#     tans += i[3] * i[4] * i[5]
# print(tans)
ans = 0

while len(stack) > 0:
    # print(stack)
    top, mult = stack[-1]
    del stack[-1]
    # print(len(stack))
    if len(top) > 10000:
        x = [[] for i in range(10000)]
        for c in top:
            ans += mult * c[3] * c[4] * c[5]
            ns = []
            for j in range(max(0, c[0]-400), min(10000, c[0]+400)):
                for k in x[j]:
                    nc = intersection(c, k)
                    if nc[3] <= 0 or nc[4] <= 0 or nc[5] <= 0:
                        continue
                    ns.append(nc)
            stack.append((ns, -mult))
            x[c[0]].append(c)
    else:
        for i in range(len(top)):
            c = top[i]
            ans += mult * c[3] * c[4] * c[5]
            ns = []
            for j in range(i):
                nc = intersection(c, top[j])
                if nc[3] <= 0 or nc[4] <= 0 or nc[5] <= 0:
                    continue
                ns.append(nc)
            stack.append((ns, -mult))
print(ans)
