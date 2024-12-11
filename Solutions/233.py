import math
from prime import primes

minn = 4151485
n = 10**11
p3 = []
p1 = []
for i in primes(n//21125 + 1):
    if i%4 == 1:
        p1.append(i)
    elif i%4 == 3:
        p3.append(i)

def p1d(n):
    for i in p1:
        if n%i == 0:
            return True
        if i > n:
            break
    return False
        


import itertools
c = 0
d = {}
for i in p1:

    for j in p1:

        if j == i:
            continue

        if i*j**2 > n:
            break

        for k in p1:


            if k == j:
                continue
            if k == i:
                continue
            
            if i*j**2*k**3 > n:
                break

            a = i*j**2*k**3
            b = n//a
            #print(a, b)
            if b in d.keys():
                c += d[b] * a
            else:
                d[b] = 0
                for x in range(1,b+1):
                    if not p1d(x):
                        c += x*a
                        d[b] += x
                    #print(c)

for i in p1:

    if i**7 > n:
        break

    for j in p1:

        if j == i:
            continue

        a = i**7*j**3
        if a > n:
            break
        b = n//a
        if b in d.keys():
            c += d[b] * a
        else:
            d[b] = 0
            for x in range(1,b+1):
                if not p1d(x):
                    c += x*a
                    d[b] += x


for i in p1:

    if i**10 > n:
        break

    for j in p1:

        if j == i:
            continue

        a = i**10*j**2
        if a > n:
            break
        b = n//a
        if b in d.keys():
            c += d[b] * a
        else:
            d[b] = 0
            for x in range(1,b+1):
                if not p1d(x):
                    c += x*a
                    d[b] += x


print(c)
            
