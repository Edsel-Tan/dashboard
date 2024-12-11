from prime import primes

n = 10**6
p = primes(n)

def factor(m):
    output = 1
    for i in p:
        if i > m:
            break
        e = 0
        while m%i == 0:
            e += 1
            m = m // i
        output *= (e+1)
    return output

s = {}
for i in range(1, n//4+1):
    f = factor(i)//2
    if f in s.keys():
        s[f] += 1
    else:
        s[f] = 1


ans = 0
for i in range(1, 11):
    ans += s[i]
print(ans)
