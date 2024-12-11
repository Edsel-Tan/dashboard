from prime import miller_rabin, primes
import math

def fast_elim(n):
    c = [2,3,5,7,11]
    for _ in c:
        if n%_ == 0:
            return False
    return True

def check(n):
    while n > 100:
        if n%1000 == 200:
            return True
        n = n//10
    return False

LIMIT = 10**12
p = primes(math.isqrt(LIMIT//8))
answer = []


for i in range(len(p)):
    for j in range(i+1, len(p)):
        t = p[i]**2 * p[j]**3
        if t > LIMIT:
            continue
        if check(t):
            m = list(str(t))
            pp = True
            for k in range(len(m)):
                if not pp:
                    break
                for l in range(10):
                    m[k] = str(l)
                    o = int(''.join(m))
                    if fast_elim(o):
                        if miller_rabin(o):
                            pp = False
                            break
                m[k] = str(t)[k]
            if pp:
                answer.append(t)

        else:
            continue

for i in range(len(p)):
    for j in range(i+1, len(p)):
        t = p[j]**2 * p[i]**3
        if t > LIMIT:
            continue
        if check(t):
            m = list(str(t))
            pp = True
            for k in range(len(m)):
                if not pp:
                    break
                for l in range(10):
                    m[k] = str(l)
                    o = int(''.join(m))
                    if fast_elim(o):
                        if miller_rabin(o):
                            pp = False
                            break
                m[k] = str(t)[k]
            if pp:
                answer.append(t)

        else:
            continue


print(sorted(answer)[199])
