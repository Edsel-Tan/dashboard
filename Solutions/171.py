import math
n = 20
q = 11
r = n - q
mod = 10**r
m = (mod - 1)//9

fcache = {}
gcache = {}

def memoize(f):
    cache = {}
    def g(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]      
    return g


@memoize
def c(n, r):
    if r > n:
        return 0
    if r > n//2:
        r = n - r
    output = 1
    for i in range(r):
        output *= n - i
        output = output // (i+1)
    return output


def f(x, y, z=9, total=0, ways=1):
    """
    x = number of digits
    y = target 
    z = number of digits left to use
    total = sum of digits so far
    ways = no of ways to rearrange
    Returns sum of digits
    """
    if y == 0:
        return (total * ways * m)//r
    if x == 0:
        return 0
    if z == 0:
        return 0 
    output = 0
    for i in range(0, min(x+1, y//(z**2)+1)):
        output += f(x-i, y-i*z**2, z-1, total + i * z, c(x, i) * ways)
        output = output % mod
    return output % mod
        

def g(x, y, z=9, ways=1):
    """
    x = number of digits
    y = target
    z = number of digits left to use
    Returns no of combinations
    """
    if y == 0:
        return ways
    if x == 0:
        return 0
    if z == 0:
        return 0
    output = 0
    for i in range(0, min(x+1, y//(z**2)+1)):
        output += g(x-i, y-i*z**2, z-1, c(x, i) * ways)
        output = output % mod
    return output % mod


limit = 81 * n
l = math.isqrt(limit) + 1

ans = 0
for i in range(1, l):
    d = i**2
    for j in range(d+1):
        k = d - j
        if (q, j) in gcache:
            gg = gcache[(q,j)]
        else:
            gcache[(q,j)] = g(q,j)
            gg = gcache[(q,j)]
        if (r, k) in fcache:
            ff = fcache[(r, k)]
        else:
            fcache[(r,k)] = f(r,k)
            ff = fcache[(r,k)]

        ans += gg * ff
        ans = ans % mod

print(ans)



