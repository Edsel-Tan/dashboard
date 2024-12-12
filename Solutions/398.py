from prime import memoize

n = 10**7
m = 100
E = [0 for i in range(n+1)]
p = 1
for i in range(m-2):
    p *= ((m-1)-1-i) / (2*(m-1)-i-1)
for i in range(m-1,n+1):
    E[i] = p * (1 + E[i-m+1])
    p *= (i) / (i-1-(m-3))
    p /= (i+m-1) / (i+m-1-(m-3)-1)

def E_least(n, m):
    if m == 1:
        return n
    if m > n:
        return 0

    return E[n]

@memoize
def E_l(n, m):
    if m == 1:
        return n
    if m > n:
        return 0
    p = 1
    for i in range(m-1):
        p *= (n-1-i) / (n+m-i-1)
    
    return p * (1 + E_l(n-m,m))

# def E_least2(n, m):
def P(n,m,k):
    p = 1
    x = n - (k-1) * m
    for i in range(m-1):
        p *= (x-1-i)/(n-1-i)
    return p


def Q(n,m,i):
    p = m*(m-1)
    z = n - i*m
    for j in range(m-2):
        p *= (z-1-j)/(n-1-j)
    p /= (n-1-(m-2))
    return p


ans = 0
for i in range(1,n//m+1):
    p = P(n,m,i) - P(n,m,i+1)
    ans += p * i
    ans += (Q(n,m,i)) * (1 + E_least(n-i*m-m+1, m-1))
print("{:.5f}".format(ans))