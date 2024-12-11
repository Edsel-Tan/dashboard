from prime import primes
import math

n = 10**9
p = primes(100)
# q = primes(10000)
# for i in p:
#     q.remove(i)
# c = 0
# for i in q:
#     c += n // i
# print(c)


def count(pr, n):
    if n < 1:
        return 0
    if len(pr) == 0:
        return 1
    if n < pr[0]:
        return 1
    
    output = 0
    i = 0
    while p[0] ** i <= n:
        output += count(pr[1:], n//(pr[0] ** i))
        i += 1
        # print(i, p[0], p[0] ** i, n)
    return output

def product(lis):
    output = 1
    for i in lis:
        output *= p[i]
    return output

ans = 1
c = 1
while c <= len(p):
    start = list(range(c))
    m = product(start)
    
    if m > n:
        break
    while True:
        ans += count([p[i] for i in start], n//m)
        # print(count([p[i] for i in start], n//m), m)

        t = c-1
        while t != -1 and start[t] == len(p) - c + t:
            t -= 1

        if t == -1:
            break

        start[t] += 1
        for i in range(t+1, c):
            start[i] = start[i-1] + 1
        m = product(start)

        while m > n:
            t -= 1
            if t == -1:
                break
            start[t] += 1
            for i in range(t+1, c):
                start[i] = start[i-1] + 1
            m = product(start)

        if t == -1:
            break

    c += 1

print(ans)



