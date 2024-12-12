n = 12345

g = [0,0,0]
for i in range(1, n+1):
    g.append(g[-3] + (i*(i+1))//2)

for i in range(3, n+1):
    g[i] += g[i-3]

print(sum(g[:n+1]))