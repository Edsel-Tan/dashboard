import math
mod = 10**9

def f(n):
    if n % 6 == 1:
        t = int((n+1)/2) * int((2*n+1)/3) * n
    if n % 6 == 2:
        t = int(n/2) * int((n+1)/3) * (2*n+1)
    if n % 6 == 3:
        t = int(n/3) * int((n+1)/2) * (2*n+1)
    if n % 6 == 4:
        t = int(n/2) * int((2*n+1)/3) * (n+1)
    if n % 6 == 5:
        t = int((n+1)/6) * (2*n+1) * (n)
    if n % 6 == 0:
        t = int(n/6) * (2*n+1) * (n+1)
    return t % mod


def solve(n):
    sqrtn = math.ceil(math.sqrt(n))

    t = 0
    c = f(sqrtn)

    for i in range(1, sqrtn+1):
        t += math.floor(n/i) * i**2


    for i in range(1, sqrtn):
        if math.floor(n/i) >= sqrtn:
            t += (f(math.floor(n/i)) - c)

    return t % mod

def check(n):

    t = 0

    for i in range(1,n+1):
        t += math.floor(n/i) * i**2

    return t % mod

print(solve(10**15))