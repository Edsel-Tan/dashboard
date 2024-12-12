from decimal import Decimal #type: ignore
import decimal #type: ignore


from prime import miller_rabin, primes

i = 724609891
candidates = []
while i < 729927007:
    if miller_rabin(i):
        candidates.append(i)
    i += 100000

p = primes(100000)
import math
for i in candidates:
    j = i-1
    pos = True
    for k in p:
        if k > math.isqrt(j):
            break
        if j%k == 0:
            if pow(10, j//k, i) == 1:
                pos = False
                break
    if pos:
        c = i


digits = (9*c)//10
ans = 9

while digits > 0:
    k = digits%10
    k = 9-k
    ans += k
    digits += k*c
    digits = digits//10
print(ans)


