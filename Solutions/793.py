s = [290797]
n = 1000003

for i in range(n-1):
    s.append((s[-1] ** 2) % 50515093)

s = sorted(s)

l = 0
r = s[-1] * s[-1]

def idx(x):
    l = 0
    r = len(s)

    while (r-l):
        m = (l+r)//2
        if s[m] > x:
            r = m
        else:
            l = m+1
    return l

while (r-l):
    m = (l+r)//2
    cnt = 0
    for i in range(n):
        cnt += min(idx(m//s[i]), i)
    if cnt <= (n*(n-1)//2)//2:
        l = m+1
    else:
        r = m

print(l)
