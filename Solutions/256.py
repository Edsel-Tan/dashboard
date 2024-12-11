import math
n = 100000000
ans = [0] * (n+1)

for k in range(2,math.isqrt(n),2):
    r = k+3
    i = 1
    while k*r < n:
        if (k-1) * (i+1) - 1 <= r:
            break
        for j in range(r, (k-1)*(i+1)-1):
            if j * k > n:
                break
            ans[j*k] += 1
        i += 1
        r = (k+1)*i + 2

for k in range(3,math.isqrt(n),2):
    for i in range(1,(k-1)//2):
        for j in range((i*(k+1))%(k-1)+k-1, i*(k+1), k-1):
            if j * k > n:
                break
            ans[j*k] += 1

for i in range(2, len(ans), 2):
    if ans[i] == 200:
        print(i)
        break


