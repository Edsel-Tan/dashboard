from prime import primes, miller_rabin

n = 10000
p = primes(n)
s = set(p)

def concat(x, y):
    z = y
    while z > 0:
        x *= 10
        z = z//10
    return x + y

def is_prime(x):
    if x <= n:
        return n in s
    return miller_rabin(x)


r = [set() for i in range(len(p))]

for i in range(len(p)):
    for j in range(i+1, len(p)):
        x = p[i]
        y = p[j]
        if is_prime(concat(x, y)) and is_prime(concat(y, x)):
            r[i].add(j)
            r[j].add(i)

c = []

ans = 10**6

def f(s: set, x: int):
    global ans
    if len(c) == 5:
        ans = min(ans, sum(c))
        return
    for i in s:
        if i < x:
            continue
        c.append(p[i])
        f(s.intersection(r[i]), i)
        c.pop()
        
f(set(range(len(p))), 0)
print(ans)