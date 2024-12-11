
import math
def calc(a, x):
    f = lambda y : math.floor((y+math.ceil(x/y))/2)
    ans = 0
    while f(a) != a:
        a = f(a)
        ans += 1
    return ans

n = 14
a = 7 * 10 ** ((n-1)//2)

l = 10**(n-1)
r = 10**(n)-1

def f(a, x, y):
    output = 0
    b = math.ceil((x/a-1+a)/2)
    while b <= (y/a+1+a)/2:
        if b == a:
            b += 1
            continue
        l = a*(2*b-a-1) + 1
        r = a*(2*b-a+1)
        l = max(l, x)
        r = min(y, r)
        output += f(b, l, r) + r - l + 1
        b += 1
    return output

print("{0:.10f}".format(f(a, l, r)/(r-l+1)+1))


