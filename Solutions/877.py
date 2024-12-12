
def mult(a, b):
    ans = 0
    while a != 0:
        l = a & (-a)
        ans = ans ^ (l*b)
        a -= l
    return ans

def f(a, b):
    return mult(a, a) ^ mult(b, b) ^ (mult(2*a, b))


def next(a, b):
    return b, (2*b ^ a)
    
    
def x(n):
    ans = 0
    s = (0, 3)
    while s[1] < n:
        ans = ans ^ s[1]
        s = next(*s)
    return ans

print(x(10**18))
            