from fractions import Fraction
from math import floor, log, exp

ans = 0
for e in range(51):
    x = Fraction(0,1)
    c = Fraction(1,2)
    m = 2**e

    for i in range(15):
        x += c * m
        c *= c

    x -= floor(x)
    x = 1/x
    c = []
    while x > 0:
        c.append(floor(x))
        if x-floor(x) == 0:
            break
        x = 1/(x-floor(x))

    d = dict(zip(set(c), [0 for i in set(c)]))
    for i in c:
        d[i] += 1

    for i in d:
        d[i] = d[i] / len(c)

    t = 1
    s = 0
    if e < 32:
        for i in d:
            est = 0
            est_min = 1
            for a in range(30):
                for b in [1,2,3,4,5,6,8,12]:
                    if abs(a/b - d[i]) * (b) < est_min:
                        est_min = abs(a/b - d[i]) * (b)
                        est = (a,b)
    ##        if est_min > 0.01:
    ##            est = (0, 1)
            t *= i ** (est[0] / est[1])
    ##        print(d[i], est[0], est[1], i)
            s += est[0] / est[1]
            d[i] = (d[i], est)
    else:
        for i in d:
            est = 0
            est_min = 1
            for a in range(12):
                for b in [1,2,3,4,5,6,8,12,24]:
                    if abs(a/b - d[i]) * (b) < est_min:
                        est_min = abs(a/b - d[i]) * (b)
                        est = (a,b)
    ##        if est_min > 0.01:
    ##            est = (0, 1)
            t *= i ** (est[0] / est[1])
##            print(d[i], est[0], est[1], i)
            s += est[0] / est[1]
            d[i] = (d[i], est)
    ans += log(t)

print("{:.6f}".format(exp(ans/51)))