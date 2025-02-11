from prime import primes

p = primes(10**6)
for i in range(len(p)):
    if p[i] > 10**5:
        break
p = p[i:]

import itertools
p = set(p)
ans = 10**6
for mask in itertools.combinations(range(6), 3):
    for i in range(1000):
        j = [i//100, (i//10)%10, i%10]
        idx = 0
        number = ["" for i in range(6)]
        for k in range(6):
            if k not in mask:
                number[k] = str(j[idx])
                idx += 1
        
        s = 10**6
        count = 0
        for k in range(10):
            for l in mask:
                number[l] = str(k)
                z = int("".join(number))
            if z in p:
                count += 1
                s = min(z, s)
        
        if count >= 8:
            ans = min(ans, s)

print(ans)
