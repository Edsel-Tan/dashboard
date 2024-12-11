n = 10**12
m = 10**5

def memoize(f):
    cache = {}
    def g(n):
        if n in cache:
            return cache[n]
        else:
            cache[n] = f(n)
            return cache[n]
    return g

c = 1
for i in range(1, m, 2):
    if i%5 == 0:
        continue
    c *= i
    c = c % m

@memoize
def f(n):
    if n == 0:
        return 1
    ans = 1
    q = n//m
    r = n%m
    for i in range(1, r+1, 2):
        if i%5==0:
            continue
        ans *= i
        ans = ans % m
    ans *= pow(c, q, m)
    ans *= f(n//5)
    return ans

expp = 0
l = 5
while l < n:
    expp += n//l
    l *= 5

ans = 1
exp = 0

while n > 1:
    ans *= f(n)
    ans = ans % m
    n = n//2
    exp += n

ans *= pow(2, exp-expp, m)
ans = ans % m
print(ans)

