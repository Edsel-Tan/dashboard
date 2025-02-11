from prime import primes

p = set(primes(10**7))
import itertools
c = sorted("1234567", reverse=True)
for i in itertools.permutations(c, 7):
    x = int("".join(i))
    if x in p:
        break
print(x)