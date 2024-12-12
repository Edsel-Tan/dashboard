from prime import primes

p = primes(5000)
q = []
for i in p:
    if i > 1000:
        q.append(i)


def vp(n,p):
    ans = 0
    while n > 0:
        ans += n//p
        n = n//p
    return ans

n = 10**18
r = 10**9
x = 0
mq = []

def crt(a, b, x, y):
    return (b*x*pow(b,-1,y) + y*a*pow(y,-1,b))%(b*y), b*y

def mp(n, p):
    if n <= 1:
        return 1
    ans = mp(n//p, p)
    for i in range(n%p):
        ans *= (i+1)
    ans *= pow(-1, n//p, p)
    return ans%p


for i in q:
    if vp(n, i) - vp(r, i) - vp(n-r, i) == 0:
        mq.append((mp(n, i) * pow(mp(r, i), -1, i) * pow(mp(n-r, i), -1, i))%i)
    else:
        mq.append(0)

import math
ln = len(q)
ans = 0


for i in range(ln):
    a = mq[i]
    b = q[i]

    for j in range(i+1, ln):
        c,d = crt(a, b, mq[j], q[j])

        for k in range(j+1, ln):
            e,f = crt(c, d, mq[k], q[k])


            ans += e

print(ans)
            