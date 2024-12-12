mod = 10**9 + 7

def memoize(f):
    cache = {}
    def g(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return g

def memoize_mod(f):
    cache = {}
    def g(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args] % mod
    return g


@memoize
def num_odd(n):
    if n <= 6:
        return (n+1)//2
    if n == 7:
        return 3
    p2 = len(bin(n)) - 2
    x = ((1 << (p2 - 1)) - 1)
    y = n - x - 1
    if y >= (3 << (p2 - 3)):
        return num_odd(x) + num_odd((3 << (p2-3)) - 1)
    return num_odd(x) + num_odd(y)

@memoize
def num_bin(n):
    if n <= 6:
        return n
    if n == 7:
        return 6
    p2 = len(bin(n)) - 2
    x = ((1 << (p2 - 1)) - 1)
    y = n - x - 1
    z = (3 << (p2 - 3))
    if y >= z:
        return num_bin(x) + num_bin(z - 1) + 1
    return num_bin(x) + num_bin(y) + 1

@memoize_mod
def num_sum(n):
    if n <= 7:
        return [0,1,1,4,4,9,9,9][n]
    p2 = len(bin(n)) - 2
    x = ((1 << (p2 - 1)) - 1)
    y = n - x - 1
    z = (3 << (p2 - 3))
    if y >= z:
        return num_sum(x) + num_sum(z - 1) + (num_odd(n) - num_odd(x)) * (num_bin(x) + 1)
    return num_sum(x) + num_sum(y) + (num_odd(n) - num_odd(x)) * (num_bin(x) + 1)
        
@memoize_mod
def num_sq(n):
    if n <= 7:
        return [0,1,1,10,10,35,35,35][n]
    p2 = len(bin(n)) - 2
    x = ((1 << (p2 - 1)) - 1)
    y = n - x - 1
    z = (3 << (p2 - 3))
    if y >= z:
        return num_sq(x) + num_sq(z - 1) + (num_odd(n) - num_odd(x)) * (num_bin(x) + 1) ** 2 + 2 * (num_bin(x) + 1) * (num_sum(z - 1))
    return num_sq(x) + num_sq(y) + (num_odd(n) - num_odd(x)) * (num_bin(x) + 1) ** 2 + 2 * (num_bin(x) + 1) * (num_sum(y))
    


n = 10**16
l = 0
r = 10**18 * 2

while (r-l):
    m = (l+r)//2
    if num_bin(m) >= n:
        r = m
    else:
        l = m+1

print(num_sq(l))


