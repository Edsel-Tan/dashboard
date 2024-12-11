from prime import primes, miller_rabin, memoize
import itertools

e = [6+3+1, 4+1, 2, 1, 1, 1]
p = primes(15)

def f(x):
    output = 1
    for i in range(len(x)):
        output *= p[i] ** x[i]
    return output

vp = []
pp = []
for k in itertools.product(*tuple([[i for i in range(j+1)] for j in e])):
    x = f(k)
    if miller_rabin(x+1):
        # vp.append((x+1, k))
        if x+1 not in p:
            vp.append((x+1, k))
        else:
            pp.append((x+1, k))

states = [(1, (0,0,0,0,0,0))]
for i in vp:
    ns = []
    for j in states:
        ns.append(j)
        skip = False
        for k in range(len(e)):
            if j[1][k] + i[1][k] > e[k]:
                skip = True
                break
        if skip:
            continue
        ns.append((j[0] * i[0], tuple([j[1][k] + i[1][k] for k in range(len(e))])))
    states = ns

s = {}
for i in states:
    if i[1] in s:
        s[i[1]].append(i[0])
    else:
        s[i[1]] = [i[0]]


states = [(1, tuple(e))]
for i in pp:
    z = p.index(i[0])
    ns = []
    for j in states:
        ns.append(j)
        skip = False
        for k in range(len(e)):
            if j[1][k] - i[1][k] < 0:
                skip = True
                break
        if skip:
            continue
        t = (j[0] * i[0], tuple([j[1][k] - i[1][k] for k in range(len(e))]))
        ns.append(t)
        for k in range(1,t[1][z]+1):
            nt = list(t[1])
            nt[z] -= k
            ns.append((t[0] * (i[0] ** k), tuple(nt)))


    states = ns

ss = {}
for i in states:
    if i[1] in ss:
        ss[i[1]].append(i[0])
    else:
        ss[i[1]] = [i[0]]


ans = []
for i in ss.keys():
    if i in s:
        for j in ss[i]:
            for k in s[i]:
                ans.append(j*k)
ans = sorted(ans)
print(ans[150000-1])

# ans = []
# for i in states:
#     y = i[0]
#     j = list(i[1])
#     skip = True
#     for x in range(len(p)-1, -1, -1):
#         if j[x] < 0:
#             skip = False
#             break
#         elif j[x] > 0:
#             y *= p[x] ** (j[x]+1)
#             for k in range(len(pp[p[x]])):
#                 j[k] -= pp[p[x]][k]
#     if skip:
#         if y < 203:
#             print(i[0], i[1], y)
#         ans.append(y)
# ans = sorted(ans)
# print(ans[0])
# print(len(ans))
# print(ans[150000-1])