from prime import primes

n = 100000
p = primes(n)

rad = [(1, i+1) for i in range(n)]
for i in p:
    rad[i-1::i] = [(j[0] * i, j[1]) for j in rad[i-1::i]]

print(sorted(rad)[9999][1])