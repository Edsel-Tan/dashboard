import math

n = 1000000-1
m = math.isqrt(n)
sols = {}

for i in range(1, m+1):
    for j in range(i+1, m+1, 2):
        if i**2 + j**2 > n:
            break
        if math.gcd(i,j) != 1:
            continue
        for k in range(1, n//(i**2+j**2)+1):
            x = 2*k*i*j
            y = k*(j**2-i**2)
            if x in sols:
                sols[x].append(y)
            else:
                sols[x] = [y]
            if y in sols:
                sols[y].append(x)
            else:
                sols[y] = [x]

ans = 0

for i in sols:
    for j in range(len(sols[i])):
        for k in range(j+1, len(sols[i])):
            a = sols[i][j]
            b = sols[i][k]
            if (a*b) % (a+b) == 0:
                ans += 1
                
print(ans)