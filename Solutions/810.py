def xor_product(x, y):
    output = 0
    while x > 0:
        if x & 1:
            output = output ^ y
        x = x >> 1
        y = y << 1
    return output

n = 2*10**8
primes = []
isPrime = [True for i in range(n+1)]

for i in range(2, n+1):
    if isPrime[i]:
        primes.append(i)
        j = 1
        x = xor_product(i,j)
        k = 2*(n//i)
        while j <= k:
            if x <= n:
                isPrime[x] = False
            j += 1
            x = xor_product(i,j)

print(primes[4999999])
