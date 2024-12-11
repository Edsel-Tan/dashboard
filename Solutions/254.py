import math
import itertools

def f(n):
    ans = 0
    while n > 0:
        ans += math.factorial(n % 10)
        n = n // 10
    return ans

def finv(n):
    ans = ""
    for i in range(8, 0, -1):
        j = math.factorial(i)
        while n >= j:
            ans = str(i) + ans
            n -= j
    return ans

def s(n):
    ans = 0
    while n > 0:
        ans += n % 10
        n = n // 10
    return ans

ml = 36
keys = []
d = {}
for x in itertools.product(*tuple([[j for j in range(i+1)] for i in range(1, 9)])):
    r = ""
    for i in range(len(x)):
        r += x[i] * str(i+1)
    if r != "":
        keys.append(int(r))
        d[int(r)] = f(int(r))
    
    while len(r) < ml:
        r += "9"
        keys.append(int(r))
        d[int(r)] = f(int(r))

keys = sorted(keys)
n = 150
nine = math.factorial(9)

ans = 0
for i in range(1, n+1):
    j = i
    k = ""
    while j >= 10:
        k += "9"
        j -= 9
    k = str(j) + k
    k = int(k)
    t = k // nine

    base = t * nine
    l = t * 9

    for j in keys:
        if s(base + d[j]) == i:
            l = t * 9 + s(j)
            break
    ans += l

print(ans)


