n = 18

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
        r = n-r
    output = 1
    for i in range(r):
        output *= n-i
        output = output // (i+1)
    return output


import math

@memoize
def dpp(n, x):
    if n < 0:
        return 0
    if x == 1:
        return n >= 0 and n <= 3
    else:
        output = 0
        for i in range(4):
            output += c(n, i) * dpp(n-i, x-1)
        return output

@memoize
def dp(n, x, s, q):
    if s == 0 and n == 0:
        return math.factorial(q)
    if s == 0:
        return 0
    output = 0
    for i in range(0, n//s+1):
        output += c(x, i) * dp(n-s*i, x-i, s-1, q) // pow(math.factorial(s), i)
    return output

def xd(x):
    return dp(x, 9, 3, x) + dp(x-1, 9, 3, x-1) * c(x, 1) + dp(x-2, 9, 3, x-2) * c(x, 2) + dp(x-3, 9, 3, x-3) * c(x, 3)

def xdd(x):
    return dp(x, 9, 3, x) + dp(x-1, 9, 3, x-1) * c(x-1, 1) + dp(x-2, 9, 3, x-2) * c(x-1, 2) + dp(x-3, 9, 3, x-3) * c(x-1, 3)

def xddd(x):
    return dpp(x, 9) + dpp(x-1, 9) * c(x-1, 1) + dpp(x-2, 9) * c(x-1, 2) + dpp(x-3, 9) * c(x-1, 3)


print(xddd(n))