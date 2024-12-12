n = 10**7
from prime import primes
m = [[] for i in range(n+1)]
ans = [1 for i in range(n+1)]
ans[1] = 0
ans[0] = 0
p = primes(n+1)

def factors(x):
    output = [1]
    for a in x:
        b = x[a]
        c = a
        l = len(output)
        for i in range(b):
            for j in range(l):
                if c*output[j] <= n:
                    output.append(c*output[j])
            c *= a
    return output

for i in p:
    for j in range(i, n+1, i):
        m[j].append((i,1))
    j = i*i
    while j <= n:
        for k in range(j, n+1, j):
            m[k][-1] = (m[k][-1][0], m[k][-1][1]+1)
        j *= i

for i in range(1, n):
    s = {}
    for a,b in m[i]:
        s[a] = b
    for a,b in m[i+1]:
        if a in s:
            s[a] += b
        else:
            s[a] = b
    f = factors(s)
    f = sorted(f, reverse=True)
    for j in f:
        if j <= i+1:
            break
        ans[j] = i+1
print(sum(ans))