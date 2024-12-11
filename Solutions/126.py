def expand(cuboid : list[tuple[int,int]], n : int) -> tuple[list, int]:
    new_cuboid = []
    count = cuboid[0][0] * cuboid[0][1] + cuboid[-1][0] * cuboid[-1][1]
    new_cuboid.append(cuboid[0])
    for i,j in cuboid:
        count += (i+2) * (j+2) - i * j
        new_cuboid.append( (i+2, j+2) )
    new_cuboid.append(cuboid[-1])
    return count - 4 * (n+1) * len(cuboid) + 4 * (n+1) * n, new_cuboid

def cuboid(i, j, k):
    output = []
    for l in range(i):
        output.append((j, k))
    return output


n = 2*10**4
ans = dict(zip([i for i in range(1,n+1)], [0 for i in range(n)]))

for i in range(1, n):
    for j in range(i, n):
        if (i*j) > n:
            break
        for k in range(j, n):
            if (i*j + j*k + i*k) * 2 > n:
                break
            c = cuboid(i, j, k)
            t = 0
            tt = 0
            while t < n:
                t, c = expand(c, tt)
                tt += 1
                if t < n:
                    ans[t] += 1

for i in range(1, n+1):
    if ans[i] == 1000:
        print(i)
        break
