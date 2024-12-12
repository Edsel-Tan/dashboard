
n = 20000
from math import perm, factorial, comb


ans = 1/n

for jk in range(1,n):
    x = 1
    y = 0
    i = 0
    while x > 0:
        y += x
        x = x * (n-i-jk-1) / (n-i-1)
        i += 1
    s = 1/(n*n)
        
    for j in range((jk+1)//2):
        ans += s * y * 2
        s *= (n - (jk - j)) / (n - j - 1)
    if jk % 2 == 0:
        ans += s * y
        

print("{:.10f}".format(ans))