n = 32
matrix = [[0 for i in range(n)] for j in range(n)]

from prime import memoize
@memoize
def c(n, r):
    output = 1
    for i in range(r):
        output *= n-i
        output //= i+1
    return output

v = [1 for i in range(n)]
for i in range(n):
    for j in range(i, n):
        matrix[i][j] = -c(n-i, j-i) / (2**(n-i))

for i in range(n):
    matrix[i][i] += 1

def add(p, q, r):
    for i in range(len(q)):
        p[i] += r * q[i]

for i in range(n):
    for j in range(n):
        if j != i:
            r = matrix[j][i] / matrix[i][i]
            add(matrix[j], matrix[i], -r)
            v[j] -= r * v[i]

print("{:.10f}".format(v[0] / matrix[0][0]))