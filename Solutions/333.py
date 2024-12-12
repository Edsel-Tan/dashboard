from prime import primes
import math

n = 10**6

p = set(primes(n))
tl = math.ceil(math.log2(n))
trl = math.ceil(math.log(n, 3))

count = dict(zip(p, [0 for i in p]))
f = lambda a,b: 2**a * 3**b

def enum(a, b, x):
    if x + f(a,b) >= n:
        return []
    
    c = x + f(a,b)
    output = [c]
    for i in range(a+1, tl):
        for j in range(b):
            if c + f(i,j) >= n:
                break
            for k in enum(i, j, c):
                output.append(k)
    return output
            


for a in range(tl):
    for b in range(trl):
        for k in enum(a,b,0):
            if k in count:
                count[k] += 1

ans = 0
for q in count:
    if count[q] == 1:
        ans += q
print(ans)