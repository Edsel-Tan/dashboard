from prime import primes, memoize, miller_rabin

n = 10**9
p = primes(1000)
t = 1
c = 0
for i in p:
    if t > n:
        c -= 1
        break
    c += 1
    t *= i

# print(c, p[:c])
p = p[:c]

admissible = []
def multiples(p, m):
    if m < 1:
        return []
    if len(p) == 0:
        return [1]
    output = []
    for i in multiples(p[1:], m):
        a = 1
        while a * i < m:
            output.append(a*i)
            a = a * p[0]
    return output

c = 1
for i in range(len(p)):
    c = c*p[i]
    for j in multiples(p[:i+1], n//c+1):
        admissible.append(c*j)
admissible = sorted(admissible)

fortunate = set()
miller_rabin = memoize(miller_rabin)
for i in range(3, n, 2):
    if len(admissible) == 0:
        break
    remove = []
    for j in admissible:
        if miller_rabin(j+i):
            fortunate.add(i)
            remove.append(j)
    for j in remove:
        admissible.remove(j)
print(sum(fortunate))