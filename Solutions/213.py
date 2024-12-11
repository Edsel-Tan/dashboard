n = 30

def advance(x):
    output = [[0 for i in range(n)] for j in range(n)]
    output[0][1] += x[0][0] / 2
    output[1][0] += x[0][0] / 2
    output[n-1][1] += x[n-1][0] / 2
    output[n-2][0] += x[n-1][0] / 2
    output[1][n-1] += x[0][n-1] / 2
    output[0][n-2] += x[0][n-1] / 2
    output[n-2][n-1] += x[n-1][n-1] / 2
    output[n-1][n-2] += x[n-1][n-1] / 2

    for i in range(1, n-1):
        output[0][i-1] += x[0][i] / 3
        output[0][i+1] += x[0][i] / 3
        output[1][i] += x[0][i] / 3
        output[n-1][i-1] += x[n-1][i] / 3
        output[n-1][i+1] += x[n-1][i] / 3
        output[n-2][i] += x[n-1][i] / 3
        output[i-1][0] += x[i][0] / 3
        output[i+1][0] += x[i][0] / 3
        output[i][1] += x[i][0] / 3
        output[i-1][n-1] += x[i][n-1] / 3
        output[i+1][n-1] += x[i][n-1] / 3
        output[i][n-2] += x[i][n-1] / 3

    for i in range(1, n-1):
        for j in range(1, n-1):
            output[i-1][j] += x[i][j] / 4
            output[i+1][j] += x[i][j] / 4
            output[i][j-1] += x[i][j] / 4
            output[i][j+1] += x[i][j] / 4
    return output

e = [[1 for i in range(n)] for j in range(n)]

for i in range(n):
    for j in range(n):
        s = [[0 for _ in range(n)] for _ in range(n)]
        s[i][j] = 1
        for _ in range(50):
            s = advance(s)
        for x in range(n):
            for y in range(n):
                e[x][y] *= 1 - s[x][y]

print("{:.6f}".format(sum([sum(i) for i in e])))

