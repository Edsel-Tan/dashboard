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
    return tuple(sorted((b, (2*b ^ a))))

n = 1000000
m = 10**17
found = [False for i in range(n+1)]
ss = set()

def msb(n):
    a = 0
    while n != 0:
        n = n>>1
        a+=1
    return a

def all(s):
    return s, (s[1], s[0])

def norm(s):
    return tuple(sorted(s))

def x(n, s):
    if s == (0,0):
        ss.add(s)
    s = norm(s)
    stack = [s]
    while len(stack) > 0:
        t = stack[-1]
        del stack[-1]
        if t not in ss and t[1] < n:
            ss.add(t)
            for i in all(t):
                stack.append(next(*i))


for a in range(2000):
    for b in range(a,100000):
        c = f(a,b)
        if c <= n:
            x(m, (a,b))
print(len(ss))
