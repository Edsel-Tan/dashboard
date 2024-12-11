from prime import primes
import math

n = 10**16
p = primes(100)

def c(n, r):
    return math.factorial(n)//math.factorial(r)//math.factorial(n-r)

mults = []

def product(lis):
    output = 1
    for i in lis:
        output *= p[i]
    return output

ans = 0

count = 4
while count <= len(p):
    mult = 0
    for i in range(len(mults)):
        mult += c(count, 4+i) * mults[i]
    mult = 1-mult
    mults.append(mult)

    start = list(range(count))
    x = product(start)

    if x > n:
        break

    while x <= n:
        ans += (n//x) * mult

        t = count - 1
        while start[t] == len(p) - count + t:
            t -= 1
            if t < 0:
                break
        
        if t < 0:
            break

        start[t] += 1
        for i in range(t+1, count):
            start[i] = start[i-1] + 1

        x = product(start)
        while x > n:
            t -= 1
            if t < 0:
                break

            start[t] += 1
            for i in range(t+1, count):
                start[i] = start[i-1] + 1
            x = product(start)
        
        if t < 0:
            break

    count += 1
            


print(ans)
