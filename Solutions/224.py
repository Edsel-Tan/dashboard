from __future__ import annotations
from prime import primes
import math

class Complex:

    def __init__(self, a, b):
        self.real = a
        self.img = b

    def __add__(self, other : Complex):
        return Complex(self.real + other.real, self.img + other.img)
    
    def __mul__(self, other : Complex):
        return Complex(self.real * other.real - self.img * other.img, self.real * other.img + self.img * other.real)
    
    def norm(self):
        return self.real * self.real + self.img * self.img
    
    def __str__(self):
        return f"{self.real}+{self.img}i"
    
    def __repr__(self):
        return f"{self.real}+{self.img}i"
    
    def __floordiv__(self, other : int):
        return Complex(self.real//other, self.img//other)
    
    def conj(self):
        return Complex(self.real, -self.img)
    
    def __pow__(self, power : int):
        if power == 0:
            return Complex(1, 0)
        if power%2 == 0:
            return (self*self) ** (power//2)
        else:
            return self * ((self*self) ** (power//2))
    


n = 75000000
cl = math.ceil(n/2)

sieve = [True] * (cl//2)
for i in range(3,int(cl**0.5)+1,2):
    if sieve[i//2]:
        sieve[i*i//2::i] = [False] * ((cl-i*i-1)//(2*i)+1)

p1 = {}
for a in range(1, math.isqrt(cl)+1):
    for b in range(a+1, math.isqrt(cl)+1, 2):
        d = a**2 + b**2
        if d > cl:
            break
        
        if sieve[d//2]:
            p1[d] = Complex(a, b)

pos = [True for i in range(cl+2)]
p = [2] + [2*i+1 for i in range(1,cl//2) if sieve[i]]
del sieve

for i in p:
    if i%4 != 3:
        continue

    pi = i
    while pi < cl:
        for j in range(pi, cl+2, pi):
            if j % (pi * i) != 0:
                pos[j] = False
        pi *= i * i


npos = [None for i in range(cl+1)]
for i in range(2,cl):
    npos[i] = pos[i-1] and pos[i+1]
del pos
pos = [i for i in range(1,cl+1) if npos[i]]
del npos

def pf(n):
    output = []
    for i in p:
        if i > math.sqrt(n):
            if n != 1:
                output.append([n, 1])
            break
        if n % i == 0:
            output.append([i, 0])
            while n % i == 0:
                output[-1][1] += 1
                n = n // i
    return output

# print(pos)

ans = 0
for i in pos:
    f = pf(i**2-1)
    g = [Complex(1, 0)]

    for j in f:
        if j[0] % 4 == 1:
            ng = []
            c = p1[j[0]] ** j[1]
            for k in range(j[1]+1):
                # print(c, j[1])
                for l in g:
                    ng.append(c * l)
                c *= p1[j[0]].conj() * p1[j[0]].conj()
                c //= p1[j[0]].norm()
            g = ng
        elif j[0] == 2:
            e = Complex(1,0)
            for k in range(j[1]):
                e *= Complex(1,1)
            for k in range(len(g)):
                g[k] *= e
        else:
            e = j[0] ** (j[1]//2)
            for k in range(len(g)):
                g[k] *= Complex(e, 0)

    s = set()
    for j in g:
        l = [k for k in sorted([abs(j.real), abs(j.img)])]
        l = tuple(l)
        if l in s:
            continue
        else:
            if (sum(l) + i) <= n:
                # print(*l, i)
                ans += 1
            s.add(l)


print(ans)


        

        
