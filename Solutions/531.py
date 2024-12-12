from prime import primes, memoize

n = 10**6 + 5000

p = primes(n)

@memoize
def pf(x) -> dict[int, int]:
    output = {}
    for i in p:
        if i * i > x:
            if x > 1:
                output[x] = x
                break
        if x % i == 0:
            output[i] = 1
        while x % i == 0:
            output[i] *= i
            x = x//i
    return output

def totient(x):
    output = 1
    pfx = pf(x)
    for i in pfx:
        output *= pfx[i] // i * (i-1)
    return output


def crt_coprime(a,n,b,m):
    return (b*n*pow(n,-1,m) + a*m*pow(m,-1,n)) % (n*m)

def crt(a,n,b,m):
    pfn = pf(n)
    pfm = pf(m)

    p = set(pfn.keys())
    p = p.union(set(pfm.keys()))
    q = 0
    r = 1
    for i in p:
        x = 0
        y = 1
        if i in pfn:
            x = a
            y = pfn[i]
        if i in pfm:
            z = min(y, pfm[i])
            if x % z == b % z:
                if pfm[i] > y:
                    y = pfm[i]
                    x = b
            else:
                return 0
        q, r = crt_coprime(q, r, x, y), r*y
    return q


ans = 0
for i in range(10**6, n):
    for j in range(i+1, n):
        ans += crt(totient(i),i,totient(j),j)
print(ans)