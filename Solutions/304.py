from prime import segmented_sieve, miller_rabin
import math

p = segmented_sieve(10**8)
m = [3,7,13,67,107,630803]
n = 1234567891011

a = 0
b = 1
c = 1
d = [False for i in m]
e = [[a,b] for i in m]
while False in d:
    c += 1
    a = a+b
    b = a+b
    a = b-a
    b -= a
    a = a%n
    b = b%n
    for i in range(len(m)):
        if not d[i] and b % m[i] == 0:
            d[i] = (c, (a+b) % m[i])

        if not d[i]:
            e[i].append(b)

l = 10**7
sieve = [True for i in range(l)]
for i in p:
    for j in range((-10**14)%i, l, i):
        sieve[j] = False

x = [10**14+i for i in range(l) if sieve[i]]

def crt(a, b, x, y):
    return (x*b*pow(b,-1,y) + a*y*pow(y,-1,b)) % (b*y), b*y

def g(n):
    x, y = 0, 1
    for i in range(len(m)):
        j = n%d[i][0]
        a = pow(d[i][1], n//d[i][0], m[i]) * e[i][j]
        x, y = crt(a, m[i], x, y)
    return x

ans = 0
for i in range(100000):
    ans += g(x[i])
print(ans%n)