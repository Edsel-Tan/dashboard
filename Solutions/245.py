from prime import segmented_sieve
import math

n = 2*10**11
m = math.isqrt(n)
p = segmented_sieve(math.ceil(n**(2/3)))[1:]
ans = 0

for i in range(len(p)-1):
    if p[i] * p[i+1] > n:
        break
    for j in range(i+1, len(p)):
        if p[i] * p[j] > n:
            break

        if (p[i] * p[j] - 1) % (p[i] + p[j] - 1) == 0:
            # print("---")
            ans += p[i] * p[j]
            # print(p[i], p[j])
            # print((p[i] * p[j] - 1),  (p[i] + p[j] - 1))
            # print("---")


for i in range(len(p)-2):
    if p[i] * p[i+1] * p[i+2]> n:
        break

    for j in range(i+1, len(p)-1):
        a = p[i] * p[j]
        aa = (p[i] - 1) * (p[j] - 1)
        if a * p[j+1] > n:
            break

        if math.gcd(a, aa) != 1:
            continue

        for k in range(j+1, len(p)):
            b = a * p[k]
            bb = aa * (p[k] - 1)
            if b > n:
                break

            if (b - 1) % (b - bb) == 0:
                ans += b

for i in range(len(p)-3):
    if p[i] * p[i+1] * p[i+2] * p[i+3] > n:
        break

    for j in range(i+1, len(p)-2):
        a = p[i] * p[j]
        aa = (p[i] - 1) * (p[j] - 1)
        if a * p[j+1] * p[j+2] > n:
            break

        if math.gcd(a, aa) != 1:
            continue

        for k in range(j+1, len(p)-1):
            b = a * p[k]
            bb = aa * (p[k] - 1)
            if b * p[k+1] > n:
                break

            if math.gcd(b, bb) != 1:
                continue

            for l in range(k+1, len(p)):
                c = b * p[l]
                cc = bb * (p[l] - 1)
                if c > n:
                    break

                if (c - 1) % (c - cc) == 0:
                    ans += c

for i in range(len(p)-4):
    if p[i] * p[i+1] * p[i+2] * p[i+3] * p[i+4] > n:
        break

    for j in range(i+1, len(p)-3):
        a = p[i] * p[j]
        aa = (p[i] - 1) * (p[j] - 1)
        if a * p[j+1] * p[j+2] * p[j+3]> n:
            break

        if math.gcd(a, aa) != 1:
            continue

        for k in range(j+1, len(p)-2):
            b = a * p[k]
            bb = aa * (p[k] - 1)
            if b * p[k+1] * p[k+2] > n:
                break

            if math.gcd(b, bb) != 1:
                continue

            for l in range(k+1, len(p)-1):
                c = b * p[l]
                cc = bb * (p[l] - 1)
                if c * p[l+1] > n:
                    break

                if math.gcd(c, cc) != 1:
                    continue

                for m in range(l+1, len(p)):
                    d = c * p[m]
                    dd = cc * (p[m] - 1)
                    if d > n:
                        break

                    if (d - 1) % (d - dd) == 0:
                        ans += d

print(ans)

