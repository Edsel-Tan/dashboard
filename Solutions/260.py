n = 1000
invariant1 = [[True for i in range(n+1)] for j in range(n+1)]
invariant2 = [[True for i in range(n+1)] for j in range(n+1)]
invariant3 = [[True for i in range(n+1)] for j in range(n+1)]

ans = 0
for x in range(n+1):
    for y in range(x, n+1):
        if invariant1[x][y]:
            for z in range(y, n+1):
                if invariant1[y][z] and invariant1[x][z] and invariant2[x][z-y] and invariant2[y][z-x] and invariant2[z][y-x] and invariant3[z-y][y-x]:
                    ans += x + y + z
                    invariant1[x][y] = False
                    invariant1[y][z] = False
                    invariant1[x][z] = False
                    invariant2[x][z-y] = False
                    invariant2[y][z-x] = False
                    invariant2[z][y-x] = False
                    invariant3[z-y][y-x] = False
                    break
print(ans)