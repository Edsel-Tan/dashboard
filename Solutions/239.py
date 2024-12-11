import math
from prime import primes

# print(math.factorial(100))
p = primes(100)
print(p, len(p))

total = math.factorial(100)

def c(n, r):
    output = 1
    for i in range(r):
        output *= n-i
        output //= i+1
    return output

ans = 0

for i in range(23):
    ans += pow(-1, i) * c(22, i) * math.factorial(97-i)
ans *= c(25,3)
print("{:.12f}".format(ans/total))