from prime import primes
import itertools

pr = primes(5000)
ans = 0
for p, q, r in itertools.combinations(pr, 3):
    ans += 2 * p * q * r - p * q - q * r - p * r
print(ans)