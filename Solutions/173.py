from prime import primes
import math

n = 10**6
t = math.isqrt(n) + 1
p = primes(n)

def factor2(m):
    output = 1
    for i in p[1:]:
        if i > m:
            break
        e = 0
        if m%i == 0:
            e += 1
            m = m // i
        output *= (e+1)
    return output * 2

def factor(m):
    output = 1
    for i in p:
        if i > m:
            break
        e = 0
        while m%i == 0:
            e += 1
            m = m // i
        output *= (e+1)
    return output

ans = 0
for i in range(1, n+1):
    if i%4 == 0:
        ans += (factor(i//4) + 1) // 2
        # print(i, (factor(i//4) + 1) // 2)
        # ans += (factor(i) - factor2(i) + 1) // 2
        # print(i, factor(i), factor2(i), (factor(i) - factor2(i) + 1) // 2)
ans -= t//2
print(ans)

# s = {}
# for i in range(3, 27):
#     for j in range(1, i):
#         if j%2 == i%2 and i**2-j**2 <= n:
#             if i**2-j**2 in s.keys():
#                 s[i**2-j**2] += 1
#             else:
#                 s[i**2-j**2] = 1

# for i in sorted(s.keys()):
#     print(i, s[i])

# print(sum(s.values()))
# print(factor(22))