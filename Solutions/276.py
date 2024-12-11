n = 10000000
m = n//3
from prime import memoize

mf = [1 for i in range(m+1)]

@memoize
def f(n):
    m = n//3
    output = 0
    for a in range(1, m+1):
        t = n - 3*a + 1
        if t <= a:
            if t % 2 == 0:
                output += ((t//2) * (t//2 + 1))
            else:
                output += ((t//2) * (t//2 + 1))+ t//2 + 1
        else:
            s = (t-a)//2 + 1
            t = t - 2*s
            output += s*a
            if t % 2 == 0:
                output += ((t//2) * (t//2 + 1))
            else:
                output += ((t//2) * (t//2 + 1)) + t//2 + 1

    return output

ans = f(n)
for i in range(2, m+1):
    ans -= mf[i] * f(n//i)
    for j in range(2*i, m+1, i):
        mf[j] -= mf[i]

print(ans)

# ans = 0
# import math
# for a in range(1, n):
#     for b in range(a, n):
#         for c in range(b, n):
#             if math.gcd(a,b,c) != 1:
#                 continue
#             if a + b + c > n or c >= a + b:
#                 break
#             # print(a,b,c)
#             ans += 1
#     # print(a, ans)
# print(ans)