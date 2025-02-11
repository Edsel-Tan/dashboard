from prime import primes

n = 10**6
p = set(primes(n))

def circ(x):
    x = str(x)
    for i in range(len(x)):
        if int(x[i:] + x[:i]) not in p:
            return False
    return True

ans = 0
for i in p:
    if circ(i):
        ans += 1
print(ans)
