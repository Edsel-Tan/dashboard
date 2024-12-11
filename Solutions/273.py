from complex import Complex
from prime import primes

p = primes(150)
c = []

for a in range(1, 14):
    for b in range(a+1, 14):
        if a**2 + b**2 in p:
            p.remove(a**2+b**2)
            c.append((Complex(a, b), Complex(a, b).conj(), Complex(1, 0)))

c = sorted(c)
solutions = set()
ans = 0

def product(l):
    output = Complex(1, 0)
    for i in l:
        output *= i
    return output


import itertools
for i in itertools.product(*c):
    j = product(i)
    s = (min(abs(j.real), abs(j.img))), abs(max(abs(j.real), abs(j.img)))
    if s not in solutions:
        solutions.add(s)
        ans += s[0]

print(ans)

