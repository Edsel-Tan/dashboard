from prime import primes
n = 500
p = primes(10**5)

def nfactors(n):
    c = 1
    for i in p:
        z = 0
        while n % i == 0:
            n = n//i
            z += 1
        c *= z+1
    return c

for i in range(1, 10**5):
    if nfactors((i*(i+1))//2) > n:
        print((i*(i+1))//2)
        break
    