from prime import primes
import itertools
import math


n = 10**8
p = primes(n+2)
q = set(p)
p = p[1:]

    

def product(lis):
    output = 2
    for i in lis:
        output *= p[i]
    return output


def check(lis):
    n = product(lis)
    for i in range(len(lis)+1):
        for j in itertools.combinations(lis, i):
            d = product(j)

            if d + n//d not in q:
                return False
    return True


ans = 3
count = 0
while True:
    count += 1
    start = list(range(count))

    m = product(start)
    if m > n:
        break
    while True:
        if check(start):
            ans += product(start)
        
        t = count-1
        while start[t] == len(q) - count + t:
            t -= 1
        
        if t == -1:
            break

        start[t] += 1
        for i in range(t+1, count):
            start[i] = start[i-1] + 1
        m = product(start)

        while m > n:
            t -= 1
            if t == -1:
                break
            start[t] += 1
            for i in range(t+1, count):
                start[i] = start[i-1] + 1
            m = product(start)

        if t == -1:
            break

print(ans)