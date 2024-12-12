def convolute(A,B):
    C = [0 for i in range(len(A)+len(B)-1)]
    for i in range(len(A)):
        for j in range(len(B)):
            C[i+j] += A[i] * B[j]
    return C

def ones(n):
    return [1 for i in range(n+1)]

import itertools
from prime import primes

p = primes(50)
s = [10,10,10,5,4,3,3,3,2,2,2,2,2]
s = [range(i) for i in s]
c = itertools.product(*s)

import math
ans = math.inf
for j in c:
    s = ones(0)
    for i in j:
        s = convolute(s,ones(i))

    
    if max(s) >= 10000:
        t = 1
        for x,y in enumerate(j):
            t *= p[x] ** y
        ans = min(ans, t)

# j = [2,1]
# s = ones(0)
# for i in j:
#     s = convolute(s,ones(i))



# t = 1
# for x,y in enumerate(j):
#     t *= p[x] ** y
# ans = min(ans, t)
# print(max(s), s)

print(ans)

"""
5342931457063200

"""