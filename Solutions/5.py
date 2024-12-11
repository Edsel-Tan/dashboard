from math import lcm

ans = 1
n = 20
for i in range(1, n+1):
    ans = lcm(ans, i)
print(ans)