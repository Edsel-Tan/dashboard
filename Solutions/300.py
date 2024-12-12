import itertools

n = 15

def rotate(p):
    return p[1:] + p[0]

def invert(p):
    return "".join(["A" if i == "B" else "B" for i in p])

def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


paths = []
for q in itertools.product([-1,0,1], repeat = n-2):
    d = False
    for i in q:
        if i == -1:
            break
        if i == 1:
            d = True
            break
    if d:
        continue

    o = 0
    s = (0,0)
    p = {}
    p[s] = 0
    s = (1,0)
    p[s] = 1
    j = 1
    v = True
    for i in q:
        o += i
        o = o%4
        j += 1

        if o == 0:
            s = (s[0] + 1, s[1])
        if o == 1:
            s = (s[0], s[1] - 1)
        if o == 2:
            s = (s[0] - 1, s[1])
        if o == 3:
            s = (s[0], s[1] + 1)
        
        if s in p:
            v = False
            break

        p[s] = j

    if v:
        output = []
        for i in p:
            for j in p:
                if dist(i, j) == 1:
                    output.append((p[i], p[j]))
        if len(output) > 38:
            paths.append(output)

ans = 0
z = 0
for i in itertools.product("AB", repeat=n):
    z += 1
    m = 0
    for j in paths:
        s = 0
        for k in j:
            if i[k[0]] == "A" and i[k[1]] == "A":
                s += 1
        m = max(m, s)
    ans += m//2

print(ans/(2**n))