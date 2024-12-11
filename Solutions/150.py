t = 0
n = 1000
rows = []
p = 2**20
c = 2**19

for i in range(1,n+1):
    row = [0]
    for j in range(i):
        t = (615949*t + 797807) % p
        row.append(t - c + row[-1])
    rows.append(row)


ans = 0
for i in range(1,n+1):
    r = rows[-i]
    for j in range(1, len(r)):
        e = [r[j] - r[j-1]]
        for k in range(i-1, 0, -1):
            e.append(rows[-k][j+i-k] - rows[-k][j-1] + e[-1])
        # d.append(e)
        ans = min(ans, min(e))

print(ans)