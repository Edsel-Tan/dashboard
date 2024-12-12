up1 = [1,1,1]
down1 = [1,1,0]
up2 = [0,0,0]
down2 = [0,0,1]

m = 10**9+7
n = 10**7

for i in range(len(up1), n):
    up1.append((up1[i-1] + down2[i-1]) % m)
    down1.append(up2[i-1])
    up2.append(0)
    down2.append((up1[i-3] + down2[i-3]) % m)
    if i % 4 == 1 or i % 4 == 2:
        down2[-1] += 1
    else:
        up2[-1] += 1

# print(up1, down1, up2, down2, sep="\n")

ans = up1[n-1] + down2[n-1] + up2[n-1]

for i in range(3, n+1):
    if i % 4 == 1 or i % 4 == 0:
        ans = (ans + down1[n-(i-1)]) % m
    else:
        ans = (ans + up1[n-(i-1)]) % m

print((ans * 2) % m)