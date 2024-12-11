n = 10
def f(x):
    output = 0
    for i in range(n+1):
        output += (-x)**i
    return output

ans = 0
p = [[f(i) for i in range(1, n+2)]]
while len(p[-1]) > 1:
    d = []
    for i in range(1, len(p[-1])):
        d.append(p[-1][i] - p[-1][i-1])
    p.append(d)

for i in range(n):
    c = 0
    for j in range(i+1):
        c += p[i-j][j]
    ans += c
print(ans)