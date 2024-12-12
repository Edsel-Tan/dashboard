from math import comb

def f(n, i):
    j = i - 1
    l = (n)%j
    m = (n)//j
    return l * comb(m+1, 2) + (j-l) * comb(m, 2)


n = 10**7

ans = 0
for i in range(2,n+1):
    j = i - 1
    l = (n)%j
    m = (n)//j
    ans += l * comb(m+1, 2) + (j-l) * comb(m, 2)

print(ans)