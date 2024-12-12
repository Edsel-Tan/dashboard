n = 1234567890123456789

def g(x):
    c = 1
    while c <= x:
        c *= 10
    return c // 10

def f(x):
    if x < 10:
        c = {}
        for i in range(x+1):
            c[i] = [1,i]
        return c
    m = g(x)
    l = x//m * m
    a = f(m - 1)
    b = f(x - l)
    c = {}
    d = x//m
    for i in range(0, x//m):
        for j in a:
            if i + j in c:
                c[i+j][0] += a[j][0]
                c[i+j][1] += a[j][0] * m * i + a[j][1]
            else:
                c[i+j] = a[j].copy()
                c[i+j][1] +=  a[j][0] * m * i

    for i in b:
        if i+d in c:
            c[i+d][0] += b[i][0]
            c[i+d][1] += b[i][1] + b[i][0] * d * m
        else:
            c[i+d] = [0,0]
            c[i+d][0] = b[i][0]
            c[i+d][1] = b[i][1] + b[i][0] * d * m

    # print()
    # print(x,b,c,d,m,l,sep="\n")
    # print()
    return c

ans = 0
m = f(n)
for i in m:
    if i != 0:
        ans += m[i][1] / i
print("{:.12E}".format(ans))