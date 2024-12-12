m = [[0 for i in range(1000)] for j in range(1000)]

f = lambda a,b: 500*a + b

m[0][0] = 500
m[0][f(1,0)] = -1

for b in range(1, 500):
    m[f(0,b)][f(0,b)] = 500+b
    m[f(0,b)][f(0,b-1)] = -2*b
    m[f(0,b)][f(1,b)] = -1

    m[f(1,b)][f(1,b)] = 500+b
    m[f(1,b)][f(1,b-1)] = -2*b

m[500][500] = 500

def add(m, x, y, c):
    for i in range(len(m[x])):
        m[x][i] += c * m[y][i]

ans = [[1000] for i in range(1000)]


for i in range(1000):
    for j in range(1000):
        if i == j:
            continue
        add(ans, j, i, -m[j][i]/m[i][i])
        add(m, j, i, -m[j][i]/m[i][i])

print("{:.8f}".format(ans[499][0] / m[499][499]))