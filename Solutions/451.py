from prime import primes

n = 2 * 10 ** 7
p = primes(n+10)
pf = [[] for i in range(n+1)]

for i in p:
    for j in range(i, n+1, i):
        pf[j].append((i, 1))
    j = i * i
    while j < n+1:
        c = pf[j][-1][-1] + 1
        for k in range(j, n+1, j):
            pf[k][-1] = (i, c)
        j *= i

def factors(pf):
    output = [1]
    for i in pf:
        noutput = []
        for j in range(pf[i]+1):
            c = i ** j
            for k in output:
                if k * c <= n:
                    noutput.append(k*c)
        output = noutput
    return output

ans = [1 for i in range(n+1)]

for i in range(2, n):
    f = {}
    for j, k in pf[i-1]:
        f[j] = k
    for j, k in pf[i+1]:
        if j not in f:
            f[j] = 0
        f[j] += k
    f = sorted(factors(f))
    for j in f:
        if j > i + 1:
            ans[j] = i

print(sum(ans) - 3)