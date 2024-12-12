n = 10**14

def log(n, k):
    ans = 0
    c = 1
    while c < n:
        c *= k
        ans += 1
    return ans

from prime import primes
p = primes(48)

def p_smooth():
    o = [1]
    for i in p:
        no = []
        for j in o:
            while j < n:
                no.append(j)
                j *= i
        o = no
    return o

s = set(p_smooth())

ans = 0

for i in s:
    if i+1 in s:
        ans += i

print(ans)