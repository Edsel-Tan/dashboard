from prime import primes

p = primes(10**6)

for i,j in enumerate(p):
    n = i+1
    
    if n%2 == 0:
        continue


    if 2 * j * n > 10**10:
        break


print(n)
