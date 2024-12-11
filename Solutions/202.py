from prime import primes, memoize
import math

n = 12017639147
# n = 1000001
m = (n+3) // 2

def pf(n):
    p = primes(math.isqrt(n)+1)
    pfs = {}
    for i in p:
        if i > n:
            break
        if n%i == 0:
            pfs[i] = 0
            while n % i == 0:
                n = n // i
                pfs[i] += 1
    if n != 1:
        pfs[n] = 1
    output = [1]
    for i in pfs.keys():
        temp = output.copy()
        for j in range(pfs[i]):
            for k in output:
                temp.append(i**(j+1) * k)
        output = temp
    return output
    
# @memoize
# def totient(n):
#     p = primes(math.isqrt(n)+1)
#     pfs = {}
#     for i in p:
#         if i > n:
#             if n != 1:
#                 pfs[n] = 1
#             break
#         if n%i == 0:
#             pfs[i] = 0
#             while n % i == 0:
#                 n = n // i
#                 pfs[i] += 1
#     ans = 1
#     for i in pfs.keys():
#         ans *= (i-1) * i ** (pfs[i] - 1)
#     return ans
        


@memoize
def f(x):
    if x == 1:
        return 0
    ans = x // 3 if x%3 == 1 else x//3 + 1
    pfs = pf(x)
    for i in pfs[:-1]:
        ans -= f(i)
        # print(x, i, f(i))
    return ans

# print(pf(6))
print(f(m))
