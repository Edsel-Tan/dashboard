from math import isqrt
n = 10**12
m = isqrt(n)
ans = set()

for i in range(2, m+1):
    z = 3
    while True:
        rep = (i**z-1)//(i-1)
        if rep > n:
            break
        ans.add(rep)
        z += 1

print(sum(ans)+1)