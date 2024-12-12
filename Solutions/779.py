n = 10**8
from prime import primes

p = primes(n+1)
r = 1
ans = 0
tans = 0

for i in p:
    ans += r/((i-1)*(i-1)*i)
    tans += r/((i-1)*i*i)
    r *= 1 - 1/i

print("{:.12f}".format(ans))
