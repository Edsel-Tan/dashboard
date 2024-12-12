m = 10**9+7

from prime import primes
n = 20000
p = primes(n+1)

D = [1 for i in range(n+1)]

for i in p:
    f = [j for j in range(n//i+1)]
    g = [0 for j in range(n//i+1)]
    j = i
    while j < n//i+1:
        for k in range(j,n//i+1,j):
            g[k] += 1
        j *= i

    h = 0
    for j in range(n//i+1):
        h += g[j]
        f[j] += h



    fp = [0 for j in range(n//i+1)]
    for k in range(1, n//i+1):
        fp[k] += fp[k-1] + i * f[k-1]
    
    for j in range(1, n+1):
        vp = (j+1) * f[j//i] - 2 * (fp[j//i] + (j-(j//i)*i+1) * f[j//i])
        D[j] *= (pow(i, vp+1, m) - 1) * pow(i-1, -1, m)
        D[j] = D[j] % m


print((sum(D) - 1)%m)
    
