import math
from prime import memoize
n = 12

def T(n):
    return (n*(n-1))//2

def TT(s):
    output = math.factorial(sum(s))
    for i in s:
        output = output // math.factorial(i)
    return T(output)


def generateStates(n, v, state):
    if v == 0:
        yield state
        return
    for i in generateStates(n, v-1, state.copy()):
        yield i
    for i in range(1, n//v+1):
        s = state.copy()
        s[v] = i
        for j in generateStates(n-i*v, v-1, s):
            yield j

def choose(n, r):
    return math.factorial(n) // math.factorial(r) // math.factorial(n-r)

ans = 0
for i in generateStates(n, n, {}):
    if sum(i.values()) > 9 or sum(i.values()) <= 0: 
        continue
    ways = 1
    digits = 9
    x = 0
    zeroes = n
    for j in i.keys():
        x += i[j] * j
        zeroes -= i[j] * j

    p = math.factorial(x)
    for j in i.keys():
        ways *= choose(digits, i[j])
        p //= math.factorial(j) ** i[j]
        digits -= i[j]
    p *= choose(n-1, zeroes)
    ans += T(p) * ways

print(ans)






