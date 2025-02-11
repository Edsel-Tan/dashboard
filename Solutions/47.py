n = 10**6
f = [0 for i in range(n+1)]

for i in range(2, n+1):
    if f[i] != 0:
        continue

    for j in range(i, n+1, i):
        f[j] += 1
    
for i in range(2, n+1):
    if f[i] == 4 and f[i+1] == 4 and f[i+2] == 4 and f[i+3] == 4:
        print(i)
        break