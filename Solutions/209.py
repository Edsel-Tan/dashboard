bs = lambda x : bin(x)[2:].rjust(6, '0')
bstoi = lambda x : int(x, 2)
from prime import memoize


def edge(s):
    return s[1:6] + str(bstoi(s[0]) ^ (bstoi(s[1]) & bstoi(s[2])))


visited = set()

@memoize
def f(n, v):
    if v == 0:
        return 1
    if n < 2*v:
        return 0
    return f(n-1, v) + f(n-2, v-1)

ans = 1
def choose(n, r):
    output = 1
    for i in range(r):
        output *= n-i
        output //= i+1
    return output

for i in range(64):
    if i in visited:
        continue
    t = 0
    while i not in visited:
        t += 1
        visited.add(i)
        i = bstoi(edge(bs(i)))
    z = 1
    for j in range(1, t//2+1):
        z += (t * f(t-2, j-1))//(j)
    ans *= z

print(ans)
    
        
