#6,24,54,243,


def g(x,y):
    return 2**x * 3**y

def wut(n):
    grid = [[0 for j in range(15)] for i in range(15)]

    p2 = 0
    c = g(p2,0)
    while c <= n:
        p3 = 0
        c = g(p2,p3)

        while c <= n:
            grid[p2][p3] = 1
            p3+=1
            c = g(p2,p3)
        p2+=1
        c = g(p2,0)

    for i in grid:
        print(i)

            
            
            
n = 10**16

#9214701193868381
#9214701193867859
#9277065527065526
#9155889870588942
#9216989374703836
#9217439278073505
#9226119833629061
#9248575498575499
#9216265995421336

import math

def logg(n,base):
    exp = 0
    while base ** exp <= n:
        exp += 1
    return exp-1

def f(n):
    if n < 6:
        return 0
    if n < 24:
        return 1
    if n < 54:
        return 2
    else:
        output = 0
        s = logg(n,3)
        output = (s+1)//3
        s = logg(n,2)
        output += (s+1)//3
        if s%3 == 2:
            if 2**(s-1)*3 <= n:
                return output
            else:
                return output - 1
        return output
##        s = logg(n,3)
##        output += (s+1)//3
##        s = logg(n,2)
##        output += (s+1)//3
##        if n&(n-1)==0:
##            if (s+1)%3 == 0:
##                return output - 1
##        return output


output = 0
lis = []
for i in range(60):
    for j in range(60):
        if g(i,j) < n:
            lis.append(g(i,j))
lis.append(n)
lis = sorted(lis, reverse = True)

ranges = []
r = []
for i in lis:
    if n//i in ranges:
        continue
    ranges.append(n//i)
    r.append((n//i, i))


def h(a,b):
    if b < a:
        return 0
    return ((b-1)//6 - (a-2)//6) + ((b-5)//6 - (a-6)//6)

output += f(n)
for i in range(len(r)-1):
    m = h(r[i][0]+1,r[i+1][0])
    output += m*f(r[i+1][1])
    #print(f(r[i][1]), r[i], r[i+1], m*f(r[i+1][1]))

print(n - output)
