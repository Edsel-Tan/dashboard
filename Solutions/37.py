from prime import primes

p = primes(10**6)

def log10(x):
    c = 1
    while x > 0:
        c *= 10
        x = x//10
    return c

ans = set()
start = [2,3,5,7]

for i in start:
    for j in range(1, 10):
        k = j*log10(i) + i
        if k in p:
            start.append(k)
            ans.add(k)

ans2 = set()
start = [2,3,5,7]
for i in start:
    for j in range(1,10):
        k = i*10+j
        if k in p:
            start.append(k)
            ans2.add(k)

print(sum(ans2.intersection(ans)))