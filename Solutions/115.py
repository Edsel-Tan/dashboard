def C(n,r):
    if r > n // 2:
        r = n - r

    output = 1
    for i in range(r):
        output *= n-i
        output = output // (i+1)
    return output

def F(n, m=50):
    ans = 0
    for i in range((n+1)//(m+1) + 1):
        o = i * (m+1) - 1
        ans += C(n-o + 2*i, 2*i)
    return ans

def binary_search(l, r, v):
    if l == r:
        return l
    m = (l+r)//2
    if v > F(m):
        return binary_search(m+1, r, v)
    else:
        return binary_search(l, m, v)
    
print(binary_search(0, 500, 10**6))
