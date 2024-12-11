import math
from prime import segmented_sieve

n = 2*10**9
p = segmented_sieve(n+1)

ps = []
for i in p:
    if i % 168 in [1,25,121]:
        ps.append(i)

# print(ps, len(ps))

ans = 0
for i in ps:
    ans += math.isqrt(n//i)

for i in range(len(ps)):
    if ps[i] * ps[i+1] > n:
        break
    for j in range(i+1, len(ps)):
        if ps[i] * ps[j] > n:
            break
        ans += math.isqrt(n//(ps[i]*ps[j]))


for i in range(len(ps)):
    if ps[i] * ps[i+1] * ps[i+2] > n:
        break
    for j in range(i+1, len(ps)):
        if ps[i] * ps[j] * ps[j+1] > n:
            break
        for k in range(j+1, len(ps)):
            if ps[i] * ps[j] * ps[k] > n:
                break
            ans += math.isqrt(n//(ps[i]*ps[j]*ps[k]))


for i in range(len(ps)):
    if ps[i] * ps[i+1] * ps[i+2] * ps[i+3] > n:
        break
    for j in range(i+1, len(ps)):
        if ps[i] * ps[j] * ps[j+1] * ps[j+2] > n:
            break
        for k in range(j+1, len(ps)):
            if ps[i] * ps[j] * ps[k] * ps[k+1]> n:
                break
            for l in range(k+1, len(ps)):
                if ps[i] * ps[j] * ps[k] * ps[l]> n:
                    break
                ans += math.isqrt(n//(ps[i]*ps[j]*ps[k]*ps[l]))


m = math.isqrt(n)
sieve = [[False for i in range(m+1)] for j in range(4)]
for i in p:
    if i % 4 == 1:
        for j in range(i, m+1, i):
            sieve[0][j] = True
    if i % 8 == 1 or i % 8 == 3:
        for j in range(i, m+1, i):
            sieve[1][j] = True
    if i % 12 == 1 or i % 12 == 7:
        for j in range(i, m+1, i):
            sieve[2][j] = True
    if i % 28 == 1 or i % 28 == 9 or i % 28 == 25 or i % 28 == 15 or i % 28 == 11 or i % 28 == 23:
        for j in range(i, m+1, i):
            sieve[3][j] = True

for i in range(2, m+1, 2):
    sieve[2][i] = True

for i in range(4, m+1, 4):
    sieve[3][i] = True


for i in range(1, m+1):
    if sieve[0][i] and sieve[1][i] and sieve[2][i] and sieve[3][i]:
        ans += 1


print(ans)