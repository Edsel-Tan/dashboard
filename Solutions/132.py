from prime import primes

exp = 9

bound = 10**6
p = primes(bound)
p.remove(3)
ans = []

for i in p:
    texp, fexp = 0, 0
    totient = i-1
    while totient % 2 == 0:
        texp += 1
        totient = totient // 2
    while totient % 5 == 0:
        fexp += 1
        totient = totient // 5
    t = False
    for j in range(min(exp, texp)+1):
        for k in range(min(exp, fexp)+1):
            if pow(10,2**j*5**k, i) == 1:
                ans.append(i)
                t = True
                break
        if t:
            break
    if len(ans) == 40:
        break

print(sum(ans))
