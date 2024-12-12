n = 101

l = -1
r = -0.98
eps = 1e-15

f = lambda x : x**4
f_ = lambda x : 4*x**3

def solve(y, a, b):
    l = a
    r = b

    ispositive = y(a+eps) > 0
    
    while (r-l) > eps:
        m = (r+l)/2
        if (y(m) > 0) == ispositive:
            l = m
        else:
            r = m

    return l

y = lambda x : x**2 - 2

while r-l > eps:
    m = (r+l)/2

    ngon = [(-1, 1), (m, f(m))]

    for i in range(n-2):
        g = f_(ngon[-1][0])
        c = ngon[-2][1] - g * ngon[-2][0]

        y = lambda x : x**4 - g * x - c
        x = solve(y, ngon[-1][0], 2)
        ngon.append((x, f(x)))
        if x > 1:
            break


    if ngon[-1][0] > 1:
        r = m
    else:
        l = m

def area(a,b,c):
    return abs(a[0] * b[1] + b[0] * c[1] + c[0] * a[1] - a[0] * c[1] - b[0] * a[1] - c[0] * b[1])

def arean(ngon):
    a = 0
    for i in range(1, len(ngon)-1):
        a += area(ngon[0], ngon[i], ngon[i+1])
    return a/2

print("{:.9f}".format(arean(ngon)))
