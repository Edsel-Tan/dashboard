n = 1234567

from prime import primes
p = primes(n+1)

f = [{} for i in range(n+1)]

for i in p:
    for j in range(i,n+1,i):
        f[j][i] = 1
    j = i*i
    while j < n+1:
        for k in range(j, n+1, j):
            f[k][i] += 1
        j *= i

def factors(x):
    output = [1]
    for i in x:
        o = []
        c = 1
        for j in range(x[i]+1):
            for k in output:
                o.append(c*k)
            c *= i
        output = o
    return output

import itertools
ans = 0
for i in range(3, n+1):
    d = {}
    for x in f[i]:
        d[x] = f[i][x]
    for x in f[i-1]:
        if x in d:
            d[x] += f[i-1][x]
        else:
            d[x] = f[i-1][x]
    
    for j in factors(d):
        if j > i:
            m = j-i
            if ((m+1)*(2*i+m))%(2*i+2*m) == 0:
                ans += j-i
print(ans)

    
