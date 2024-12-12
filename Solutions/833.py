##p = 3017498651375135641223068262380416846553
p=136101521
import math

def add(a, b):
    r = max(len(a),len(b))
    s = [0 for i in range(r)]
    for i in range(r):
        if i < len(a):
            s[i] += a[i]
        if i < len(b):
            s[i] += b[i]
        s[i] = s[i]
    return s

def multiply(a,b):
    r = len(a) + len(b) - 1
    s = [0 for i in range(r)]
    for i in range(r):
        for j in range(i+1):
            if j < len(a):
                if i-j < len(b):
                    s[i] += a[j] * b[i-j]
        s[i] = s[i]
    return s

def polyv(poly, x):
    output = 0
    for i in range(len(poly)):
        output += (poly[i] * x**i)
    return output
    

class Polynomial:

    def __init__(self, lis):
        self.lis = lis

    def __add__(self, other):
        return Polynomial(add(self.lis, other.lis))

    def __mul__(self, other):
        return Polynomial(multiply(self.lis, other.lis))

    def value(self, x):
        return polyv(self.lis, x)




###Non trivial solution to Pell's Polynomials
Q = Polynomial([1,2])
P = Polynomial([2])
C1 = Polynomial([0,1,1])
C2 = Polynomial([0,1])
C3 = Polynomial([1,1])

###Base solutions
R = Polynomial([1,4])
S = Polynomial([3,4])

###Recurrences
n = 25
x = [(Q,P)]
y = [(R,S)]
for i in range(n):
    x.append((x[-1][0]*Q + C1 * x[-1][1] * P, x[-1][1] * Q + x[-1][0] * P))
    y.append((y[-1][0]*Q + y[-1][1] * P * C2, y[-1][1] * Q + y[-1][0] * P * C3))

z = []
for i in range(n):
    z.append(x[i])
    z.append(y[i])


n = 35
limit = 2*10**n
output = 0
solutions = []

Pn = C1 * z[0][0] * z[0][1]
deg = len(Pn.lis) - 1
limits = [0, 10**(n//deg+2)]
while limits[1] - limits[0] > 1:
    mid = (limits[0] + limits[1]) // 2
    if Pn.value(mid) > limit:
        limits = [limits[0], mid]
    else:
        limits = [mid, limits[1]]

l = limits[0]%p
output += Pn.lis[0] * l
output += Pn.lis[1] * l*(l+1) * pow(2, -1, p) 
output += Pn.lis[2] * l*(l+1)*(2*l+1) * pow(6, -1, p)
output += Pn.lis[3] * l**2*(l+1)**2 * pow(4, -1, p)
output = output%p

##print("done")

for i in range(1,len(z)):
    Pn = C1 * z[i][0] * z[i][1]
    deg = len(Pn.lis) - 1
    limits = [0, 10**(n//deg+2)]
    while limits[1] - limits[0] > 1:
        mid = (limits[0] + limits[1]) // 2
        if Pn.value(mid) > limit:
            limits = [limits[0], mid]
        else:
            limits = [mid, limits[1]]

    l = limits[1]%p
    for k in range(1,l):
        output += Pn.value(k)%p
    output = output%p

for i in range(len(z)):
    for j in range(i,len(z)):
        if math.gcd((j+2),(i+2))!=1:
            continue
        else:
            Pn = C1 * z[i][0] * z[i][1] * z[j][0] * z[j][1]
            deg = len(Pn.lis) - 1
            limits = [0, 10**(n//deg+2)]
            while limits[1] - limits[0] > 1:
                mid = (limits[0] + limits[1]) // 2
                if Pn.value(mid) > limit:
                    limits = [limits[0], mid]
                else:
                    limits = [mid, limits[1]]

            l = limits[1]%p
            for k in range(1,l):
                output += Pn.value(k)%p
            output = output%p

print(output//2)
        