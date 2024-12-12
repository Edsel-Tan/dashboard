from matrix import Matrix
m = 10**9

state = {0:[0,1]}
ans = 0
tans = 0
for i in range(9):
    x = 10**i
    nstate = {}
    for j in range(1,10):
        for k in state:
            if j+k in nstate:
                nstate[k+j][0] += state[k][1] * j * x + state[k][0]
                nstate[k+j][1] += state[k][1]
                nstate[k+j][0] %= m
                nstate[k+j][1] %= m
            else:
                nstate[k+j] = [0,0]
                nstate[k+j][0] += state[k][1] * j * x + state[k][0]
                nstate[k+j][1] += state[k][1]
                nstate[k+j][0] %= m
                nstate[k+j][1] %= m

    state = nstate
    n = 13
    while n in state:
        ans += state[n][0]
        n *= 13
    if 5 in state:
        tans += state[5][0]

matrix = [[0 for i in range(9)] for j in range(9)]
for i in range(0,8):
    matrix[i][i+1] = 1
for i in range(9):
    matrix[8][i] = 1
matrix = Matrix(matrix)

v = [[0] for i in range(9)]
v[8] = [1]
v = Matrix(v)

def f(x):
    return (matrix.fastexp(x, m) * v).entries[-1][0]

keys = sorted(state.keys())
for i in range(1, 18):
    n = 13**i
    for j in keys:
        if j >= n:
            break
        ans += f(n-j) * state[j][0]
        ans %= m

print(ans)
