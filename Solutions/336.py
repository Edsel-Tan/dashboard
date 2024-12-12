import itertools

def simon(p):
    p = list(p)
    ans = 0
    c = 0

    while c < len(p):
        while c < len(p) and p[c] == c:
            c += 1
        if c >= len(p):
            break

        i = p.index(c)
        if i != len(p) - 1:
            ans += 1
        ans += 1
        temp = []
        for j in range(c, i):
            temp.append(p[j])

        for j in range(i, len(p)):
            p[c+j-i] = p[j]
        for j in range(i-c):
            p[len(p)-j-1] = temp[j]

    return ans


n = 11
m = 0
a = []
for i in itertools.permutations(range(n)):
    k = simon(i)
    if k == m:
        a.append(i)
    if k > m:
        m = k
        a = []
        a.append(i)

print("".join([chr(65+i) for i in a[2010]]))