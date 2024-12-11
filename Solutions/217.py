n = 47
m = 3**15

d = n//2
nz = {0:{0:1}}
wz = {0:{0:1}}

for i in range(1, d+1):
    nz[i] = {}
    wz[i] = {}
    for j in wz[i-1].keys():
        for k in range(10):
            if j+k in wz[i]:
                wz[i][j+k] += wz[i-1][j]
            else:
                wz[i][j+k] = wz[i-1][j]
        for k in range(1, 10):
            if j+k in nz[i]:
                nz[i][j+k] += wz[i-1][j]
            else:
                nz[i][j+k] = wz[i-1][j]
    for j in nz[i].keys():
        nz[i][j] = nz[i][j] % m
    for j in wz[i].keys():
        wz[i][j] = wz[i][j] % m

nzs = {0:{0:0}}
wzs = {0:{0:0}}

for i in range(1, d+1):
    nzs[i] = {}
    wzs[i] = {}
    for j in wzs[i-1].keys():
        for k in range(10):
            if j+k in wzs[i]:
                wzs[i][j+k] += wzs[i-1][j] + wz[i-1][j] * k * pow(10, i-1, m)
            else:
                wzs[i][j+k] = wzs[i-1][j] + wz[i-1][j] * k * pow(10, i-1, m)
        for k in range(1, 10):
            if j+k in nzs[i]:
                nzs[i][j+k] += wzs[i-1][j] + wz[i-1][j] * k * pow(10, i-1, m)
            else:
                nzs[i][j+k] = wzs[i-1][j] + wz[i-1][j] * k * pow(10, i-1, m)
    for j in nzs[i].keys():
        nzs[i][j] = nzs[i][j] % m
    for j in wz[i].keys():
        wzs[i][j] = wzs[i][j] % m

# print(nz, wz)
# print(nzs, wzs)
ans = 0
for i in range(1, n+1):
    if i % 2 == 0:
        j = i//2
        l = pow(10, j, m)
        for k in nz[j].keys():
            ans += nz[j][k] * wzs[j][k] + wz[j][k] * nzs[j][k] * l
            ans = ans % m
    if i % 2 == 1:
        j = i//2
        l = pow(10, j+1, m)
        ll = pow(10, j, m)
        for k in nz[j].keys():
            ans += 10 * (nz[j][k] * wzs[j][k] + wz[j][k] * nzs[j][k] * l)
            ans += 45 * ll * nz[j][k] * wz[j][k]
            ans = ans % m
print(ans%m)