n = 10**9

f = [0,0,0,1]
s = 1

while s < n:
    f.append(f[-1] + f[-4])
    s += f[-1]

ans = 0
n -= 1

i = 0
while n > 0:
    ans += min(f[i], n) * (i+2)
    n -= f[i]
    i += 1

print(ans)