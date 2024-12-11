from prime import primes

n = 10**6
p = primes(n)

factors = dict(zip([i for i in range(1, n)], [{1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0} for i in range(1, n)]))

for pi in p:
    c = pi
    while c < n:
        for i in range(c, n, c):
            factors[i][pi%9] += 1
        c = c * pi
        
ans = 0
for i in range(2, n):
    t = 0
    idd = factors[i]
    x = idd[3] // 2
    idd[3] -= 2 * x
    idd[9] += x
    
    x = min(idd[4], idd[2])
    idd[4] -= x
    idd[2] -= x
    idd[8] += x

    x = idd[2] // 3
    idd[2] -= x * 3
    idd[8] += x

    x = min(idd[2], idd[3])
    idd[3] -= x
    idd[2] -= x
    idd[6] += x

    for j in range(1,10):
        t += j * idd[j]

    ans += t

print(ans)