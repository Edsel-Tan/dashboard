u = 200000000
from prime import primes

ps = primes(u//34)

ans = 130775524

a = 1.0
b = 0.0
g = 0
h = 0
c = 1
d = 0

for _ in range(ans):
    e = g-h
    x = 10**e * a + b
    if x >= 10:
        i = h + 1
        a = b
        g = h
        h = i
        b = x/10
    else:
        a = b
        g = h
        b = x

    

    x = (c+d)%(10**16)
    c = d
    d = x

print(f"{d},{'{:.1f}'.format(b)}e{h}")